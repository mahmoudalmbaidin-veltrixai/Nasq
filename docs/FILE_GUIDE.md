# File guide

Every file in this pre-development kit: what it is for, who works on it, which AI model to use with it, when it is needed and what you must do.

Status: **Ready to use** = use as is. **Draft: approve** = a person must review and approve it. **You fill in** = a person must complete it.

## Before day one

1. Read README.md and this guide. (`README.md`, 15 minutes)
2. Name the people: product owner, tech lead, OR specialist, customer owners. Record them in the decisions log and the RACI. (`docs/decisions-log.md`, Humans)
3. Make the remaining decisions in the log, at least the pilot customer and the first operating family. (`docs/decisions-log.md`, Humans)
4. Create the Git repository, copy this kit into it and commit it as the first commit. (`README.md`, Tech lead)
5. Replace the example handles in CODEOWNERS with real users. (`.github/CODEOWNERS`, Tech lead)
6. Set up Claude Code and Codex access to the repository and check which models your plans offer. (`docs/runbooks/model-selection.md`, Tech lead)
7. Send the fit questionnaire and the data request checklist to the pilot customer. (`docs/pilot/fit-assessment-questionnaire.md`, Product owner)
8. Send the data protection questions to a specialist. (`docs/security/jordan-data-protection-questions.md`, Tech lead)
9. Read the draft data dictionary, source-of-truth matrix, state machines and permissions; note corrections for P0-04. (`docs/data-dictionary/README.md`, Product owner)
10. Open issues for sprint S0 (P0-01 to P0-05) and start P0-01 with Claude Code on Claude Sonnet 5.5. (`docs/tasks/P0-01.md`, Tech lead)

## Which model for what

| Who | Model | Use for |
|---|---|---|
| Claude Code, deep tier | Claude Opus 5.5 | Architecture, tenancy, authorization, lifecycle, approval, outbox, engines and formulations, diagnosis, finance, security, release audit |
| Claude Code, standard tier | Claude Sonnet 5.5 | Scaffold, data model from approved dictionary, frontend foundation, Gantt, deployment, acceptance pack |
| Claude Code, quick | Claude Haiku 5.5 | Small doc edits and status updates only |
| Claude Code, optional | Claude Fable 5.2 | The hardest reasoning (formulations, threat model) if your plan includes it |
| Codex, deep tier | Top coding model, highest reasoning effort | Validators, test and benchmark suites, enumerator, authentication, units and time, reviews of deep-tier work |
| Codex, standard tier | Top coding model, medium reasoning effort | CRUD, import rules, reports, alerts, screens, CI, observability, backups, support tooling |
| Humans | None | Every human gate, decisions log, pilot and legal documents |

## Start here

| File | Status | Purpose | Who works on it | Model | When | Your action |
|---|---|---|---|---|---|---|
| `README.md` | Ready to use | Front page of the repository: what Veltrix is and where to start. | Human | Any model can read it; no edits needed | Before day one | Read it first. |
| `docs/FILE_GUIDE.md` | Ready to use | This guide as a Markdown file inside the repository, so the team and the agents can find it. | Tech lead | Claude Haiku 5.5 for small updates | Always | Update it when you add a new kind of file. |
| `docs/decisions-log.md` | You fill in | The twelve decisions that must be made by named people before coding: pilot customer, OR specialist, hosting, tech lead and more. | Product owner and tech lead | No AI needed. Humans decide. | Before day one | Fill in Decision, Owner and Date for every row. |

## Agent context

| File | Status | Purpose | Who works on it | Model | When | Your action |
|---|---|---|---|---|---|---|
| `CLAUDE.md` | Ready to use | Instructions Claude Code reads automatically every session: stack, commands, non-negotiable rules and how it must work. | Tech lead | Read by Claude Code (all models) | Every Claude Code session | Keep at the repository root. Edit only through a reviewed PR. |
| `AGENTS.md` | Ready to use | The same for Codex: rules, commands and the independence rule for validators. | Tech lead | Read by Codex | Every Codex task | Keep at the repository root. |
| `docs/runbooks/agent-workflow.md` | Ready to use | Step-by-step: how to run one task from kickoff prompt to merge with both agents. | Tech lead | Humans follow it | Every task | Read once; keep it open during the first sprint. |
| `docs/runbooks/model-selection.md` | Ready to use | Which Claude and Codex model to use for each kind of work, and why. | Tech lead | Humans follow it | Every task | Check model names against your plans and update if they change. |

## Product requirements

