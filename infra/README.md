# infra

Infrastructure used by the local stack in `docker-compose.yml`.

| Path | Purpose |
|---|---|
| `postgres/init/01-roles.sh` | Creates `veltrix_app`, the role the API and worker connect as. It has no superuser rights and no `BYPASSRLS` (ADR-004). Runs only when the Postgres volume is first created. |

Local object storage is RustFS (`rustfs/rustfs:1.0.6`), replacing MinIO, whose community images
are no longer published.

Deployment environments are defined in P11-05 after the hosting decision (ADR-007).
