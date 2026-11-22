"""Base error type and RFC 7807 problem documents."""

from collections.abc import Mapping
from types import MappingProxyType
from typing import ClassVar

from nasq_core.messages import Locale, message_for

PROBLEM_CONTENT_TYPE = "application/problem+json"

_RESERVED_MEMBERS = frozenset(
    {"type", "title", "status", "detail", "instance", "code", "request_id"}
)
_CODE_BY_STATUS: Mapping[int, str] = MappingProxyType(
    {
        404: "not_found",
        405: "method_not_allowed",
        422: "validation_failed",
        500: "internal_error",
        503: "service_not_ready",
    }
)


class NasqError(Exception):
    """An expected failure that becomes a problem response with a stable `code`.

    The `code` selects the translated title and detail; never put user input,
    personal data or secrets in `extensions`.
    """

    code: ClassVar[str] = "internal_error"
    status: ClassVar[int] = 500

    def __init__(self, *, extensions: Mapping[str, object] | None = None) -> None:
        super().__init__(self.code)
        self.extensions: dict[str, object] = dict(extensions or {})


class ServiceNotReadyError(NasqError):
    code: ClassVar[str] = "service_not_ready"
    status: ClassVar[int] = 503


def code_for_status(status: int) -> str:
    return _CODE_BY_STATUS.get(status, "http_error")


def problem_document(
    *,
    code: str,
    status: int,
    locale: Locale,
    instance: str | None,
    request_id: str | None,
    extensions: Mapping[str, object] | None = None,
) -> dict[str, object]:
    extra = dict(extensions or {})
    clash = _RESERVED_MEMBERS & extra.keys()
    if clash:
        raise ValueError(f"problem extensions cannot overwrite standard members: {sorted(clash)}")
    message = message_for(code, locale)
    return {
        "type": f"urn:nasq:problem:{code}",
        "title": message.title,
        "status": status,
        "detail": message.detail,
        "instance": instance,
        "code": code,
        "request_id": request_id,
        **extra,
    }
