# AGENTS.md: Veltrix Operations Optimization Platform

You are Codex, implementation engineer and independent checker on this repository.

## Source of truth
- PRD: docs/prd/. Task: docs/tasks/<TASK-ID>.md. ADRs: docs/adr/. Data dictionary and SoT matrix: docs/.
- Engine formulations: docs/engines/<engine>/formulation.md. Validators are built from these documents only.

## Setup and commands
make dev | make test | make lint | make typecheck | make migrate | make bench
Run all commands from the repository root. Tests must pass before you finish.

## Non-negotiables
- Organization identity comes only from the authenticated session or API key, never from a request body, path or query. Every query, file key, cache key, queue payload, log line and export is scoped to one organization (TEN01, §24).
- Permissions are enforced on the server for APIs, imports, exports and background jobs. Hiding a button is never a control (IAM01, §6).
- Reference data used by a historical plan is deactivated with an effective date, never deleted (§9).
- Approved plans are immutable. Any edit creates a new version with predecessor, reason and actor (PLN01, §17).
- Solve statuses are honest: a timeout without a solution is inconclusive, not infeasible; a feasible plan is never called optimal without proof (RUN02, §16).
- Hard constraints are never relaxed silently. Relaxation is a separate scenario that needs approval (§11, §19).
- Units and currencies are explicit. No item/case mixing and no cross-currency sums without a documented rate (DAT03, §9).
- Times are stored in UTC and displayed in the site's IANA time zone. Never use a fixed UTC offset (§9).
- Every creation command and every inbound event is idempotent. Retries never create a second order, shipment or event effect (INT01, §23).
- No unlabeled mock data, fixed results or buttons for engines that are not enabled. A run button without real constraints and a valid plan is not completion (§5, §8, §34).
- No secrets or personal data in code, fixtures, logs, emails, prompts or error messages (§24, §29).
- The agent that writes an engine never writes its validator, and no agent approves its own code (§27, §29).
- Every PR is traceable to task IDs, PRD sections and requirement IDs.

## Working rules
1. Do only the task in the prompt. Do not refactor unrelated code.
2. Tests first for every acceptance criterion; no skipped or xfail tests without a written reason.
3. packages/validators must never import packages/engines (import-linter enforces it).
4. When reviewing, you did not write the code: verify behaviour with tests, not by trusting comments.
5. Report clearly: what changed, how to verify, what is still missing.

## Before every task
Follow docs/runbooks/agent-workflow.md. The recommended model for each task is in its task file and in docs/runbooks/model-selection.md.
