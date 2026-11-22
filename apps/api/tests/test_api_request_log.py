import logging
from collections.abc import Callable

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient


def test_each_request_writes_one_structured_log_line(
    client: TestClient, caplog: pytest.LogCaptureFixture
) -> None:
    with caplog.at_level(logging.INFO, logger="nasq.api.access"):
        response = client.get("/healthz?email=jane@example.com")

    records = [r for r in caplog.records if r.name == "nasq.api.access"]
    assert len(records) == 1
    record = records[0]
    assert record.__dict__["method"] == "GET"
    assert record.__dict__["path"] == "/healthz"
    assert record.__dict__["status_code"] == 200
    assert record.__dict__["request_id"] == response.headers["x-request-id"]
    assert record.__dict__["duration_ms"] >= 0
    assert "jane@example.com" not in caplog.text


def test_unhandled_exception_is_logged_with_the_request_id(
    make_app: Callable[..., FastAPI], caplog: pytest.LogCaptureFixture
) -> None:
    app = make_app()

    @app.get("/_test/crash")
    def crash() -> None:
        raise RuntimeError("boom")

    with caplog.at_level(logging.ERROR, logger="nasq.api"):
        response = TestClient(app, raise_server_exceptions=False).get("/_test/crash")

    errors = [r for r in caplog.records if r.levelno == logging.ERROR]
    assert errors
    assert errors[0].__dict__["request_id"] == response.headers["x-request-id"]
