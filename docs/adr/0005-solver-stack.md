# ADR-005: Optimization solver stack

- Status: Proposed (decide in task P0-03)
- Date: 2026-11-22
- Deciders: Tech lead, product owner, OR specialist
- PRD: §16, §22

## Context

Each engine needs a method suited to its problem. The PRD names OR-Tools as a reference and warns against forcing one solver on everything. Licences matter for commercial use.

## Options considered

Production scheduling: OR-Tools CP-SAT (Apache 2.0) or a commercial MILP solver.
Transportation: OR-Tools routing (Apache 2.0), or a commercial VRP library.
Inventory: MILP via HiGHS (MIT) or SCIP (Apache 2.0), or a commercial solver.

## Recommended decision

CP-SAT for production, OR-Tools routing for transportation, HiGHS for inventory MILP. All open source with permissive licences.

## Consequences

No licence fees, but compute, support and benchmarking costs remain (§22). Results are not guaranteed identical across versions, so solver versions are pinned and recorded with every result.

## Evidence required before acceptance

Spike measurements (time, memory, cancellation latency) recorded here. Licence review by the tech lead.

## Revisit when

When benchmarks on real pilot data miss the decision window (§25), or a customer needs a capability these solvers lack.
