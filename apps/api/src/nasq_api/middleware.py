"""Request id, access log and last-resort error handling for every HTTP request."""

import logging
import re
import time

from starlette.datastructures import Headers, MutableHeaders
from starlette.requests import Request
from starlette.types import ASGIApp, Message, Receive, Scope, Send

from nasq_api.errors import problem_response
from nasq_core.ids import uuid7
from nasq_core.request_context import bind_request_id, reset_request_id

REQUEST_ID_HEADER = "X-Request-ID"
_VALID_REQUEST_ID = re.compile(r"[A-Za-z0-9._-]{8,128}")

_log = logging.getLogger("nasq.api")
_access_log = logging.getLogger("nasq.api.access")


def _request_id_from(scope: Scope) -> str:
    incoming = Headers(scope=scope).get(REQUEST_ID_HEADER)
    if incoming is not None and _VALID_REQUEST_ID.fullmatch(incoming):
        return incoming
    return str(uuid7())


class RequestContextMiddleware:
    """Binds a request id, echoes it in X-Request-ID and logs one line per request.

    Unhandled exceptions become a 500 problem response here, inside the request id
    scope, so the response and the error log share the same id.
    """

    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        request_id = _request_id_from(scope)
        token = bind_request_id(request_id)
        started = time.perf_counter()
        status_code = 500
        response_started = False

        async def send_with_request_id(message: Message) -> None:
            nonlocal status_code, response_started
            if message["type"] == "http.response.start":
                response_started = True
                status_code = message["status"]
                MutableHeaders(scope=message)[REQUEST_ID_HEADER] = request_id
            await send(message)

        context = {"request_id": request_id, "method": scope["method"], "path": scope["path"]}
        try:
            await self.app(scope, receive, send_with_request_id)
        except Exception:
            _log.exception("unhandled error while handling request", extra=context)
            if response_started:
                raise
            response = problem_response(Request(scope), code="internal_error", status=500)
            await response(scope, receive, send_with_request_id)
        finally:
            duration_ms = round((time.perf_counter() - started) * 1000, 2)
            _access_log.info(
                "request completed",
                extra={**context, "status_code": status_code, "duration_ms": duration_ms},
            )
            reset_request_id(token)
