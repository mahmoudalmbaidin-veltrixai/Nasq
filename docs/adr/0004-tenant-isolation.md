# ADR-004: Tenant isolation

- Status: Proposed (decide in task P0-03)
- Date: 2026-11-22
- Deciders: Tech lead, product owner
- PRD: §23, §24 (TEN01)

## Context

One customer must never see another customer's data, including in files, caches, queues, logs, exports and restored backups. The organization must never be chosen by the client.

## Options considered

1. Shared database, org_id column, application-level scoping only.
2. Shared database with org_id plus Postgres row-level security (defence in depth).
3. Database or schema per customer.

## Recommended decision

Option 2. Application scoping plus RLS policies, with the application role lacking BYPASSRLS and the org set per transaction.

## Consequences

Every org-owned table needs org_id, an index and a policy. Migrations and reports must set the org context. Per-customer databases remain possible later for customers that demand them.

## Evidence required before acceptance

Cross-tenant test harness covering every route (P1-01). Direct SQL with the app role cannot cross organizations.

## Revisit when

If a customer contract requires physical separation.