| File | Status | Purpose | Who works on it | Model | When | Your action |
|---|---|---|---|---|---|---|
| `docs/prd/PRD_v1.0_EN.md` | Ready to use | The full product specification in English. Every task cites its sections (§). | Product owner | Read by both agents | Throughout | Change only through the product owner. |
| `docs/prd/PRD_v1.0_AR.md` | Ready to use | The Arabic edition of the same specification. | Product owner | Human reference | Throughout | Keep in sync with the English edition. |

## Plan and tasks

| File | Status | Purpose | Who works on it | Model | When | Your action |
|---|---|---|---|---|---|---|
| `docs/plan/Veltrix_Engineering_Plan.docx` | Ready to use | The master engineering plan (editable): team model, protocol, architecture, sprints, every task with prompts. | Tech lead | Humans | Throughout | Edit here first when scope changes, then update the task file. |
| `docs/plan/veltrix-system-map.html` | Ready to use | Interactive overview, guided tour and mind map of the whole platform. | Tech lead | Humans; share with anyone | Onboarding | Open in a browser. Share with new team members and customers. |
| `docs/plan/roadmap.md` | Ready to use | Phases, sprint plan and the Release 1 gate checklist in Markdown. | Tech lead | Claude Sonnet 5.5 for the end-of-sprint status | Every sprint | Tick the release gate items as evidence arrives. |
| `docs/plan/traceability.md` | Ready to use | Each requirement ID, the tasks that prove it, and an evidence column. | Tech lead | Claude Opus 5.5 in P12-01 (release audit) | Every sprint | Paste CI or PR links into Evidence as requirements pass. |
| `docs/tasks/ (69 files)` | Ready to use | One file per task: owner, recommended model, reviewer, dependencies, human gate, build prompt and review prompt. | Tech lead | The model named inside each file | Per task | Paste the prompts into the agents. Set Status and PR when done. |
| `prompts/ (6 files)` | Ready to use | Standing prompts: session kickoff for each agent, bug fix, engine regression, sprint status, disagreement resolution. | Tech lead | Named in each prompt | When the situation occurs | Use the kickoff prompt at the start of every session. |

## Decisions and data contracts

| File | Status | Purpose | Who works on it | Model | When | Your action |
|---|---|---|---|---|---|---|
| `docs/adr/0001 to 0007` | Draft: approve | Seven proposed architecture decisions: modular monolith, job queue, authentication, tenant isolation, solver stack, file storage, hosting. | Tech lead and product owner | Claude Opus 5.5 completes them in P0-03 with spike evidence | Sprint S0 | Read the recommendations now; accept or change them when P0-03 delivers evidence. |
| `docs/adr/0000-template.md` | Ready to use | Template for any new decision. | Tech lead | Claude Sonnet 5.5 | When a new decision arises | Copy it for new ADRs. |
| `docs/data-dictionary/ (10 files)` | Draft: approve | Draft definition of every entity and field from PRD §9: types, units, rules. | Product owner | Claude Opus 5.5 finalises it in P0-04 | Sprint S0 | Review against your pilot data; approve in the P0-04 PR. |
| `docs/sot-matrix.yaml` | Draft: approve | Which system owns each piece of data, who edits it and how fresh it must be. | Product owner | Claude Opus 5.5 in P0-04 | Sprint S0 | Confirm the owners match the pilot customer's systems. |
| `docs/state-machines/ (3 files)` | Draft: approve | Allowed states and transitions for solves, result statuses and plans. | Product owner and tech lead | Claude Opus 5.5 in P0-04 | Sprint S0 | Approve in the P0-04 PR; code is generated from these. |
| `docs/permissions.yaml` | Draft: approve | Who may do what, for the eight roles in PRD §6. | Product owner | Claude Opus 5.5 implements it in P1-03 | Sprint S1 | Check each role against how the pilot customer works. |
| `docs/coverage-register.yaml` | Draft: approve | Honest list of what each template supports and excludes, and how large a problem it was tested on. | Product owner | Codex (medium) builds the tooling in P3-02 | Before any sale | Keep status planned until validation is complete. |

## Engines

| File | Status | Purpose | Who works on it | Model | When | Your action |
|---|---|---|---|---|---|---|
| `docs/engines/README.md` | Ready to use | Index of engines with their formulation, engine and validator tasks. | OR specialist | Humans | Reference | None. |
| `docs/engines/production/formulation.md` | You fill in | Template for the production engine mathematics. Must be signed before engine code is written. | OR specialist | Claude Opus 5.5 writes it in P5-01 (Claude Fable 5.2 if available) | Sprint S1 | OR specialist reviews and signs it. |
| `docs/engines/production/thresholds.yaml` | You fill in | Regression limits for engine changes. | OR specialist | Codex (high reasoning) uses it in P5-04 | Sprint S4 | OR specialist sets the objective regression limit. |

