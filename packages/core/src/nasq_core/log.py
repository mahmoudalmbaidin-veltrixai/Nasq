"""Structured JSON logging: one JSON object per line on stdout."""

import json
import logging
import sys
from datetime import UTC, datetime

from nasq_core.request_context import get_request_id

_STANDARD_ATTRS = frozenset(
    logging.LogRecord("", 0, "", 0, "", (), None).__dict__.keys() | {"message", "asctime"}
)


class JsonFormatter(logging.Formatter):
    """Formats a record as JSON with a UTC timestamp, the request id and any `extra` fields.

    Callers must not pass personal data or secrets in messages or `extra` (PRD §24).
    """

    def format(self, record: logging.LogRecord) -> str:
        payload: dict[str, object] = {
            "timestamp": datetime.fromtimestamp(record.created, tz=UTC)
            .isoformat(timespec="milliseconds")
            .replace("+00:00", "Z"),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "request_id": get_request_id(),
        }
        payload.update(
            {
                key: value
                for key, value in record.__dict__.items()
                if key not in _STANDARD_ATTRS and not key.startswith("_")
            }
        )
        if record.exc_info and record.exc_info[0] is not None:
            payload["exception_type"] = record.exc_info[0].__name__
            payload["exception"] = self.formatException(record.exc_info)
        return json.dumps(payload, default=repr, ensure_ascii=False)


class _NasqHandler(logging.StreamHandler):  # type: ignore[type-arg]
    pass


def configure_logging(level: str) -> None:
    """Send every log record, including uvicorn's, to stdout as JSON."""
    root = logging.getLogger()
    for handler in [h for h in root.handlers if isinstance(h, _NasqHandler)]:
        root.removeHandler(handler)
    handler = _NasqHandler(sys.stdout)
    handler.setFormatter(JsonFormatter())
    root.addHandler(handler)
    root.setLevel(level)
    for name in ("uvicorn", "uvicorn.error", "uvicorn.access"):
        server_logger = logging.getLogger(name)
        server_logger.handlers.clear()
        server_logger.propagate = True
