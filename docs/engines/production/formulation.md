# Production engine formulation (template)

Status: TEMPLATE. Claude Code fills it in task P5-01; the OR specialist signs it before any engine code is written.

## 1. Scope and exclusions
In scope: batch production with defined operations and known alternative lines (§12).
Excluded: long-range aggregate planning, continuous manufacturing, furnace physics, joint products.

## 2. Sets and indices
## 3. Parameters (with units and data dictionary references)
## 4. Decision variables
## 5. Constraints
For each: name, mathematical form, unit, hard or soft, penalty, PRD source.

## 6. Objectives and their combination
Lexicographic order or normalized weights (§11). No unexplained mixed-unit weights.

## 7. CP-SAT mapping
Intervals, presence literals, NoOverlap, circuit or transition constraints, reservoir constraints, objective handling.

## 8. Traceability to the PRD §12 rules table

| §12 rule | Constraint(s) in this document | Validator rule (P5-03) |
|---|---|---|
| Line compatibility | | |
| No overlap | | |
| Operation precedence | | |
| Changeover time | | |
| Working calendar | | |
| Materials | | |
| Due dates | | |
| Frozen plan | | |

## 9. Worked tiny example (must match the enumerator in tests/reference-cases)
## 10. Scaling estimates and known limitations
## 11. Sign-off
OR specialist: ______  Date: ______
