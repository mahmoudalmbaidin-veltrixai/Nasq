"""Container healthcheck: exit 0 if the worker wrote a heartbeat recently.

Run with: python -m nasq_worker.health
"""

import sys
import time
from pathlib import Path

from nasq_worker.main import WorkerSettings

_MISSED_BEATS_ALLOWED = 3


def heartbeat_is_fresh(path: Path, *, max_age_seconds: float, now: float | None = None) -> bool:
    try:
        written = float(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return False
    current = time.time() if now is None else now
    return current - written <= max_age_seconds


def main() -> int:
    settings = WorkerSettings()
    fresh = heartbeat_is_fresh(
        settings.worker_heartbeat_file,
        max_age_seconds=_MISSED_BEATS_ALLOWED * settings.worker_heartbeat_seconds,
    )
    return 0 if fresh else 1


if __name__ == "__main__":
    sys.exit(main())
