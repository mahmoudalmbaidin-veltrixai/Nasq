# Dependency licenses

Every direct dependency is pinned to an exact version. Transitive dependencies are pinned by
`uv.lock` and `package-lock.json`. Licenses below are taken from each package's own metadata
at the pinned version. `tests/conventions/test_repository_layout.py` fails if a direct
dependency is missing from this file.

Rule for new dependencies: permissive licenses (MIT, BSD, Apache-2.0, ISC, PSF, MPL-2.0 for
development tools) are acceptable. Anything copyleft that ships with the product needs a note
here and tech lead approval in the PR. P0-02 adds an automated license allowlist check.

Status: recorded by Claude Code in P0-01 (2026-11-22). Licence review by the tech lead is part
of ADR-005 acceptance.

## Python (runtime)

| Package | Version | License | Used by | Notes |
|---|---|---|---|---|
| fastapi | 0.165.0 | MIT | apps/api | |
| uvicorn | 0.54.0 | BSD-3-Clause | apps/api | |
| alembic | 1.20.1 | MIT | apps/api | Migrations |
| pydantic | 2.14.4 | MIT | packages/core | |
| pydantic-settings | 2.16.3 | MIT | packages/core | |
| sqlalchemy | 2.1.9 | MIT | packages/core | |
| psycopg | 3.3.9 | LGPL-3.0-only | packages/core | PostgreSQL driver, used unmodified as a dynamically loaded library. LGPL obligations apply if we modify it or distribute it statically linked. Tech lead to confirm. |

`psycopg[binary]` also installs `psycopg-binary` 3.3.9 (LGPL-3.0-only), which bundles libpq
(PostgreSQL License) and OpenSSL (Apache-2.0).

## Python (development and build only)

| Package | Version | License | Used by | Notes |
|---|---|---|---|---|
| httpx2 | 2.16.2 | BSD-3-Clause | tests | Required by Starlette's TestClient (replaces httpx) |
| hypothesis | 6.170.17 | MPL-2.0 | tests | Not shipped |
| import-linter | 2.17 | BSD-2-Clause | make lint | |
| mypy | 2.4.1 | MIT | make typecheck | |
| pytest | 9.2.0 | MIT | make test | |
| pytest-cov | 7.1.0 | MIT | make test | |
| ruff | 0.17.6 | MIT | make lint | |
| hatchling | 1.33.0 | MIT | package builds | Build backend for every workspace member |

## JavaScript (runtime, shipped to the browser)

| Package | Version | License | Used by | Notes |
|---|---|---|---|---|
| vue | 3.5.46 | MIT | apps/web | |
| vue-router | 5.5.1 | MIT | apps/web | |
| pinia | 4.1.0 | MIT | apps/web | |
| vue-i18n | 11.4.23 | MIT | apps/web | |

## JavaScript (development only)

| Package | Version | License | Used by | Notes |
|---|---|---|---|---|
| vite | 8.3.8 | MIT | apps/web | Dev server and build |
| @vitejs/plugin-vue | 6.0.11 | MIT | apps/web | |
| typescript | 6.0.3 | Apache-2.0 | apps/web | Held below 6.1 because typescript-eslint 8.73 supports `<6.1.0` |
| vue-tsc | 3.3.14 | MIT | make typecheck | |
| @vue/tsconfig | 0.9.1 | MIT | apps/web | |
| @types/node | 24.19.2 | MIT | apps/web | Matches Node 24 LTS |
| vitest | 5.1.1 | MIT | make test | |
| @vue/test-utils | 2.6.0 | MIT | make test | |
| jsdom | 31.0.1 | MIT | make test | |
| @playwright/test | 1.65.1 | Apache-2.0 | make e2e | |
| eslint | 10.15.0 | MIT | make lint | |
| eslint-plugin-vue | 10.12.1 | MIT | make lint | |
| @vue/eslint-config-typescript | 14.9.0 | MIT | make lint | Brings typescript-eslint 8 |
| @vue/eslint-config-prettier | 10.2.0 | MIT | make lint | |
| prettier | 3.10.1 | MIT | make lint | |

## Container images and tools (local development)

| Image or tool | Version | License | Used by | Notes |
|---|---|---|---|---|
| postgres | 16.16-bookworm | PostgreSQL License | docker-compose | |
| python | 3.12.16-slim-bookworm | PSF-2.0 (Debian packages: various) | api and worker images | |
| node | 24.22.3-bookworm-slim | MIT (Debian packages: various) | web image | |
| ghcr.io/astral-sh/uv | 0.11.28 | Apache-2.0 or MIT | api and worker images | |
| axllent/mailpit | v1.34.0 | MIT | docker-compose | |
| quay.io/minio/minio | RELEASE.2025-09-07T16-13-09Z | AGPL-3.0 | docker-compose | Local development only, never shipped or offered over a network to customers. MinIO no longer publishes free community images; production storage is chosen with ADR-006/ADR-007. |
| gitleaks | 8.30.1 (developer machine) | MIT | make secrets | |