## Governance

| File | Status | Purpose | Who works on it | Model | When | Your action |
|---|---|---|---|---|---|---|
| `docs/definition-of-done.md` | Ready to use | The ten conditions every task must meet before it is done. | Tech lead | Both agents check it | Every PR | Enforce it at merge. |
| `docs/risk-register.md` | Draft: approve | The PRD §33 risks with controls, tasks and owners. | Tech lead | Claude Sonnet 5.5 in the sprint status | Every sprint | Assign owners; review at each sprint end. |
| `docs/team-raci.md` | Ready to use | Who does, signs, is consulted and informed for each activity. | Product owner | Humans | Before day one | Put real names next to each role. |
| `docs/glossary.md` | Ready to use | Plain definitions of the terms used across the project. | Product owner | Any | Reference | None. |

## Pilot customer and legal

| File | Status | Purpose | Who works on it | Model | When | Your action |
|---|---|---|---|---|---|---|
| `docs/pilot/fit-assessment-questionnaire.md` | You fill in | Questions for the pilot customer to confirm the problem, data and people exist before building for them. | Product owner | No AI needed | Sprint S0 (in parallel) | Run the interview and record answers. |
| `docs/pilot/data-request-checklist.md` | You fill in | Exactly which data to request from the pilot, and how to handle it safely. | Product owner | No AI needed | Sprint S0 | Send to the customer; tick items as received. Never commit customer data. |
| `docs/security/jordan-data-protection-questions.md` | You fill in | Twelve questions for a data protection specialist before choosing hosting. | Tech lead | No AI needed | Before ADR-007 | Send to the specialist and record answers. |

## Repository settings

| File | Status | Purpose | Who works on it | Model | When | Your action |
|---|---|---|---|---|---|---|
| `.github/pull_request_template.md` | Ready to use | Every PR gets the traceability table and the Definition of Done checklist. | Tech lead | Filled by the authoring agent | Every PR | None. |
| `.github/ISSUE_TEMPLATE/ (3 files)` | Ready to use | Templates for plan tasks, bugs and change requests. | Tech lead | Humans | When opening issues | Create one task issue per file in docs/tasks. |
| `.github/CODEOWNERS` | You fill in | Routes engine, data and PRD changes to the right human reviewers. | Tech lead | No AI needed | Before day one | Replace the example @handles with real GitHub users or teams. |
| `.env.example` | Ready to use | Placeholder environment settings for local development. No real secrets. | Tech lead | Claude Sonnet 5.5 extends it in P0-01 | Sprint S0 | Never put real values here. |
| `.gitignore and .editorconfig` | Ready to use | Keep secrets and customer data out of Git; consistent formatting. | Tech lead | None | Always | None. |

## Task files and their models

