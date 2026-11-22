# Task files

One file per task. Each holds the build prompt for the owner agent and the review prompt for the other agent. Update Status and PR as work progresses.

| Task | Title | Owner | Model | Reviewer model | Depends on |
|---|---|---|---|---|---|
| [P0-01](P0-01.md) | Repository scaffold and engineering conventions | Claude Code | Claude Sonnet 5.5 | Codex, medium reasoning effort | - |
| [P0-02](P0-02.md) | CI pipeline and quality gates | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P0-01 |
| [P0-03](P0-03.md) | Architecture decisions and technical spike | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort | P0-01 |
| [P0-04](P0-04.md) | Data dictionary, source-of-truth matrix and state machines | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort | P0-01 |
| [P0-05](P0-05.md) | Reference case library and synthetic data generator | Codex | Codex, top coding model, highest reasoning effort | Claude Opus 5.5 | P0-04 |
| [P1-01](P1-01.md) | Tenancy and organization isolation | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort | P0-03, P0-04 |
| [P1-02](P1-02.md) | Authentication, invitations and sessions | Codex | Codex, top coding model, highest reasoning effort | Claude Opus 5.5 | P1-01, P0-03 |
| [P1-03](P1-03.md) | Authorization: role and site policy | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort | P1-01, P1-02 |
| [P1-04](P1-04.md) | Audit trail | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P1-01 |
| [P1-05](P1-05.md) | Platform administration and engine entitlements | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P1-03 |
| [P2-01](P2-01.md) | Shared data model and migrations | Claude Code | Claude Sonnet 5.5 | Codex, medium reasoning effort | P0-04, P1-01 |
| [P2-02](P2-02.md) | Master data APIs | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P2-01, P1-03, P1-04 |
| [P2-03](P2-03.md) | Units, currencies and time module | Codex | Codex, top coding model, highest reasoning effort | Claude Opus 5.5 | P2-01 |
| [P2-04](P2-04.md) | Import pipeline: staging, mapping, preview, publish | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort | P2-01, P2-03 |
| [P2-05](P2-05.md) | Validation rules and error reporting | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P2-03 |
| [P2-06](P2-06.md) | Data versions, snapshots and freshness | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P2-04 |
| [P2-07](P2-07.md) | Secure file handling and safe exports | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P1-03 |
| [P3-01](P3-01.md) | Objectives and constraints configuration | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort | P0-04, P2-01 |
| [P3-02](P3-02.md) | Industry templates and coverage register | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P3-01 |
| [P4-01](P4-01.md) | Solve job service | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort | P0-03, P1-03, P2-06 |
| [P4-02](P4-02.md) | Engine interface, solve contract and honest statuses | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort | P4-01, P3-01 |
| [P4-03](P4-03.md) | Independent validation framework and approval gate | Codex | Codex, top coding model, highest reasoning effort | Claude Opus 5.5 | P4-02 |
| [P5-01](P5-01.md) | Production formulation specification | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort | P0-04, P0-05 |
| [P5-02](P5-02.md) | Production engine with CP-SAT | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort | P5-01, P4-02 |
| [P5-03](P5-03.md) | Production independent validator | Codex | Codex, top coding model, highest reasoning effort | Claude Opus 5.5 | P5-01, P4-03 |
| [P5-04](P5-04.md) | Production test and benchmark suite | Codex | Codex, top coding model, highest reasoning effort | Claude Opus 5.5 | P5-02, P5-03 |
| [P5-05](P5-05.md) | Production replanning and disruption handling | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort | P5-02, P6-01, P7-03 |
| [P5-06](P5-06.md) | Production results, indicators and reasons | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P5-02 |
| [P6-01](P6-01.md) | Plan versioning and lifecycle | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort | P0-04, P4-02 |
| [P6-02](P6-02.md) | Concurrency-safe approval | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort | P6-01, P4-03, P2-06 |
| [P6-03](P6-03.md) | Scenarios and comparison | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P6-01 |
| [P6-04](P6-04.md) | Manual edit and revalidation | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P6-01, P5-03 |
| [P7-01](P7-01.md) | Transactional outbox, idempotency and reconciliation | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort | P6-02 |
| [P7-02](P7-02.md) | Approved plan export and manual execution record | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P6-02, P2-07 |
| [P7-03](P7-03.md) | Execution events | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P6-01 |
| [P7-04](P7-04.md) | Public integration API v1 | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P2-04, P7-01, P7-03 |
| [P8-01](P8-01.md) | Explanation and infeasibility diagnosis | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort | P5-02, P6-03 |
| [P9-01](P9-01.md) | KPI registry and measurement | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P5-06, P7-03 |
| [P9-02](P9-02.md) | Financial impact and ROI | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort | P9-01 |
| [P9-03](P9-03.md) | Reports and exports | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P6-03, P9-02, P2-07 |
| [P9-04](P9-04.md) | Alerts and notifications | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P2-06, P4-01, P6-02 |
| [P10-01](P10-01.md) | Frontend foundation, i18n and RTL | Claude Code | Claude Sonnet 5.5 | Codex, medium reasoning effort | P0-01, P1-02, P1-05 |
| [P10-02](P10-02.md) | Screens: sign in, operations overview, administration and integration | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P10-01, P1-02, P1-03, P7-04 |
| [P10-03](P10-03.md) | Screens: data center and master data | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P10-01, P2-02, P2-04, P2-05 |
| [P10-04](P10-04.md) | Screens: engine configuration and planning workspace | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P10-01, P3-01, P6-03, P4-01 |
| [P10-05](P10-05.md) | Production results Gantt with lock, edit and revalidation | Claude Code | Claude Sonnet 5.5 | Codex, medium reasoning effort | P10-01, P5-06, P6-04 |
| [P10-06](P10-06.md) | Screens: approvals, execution monitoring, impact and reports | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P10-01, P6-02, P7-02, P7-03, P9-01, P9-02, P9-03 |
| [P10-07](P10-07.md) | End-to-end and accessibility quality | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P10-02, P10-03, P10-04, P10-05, P10-06 |
| [P11-01](P11-01.md) | Security hardening, threat model and privacy | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort | P1-01, P1-03, P2-07, P7-04 |
| [P11-02](P11-02.md) | Observability | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P4-01 |
| [P11-03](P11-03.md) | Backup, restore and recovery runbook | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P11-05 |
| [P11-04](P11-04.md) | Performance and fairness testing | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P4-01, P5-04, P10-06 |
| [P11-05](P11-05.md) | Deployment, environments and release process | Claude Code | Claude Sonnet 5.5 | Codex, medium reasoning effort | P0-02 |
| [P12-01](P12-01.md) | Release readiness audit and acceptance matrix | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort | All R1 tasks |
| [P12-02](P12-02.md) | Pilot onboarding and parallel-run tooling | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P2-04, P6-03, P9-01 |
| [P12-03](P12-03.md) | Support tooling | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P1-03, P11-02 |
| [P12-04](P12-04.md) | Operational acceptance pack | Claude Code | Claude Sonnet 5.5 | Codex, medium reasoning effort | P12-01, P12-02 |
| [P13-01](P13-01.md) | Routing formulation specification | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort | Release 1 gate |
| [P13-02](P13-02.md) | Road travel-time provider adapter | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P13-01 |
| [P13-03](P13-03.md) | Routing engine | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort | P13-01, P13-02, P4-02 |
| [P13-04](P13-04.md) | Route independent validator | Codex | Codex, top coding model, highest reasoning effort | Claude Opus 5.5 | P13-01, P4-03 |
| [P13-05](P13-05.md) | Transportation replanning | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort | P13-03, P7-03 |
| [P13-06](P13-06.md) | Transportation screens | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P13-03, P13-05, P10-01 |
| [P14-01](P14-01.md) | Inventory formulation specification | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort | Release 2 gate |
| [P14-02](P14-02.md) | Inventory engine | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort | P14-01, P4-02 |
| [P14-03](P14-03.md) | Inventory independent validator | Codex | Codex, top coding model, highest reasoning effort | Claude Opus 5.5 | P14-01, P4-03 |
| [P14-04](P14-04.md) | Purchase and transfer proposals, ERP submission and inventory screens | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 | P14-02, P7-01, P10-01 |
| [P14-05](P14-05.md) | Engine orchestration and handoffs | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort | P14-02, P13-03, P5-02 |
| [P15-01](P15-01.md) | Explanation assistant (deferred extension) | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort | P8-01, customer demand |
