"""Request id carried through logs and error responses for the current task or thread."""

from collections.abc import Iterator
from contextlib import contextmanager
from contextvars import ContextVar, Token

_request_id: ContextVar[str | None] = ContextVar("nasq_request_id", default=None)


def get_request_id() -> str | None:
    return _request_id.get()


def bind_request_id(value: str) -> Token[str | None]:
    return _request_id.set(value)


def reset_request_id(token: Token[str | None]) -> None:
    _request_id.reset(token)


@contextmanager
def request_id_scope(value: str) -> Iterator[None]:
    token = bind_request_id(value)
    try:
        yield
    finally:
        reset_request_id(token)
