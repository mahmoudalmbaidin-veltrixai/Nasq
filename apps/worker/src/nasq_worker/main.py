"""Background worker process.

Runs no jobs yet: the queue is decided in ADR-002 (P0-03) and built in P4-01. Until then
the worker proves it can start, reach the database, report health and stop cleanly.

Run with: python -m nasq_worker.main
"""

import logging
import signal
import tempfile
import threading
import time
from collections.abc import Callable
from pathlib import Path
from types import FrameType

from pydantic import Field

from nasq_core.database import create_database_engine, ping_database
from nasq_core.log import configure_logging
from nasq_core.settings import Settings

_log = logging.getLogger("nasq.worker")


class WorkerSettings(Settings):
    worker_heartbeat_seconds: float = Field(default=10.0, gt=0, le=300)
    worker_heartbeat_file: Path = Field(
        default_factory=lambda: Path(tempfile.gettempdir()) / "nasq-worker-heartbeat"
    )


def _write_heartbeat(path: Path) -> None:
    partial = path.with_suffix(".partial")
    partial.write_text(f"{time.time()}", encoding="utf-8")
    partial.replace(path)


def run_worker(
    settings: WorkerSettings,
    *,
    check_database: Callable[[], None],
    stop: threading.Event,
    max_beats: int | None = None,
) -> None:
    _log.info(
        "worker started; no job handlers are registered until the queue is decided "
        "(ADR-002) and built (P4-01)"
    )
    beats = 0
    while not stop.is_set():
        try:
            check_database()
        except Exception as exc:  # noqa: BLE001 - any failure means the database is unusable
            _log.warning(
                "database unreachable; heartbeat skipped",
                extra={"error_type": type(exc).__name__},
            )
        else:
            _write_heartbeat(settings.worker_heartbeat_file)
            _log.debug("heartbeat written")
        beats += 1
        if max_beats is not None and beats >= max_beats:
            break
        stop.wait(settings.worker_heartbeat_seconds)
    _log.info("worker stopped")


def main() -> None:
    settings = WorkerSettings()
    configure_logging(settings.log_level)
    engine = create_database_engine(
        settings.database_url, timeout_seconds=settings.readiness_timeout_seconds
    )
    stop = threading.Event()

    def request_stop(signum: int, _frame: FrameType | None) -> None:
        _log.info("stop requested", extra={"signal": signal.Signals(signum).name})
        stop.set()

    signal.signal(signal.SIGTERM, request_stop)
    signal.signal(signal.SIGINT, request_stop)
    try:
        run_worker(settings, check_database=lambda: ping_database(engine), stop=stop)
    finally:
        engine.dispose()


if __name__ == "__main__":
    main()
