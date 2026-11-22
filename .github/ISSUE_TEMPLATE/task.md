---
name: Plan task
about: One task from docs/tasks
title: "[P?-??] <task title>"
labels: task
---

**Task file:** docs/tasks/<ID>.md
**Owner agent:** Claude Code / Codex
**Reviewer agent:** Codex / Claude Code
**Recommended model:** <!-- copy from the task file -->
**Depends on:** <!-- task IDs; all must be merged first -->
**Human gate:** <!-- person, or "Tech lead merge" -->

### Steps
- [ ] Kickoff prompt run (prompts/session-kickoff-*.md)
- [ ] Build prompt run, PR opened
- [ ] Review prompt run by the other agent
- [ ] Human gate signed (if any)
- [ ] Merged; task file Status set to done with PR link
