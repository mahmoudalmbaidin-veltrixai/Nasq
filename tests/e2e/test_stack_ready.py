"""Checks against the running Docker Compose stack.

Start the stack with `make dev`, then run `make test-stack`.
"""

import os
import uuid

import httpx2 as httpx
import pytest

pytestmark = pytest.mark.stack

API_URL = os.environ.get("NASQ_STACK_API_URL", "http://localhost:8000")
WEB_URL = os.environ.get("NASQ_STACK_WEB_URL", "http://localhost:5173")
MAILPIT_URL = os.environ.get("NASQ_STACK_MAILPIT_URL", "http://localhost:8025")
STORAGE_URL = os.environ.get("NASQ_STACK_STORAGE_URL", "http://localhost:9000")
TIMEOUT = httpx.Timeout(10.0)


def test_readyz_returns_200_with_database_and_queue_reachable() -> None:
    response = httpx.get(f"{API_URL}/readyz", timeout=TIMEOUT)

    assert response.status_code == 200, response.text
    assert response.json() == {"status": "ready", "checks": {"database": "ok", "queue": "ok"}}


def test_healthz_returns_200_and_a_uuid7_request_id() -> None:
    response = httpx.get(f"{API_URL}/healthz", timeout=TIMEOUT)

    assert response.status_code == 200
    assert uuid.UUID(response.headers["x-request-id"]).version == 7


def test_web_app_is_served() -> None:
    response = httpx.get(WEB_URL, timeout=TIMEOUT)

    assert response.status_code == 200
    assert '<div id="app">' in response.text


def test_mailpit_is_ready() -> None:
    assert httpx.get(f"{MAILPIT_URL}/readyz", timeout=TIMEOUT).status_code == 200


def test_object_storage_is_ready() -> None:
    assert httpx.get(f"{STORAGE_URL}/health/ready", timeout=TIMEOUT).status_code == 200
