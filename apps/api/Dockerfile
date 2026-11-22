# Build context: repository root (see docker-compose.yml).
FROM python:3.12.16-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:0.11.28 /uv /usr/local/bin/uv

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PROJECT_ENVIRONMENT=/opt/venv \
    PATH="/opt/venv/bin:$PATH" \
    PYTHONUNBUFFERED=1

WORKDIR /app

# uv needs every workspace member's pyproject.toml to read the lockfile.
COPY pyproject.toml uv.lock ./
COPY apps/api/pyproject.toml apps/api/
COPY apps/worker/pyproject.toml apps/worker/
COPY packages/core/pyproject.toml packages/core/
COPY packages/contracts/pyproject.toml packages/contracts/
COPY packages/engines/production/pyproject.toml packages/engines/production/
COPY packages/engines/transportation/pyproject.toml packages/engines/transportation/
COPY packages/engines/inventory/pyproject.toml packages/engines/inventory/
COPY packages/validators/pyproject.toml packages/validators/
RUN uv sync --locked --no-dev --no-install-workspace --package nasq-api

COPY packages/core packages/core
COPY apps/api apps/api
RUN uv sync --locked --no-dev --no-editable --package nasq-api

RUN useradd --system --uid 10001 --no-create-home nasq
USER nasq

EXPOSE 8000
CMD ["uvicorn", "--factory", "nasq_api.main:app_factory", "--host", "0.0.0.0", "--port", "8000", "--no-access-log"]
