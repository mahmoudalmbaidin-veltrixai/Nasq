# Roadmap

Two-week sprints with two parallel lanes. Durations are planning estimates, not commitments (PRD §30).

## Phases

| Phase | Name | Release | Goal | Exit criteria |
|---|---|---|---|---|
| P0 | Foundations and engineering system | R1 | A repository, CI, architecture decisions, data contracts and reference cases that every later task depends on. | ADRs, data dictionary, source-of-truth matrix and state machines approved; CI blocks bad PRs; reference cases committed. |
| P1 | Identity, tenancy and audit | R1 | Isolated organizations, trusted sign-in, role and site permissions on every path, and a tamper-resistant audit trail. | TEN01, IAM01 and AUD01 proven by automated cross-tenant and permission-matrix tests. |
| P2 | Data foundation | R1 | The shared data model, master data, safe imports, unit and time handling, snapshots and secure files. | DAT01, DAT02 and DAT03 pass; the pilot data sample imports through staging and publishes atomically. |
| P3 | Configuration and templates | R1 | Versioned objectives and constraints, and industry templates backed by a coverage register. | CFG01 passes; the batch manufacturing template exists and its coverage statement can be exported. |
| P4 | Solve service | R1 | Durable, fair, cancellable background solving with an honest result contract and an independent validation gate. | RUN01, RUN02 and RUN03 pass with the spike model. |
| P5 | Production engine | R1 | A signed formulation, a CP-SAT engine, an independent validator, benchmarks, replanning and explainable outputs. | PRD01, PRD02 and PRD03 pass on the reference set; engine proof gate signed by the OR specialist. |
| P6 | Scenarios, plan lifecycle and approval | R1 | Immutable plan versions, scenario comparison, safe manual edits and concurrency-safe approval. | PLN01 and APR01 pass, including parallel approval tests. |
| P7 | Execution and integration | R1 | Exports, execution events, a public API and an outbox that never duplicates business effects. | EXE01 and INT01 pass, including retry and duplicate-event tests. |
| P8 | Explanation and diagnosis | R1 | Explanations typed as fact, counterfactual or inference, and honest infeasibility diagnosis. | Diagnosis returns correct conflicts on infeasible reference cases and never relaxes constraints silently. |
| P9 | Indicators, finance, reports and alerts | R1 | Defined KPIs, a defensible financial impact model, core reports and deduplicated alerts. | KPI01 and FIN01 pass; reports carry scope, version, currency and units. |
| P10 | Web application | R1 | All thirteen screens in Arabic and English with correct RTL, built on a shared foundation. | End-to-end tests cover the packaging use case (§31) in both languages; accessibility checks pass. |
| P11 | Security, reliability and operations | R1 | Threat-modelled security, observability, tested restoration, measured performance and repeatable deployment. | OPS01 passes; security review and restoration exercise signed. |
| P12 | Pilot and Release 1 gate | R1 | Evidence-based release readiness, pilot onboarding, support tooling and operational acceptance. | Release 1 gate checklist fully signed. |
| P13 | Release 2: transportation engine | R2 | A road-time-based routing engine with its own validator, replanning and screens. | LOG01, LOG02 and LOG03 pass; transportation gate signed. |
| P14 | Release 3: inventory and coordination | R3 | A time-phased inventory engine, ERP proposals and traceable handoffs between engines. | INV01, INV02, INV03 and ORC01 pass; inventory gate signed. |
| P15 | Extension: explanation assistant | EXT | An optional language layer that only rephrases verified facts. Deferred until need and value are proven. | AI01 passes with separate testing; no constraint can change without approval. |

## Sprint plan

| Sprint | Weeks | Claude Code lane | Codex lane | Gate or milestone |
|---|---|---|---|---|
| S0 | 1–2 | P0-01, P0-03, P0-04 | P0-02, P0-05 | ADRs and data dictionary signed. In parallel: pilot fit assessment (§30, 2–4 weeks). |
| S1 | 3–4 | P1-01, P1-03, P5-01 | P1-02, P1-04, P1-05 | Production formulation signed by OR specialist. |
| S2 | 5–6 | P2-01, P2-04 | P2-02, P2-03, P2-05 | Import of the pilot's data sample succeeds on staging. |
| S3 | 7–8 | P3-01, P4-01, P4-02 | P2-06, P2-07, P3-02, P4-03 | Solve service runs the spike model end to end. |
| S4 | 9–10 | P5-02 | P5-03, P5-04 | Engine proof gate (§30): correct and useful on representative cases. |
| S5 | 11–12 | P6-01, P6-02, P10-01 | P5-06, P6-03, P6-04 | Vertical slice demo (§34): import, solve, validate, view, approve, export. |
| S6 | 13–14 | P5-05, P7-01 | P7-02, P7-03, P10-02, P10-03 | Replanning preserves started work on reference cases. |
| S7 | 15–16 | P8-01, P10-05 | P7-04, P9-01, P10-04 | Planner can run the full packaging use case (§31) on staging. |
| S8 | 17–18 | P9-02, P11-01 | P9-03, P9-04, P10-06 | Finance owner reviews ROI method. |
| S9 | 19–20 | P11-05 | P10-07, P11-02, P11-03, P11-04 | Security review and restoration exercise passed. |
| S10 | 21–22 | P12-01 | P12-02, P12-03 | Pilot parallel run starts with the customer. |
| S11 | 23–24+ | P12-04 | Fixes from pilot | Release 1 operational acceptance signed. |
| R2 | after R1 | P13-01, P13-03, P13-05 | P13-02, P13-04, P13-06 | Transportation engine gate (value, support, tests). |
| R3 | after R2 | P14-01, P14-02, P14-05 | P14-03, P14-04 | Inventory engine and coordination gate. |
| EXT | on demand | P15-01 | Reviews and tests | Only when need and value are established (§32). |

## Release 1 gate

- [ ] Every R1 requirement ID (TEN01 to OPS01) has passing automated tests and recorded evidence (P12-01).
- [ ] Coverage statement published for the batch manufacturing template: supported constraints, exclusions, tested sizes, last validation date (§4, §30).
- [ ] Reference acceptance set at small, medium and large sizes passes with recorded solve-time and memory distributions (§27).
- [ ] Security review completed, including cross-tenant tests on queries, files, queues, caches, logs, exports and restored backups (§24).
- [ ] Restoration exercise passed and RPO/RTO measured against the customer's cost of disruption (§25).
- [ ] Configuration documentation, runbooks and support records exist (§28, §30).
- [ ] Parallel run completed; customer operations owner signed constraints, measures and real plans (§7, §27).
- [ ] Finance owner approved the benefit attribution method; projected, actual and liquidity measures are separate (§20).
- [ ] Customer-authorized outcome reference recorded before any repeat sale (§30).
