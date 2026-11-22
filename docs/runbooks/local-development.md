# Local development

How to run Nasq on a developer machine (Linux, macOS or Windows).

## Prerequisites

| Tool | Version | Notes |
|---|---|---|
| Git | 2.40 or later | |
| Docker Desktop or Docker Engine with Compose v2 | Docker 25+, Compose 2.20+ | Must be running before `make dev`. |
| uv | 0.11 or later | Installs and pins Python 3.12 itself (`.python-version`). |
| Node.js and npm | Node 24 LTS (`>=24.21 <25`), npm 11 | |
| GNU Make | 4.x | On Windows: `winget install GnuWin32.Make` or use Git Bash. |
| gitleaks | 8.30 or later | Used by `make lint` (`make secrets`). |

Python itself does not need to be on `PATH`: `uv` downloads and uses 3.12.

## First run

```sh
make install     # uv sync + npm ci
make dev         # builds images, starts every service, waits for health, runs migrations
make test-stack  # confirms /readyz returns 200 and every service answers
```

No `.env` file is needed: `docker-compose.yml` defaults every password to the `CHANGE_ME`
placeholder, which is acceptable only on your machine. To change values, copy `.env.example`
to `.env` (it is git-ignored) and edit it. Never commit `.env`.

## Services

| Service | URL on your machine | Purpose |
|---|---|---|
| api | http://localhost:8000 (`/healthz`, `/readyz`, `/docs`) | FastAPI application service |
| worker | no port; healthcheck via heartbeat file | Background worker. Runs no jobs until P4-01. |
| web | http://localhost:5173 | Vue web application (Vite dev server) |
| postgres | localhost:5432, database `veltrix` | PostgreSQL 16 |
| mailpit | http://localhost:8025 (SMTP on 1025) | Captures outgoing email locally |
| rustfs | http://localhost:9000 (console on 9001) | S3-compatible object storage (ADR-006) |

All ports bind to `127.0.0.1` only. P0-01 named MinIO for object storage, but MinIO no longer
publishes community images, so the local stack uses RustFS (Apache-2.0, S3-compatible).

If another program already uses one of these ports, set the matching variable in `.env`
(`POSTGRES_HOST_PORT`, `API_HOST_PORT`, `WEB_HOST_PORT`, `MAILPIT_HOST_PORT`, `SMTP_HOST_PORT`,
`STORAGE_HOST_PORT`, `STORAGE_CONSOLE_HOST_PORT`). `make test-stack` reads the matching URLs
from `NASQ_STACK_API_URL`, `NASQ_STACK_WEB_URL`, `NASQ_STACK_MAILPIT_URL` and
`NASQ_STACK_STORAGE_URL`.

Database roles: `veltrix_owner` owns the schema and runs migrations (`DATABASE_MIGRATION_URL`).
`veltrix_app` is what the API and worker use; it cannot bypass row-level security (ADR-004).

## Everyday commands

| Command | What it does |
|---|---|
| `make test` | Python unit tests for every package plus Vitest for the web app |
| `make lint` | ruff, ruff format check, import-linter, ESLint, Prettier and gitleaks |
| `make typecheck` | mypy `--strict` and `vue-tsc` |
| `make migrate` | `alembic upgrade head` inside the api container |
| `make e2e` | Playwright browser tests (run `npx playwright install chromium` once first) |
| `make bench` | Reports that no benchmarks exist yet (P5-04 adds them) |
| `make down` | Stops the stack; add `docker compose down -v` to delete local data |

## Health endpoints

- `GET /healthz` returns 200 while the API process runs. It never touches the database.
- `GET /readyz` returns 200 only when the database and the queue are reachable, otherwise a
  503 `application/problem+json` response listing which check failed. Until ADR-002 is
  accepted the queue check tests the Postgres connection the recommended queue will use.

## Troubleshooting

| Symptom | Fix |
|---|---|
| `failed to connect to the docker API` | Start Docker Desktop and wait until `docker info` shows a server version. |
| `make dev` times out waiting for `api` | `docker compose logs api postgres`; usually Postgres is still initialising or a port is in use. |
| `Bind for 0.0.0.0:5432 failed: port is already allocated` | Another program uses that port. Set `POSTGRES_HOST_PORT` (or the matching `*_HOST_PORT`) in `.env` and run `make dev` again. |
| Postgres role errors after changing passwords | The init script runs only on a new volume: `docker compose down -v`, then `make dev`. |
| `python` opens the Microsoft Store on Windows | Use `uv run python`, or disable the App execution aliases for python.exe in Windows Settings. |
