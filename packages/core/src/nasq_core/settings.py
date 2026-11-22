"""Process settings read from environment variables (see .env.example)."""

from typing import Literal, Self

from pydantic import Field, SecretStr, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

type AppEnv = Literal["local", "test", "staging", "production"]
type LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR"]

PLACEHOLDER = "CHANGE_ME"
_DEVELOPER_ENVS: frozenset[str] = frozenset({"local", "test"})


class Settings(BaseSettings):
    """Settings shared by the API and the worker."""

    model_config = SettingsConfigDict(
        env_file=None,
        extra="ignore",
        frozen=True,
        hide_input_in_errors=True,
    )

    app_env: AppEnv = "local"
    database_url: SecretStr
    database_migration_url: SecretStr | None = None
    log_level: LogLevel = "INFO"
    readiness_timeout_seconds: float = Field(default=2.0, gt=0, le=30)

    @model_validator(mode="after")
    def _refuse_placeholder_secrets(self) -> Self:
        if self.app_env in _DEVELOPER_ENVS:
            return self
        offenders = [
            name
            for name in type(self).model_fields
            if isinstance(value := getattr(self, name), SecretStr)
            and PLACEHOLDER in value.get_secret_value()
        ]
        if offenders:
            raise ValueError(
                f"{', '.join(offenders)} still contain the {PLACEHOLDER} placeholder. "
                f"Set real values from the secret manager when APP_ENV is {self.app_env}."
            )
        return self
