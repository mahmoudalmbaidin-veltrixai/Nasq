# Risk register (PRD §33)

Review at the end of every sprint. Owner = person accountable for the control.

| Risk | Effect | Control in the plan | Tasks | Owner | Status |
|---|---|---|---|---|---|
| All-industry scope too early | Superficial models, high support cost | One operating family first; coverage register enforced in CI | P3-02, P12-01 | Product owner | Open |
| Poor data | Plans that cannot be executed | Staged import with blocking rules; data profiler in fit assessment | P2-04, P2-05, P12-02 | Product owner | Open |
| Missing constraints | Good-looking plans that fail in the factory | Independent validator; parallel run against real plans | P4-03, P5-03, P12-02 | OR specialist | Open |
| Slow solving | Missed decision window | Per-org limits, size benchmarks, time budgets | P4-01, P5-04, P11-04 | Tech lead | Open |
| Unreliable integration | Duplicate commands or conflicting plans | Transactional outbox, idempotency keys, reconciliation | P7-01, P7-04 | Tech lead | Open |
| Separate customization per customer | Maintenance multiplies | Templates, configuration versions, change request classification | P3-02, P12-03 | Product owner | Open |
| Inflated ROI | Disputes at renewal | Exact ROI formula, zero-cost guard, finance sign-off | P9-02 | Finance owner | Open |
| Cross-customer leakage | Commercial and legal harm | Session-derived org scope, RLS, route registry tests, threat model | P1-01, P1-03, P11-01 | Tech lead | Open |
| AI-generated code accepted without real review | Hidden defects | Cross-review by the other agent, independence rule, human gates | All | Tech lead | Open |
