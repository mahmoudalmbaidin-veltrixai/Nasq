# How to run a task with Claude Code and Codex

## One-time setup
1. Commit CLAUDE.md and AGENTS.md at the repository root (already in this kit).
2. Give Claude Code and Codex access to the repository (local clone for Claude Code; repository connection for Codex).
3. Create one tracker issue per task file using .github/ISSUE_TEMPLATE/task.md.

## For every task
1. **Check dependencies.** Every task listed under "Depends on" must be merged.
2. **Pick the model.** Use the model named in the task file (see docs/runbooks/model-selection.md).
3. **Start the owner agent.** New session. Paste `prompts/session-kickoff-<agent>.md`, then the build prompt from `docs/tasks/<ID>.md`.
4. **Read its plan before it codes.** The agent restates the task and lists assumptions. Correct anything wrong now; it is much cheaper than after coding.
5. **Let it work.** It writes tests first, then code, then opens a PR on `feat/<id>-<slug>`.
6. **Run the review.** New session with the other agent. Paste the review prompt from the same task file.
7. **Loop.** Blocking findings go back to the owner agent in the same branch. Two disagreements on one point: use `prompts/disagreement-resolution.md` and decide yourself.
8. **Human gate.** If the task names a person, get their approval written in the PR.
9. **Merge and record.** Squash-merge with green CI. Set Status: done and the PR link in the task file.

## Good habits
- One task per session and per PR. Long sessions drift.
- Never paste customer data, secrets or credentials into an agent.
- If an agent says "done" without test evidence, it is not done.
- Keep the PRD and the task file as the source of truth; if you change scope, change the file first.
