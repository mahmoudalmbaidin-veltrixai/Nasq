# Bug fix

When: A defect found in review, QA or the pilot.

```text
Bug in Veltrix: <one-line summary>. Related task: <TASK-ID>. PRD reference: <§>.
Observed: <what happened, with run id, org-free reproduction data>. Expected: <behaviour from PRD or acceptance criterion>.
1. Write a failing regression test that reproduces the bug using synthetic data only.
2. Find the root cause and explain it in the PR in plain words.
3. Fix it with the smallest change that respects CLAUDE.md/AGENTS.md non-negotiables.
4. Check whether the same cause exists elsewhere (search the repo) and list the places.
5. Run the full test suite and, if engine code changed, `make bench` and attach the regression comparison.
```
