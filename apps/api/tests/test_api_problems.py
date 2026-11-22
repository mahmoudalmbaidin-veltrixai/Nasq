import uuid
from collections.abc import Callable

from fastapi import FastAPI
from fastapi.testclient import TestClient

from nasq_core.messages import MESSAGES

PROBLEM = "application/problem+json"


def test_unknown_route_returns_not_found_problem(client: TestClient) -> None:
    response = client.get("/no-such-route")

    assert response.status_code == 404
    assert response.headers["content-type"] == PROBLEM
    body = response.json()
    assert body["code"] == "not_found"
    assert body["type"] == "urn:nasq:problem:not_found"
    assert body["instance"] == "/no-such-route"
    assert body["request_id"] == response.headers["x-request-id"]


def test_wrong_method_returns_method_not_allowed_problem(client: TestClient) -> None:
    response = client.post("/healthz")

    assert response.status_code == 405
    assert response.headers["content-type"] == PROBLEM
    assert response.json()["code"] == "method_not_allowed"


def test_invalid_input_returns_validation_problem_without_echoing_input(
    make_app: Callable[..., FastAPI],
) -> None:
    app = make_app()

    @app.get("/_test/echo")
    def echo(count: int) -> dict[str, int]:
        return {"count": count}

    response = TestClient(app).get("/_test/echo", params={"count": "jane@example.com"})

    assert response.status_code == 422
    assert response.headers["content-type"] == PROBLEM
    body = response.json()
    assert body["code"] == "validation_failed"
    assert body["errors"] == [{"location": ["query", "count"], "type": "int_parsing"}]
    assert "jane@example.com" not in response.text


def test_unhandled_exception_returns_internal_error_without_details(
    make_app: Callable[..., FastAPI],
) -> None:
    app = make_app()

    @app.get("/_test/crash")
    def crash() -> None:
        raise RuntimeError("database password is hunter2")

    response = TestClient(app, raise_server_exceptions=False).get("/_test/crash")

    assert response.status_code == 500
    assert response.headers["content-type"] == PROBLEM
    assert response.json()["code"] == "internal_error"
    assert "hunter2" not in response.text
    assert response.json()["request_id"] == response.headers["x-request-id"]


def test_problem_titles_follow_accept_language(client: TestClient) -> None:
    english = client.get("/missing", headers={"Accept-Language": "en"}).json()
    arabic = client.get("/missing", headers={"Accept-Language": "ar"}).json()

    assert english["title"] == MESSAGES["not_found"]["en"].title
    assert arabic["title"] == MESSAGES["not_found"]["ar"].title


def test_request_id_is_generated_as_uuid7_when_missing(client: TestClient) -> None:
    response = client.get("/healthz")

    assert uuid.UUID(response.headers["x-request-id"]).version == 7


def test_valid_incoming_request_id_is_echoed(client: TestClient) -> None:
    response = client.get("/healthz", headers={"X-Request-ID": "edge-proxy-0001"})

    assert response.headers["x-request-id"] == "edge-proxy-0001"


def test_malformed_incoming_request_id_is_replaced(client: TestClient) -> None:
    for bad in ["short", "has spaces in it", "x" * 200, "inject\nnewline-0001"]:
        response = client.get("/healthz", headers={"X-Request-ID": bad})

        assert response.headers["x-request-id"] != bad
        assert uuid.UUID(response.headers["x-request-id"]).version == 7
