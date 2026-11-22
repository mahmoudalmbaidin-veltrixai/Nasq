# Team and responsibilities (PRD §29)

R = does the work, A = accountable (signs), C = consulted, I = informed.

| Activity | Claude Code | Codex | Tech lead | OR specialist | Product owner | Customer owners |
|---|---|---|---|---|---|---|
| Architecture decisions (ADRs) | R | C | A | C | C | I |
| Data dictionary and SoT matrix | R | C | C | I | A | C |
| Engine formulations | R | I | I | A | I | C |
| Engine code | R | C (review) | I | A | I | I |
| Validators | C (review) | R | I | A | I | I |
| Features, screens, reports | C (review) | R | A | I | I | I |
| Security and isolation | R | C (review) | A | I | I | I |
| Test suites and benchmarks | C | R | I | A (thresholds) | I | I |
| Release audit | R | C | A | C | A | I |
| Operational acceptance | C | C | C | C | C | A |
| Benefit attribution | I | I | I | I | C | A (finance) |

Rules:
- No agent approves its own code.
- The agent that writes an engine never writes its validator.
- A tool approving its own generated code is neither proof nor independent review (§29).
