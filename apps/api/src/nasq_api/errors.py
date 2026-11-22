"""Map every error to an RFC 7807 problem response in the caller's language."""

from collections.abc import Mapping

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from nasq_core.errors import PROBLEM_CONTENT_TYPE, NasqError, code_for_status, problem_document
from nasq_core.messages import negotiate_locale
from nasq_core.request_context import get_request_id


def problem_response(
    request: Request,
    *,
    code: str,
    status: int,
    extensions: Mapping[str, object] | None = None,
    headers: Mapping[str, str] | None = None,
) -> JSONResponse:
    locale = negotiate_locale(request.headers.get("accept-language"))
    body = problem_document(
        code=code,
        status=status,
        locale=locale,
        instance=request.url.path,
        request_id=get_request_id(),
        extensions=extensions,
    )
    return JSONResponse(
        body,
        status_code=status,
        media_type=PROBLEM_CONTENT_TYPE,
        headers={**(headers or {}), "Content-Language": locale},
    )


async def _nasq_error(request: Request, exc: Exception) -> JSONResponse:
    assert isinstance(exc, NasqError)  # noqa: S101 - registered for NasqError only
    return problem_response(request, code=exc.code, status=exc.status, extensions=exc.extensions)


async def _http_error(request: Request, exc: Exception) -> JSONResponse:
    assert isinstance(exc, StarletteHTTPException)  # noqa: S101 - registered for HTTPException only
    return problem_response(
        request,
        code=code_for_status(exc.status_code),
        status=exc.status_code,
        headers=exc.headers,
    )


async def _validation_error(request: Request, exc: Exception) -> JSONResponse:
    assert isinstance(exc, RequestValidationError)  # noqa: S101 - registered for validation only
    # Only the location and the error type: echoing the input could leak personal data.
    errors = [{"location": list(error["loc"]), "type": error["type"]} for error in exc.errors()]
    return problem_response(
        request, code="validation_failed", status=422, extensions={"errors": errors}
    )


def install_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(NasqError, _nasq_error)
    app.add_exception_handler(StarletteHTTPException, _http_error)
    app.add_exception_handler(RequestValidationError, _validation_error)
