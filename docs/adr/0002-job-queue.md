# ADR-002: Durable job queue for solves and outbox

- Status: Proposed (decide in task P0-03)
- Date: 2026-11-22
- Deciders: Tech lead, product owner
- PRD: §22, §23, §25

## Context

Solves can run for minutes, must survive browser closure and worker crashes, support cancellation and deduplication, and respect per-organization concurrency limits (RUN01, §25). The outbox dispatcher needs the same durability.

## Options considered

1. Postgres-backed queue (for example procrastinate, or a custom SKIP LOCKED table): no extra infrastructure, transactional enqueue with business data.
2. Redis with Dramatiq or Celery: mature, fast, but a second datastore and no transactional enqueue.
3. Managed cloud queue: depends on hosting choice (ADR-007).

## Recommended decision

Option 1, because enqueueing inside the same database transaction as the business change removes a whole class of consistency bugs, and the expected volume is modest.

## Consequences

Fair scheduling per organization must be implemented in the dequeue query. Very high job volume may later need a dedicated broker.

## Evidence required before acceptance

Spike (P0-03): enqueue in a transaction, cancel a running solve within 2 seconds, recover after killing a worker, fairness between two organizations.

## Revisit when

If queue latency or database load becomes a bottleneck under measured pilot load (P11-04).
