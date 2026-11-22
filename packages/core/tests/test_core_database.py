import pytest
from pydantic import SecretStr
from sqlalchemy.exc import OperationalError

from nasq_core.database import create_database_engine, ping_database

UNREACHABLE = SecretStr("postgresql+psycopg://nobody:CHANGE_ME@127.0.0.1:1/nothing")


def test_engine_targets_postgres_through_psycopg() -> None:
    engine = create_database_engine(UNREACHABLE, timeout_seconds=2)

    assert engine.dialect.name == "postgresql"
    assert engine.dialect.driver == "psycopg"
    assert "CHANGE_ME" not in repr(engine.url)


def test_ping_raises_when_the_database_is_unreachable() -> None:
    engine = create_database_engine(UNREACHABLE, timeout_seconds=2)

    with pytest.raises(OperationalError):
        ping_database(engine)


def test_timeout_must_be_positive() -> None:
    with pytest.raises(ValueError, match="timeout"):
        create_database_engine(UNREACHABLE, timeout_seconds=0)
