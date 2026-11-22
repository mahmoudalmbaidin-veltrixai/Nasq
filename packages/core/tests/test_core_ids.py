import uuid

import pytest
from hypothesis import given
from hypothesis import strategies as st

from nasq_core.ids import Uuid7Generator, uuid7, uuid7_timestamp_ms

MAX_48_BIT = 2**48 - 1


def test_uuid7_has_version_7_and_rfc_variant() -> None:
    value = uuid7()

    assert value.version == 7
    assert value.variant == uuid.RFC_4122


@given(st.integers(min_value=0, max_value=MAX_48_BIT))
def test_uuid7_encodes_the_clock_millisecond(ms: int) -> None:
    generator = Uuid7Generator(clock_ms=lambda: ms)

    assert uuid7_timestamp_ms(generator.next()) == ms


def test_uuid7_is_strictly_increasing_within_one_millisecond() -> None:
    generator = Uuid7Generator(clock_ms=lambda: 1_700_000_000_000)

    values = [generator.next() for _ in range(10_000)]

    assert values == sorted(values)
    assert len(set(values)) == len(values)


def test_uuid7_stays_increasing_when_the_clock_goes_backwards() -> None:
    ticks = iter([1_700_000_000_500, 1_700_000_000_100, 1_700_000_000_100])
    generator = Uuid7Generator(clock_ms=lambda: next(ticks))

    first, second, third = generator.next(), generator.next(), generator.next()

    assert first < second < third


@given(st.lists(st.integers(min_value=0, max_value=MAX_48_BIT), min_size=2, max_size=50))
def test_uuid7_sequence_is_monotonic_for_any_clock(ticks: list[int]) -> None:
    clock = iter(ticks)
    generator = Uuid7Generator(clock_ms=lambda: next(clock))

    values = [generator.next() for _ in ticks]

    assert values == sorted(values)
    assert len(set(values)) == len(values)


def test_uuid7_timestamp_rejects_other_versions() -> None:
    with pytest.raises(ValueError, match="version 7"):
        uuid7_timestamp_ms(uuid.uuid4())
