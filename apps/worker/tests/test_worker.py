import logging
import threading
from pathlib import Path

import pytest
from pydantic import SecretStr

from nasq_worker.health import heartbeat_is_fresh
from nasq_worker.main import WorkerSettings, run_worker


def _settings(tmp_path: Path) -> WorkerSettings:
    return WorkerSettings(
        app_env="test",
        database_url=SecretStr("postgresql+psycopg://nobody:CHANGE_ME@127.0.0.1:1/nothing"),
        worker_heartbeat_seconds=0.01,
        worker_heartbeat_file=tmp_path / "heartbeat",
    )


def _healthy() -> None:
    return None


def _unreachable() -> None:
    raise ConnectionError("connection refused by 10.0.0.5")


def test_worker_announces_it_runs_no_jobs_yet(
    tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    with caplog.at_level(logging.INFO, logger="nasq.worker"):
        run_worker(
            _settings(tmp_path), check_database=_healthy, stop=threading.Event(), max_beats=1
        )

    assert any("no job handlers" in r.getMessage() for r in caplog.records)


def test_worker_writes_a_heartbeat_while_the_database_is_reachable(tmp_path: Path) -> None:
    settings = _settings(tmp_path)

    run_worker(settings, check_database=_healthy, stop=threading.Event(), max_beats=2)

    assert heartbeat_is_fresh(settings.worker_heartbeat_file, max_age_seconds=60)


def test_worker_skips_the_heartbeat_and_warns_when_the_database_is_unreachable(
    tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    settings = _settings(tmp_path)

    with caplog.at_level(logging.WARNING, logger="nasq.worker"):
        run_worker(settings, check_database=_unreachable, stop=threading.Event(), max_beats=2)

    assert not settings.worker_heartbeat_file.exists()
    warnings = [r for r in caplog.records if r.levelno == logging.WARNING]
    assert warnings
    assert "10.0.0.5" not in caplog.text


def test_worker_stops_promptly_when_asked(tmp_path: Path) -> None:
    stop = threading.Event()
    settings = _settings(tmp_path).model_copy(update={"worker_heartbeat_seconds": 30})
    worker = threading.Thread(
        target=run_worker, kwargs={"settings": settings, "check_database": _healthy, "stop": stop}
    )

    worker.start()
    stop.set()
    worker.join(timeout=5)

    assert not worker.is_alive()


def test_heartbeat_is_not_fresh_when_missing(tmp_path: Path) -> None:
    assert not heartbeat_is_fresh(tmp_path / "missing", max_age_seconds=60)


def test_heartbeat_is_not_fresh_when_stale(tmp_path: Path) -> None:
    path = tmp_path / "heartbeat"
    path.write_text("1000.0", encoding="utf-8")

    assert not heartbeat_is_fresh(path, max_age_seconds=60, now=2000.0)


def test_heartbeat_is_fresh_when_recent(tmp_path: Path) -> None:
    path = tmp_path / "heartbeat"
    path.write_text("1990.0", encoding="utf-8")

    assert heartbeat_is_fresh(path, max_age_seconds=60, now=2000.0)


def test_heartbeat_is_not_fresh_when_unreadable(tmp_path: Path) -> None:
    path = tmp_path / "heartbeat"
    path.write_text("not a timestamp", encoding="utf-8")

    assert not heartbeat_is_fresh(path, max_age_seconds=60, now=2000.0)
