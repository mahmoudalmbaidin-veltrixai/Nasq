"""Database engine construction and a reachability check."""

import math

from pydantic import SecretStr
from sqlalchemy import Engine, create_engine, text

# libpq treats connect_timeout values below 2 seconds as 2.
_MIN_CONNECT_TIMEOUT_SECONDS = 2


def create_database_engine(url: SecretStr, *, timeout_seconds: float) -> Engine:
    """Create a pooled engine whose connects and statements give up after `timeout_seconds`."""
    if timeout_seconds <= 0:
        raise ValueError("timeout_seconds must be positive")
    return create_engine(
        url.get_secret_value(),
        pool_pre_ping=True,
        pool_size=5,
        max_overflow=5,
        pool_timeout=timeout_seconds,
        connect_args={
            "connect_timeout": max(_MIN_CONNECT_TIMEOUT_SECONDS, math.ceil(timeout_seconds)),
            "options": f"-c statement_timeout={int(timeout_seconds * 1000)}",
        },
    )


def ping_database(engine: Engine) -> None:
    """Raise if the database cannot answer a trivial query."""
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
