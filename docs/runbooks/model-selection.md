# Which model to use

Model names change. Check what your plan offers before starting, and update this file when it changes.

## Claude Code (lead engineer)

Claude Code lets you choose the model for a session (in current versions with the `/model` command; see https://docs.claude.com/en/docs/claude-code/overview if it differs).

| Tier | Model | Use for |
|---|---|---|
| Deep | **Claude Opus 5.5** | Architecture decisions, tenancy and authorization, plan lifecycle and approval, outbox, all engine formulations and engine code, explanation and diagnosis, financial logic, security hardening, release audits. Anything where a subtle mistake is expensive. |
| Standard | **Claude Sonnet 5.5** | Repository scaffold, data model from an approved dictionary, frontend foundation, deployment scripts, acceptance documents, reviews of standard-tier Codex work. |
| Quick | **Claude Haiku 5.5** | Small edits: updating task status, fixing typos in docs, renaming, formatting. Not for features. |
| Optional | **Claude Fable 5.2** | If your plan includes it, consider it for the hardest reasoning tasks (engine formulations P5-01, P13-01, P14-01 and the threat model P11-01). Check availability and cost first. |

## Codex (implementation engineer and checker)

Use the strongest coding model your Codex plan offers. Where Codex lets you set reasoning effort:

| Tier | Setting | Use for |
|---|---|---|
| Deep | Highest available reasoning effort | Validators (P4-03, P5-03, P13-04, P14-03), test and benchmark suites (P5-04), the reference-case enumerator (P0-05), authentication (P1-02), units and time (P2-03), and every review of Claude Code's deep-tier work. |
| Standard | Medium reasoning effort | CRUD APIs, import rules, reports, alerts, screens, CI, observability, backups, support tooling. |

OpenAI changes Codex model names frequently; this plan does not name one. Pick the current top coding model in Codex settings.

## Rules
- The reviewer uses at least the same tier as the author used.
- Engine tasks and their reviews are always Deep tier.
- If a standard-tier session struggles (repeated failing tests, confused plan), restart the task on Deep tier rather than pushing on.
- Humans, not models, sign the human gates.
