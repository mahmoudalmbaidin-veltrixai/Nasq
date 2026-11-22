"""Dependency checks behind /readyz."""

import logging
from collections.abc import Iterable
from typing import Literal, Protocol

from sqlalchemy import Engine

from nasq_core.database import ping_database

type CheckStatus = Literal["ok", "unavailable"]

_log = logging.getLogger("nasq.api.readiness")


class Probe(Protocol):
    name: str

    def check(self) -> None:
        """Return if the dependency is reachable; raise otherwise."""


class DatabaseProbe:
    name = "database"

    def __init__(self, engine: Engine) -> None:
        self._engine = engine

    def check(self) -> None:
        ping_database(self._engine)


class QueueProbe:
    """Checks the store the job queue will use.

    Provisional until ADR-002 is accepted in P0-03. Its recommendation is a
    Postgres-backed queue, so this checks the Postgres connection the queue will use.
    Replace it when P4-01 builds the real queue.
    """

    name = "queue"

    def __init__(self, engine: Engine) -> None:
        self._engine = engine

    def check(self) -> None:
        ping_database(self._engine)


def run_probes(probes: Iterable[Probe]) -> dict[str, CheckStatus]:
    results: dict[str, CheckStatus] = {}
    for probe in probes:
        try:
            probe.check()
        except Exception as exc:  # noqa: BLE001 - any failure means the dependency is not ready
            _log.warning(
                "readiness check failed",
                extra={"check": probe.name, "error_type": type(exc).__name__},
            )
            results[probe.name] = "unavailable"
        else:
            results[probe.name] = "ok"
    return results