| Task | Title | Owner | Model | Reviewer model |
|---|---|---|---|---|
| P0-01 | Repository scaffold and engineering conventions | Claude Code | Claude Sonnet 5.5 | Codex, medium reasoning effort |
| P0-02 | CI pipeline and quality gates | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P0-03 | Architecture decisions and technical spike | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort |
| P0-04 | Data dictionary, source-of-truth matrix and state machines | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort |
| P0-05 | Reference case library and synthetic data generator | Codex | Codex, top coding model, highest reasoning effort | Claude Opus 5.5 |
| P1-01 | Tenancy and organization isolation | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort |
| P1-02 | Authentication, invitations and sessions | Codex | Codex, top coding model, highest reasoning effort | Claude Opus 5.5 |
| P1-03 | Authorization: role and site policy | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort |
| P1-04 | Audit trail | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P1-05 | Platform administration and engine entitlements | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P2-01 | Shared data model and migrations | Claude Code | Claude Sonnet 5.5 | Codex, medium reasoning effort |
| P2-02 | Master data APIs | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P2-03 | Units, currencies and time module | Codex | Codex, top coding model, highest reasoning effort | Claude Opus 5.5 |
| P2-04 | Import pipeline: staging, mapping, preview, publish | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort |
| P2-05 | Validation rules and error reporting | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P2-06 | Data versions, snapshots and freshness | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P2-07 | Secure file handling and safe exports | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P3-01 | Objectives and constraints configuration | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort |
| P3-02 | Industry templates and coverage register | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P4-01 | Solve job service | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort |
| P4-02 | Engine interface, solve contract and honest statuses | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort |
| P4-03 | Independent validation framework and approval gate | Codex | Codex, top coding model, highest reasoning effort | Claude Opus 5.5 |
| P5-01 | Production formulation specification | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort |
| P5-02 | Production engine with CP-SAT | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort |
| P5-03 | Production independent validator | Codex | Codex, top coding model, highest reasoning effort | Claude Opus 5.5 |
| P5-04 | Production test and benchmark suite | Codex | Codex, top coding model, highest reasoning effort | Claude Opus 5.5 |
| P5-05 | Production replanning and disruption handling | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort |
| P5-06 | Production results, indicators and reasons | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P6-01 | Plan versioning and lifecycle | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort |
| P6-02 | Concurrency-safe approval | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort |
| P6-03 | Scenarios and comparison | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P6-04 | Manual edit and revalidation | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P7-01 | Transactional outbox, idempotency and reconciliation | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort |
| P7-02 | Approved plan export and manual execution record | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P7-03 | Execution events | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P7-04 | Public integration API v1 | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P8-01 | Explanation and infeasibility diagnosis | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort |
| P9-01 | KPI registry and measurement | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P9-02 | Financial impact and ROI | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort |
| P9-03 | Reports and exports | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P9-04 | Alerts and notifications | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P10-01 | Frontend foundation, i18n and RTL | Claude Code | Claude Sonnet 5.5 | Codex, medium reasoning effort |
| P10-02 | Screens: sign in, operations overview, administration and integration | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P10-03 | Screens: data center and master data | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P10-04 | Screens: engine configuration and planning workspace | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P10-05 | Production results Gantt with lock, edit and revalidation | Claude Code | Claude Sonnet 5.5 | Codex, medium reasoning effort |
| P10-06 | Screens: approvals, execution monitoring, impact and reports | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P10-07 | End-to-end and accessibility quality | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P11-01 | Security hardening, threat model and privacy | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort |
| P11-02 | Observability | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P11-03 | Backup, restore and recovery runbook | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P11-04 | Performance and fairness testing | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P11-05 | Deployment, environments and release process | Claude Code | Claude Sonnet 5.5 | Codex, medium reasoning effort |
| P12-01 | Release readiness audit and acceptance matrix | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort |
| P12-02 | Pilot onboarding and parallel-run tooling | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P12-03 | Support tooling | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P12-04 | Operational acceptance pack | Claude Code | Claude Sonnet 5.5 | Codex, medium reasoning effort |
| P13-01 | Routing formulation specification | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort |
| P13-02 | Road travel-time provider adapter | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P13-03 | Routing engine | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort |
| P13-04 | Route independent validator | Codex | Codex, top coding model, highest reasoning effort | Claude Opus 5.5 |
| P13-05 | Transportation replanning | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort |
| P13-06 | Transportation screens | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P14-01 | Inventory formulation specification | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort |
| P14-02 | Inventory engine | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort |
| P14-03 | Inventory independent validator | Codex | Codex, top coding model, highest reasoning effort | Claude Opus 5.5 |
| P14-04 | Purchase and transfer proposals, ERP submission and inventory screens | Codex | Codex, top coding model, medium reasoning effort | Claude Sonnet 5.5 |
| P14-05 | Engine orchestration and handoffs | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort |
| P15-01 | Explanation assistant (deferred extension) | Claude Code | Claude Opus 5.5 | Codex, highest reasoning effort |

## Created later by the agents

| File or folder | Task | Built by |
|---|---|---|
| Makefile, docker-compose.yml, pyproject.toml, package.json, apps/, packages/ | P0-01 | Claude Code |
| .github/workflows/ (CI) | P0-02 | Codex |
| tests/reference-cases/ and the synthetic data generator | P0-05 | Codex |
| Generated enums and types from the YAML contracts | P0-04 | Claude Code |
| Accepted ADR-001 to ADR-007 with spike evidence | P0-03 | Claude Code |
| docs/security/threat-model.md | P11-01 | Claude Code |
| docs/runbooks/ci.md, events.md, recovery.md | P0-02, P7-03, P11-03 | Codex |
| docs/engines/transportation/ and docs/engines/inventory/ | P13-01, P14-01 | Claude Code |
| docs/performance/ results | P11-04 | Codex |
