from collections.abc import Callable
from typing import Any

from fastapi import FastAPI
from fastapi.testclient import TestClient

from nasq_api.main import create_app
from nasq_core.messages import MESSAGES
from nasq_core.settings import Settings

type AppFactory = Callable[..., FastAPI]
type ProbeFactory = Callable[..., Any]


def test_healthz_reports_the_process_is_alive(client: TestClient) -> None:
    response = client.get("/healthz")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_healthz_does_not_depend_on_the_database(
    make_app: AppFactory, fake_probe: ProbeFactory
) -> None:
    app = make_app([fake_probe("database", healthy=False), fake_probe("queue", healthy=False)])

    response = TestClient(app).get("/healthz")

    assert response.status_code == 200


def test_readyz_returns_200_when_database_and_queue_are_reachable(client: TestClient) -> None:
    response = client.get("/readyz")

    assert response.status_code == 200
    assert response.json() == {"status": "ready", "checks": {"database": "ok", "queue": "ok"}}


def test_readyz_returns_503_problem_when_database_is_unreachable(
    make_app: AppFactory, fake_probe: ProbeFactory
) -> None:
    app = make_app([fake_probe("database", healthy=False), fake_probe("queue")])

    response = TestClient(app).get("/readyz")

    assert response.status_code == 503
    assert response.headers["content-type"] == "application/problem+json"
    body = response.json()
    assert body["code"] == "service_not_ready"
    assert body["status"] == 503
    assert body["checks"] == {"database": "unavailable", "queue": "ok"}


def test_readyz_returns_503_problem_when_queue_is_unreachable(
    make_app: AppFactory, fake_probe: ProbeFactory
) -> None:
    app = make_app([fake_probe("database"), fake_probe("queue", healthy=False)])

    response = TestClient(app).get("/readyz")

    assert response.status_code == 503
    assert response.json()["checks"] == {"database": "ok", "queue": "unavailable"}


def test_readyz_never_leaks_connection_details(
    make_app: AppFactory, fake_probe: ProbeFactory
) -> None:
    app = make_app([fake_probe("database", healthy=False), fake_probe("queue")])

    response = TestClient(app).get("/readyz")

    assert "10.0.0.5" not in response.text
    assert "veltrix_app" not in response.text


def test_readyz_problem_is_in_arabic_when_requested(
    make_app: AppFactory, fake_probe: ProbeFactory
) -> None:
    app = make_app([fake_probe("database", healthy=False), fake_probe("queue")])

    response = TestClient(app).get("/readyz", headers={"Accept-Language": "ar-JO,ar;q=0.9"})

    assert response.json()["title"] == MESSAGES["service_not_ready"]["ar"].title
    assert response.headers["content-language"] == "ar"


def test_readyz_uses_real_database_probes_by_default(settings: Settings) -> None:
    response = TestClient(create_app(settings)).get("/readyz")

    assert response.status_code == 503
    assert response.json()["checks"] == {"database": "unavailable", "queue": "unavailable"}
