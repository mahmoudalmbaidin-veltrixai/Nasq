import re

import pytest

from nasq_core.messages import MESSAGES, SUPPORTED_LOCALES, message_for, negotiate_locale

ARABIC_LETTER = re.compile(r"[\u0600-\u06FF]")


def test_every_message_exists_in_arabic_and_english() -> None:
    for code, translations in MESSAGES.items():
        assert set(translations) == set(SUPPORTED_LOCALES), code
        for locale, message in translations.items():
            assert message.title.strip(), (code, locale)
            assert message.detail.strip(), (code, locale)


def test_arabic_messages_are_written_in_arabic() -> None:
    for code, translations in MESSAGES.items():
        assert ARABIC_LETTER.search(translations["ar"].title), code
        assert ARABIC_LETTER.search(translations["ar"].detail), code


def test_unknown_code_raises_instead_of_inventing_text() -> None:
    with pytest.raises(KeyError):
        message_for("no_such_code", "en")


@pytest.mark.parametrize(
    ("header", "expected"),
    [
        (None, "en"),
        ("", "en"),
        ("ar", "ar"),
        ("ar-JO,ar;q=0.9,en;q=0.8", "ar"),
        ("en-US,en;q=0.9", "en"),
        ("en;q=0.1, ar;q=0.9", "ar"),
        ("fr-FR, de;q=0.5", "en"),
        ("fr, ar;q=0.3", "ar"),
        ("ar;q=0", "en"),
        ("*", "en"),
        ("ar;q=not-a-number, en", "en"),
        ("ar;level=1", "ar"),
    ],
)
def test_negotiate_locale(header: str | None, expected: str) -> None:
    assert negotiate_locale(header) == expected
