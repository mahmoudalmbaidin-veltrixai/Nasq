# Decisions needed before development (PRD §33 initial decisions)

Fill in the Decision, Owner and Date columns before sprint S0 ends. These are planning assumptions until a named person decides them.

| # | Decision | Recommendation from the plan | Decision | Owner | Date |
|---|---|---|---|---|---|
| 1 | First operating family | Batch production with defined operations and known alternative lines (§33) | | Product owner | |
| 2 | Pilot customer | One customer able to provide a data sample and an operations owner (§7) | | Product owner | |
| 3 | Release model | Human-reviewed release with file export first; integrations later (§18) | | Product owner | |
| 4 | Hosting environment and data location | Decide after the data protection questions are answered (ADR-007) | | Tech lead | |
| 5 | Optimization owner | Name the OR specialist who signs formulations (§29) | | Product owner | |
| 6 | Tech lead and merge authority | Name the person who merges PRs and owns security review | | Product owner | |
| 7 | Git hosting and CI | GitHub with Actions (assumed by .github files) | | Tech lead | |
| 8 | AI tool accounts | Claude Code and Codex seats for the people running tasks; budget per sprint | | Tech lead | |
| 9 | Authentication approach | Built-in with MFA for Release 1 (ADR-003) | | Tech lead | |
| 10 | Job queue | Postgres-backed queue (ADR-002) | | Tech lead | |
| 11 | Language of the UI at launch | Arabic and English both required (§1, §8) | | Product owner | |
| 12 | Prove a sample solve before widening the interface | Yes: vertical slice first (§34) | | Tech lead | |
