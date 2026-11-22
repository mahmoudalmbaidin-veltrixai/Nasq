import json
import logging
import sys
from collections.abc import Iterator

import pytest

from nasq_core.log import JsonFormatter, configure_logging
from nasq_core.request_context import get_request_id, request_id_scope


def _record(message: str, **extra: object) -> logging.LogRecord:
    record = logging.LogRecord(
        name="nasq.test",
        level=logging.INFO,
        pathname=__file__,
        lineno=1,
        msg=message,
        args=(),
        exc_info=None,
    )
    for key, value in extra.items():
        setattr(record, key, value)
    return record


def test_log_line_is_one_json_object_with_utc_timestamp() -> None:
    line = JsonFormatter().format(_record("service started"))

    payload = json.loads(line)
    assert "\n" not in line
    assert payload["message"] == "service started"
    assert payload["level"] == "INFO"
    assert payload["logger"] == "nasq.test"
    assert payload["timestamp"].endswith("Z")
    assert payload["request_id"] is None


def test_log_line_carries_the_bound_request_id() -> None:
    with request_id_scope("req-12345678"):
        payload = json.loads(JsonFormatter().format(_record("handled")))

    assert payload["request_id"] == "req-12345678"
    assert get_request_id() is None


def test_log_line_includes_structured_extra_fields() -> None:
    payload = json.loads(JsonFormatter().format(_record("done", status_code=200, path="/x")))

    assert payload["status_code"] == 200
    assert payload["path"] == "/x"


def test_log_line_survives_values_that_are_not_json() -> None:
    payload = json.loads(JsonFormatter().format(_record("odd", thing=object())))

    assert payload["thing"].startswith("<object object")


def test_log_line_includes_exception_type_and_traceback() -> None:
    try:
        raise RuntimeError("boom")  # noqa: TRY301
    except RuntimeError:
        record = _record("failed")
        record.exc_info = sys.exc_info()

    payload = json.loads(JsonFormatter().format(record))

    assert payload["exception_type"] == "RuntimeError"
    assert "Traceback" in payload["exception"]


@pytest.fixture
def _restore_root_logger() -> Iterator[None]:
    root = logging.getLogger()
    handlers, level = list(root.handlers), root.level
    yield
    root.handlers[:] = handlers
    root.setLevel(level)


@pytest.mark.usefixtures("_restore_root_logger")
def test_configure_logging_writes_json_to_stdout(capsys: pytest.CaptureFixture[str]) -> None:
    configure_logging("INFO")
    configure_logging("INFO")

    logging.getLogger("nasq.test").info("configured")

    out = capsys.readouterr().out.strip().splitlines()
    assert len(out) == 1, "configuring twice must not duplicate log lines"
    assert json.loads(out[0])["message"] == "configured"
