import pytest
from pydantic import ValidationError

from nasq_core.settings import Settings

LOCAL_URL = "postgresql+psycopg://veltrix_app:CHANGE_ME@localhost:5432/veltrix"
REAL_LOOKING_URL = "postgresql+psycopg://veltrix_app:s3cret-from-vault@db:5432/veltrix"


@pytest.fixture(autouse=True)
def _clean_env(monkeypatch: pytest.MonkeyPatch) -> None:
    for name in (
        "APP_ENV",
        "DATABASE_URL",
        "DATABASE_MIGRATION_URL",
        "LOG_LEVEL",
        "READINESS_TIMEOUT_SECONDS",
    ):
        monkeypatch.delenv(name, raising=False)


def test_settings_load_from_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("APP_ENV", "local")
    monkeypatch.setenv("DATABASE_URL", LOCAL_URL)
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")
    monkeypatch.setenv("READINESS_TIMEOUT_SECONDS", "3.5")

    settings = Settings()

    assert settings.app_env == "local"
    assert settings.database_url.get_secret_value() == LOCAL_URL
    assert settings.log_level == "DEBUG"
    assert settings.readiness_timeout_seconds == 3.5


def test_settings_require_a_database_url() -> None:
    with pytest.raises(ValidationError, match="database_url"):
        Settings()


def test_settings_never_print_the_database_password(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DATABASE_URL", REAL_LOOKING_URL)

    settings = Settings()

    assert "s3cret-from-vault" not in repr(settings)
    assert "s3cret-from-vault" not in str(settings.model_dump())


@pytest.mark.parametrize("env", ["local", "test"])
def test_placeholder_secrets_are_allowed_on_developer_machines(
    monkeypatch: pytest.MonkeyPatch, env: str
) -> None:
    monkeypatch.setenv("APP_ENV", env)
    monkeypatch.setenv("DATABASE_URL", LOCAL_URL)

    assert Settings().app_env == env


@pytest.mark.parametrize("env", ["staging", "production"])
def test_placeholder_secrets_are_refused_outside_developer_machines(
    monkeypatch: pytest.MonkeyPatch, env: str
) -> None:
    monkeypatch.setenv("APP_ENV", env)
    monkeypatch.setenv("DATABASE_URL", LOCAL_URL)

    with pytest.raises(ValidationError, match="CHANGE_ME") as excinfo:
        Settings()

    assert "veltrix_app:CHANGE_ME" not in str(excinfo.value)


def test_unknown_log_level_is_rejected(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DATABASE_URL", LOCAL_URL)
    monkeypatch.setenv("LOG_LEVEL", "LOUD")

    with pytest.raises(ValidationError, match="log_level"):
        Settings()


@pytest.mark.parametrize("value", ["0", "-1", "31"])
def test_readiness_timeout_must_be_short_and_positive(
    monkeypatch: pytest.MonkeyPatch, value: str
) -> None:
    monkeypatch.setenv("DATABASE_URL", LOCAL_URL)
    monkeypatch.setenv("READINESS_TIMEOUT_SECONDS", value)

    with pytest.raises(ValidationError, match="readiness_timeout_seconds"):
        Settings()
