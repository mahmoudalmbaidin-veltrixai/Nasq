# ADR-001: Modular monolith with background workers

- Status: Proposed (decide in task P0-03)
- Date: 2026-11-22
- Deciders: Tech lead, product owner
- PRD: §22

## Context

The PRD asks for one logical backend, one relational database and long-running calculations in background workers. It explicitly rejects starting with dozens of microservices. The team is small and mostly AI-assisted, so operational simplicity matters.

## Options considered

1. Modular monolith: one FastAPI application with clear packages, plus a worker process using the same codebase.
2. Microservices per domain (imports, solving, approvals, reporting).
3. Serverless functions for solving.

## Recommended decision

Option 1. One API application and one worker application sharing `packages/core`, with module boundaries enforced by import-linter.

## Consequences

Simple deployment and debugging. Module boundaries must be policed in CI to avoid a tangle. Solve workers can scale separately because they are a separate process.

## Evidence required before acceptance

Import-linter contracts in CI (P0-02). Spike shows API and worker sharing models without circular imports.

## Revisit when

When one module needs independent scaling or release cadence that the worker split cannot provide.
