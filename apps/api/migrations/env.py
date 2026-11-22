"""Alembic environment. Migrations run as the schema owner (DATABASE_MIGRATION_URL)."""

from alembic import context
from sqlalchemy import create_engine, pool

from nasq_core.log import configure_logging
from nasq_core.settings import Settings

# The shared data model and its metadata arrive in P2-01.
target_metadata = None


def _migration_url() -> str:
    settings = Settings()
    if settings.database_migration_url is None:
        raise RuntimeError(
            "DATABASE_MIGRATION_URL is not set. Migrations run as the schema owner, "
            "not the application role; set it as shown in .env.example."
        )
    return settings.database_migration_url.get_secret_value()


def run_migrations_offline() -> None:
    context.configure(url=_migration_url(), target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    engine = create_engine(_migration_url(), poolclass=pool.NullPool)
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            transaction_per_migration=True,
        )
        with context.begin_transaction():
            context.run_migrations()


configure_logging("INFO")
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
