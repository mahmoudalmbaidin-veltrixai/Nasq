from collections.abc import Callable, Sequence
from dataclasses import dataclass

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import SecretStr

from nasq_api.main import create_app
from nasq_api.readiness import Probe
from nasq_core.settings import Settings


@dataclass
class FakeProbe:
    name: str
    healthy: bool = True
    error_text: str = "connection refused by 10.0.0.5 for user veltrix_app"

    def check(self) -> None:
        if not self.healthy:
            raise ConnectionError(self.error_text)


type ProbeFactory = Callable[..., FakeProbe]


@pytest.fixture
def fake_probe() -> ProbeFactory:
    return FakeProbe


@pytest.fixture
def settings() -> Settings:
    return Settings(
        app_env="test",
        database_url=SecretStr("postgresql+psycopg://nobody:CHANGE_ME@127.0.0.1:1/nothing"),
        log_level="INFO",
        readiness_timeout_seconds=2,
    )


@pytest.fixture
def make_app(settings: Settings) -> Callable[..., FastAPI]:
    def _make(probes: Sequence[Probe] | None = None) -> FastAPI:
        if probes is None:
            probes = [FakeProbe("database"), FakeProbe("queue")]
        return create_app(settings, probes=probes)

    return _make


@pytest.fixture
def client(make_app: Callable[..., FastAPI]) -> TestClient:
    return TestClient(make_app())
