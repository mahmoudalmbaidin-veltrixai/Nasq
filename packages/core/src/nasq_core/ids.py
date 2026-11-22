"""UUIDv7 identifiers (RFC 9562 section 5.7).

Python 3.12 has no uuid7 in the standard library. Values are time ordered and strictly
increasing within one process, using the 12-bit rand_a field as a counter (RFC 9562
section 6.2, method 1).
"""

import secrets
import threading
import time
import uuid
from collections.abc import Callable

_TIMESTAMP_MASK = (1 << 48) - 1
_MAX_COUNTER = (1 << 12) - 1
# Seeding below the counter maximum leaves room to count up within one millisecond.
_COUNTER_SEED_BITS = 11
_VERSION = 0x7
_VARIANT = 0b10


def _now_ms() -> int:
    return time.time_ns() // 1_000_000


class Uuid7Generator:
    """Thread-safe UUIDv7 source that never goes backwards, even if the clock does."""

    def __init__(self, clock_ms: Callable[[], int] = _now_ms) -> None:
        self._clock_ms = clock_ms
        self._lock = threading.Lock()
        self._last_ms = -1
        self._counter = 0

    def next(self) -> uuid.UUID:
        with self._lock:
            ms = self._clock_ms()
            if ms > self._last_ms:
                counter = secrets.randbits(_COUNTER_SEED_BITS)
            else:
                ms = self._last_ms
                counter = self._counter + 1
                if counter > _MAX_COUNTER:
                    ms += 1
                    counter = secrets.randbits(_COUNTER_SEED_BITS)
            self._last_ms = ms
            self._counter = counter

        value = (
            ((ms & _TIMESTAMP_MASK) << 80)
            | (_VERSION << 76)
            | (counter << 64)
            | (_VARIANT << 62)
            | secrets.randbits(62)
        )
        return uuid.UUID(int=value)


_default_generator = Uuid7Generator()


def uuid7() -> uuid.UUID:
    """Return a new UUIDv7 from the process-wide generator."""
    return _default_generator.next()


def uuid7_timestamp_ms(value: uuid.UUID) -> int:
    """Return the Unix timestamp in milliseconds encoded in a UUIDv7."""
    if value.version != _VERSION:
        raise ValueError(f"expected a version 7 UUID, got version {value.version}")
    return value.int >> 80
