"""Liveness and readiness endpoints."""

from collections.abc import Sequence
from typing import Literal, cast

from fastapi import APIRouter, Request
from pydantic import BaseModel

from nasq_api.readiness import CheckStatus, Probe, run_probes
from nasq_core.errors import PROBLEM_CONTENT_TYPE, ServiceNotReadyError

router = APIRouter(tags=["operations"])


class Health(BaseModel):
    status: Literal["ok"]


class Readiness(BaseModel):
    status: Literal["ready"]
    checks: dict[str, CheckStatus]


@router.get("/healthz", summary="The API process is running")
def healthz() -> Health:
    return Health(status="ok")


@router.get(
    "/readyz",
    summary="The database and the queue are reachable",
    responses={
        503: {"description": "A dependency is unavailable", "content": {PROBLEM_CONTENT_TYPE: {}}}
    },
)
def readyz(request: Request) -> Readiness:
    probes = cast(Sequence[Probe], request.app.state.probes)
    checks = run_probes(probes)
    if any(status != "ok" for status in checks.values()):
        raise ServiceNotReadyError(extensions={"checks": checks})
    return Readiness(status="ready", checks=checks)
