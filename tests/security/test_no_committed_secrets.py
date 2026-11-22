"""Configuration committed to the repository must hold placeholders only (PRD §24, §29)."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PLACEHOLDER = "CHANGE_ME"
SECRET_NAME = re.compile(r"(SECRET|PASSWORD|ACCESS_KEY|TOKEN|API_KEY|ROOT_USER)", re.IGNORECASE)
URL_CREDENTIALS = re.compile(r"://[^:/@\s]+:([^@\s]+)@")


def _env_example() -> dict[str, str]:
    values: dict[str, str] = {}
    for raw in (ROOT / ".env.example").read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line and not line.startswith("#"):
            key, _, value = line.partition("=")
            values[key.strip()] = value.strip()
    return values


def test_env_example_secrets_are_placeholders() -> None:
    offenders = [
        key
        for key, value in _env_example().items()
        if SECRET_NAME.search(key) and not value.startswith(PLACEHOLDER)
    ]
    assert not offenders, f"use {PLACEHOLDER} placeholders for: {offenders}"


def test_env_example_urls_carry_placeholder_passwords_only() -> None:
    for key, value in _env_example().items():
        for password in URL_CREDENTIALS.findall(value):
            assert password.startswith(PLACEHOLDER), key


def test_compose_secrets_default_to_placeholders() -> None:
    compose = (ROOT / "docker-compose.yml").read_text(encoding="utf-8")
    for line in compose.splitlines():
        name, sep, value = line.strip().partition(":")
        if sep and SECRET_NAME.search(name) and value.strip():
            assert PLACEHOLDER in value, line.strip()
        for password in URL_CREDENTIALS.findall(line):
            assert PLACEHOLDER in password, line.strip()


def test_real_env_file_is_ignored_by_git() -> None:
    gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines()

    assert ".env" in gitignore
    assert "!.env.example" in gitignore
