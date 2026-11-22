# Nasq developer commands. Works with GNU Make on Linux, macOS and Windows (cmd or sh).
# See docs/runbooks/local-development.md.

UV ?= uv
NPM ?= npm
COMPOSE ?= docker compose
GITLEAKS ?= gitleaks
WEB := --workspace apps/web
NODE_DEPS := node_modules/.package-lock.json

.PHONY: install dev down test test-stack e2e lint secrets typecheck migrate bench

$(NODE_DEPS): package.json package-lock.json apps/web/package.json
	$(NPM) ci

install: $(NODE_DEPS)
	$(UV) sync --locked

## Start every local service and wait until each one reports healthy.
dev:
	$(COMPOSE) up --build --detach --wait
	$(MAKE) migrate

down:
	$(COMPOSE) down

## Unit tests: every Python package and the web app.
test: $(NODE_DEPS)
	$(UV) run --locked pytest
	$(NPM) run test $(WEB)

## Checks against the stack started by `make dev`.
test-stack:
	$(UV) run --locked pytest -m stack --no-cov tests/e2e

## Browser tests. Needs `npx playwright install chromium` once.
e2e: $(NODE_DEPS)
	$(NPM) run test:e2e $(WEB)

lint: $(NODE_DEPS)
	$(UV) run --locked ruff check .
	$(UV) run --locked ruff format --check .
	$(UV) run --locked lint-imports
	$(NPM) run lint $(WEB)
	$(MAKE) secrets

secrets:
	$(GITLEAKS) git --no-banner --redact --config .gitleaks.toml .
	$(GITLEAKS) dir --no-banner --redact --config .gitleaks.toml .

typecheck: $(NODE_DEPS)
	$(UV) run --locked mypy
	$(NPM) run typecheck $(WEB)

migrate:
	$(COMPOSE) run --rm --no-deps api alembic -c apps/api/alembic.ini upgrade head

bench:
	@echo No benchmarks are defined yet. The production benchmark suite arrives in P5-04.
