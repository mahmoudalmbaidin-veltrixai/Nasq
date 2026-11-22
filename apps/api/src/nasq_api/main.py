"""FastAPI application factory.

Run with: uvicorn --factory nasq_api.main:app_factory
"""

from collections.abc import AsyncIterator, Sequence
from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import Engine

from nasq_api.errors import install_exception_handlers
from nasq_api.health import router as health_router
from nasq_api.middleware import RequestContextMiddleware
from nasq_api.readiness import DatabaseProbe, Probe, QueueProbe
from nasq_core.database import create_database_engine
from nasq_core.log import configure_logging
from nasq_core.settings import Settings


def create_app(settings: Settings, *, probes: Sequence[Probe] | None = None) -> FastAPI:
    engine: Engine | None = None
    if probes is None:
        engine = create_database_engine(
            settings.database_url, timeout_seconds=settings.readiness_timeout_seconds
        )
        probes = (DatabaseProbe(engine), QueueProbe(engine))

    @asynccontextmanager
    async def lifespan(_: FastAPI) -> AsyncIterator[None]:
        yield
        if engine is not None:
            engine.dispose()

    app = FastAPI(title="Nasq API", version="0.1.0", lifespan=lifespan)
    app.state.probes = tuple(probes)
    install_exception_handlers(app)
    app.add_middleware(RequestContextMiddleware)
    app.include_router(health_router)
    return app


def app_factory() -> FastAPI:
    """Entry point for uvicorn: read settings from the environment and log as JSON."""
    settings = Settings()
    configure_logging(settings.log_level)
    return create_app(settings)
