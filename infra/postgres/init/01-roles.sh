#!/bin/sh
# Runs once, when the local Postgres volume is first created.
# POSTGRES_USER (veltrix_owner) owns the schema and runs migrations.
# veltrix_app is what the API and worker use: it owns nothing and cannot bypass
# row-level security (ADR-004). Table privileges arrive with P1-01 and P2-01.
set -eu

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" \
  --set app_password="$DATABASE_APP_PASSWORD" <<'SQL'
CREATE ROLE veltrix_app LOGIN PASSWORD :'app_password'
  NOSUPERUSER NOCREATEDB NOCREATEROLE NOBYPASSRLS;
SELECT format('GRANT CONNECT ON DATABASE %I TO veltrix_app', current_database()) \gexec
GRANT USAGE ON SCHEMA public TO veltrix_app;
SQL
