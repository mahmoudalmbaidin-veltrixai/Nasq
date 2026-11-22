# Engine change regression

When: Any change to a model, solver version, rounding or run profile (§27).

```text
An engine change is ready on branch <branch>. Run the regression protocol from PRD §27:
1. Run the reference acceptance set (tiny, small, medium, large) for the affected engine on main and on the branch.
2. Compare per case: result status, objective values, gap where available, validator violations, solve time p50/p95, peak memory.
3. Flag any case where status got worse, any new validator violation, objective worse by more than the threshold in docs/engines/<engine>/thresholds.yaml, or p95 time worse by more than 20%.
4. Write the comparison table into the PR and state clearly whether rollback would be needed.
Do not change thresholds yourself; propose changes for the OR specialist.
```
