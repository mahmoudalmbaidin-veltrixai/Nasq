# ADR-007: Hosting environment and data location

- Status: Proposed (decide in task P0-03)
- Date: 2026-11-22
- Deciders: Tech lead, product owner
- PRD: §22, §24, §25

## Context

Start with one hosting environment. The first market is Jordan. Data protection obligations depend on data types, party roles, processing location and transfers, and must be reviewed with a specialist (§24). Hosting in a country does not by itself establish compliance.

## Options considered

1. Local Jordanian data centre or cloud region where available.
2. Major cloud provider region in the wider Middle East.
3. European region of a major cloud provider.

## Recommended decision

Not decided. Collect answers from docs/security/jordan-data-protection-questions.md and pilot customer expectations, then decide before P11-05.

## Consequences

Affects latency, cost, backup location, support access and contract terms.

## Evidence required before acceptance

Written answer from the data protection specialist; cost estimate; RPO/RTO capability (§25).

## Revisit when

When a customer's contract or regulator requires a specific location.
