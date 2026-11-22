Veltrix Operations Optimization Platform

Product description and requirements for the platform and operations research engines

Version 1.0 | 22 November 2026 | Proposed scope for development and commercial evaluation

# 01 Product and document purpose

A web platform for manufacturers, distributors and logistics operators that converts orders, resources, costs and constraints into operational plans that users can review, approve and execute. Decision engines use operations research and mathematical optimization. Predictive models may be added when suitable data and a demonstrated need exist. The initial market is Jordan, with Arabic and English interfaces and configurable currencies and units of measure.

This document defines the target product, coverage boundaries, data, screens, permissions, plan lifecycle, computation, integration and security requirements, acceptance criteria and release roadmap. The product name is descriptive and proposed under Veltrix AI; it does not assume approval of a new commercial brand.

A platform for multiple industries means a shared foundation, specialized engines and configurable operating templates. Coverage does not mean that any facility can upload an arbitrary file and automatically obtain a correct model. Each new operating pattern needs a fit assessment, and each new constraint needs modeling and testing before commercial support is offered.

These specifications describe an independent decision intelligence product. They do not describe Makkook's internal code, establish equivalent performance or guarantee a financial return. Software completion alone does not demonstrate operational readiness; release requires technical and operational acceptance with real customers.

# 02 Commercial product description

Veltrix Operations Optimization Platform helps organizations prepare production, distribution and inventory plans based on their actual resources and constraints. It receives data from files or existing systems, validates it and calculates operational alternatives that balance cost, delivery commitments and resource utilization. Operations staff review plans, compare scenarios, lock commitments and approve the appropriate version, while monitoring execution, replanning when conditions change and measuring financial and operational outcomes.

The platform is offered through subscriptions to enabled engines, together with configuration, integration and training services. Each organization's data is isolated, and plans, decisions and changes are recorded. Application fit is determined by the operating pattern, supported constraints, computation scale and available data.

Reusable product description: Veltrix Operations Optimization Platform is a configurable web platform that helps manufacturers, distributors and logistics operators build feasible production, delivery and inventory plans. It combines validated operational data with operations research models, scenario comparison, human approval and execution feedback. Customers configure supported business rules and objectives, review trade-offs and track measured outcomes. Deployment scope and performance are validated for each supported operating pattern; industry coverage does not imply support for every process or constraint.

# 03 Problems addressed and responsibility boundaries

Target problems include slow manual planning, difficulty balancing interacting constraints, unstable plans, late deliveries, poor resource utilization and excessive inventory or waste. The presence and scale of these problems must be established before contracting, using customer data and discussions with operations and finance; they are not assumed solely from the customer's industry.

The product's value is a calculated decision that is feasible and understandable. Indicators or forecasts must connect to an operational decision. The ERP retains its core business records, and execution systems retain their roles. The platform consumes authorized data and exports approved plans or instructions within the agreed integration scope.

The platform does not replace accounting, human resources, manufacturing execution or warehouse management systems. Direct machine control and industrial safety decisions are outside the initial scope. The customer remains responsible for the accuracy of supplied operating rules and authorization of plan approval. Veltrix retains its agreed responsibilities for application quality, support and data protection.

# 04 Target customers and fit criteria

A suitable customer has a recurring decision, constrained resources, a measurable cost, usable records and an owner who can authorize a new operating method. Begin with medium-sized organizations with repeatable operations, then expand complexity through validated deployments. Business size alone is insufficient; rule complexity, data quality and access to an operations owner are decisive.

| **Operating family** | **Customer examples** | **Potential scope** | **Specific pre-sale validation** |
| --- | --- | --- | --- |
| Batch manufacturing | Packaging, plastics and selected food operations | Lines, operation sequences, due dates and changeovers | Product-line compatibility, batch size and materials |
| Multistage assembly | Engineering products and assembly | Dependent operations and shared resources | Bill of materials, component availability and dependencies |
| Local distribution | Food distributors and manufacturers with fleets | Capacities, routes and delivery windows | Addresses, travel times and load requirements |
| Multisite inventory | Distributors, stores and warehouses | Replenishment and intersite transfers | Lead times, units, costs and demand source |
| Continuous or highly regulated manufacturing | Glass, chemicals and pharmaceuticals | Specialist assessment before scope definition | Process physics, batches, quality, release and compliance |

An industry logo in marketing must not imply support for all its processes. Maintain a coverage register for every template: engine, supported constraints, exclusions, tested size range and most recent validation date.

# 05 Platform structure and releases

The shared foundation covers accounts, permissions, data, configuration, computation, scenarios, approval, execution and measurement. Three engines sit above it, each with separate decision logic: production, transportation and inventory. They share product, location, resource and calendar identities without requiring every engine to use all fields belonging to the others.

| **Release** | **Committed scope** | **Capabilities not represented as ready** |
| --- | --- | --- |
| Release 1 | Shared foundation and production engine for a defined, validated batch and line pattern | Unimplemented transportation or inventory engines; untested continuous manufacturing |
| Release 2 | Standalone transportation engine and controlled integration with production readiness | Simultaneous end-to-end optimization across all engines |
| Release 3 | Inventory and replenishment engine with coordinated decision flows | Advanced forecasting, pricing or predictive maintenance without a validated project |

This is a proposed implementation priority to reduce risk. The target product includes all three engines, but only accepted capabilities are activated for a customer. Do not present controls for unfinished engines as functioning features.

# 06 Users and permissions

Enforce permissions on the server, imports, exports, APIs and background jobs, rather than only hiding interface controls. Access combines a user's role with authorized sites.

| **Role** | **Main permissions** | **Boundaries** |
| --- | --- | --- |
| Platform administrator | Create accounts, enable engines and limits, monitor service | No default access to customer operational data |
| Customer organization administrator | Manage users, sites, permissions and general settings | Own organization only |
| Data steward | Import, map columns, correct data and synchronize | Cannot approve plans without separate permission |
| Operations planner | Configure scenarios, solve, edit and submit plans | Authorized engines and sites only |
| Approver | Review, approve, reject or revoke release before execution | Document reasons for permitted overrides |
| Execution supervisor | Record progress, downtime and exceptions | Cannot change engine formulations or baseline costs |
| Analyst or finance manager | Review indicators and baseline; approve financial impact | Operational read access and authorized financial assumptions |
| Authorized support user | Diagnose within explicitly approved scope and time | Logged and revocable access |

Small organizations may assign multiple roles to one person. Separation of planning and approval is configurable according to customer policy, but every action must retain the actor's identity. Personal accounts must not share a password.

# 07 Customer journey from assessment to operation

Start with a short assessment of the process, resources, systems and financial pain, followed by a data sample and fit evaluation. Produce a written scope defining the decision, constraints, inputs, outputs, acceptance measures, exclusions, integrations and implementation estimate.

Next, configure the organization and sites, import data, agree rules with operations, test small examples and compare with a baseline plan. Run in parallel while users review results before operational adoption. Acceptance is signed against documented outcomes, and the support and update plan is defined.

Do not automatically convert a pilot into production use because a period has expired. Transition depends on data quality, plan acceptance, security and agreed performance. New requirements enter change control and are classified as configuration, reusable product development or separate customization.

# 08 Navigation and screens

Users see only enabled engines and select the organization, site and period within their permissions. Support Arabic and English directionality while preserving correct display of identifiers, numbers and dates.

| **Screen** | **Main content** | **Main actions** |
| --- | --- | --- |
| Sign in | Account, invitations, additional verification and recovery | Sign in, sign out and terminate sessions |
| Operations overview | Latest plan, data issues, delays and solve status | Open the relevant issue or plan |
| Data center | Files, sources, validation status and column mapping | Import, review and publish a data version |
| Master data | Products, locations, resources, calendars and costs | Add, edit and deactivate with effective dates |
| Engine configuration | Objectives, constraints, policies and solve limits | Save a version and validate settings |
| Planning workspace | Horizon, scope, inputs and scenarios | Create, duplicate, solve and compare |
| Production results | Line schedule, operations, conflicts and indicators | Lock, edit and revalidate |
| Transportation results | Map, routes, stops and loads | Edit, lock and revalidate |
| Inventory results | Purchase and transfer proposals; stock risks | Review quantities and submit for approval |
| Approvals | Submitted versions, differences and comments | Approve, reject or request changes |
| Execution monitoring | Work status, deviations and breakdowns | Update, record an event and request replanning |
| Impact and reports | Baseline, planned and actual results; finance sign-off | Compare and export reports |
| Administration and integration | Users, engines, credentials and synchronization | Manage permissions and sources |

Every screen includes an empty state with first-use guidance, loading state, actionable errors, filters and saved views where useful. Do not populate the interface with trial indicators or numbers calculated from fictional data without clear labeling.

# 09 Shared data model

Every organization-owned record has a stable internal identifier and, when integrated, an external identifier. Common fields include source, modification time, active status and a version or effective date where a change affects planning. Do not delete reference data used in historical plans; deactivate it for future use while preserving the original.

| **Entity** | **Main fields** | **Required controls** |
| --- | --- | --- |
| Organization and location | Code, name, type, currency and time zone | Organization isolation and location calendar |
| Product | Code, unit, conversions, weight, volume and shelf life where applicable | Explicit conversions; distinguish items from cases |
| Order and line | Identifier, product, quantity, location, priority, due date and status | Positive quantities, valid references and deduplication |
| Supplier and customer | Identifier, location, lead times and planning-related terms | Minimize personal data |
| Operational resource | Line, machine or vehicle; capacity, calendar and compatibility | Document units, capability and availability |
| Inventory and batch | Product, location, quantity, reservation, quality status and expiry | Separate available, reserved and unreleased stock |
| Cost | Type, value, unit, currency and effective period | No aggregation across currencies without documented conversion |
| Scenario and plan | Scope, input snapshot, rules, engine version and state | Traceability and version preservation |
| Execution event | Time, source, operation, quantity or status, external identifier | Deduplication and out-of-order arrival handling |

Define time and quantity precision per engine and document conversions. Store time consistently and display it in the site's time zone, preserving local workday semantics for shifts. Do not substitute a fixed UTC offset for an updatable time zone definition.

# 10 Import validation and source of truth

The import sequence is upload to staging, map columns, validate, preview differences and publish an accepted version. A failed file must not change published operational data. Mapping templates can be saved per source and reused.

Validate field types, units, dates, references, duplicates, plausible rates and durations, and calendar conflicts. Classify findings as blocking errors or warnings that may be accepted with a documented reason. Reports identify the row, field, value, issue and expected correction.

Support insert or update using a stable external identifier, with a preview of deletions or deactivations. Do not infer deletion from absence in a partial file. Assign a source of truth and editing owner for each entity or field: ERP for orders, for example, the platform for scheduling policies and the execution system for actual status.

Preserve an input snapshot for every solve, the latest synchronization marker and freshness thresholds suitable for the operation. Newer data marks an affected plan as stale and triggers a notification; it must not silently overwrite historical inputs.

# 11 Objectives constraints and industry templates

Users select supported objectives: minimize lateness, cost, changeovers or inventory, and preserve plan stability. Use lexicographic priorities or weighted objectives after normalizing scales. Do not combine minutes, currency and quantities using unexplained default weights. Record the trade-off method and explain its effect to the planner.

Every constraint has a definition, unit, scope, source, effective date and mandatory or flexible status. A soft constraint has a penalty or permitted deviation. The system must not relax a hard constraint without an explicit, authorized action. Locking an operation may create a conflict that must be detected.

An industry template combines data schemas, supported constraints, default objectives and reports, and configuration guidance. Constraints remain configurable within engine capabilities. A template cannot introduce an unimplemented formulation or automatically support a new process. Operations staff review configurations, which are versioned and reversible.

# 12 Production and capacity planning engine

The engine builds a plan on available lines, machines and shifts, respecting product compatibility, operation sequences, material availability and order due dates. The proposed first scope is batch production with defined operations and known alternative lines. Long-range aggregate planning, continuous manufacturing, furnace physics and joint products are separate extensions.

Inputs include orders, quantities and dates; product routings; processing rates by line; batch-size limits; setup and sequence-dependent changeover times; resource calendars; downtime; and available materials or confirmed receipts. Define whether orders and batches may be split, whether an operation may be interrupted, and when its output becomes available to the next operation.

Decisions include batch size when in scope, selected line, start and end times, operation sequence, authorized overtime and deferred orders where policy permits. An operation cannot end before its predecessor is complete or before its materials are available.

| **Rule** | **Required behavior** | **Acceptance example** |
| --- | --- | --- |
| Line compatibility | Select qualified resources only | A product unsupported by line 3 is never assigned there |
| No overlap | Respect processing and setup on each resource | A machine is not double-booked |
| Operation precedence | Complete predecessors before successors, including defined transfer time | Packing follows processing and required release |
| Changeover time | Apply sequence-dependent changeover matrix | A mold change reserves actual time |
| Working calendar | Respect shifts, breaks and maintenance | No batch is scheduled in a downtime window |
| Materials | Maintain time-phased balance and availability | No consumption before confirmed receipt or release |
| Due dates | Show lateness and penalty, or enforce mandatory deadlines | A late order shows delay duration and an explanation |
| Frozen plan | Protect started work and frozen window | Replanning does not reschedule an active batch |

Outputs include a timeline filtered by line, product and order; operation lists; quantities; utilization; changeover and overtime hours; and late or unscheduled orders with explainable reasons. Distinguish a proven capacity shortage from an estimated explanation requiring verification.

Scenarios show the effect of an additional shift, breakdown or urgent order. Dragging an operation manually must trigger validation before saving or approval and must prevent hard-constraint violations. A visual move alone does not establish plan feasibility.

# 13 Logistics and distribution planning engine

The initial scope is distribution from one or multiple depots according to the validated release, for orders with locations, capacities and service windows. Trips start and end under an explicit policy. Linked pickup and delivery, reloading, multileg transport and three-dimensional loading are extensions requiring dedicated models.

Inputs include orders, weight, volume, load type, verified coordinates, service duration, explicitly defined arrival or completion windows, vehicle capacities and calendars, and fixed, variable and overtime costs. Display the travel-time source and its data timestamp.

Use an appropriate road travel-time and distance matrix; straight-line distances are insufficient for a production delivery plan. Define traffic effects when supported by the provider, along with mapping costs, licensing and restrictions on storage and use in the service agreement.

Decisions include order-to-vehicle assignment, stop sequence, departure time, vehicles used and permitted order deferral. Constraints include weight, volume, compatibility, working hours, breaks, service windows and depot availability. Splitting an order between vehicles is an explicit policy rather than a hidden default.

Outputs include a map, route and stop schedules, arrival, service and departure times, costs and changing onboard loads along the route, plus unserved orders and their penalties. Distinguish estimates from guaranteed appointments; an estimated journey duration is not a commercial guarantee.

Replanning locks completed and active stops, current vehicle positions, remaining onboard loads and fixed commitments. Do not implicitly return a vehicle to its depot or assign it freight it does not carry. The supervisor reviews changes before revised driver instructions are issued.

A core acceptance criterion is independent recomputation of capacities and travel, service and break times at every route stage, with no silently dropped orders. A plan using future traffic information unavailable at decision time is not a fair comparison.

# 14 Inventory purchasing and transfer engine

The initial scope is periodic product-location planning using confirmed demand and a customer-provided forecast or demand estimate. Release 1 of this engine does not require an internal machine learning model. Identify confidence in the demand source and show scenario ranges where uncertainty matters.

Inputs include available and reserved balances, batches and expiry, open purchase and transfer orders, supplier lead times and calendars, minimum quantities and pack multiples, prices, holding and shortage costs, warehouse capacity and budget. Define unfulfilled demand as backorders or lost sales under a documented policy.

Decisions include purchase quantity and timing, supplier selection when alternatives are in scope, transfer quantities and dates, and safety stock supported by an explicit method. A probabilistic service-level target requires suitable uncertainty modeling; labeling a field as a service percentage does not make a deterministic model probabilistic.

The core balance for each period, location and product is: closing stock equals opening stock plus receipts, purchases and inbound transfers, minus served demand, outbound transfers and spoilage. Purchase availability follows lead time; stock cannot be consumed before arrival and release.

Enforce storage, budget, minimum purchase and pack-multiple constraints. Genuine shelf-life optimization requires time-phased batch-age tracking; do not market an engine as optimizing shelf life if it does not model this. First-expiry-first-out is an execution policy whose consistency with the plan must be checked.

Outputs include purchase and transfer proposals, projected balances, stockouts, excess and expected spoilage, brief explanations and cash-flow and cost impacts. Do not issue actual purchase orders before approval and integration authorization. Preserve external order identifiers and acceptance status to prevent duplicate submissions.

# 15 Coordination across engines

In an integrated extension, inventory planning generates purchasing and production requirements; production planning supplies quantities and readiness dates; transportation planning consumes ready shipments and delivery windows. Transportation may return limits or costs that require production review. This needs agreement on units, time horizons and update timing.

Begin by passing approved outputs between engines with versions, references and traceability. Define the owner of each decision, approval points and safeguards against endless recomputation loops. Conflicting engine requirements must appear as exceptions requiring a decision, not as an apparently valid overall plan.

Automated sequencing is not equivalent to global joint optimization. True joint optimization requires a unified formulation or a defined coordination algorithm, an overall objective and a testing method. Offer it as a separate extension when the customer establishes need and value.

# 16 Operations research model and solve service

Each model comprises decision variables, inputs, objectives and constraints. An optimization specialist selects suitable methods such as MILP, CP-SAT, routing algorithms or justified approximations. Do not impose one solver on every problem. OR-Tools documentation describes tools for these families and the limits of proving optimality for large routing problems [1][2].

For an assignment example, x is a binary decision assigning an order to a resource. The sum of an order's assignments equals one when service is mandatory; alternatively, add an unserved variable with an explicit penalty if policy permits. Model start and end times, precedence and resource availability through suitable variables and constraints. This is conceptual; each engine's implemented formulation requires specialist review.

Define a run profile per template: maximum time and memory, quantity and time rounding policy, objective order, model and solver versions, and random seed where applicable. Preserve the best feasible incumbent during search where supported, without promising identical plans across platforms or versions.

| **Result status** | **Meaning** | **Interface behavior** |
| --- | --- | --- |
| Proven optimal | Optimality established for the specified model under the solver's result status | Show status and relevant numerical bounds |
| Feasible | A constraint-compliant solution exists without proof of optimality | Show quality, bound and gap where available |
| Proven infeasible | The solver proved that the model has no solution | Show diagnosis and its limits; request changes |
| Inconclusive | Search or time ended without a solution or proof | Do not call the model impossible; allow adjustment or retry |
| Failed or canceled | Execution issue or user cancellation | Preserve reason; do not release an execution plan |

Not all methods provide a mathematical bound or optimality gap. Report missing information honestly and measure improvement against a documented baseline. Do not claim an absolute best solution without proof.

# 17 Scenario and plan lifecycle

Solve states are separate from plan approval states. A solve moves from queued to running, then success, time limit, failure or cancellation. A plan moves from draft to calculated, review, submitted, approved, exported or released for execution, in progress, then completed or superseded.

Each result is generated from an immutable input and configuration snapshot. Any edit creates a new version or scenario and must not rewrite a previously approved plan. Preserve predecessor reference, reason and actor. Rejection can include comments and does not delete the plan.

Before approval, validate result feasibility, data freshness, approver authority and absence of a conflicting newer version. Approval must be transactional, preventing competing approved versions for the same scope without an explicit policy. Inform users when another user has already changed the record.

Comparisons show cost, timing, utilization, changed decisions and unserved items on consistent scopes and units. Preserve scenario assumptions, such as a different shift, due date or cost. Do not attribute the effect of changed demand to improved optimization.

# 18 Approval execution and disruption handling

The first release uses human review followed by file export or authorized integration submission. Record every submission and external acceptance status. A successful network response alone does not prove execution: distinguish sent, accepted, failed and executed where execution events are available.

Every event has an identifier, occurrence time, receipt time and source. Repeated events must not double-count production or shipments. Handle out-of-order arrivals through a documented policy. Corrections create traceable adjustment events rather than erase the original.

For breakdowns, cancellations or urgent orders, show the event's impact and propose replanning. Preserve completed and active work and frozen commitments. Users review changes and affected parties before releasing a replacement version. Reconcile external systems rather than leave two conflicting versions active.

# 19 Result explanation and diagnosis

Distinguish facts extracted from the plan, counterfactual scenario diagnosis and approximate inference. A fact might be a line's finish time. A diagnostic scenario might show that extending a shift by one hour removes a specific delay. Do not claim this is the only cause without supporting analysis.

When no solution exists, begin with data, constraint and lock checks. Provide a minimal conflict where the solver supports it, or named checks with clearly stated limits. Proposed relaxation remains a separate scenario requiring approval. Never silently change a safety limit or mandatory constraint.

Show reasons for excluding orders and limits on capacity, compatibility and materials, linking to inputs. The core explanation is structured and computational. An optional language assistant may express verified information but must not invent causes or financial values.

# 20 Operational indicators and financial measurement

Every indicator has a definition, formula, unit, period, source and owner. Separate projected and actual values and show data freshness. Define whether on-time delivery is measured by order, line or quantity, and against the original or revised commitment.

| **Engine** | **Core indicators** | **Measurement controls** |
| --- | --- | --- |
| Production | Lateness, delivery, changeover hours, overtime and utilization | Define available-hours denominator; distinguish capacity gains from cash savings |
| Transportation | Cost per order, distance, load utilization and on-time delivery | Compare similar loads, areas and service windows |
| Inventory | Stock value, stockouts, spoilage, turnover and service | Consistent units and periods; separate liquidity from profit |

Financial benefit includes demonstrable cash savings, additional contribution margin after variable costs, and avoided financing, storage and spoilage costs where realized. Inventory reduction releases cash separately; do not combine the full inventory principal with recurring annual profit. Employee time released is a capacity benefit until it leads to avoided spending or verified income.

Period ROI equals attributable gross benefits minus total costs, divided by total costs and multiplied by 100. Define included items and the measurement period explicitly; do not subtract costs twice. The formula is not used when cost is zero. Include relevant implementation, subscription, operating, integration and training costs. Calculate payback from timed cash flows rather than annual ROI alone.

Finance approves attribution, adjustments for seasonality, prices and workload, and overlap between benefits. Historical testing must use information available when each decision was made. Before-and-after results may reflect other factors; disclose attribution limits and use parallel operation or comparable groups where practical.

# 21 Reports and alerts

Core reports are the detailed plan, exceptions, two-scenario comparison, planned versus actual performance, approved financial impact and change and approval history. Provide Excel and PDF export when implemented. Reports include scope, date, version, currency and units.

Required alerts cover failed data validation or synchronization, stale plans, solve failure, approval requests, disruptions affecting plans and execution conflicts. Begin with in-app alerts and email when enabled. WhatsApp is not required initially; it introduces account, cost, authorization and connectivity requirements.

Deduplicate alerts and identify recipient, severity, timestamp, current status and action link. Do not expose integration secrets or personal information in email. Recheck authorization at report download time, even if a previously saved link is used.

# 22 Proposed technical architecture

Begin with a modular application, one logical application backend and a relational database, separating long-running calculations into background workers. Do not introduce dozens of microservices at the outset. This separation allows compute capacity to grow without unnecessary product-management and operational complexity.

| **Component** | **Responsibility** | **Proposed starting choice** |
| --- | --- | --- |
| Web interface | Data, plans, review and approval | Vue and TypeScript fit the team's existing skills |
| Application service | Permissions, rules, APIs and transactions | Python and FastAPI as a proposed option |
| Relational database | Data, versions, plans and approvals | Select one database the team can support |
| Queue and solve workers | Engine execution and resource limits | Durable jobs with cancellation and deduplication |
| Optimization libraries | Model construction, solving and validation | Select by problem and license [1][2] |
| File storage | Imports, exports and large snapshots | Private storage with expiring links |
| Monitoring and operations | Errors, solve duration, resources and recovery | A small, clear toolset with an accountable owner |

Do not adopt a language or library merely because it appears here. Confirm versions, licenses and support through a small technical assessment. Recurring costs include compute, mapping, messages, monitoring, backups and support even when the solver library is open source.

# 23 Solve contracts and integration interfaces

A solve request carries organization identity derived from the session, engine, data snapshot, rule version, horizon, objectives, locks and time budget. A client must not switch organizations simply by submitting a different identifier. The service returns a run identifier and state; results are retrieved on completion.

Results include solve status, engine and solver versions, objective values and available bounds, constraint checks, exceptions, warnings, start and end timestamps and plan identity. Recheck authorization before displaying files, approving or releasing the result.

Core integration interfaces import orders, resources and stock; query solve and plan status; export an approved plan; and receive execution events. Document API versioning, pagination, time limits and standard error codes. Credentials are organization- and scope-limited, rotatable and revocable.

Persist outgoing submissions in a transactional outbox linked to approval, and use idempotency keys for creation commands. Retrying after a connection failure must not create a second purchase or shipment. Record attempts and last success, and provide periodic external reconciliation and manual review of permanent errors.

# 24 Security privacy and data governance

Enforce organization isolation across queries, files, queues, caches, logs, exports and restored backups, with cross-account access tests. Support accounts must not have permanent unrestricted access. Use trusted authentication, additional verification for sensitive accounts, sign-in throttling and session revocation.

Protect connections, secrets and storage according to the deployment design. Never expose real credentials in code, browsers or error logs. Validate and limit uploaded files and keep them outside public access. Prevent user-supplied export values from becoming executable spreadsheet formulas.

Minimize personal data, define processing roles, retention and export, correction and deletion procedures, including backups, audit records and contractual obligations. Customer data must not train a shared model without an appropriate basis and explicit agreement.

For Jordan, review applicable obligations with a specialist based on data types, party roles, processing location and transfers, including personal data protection law and ministry guidance [3]. These are design and review requirements, not a compliance certification or legal conclusion. Hosting in a particular country does not itself establish compliance.

# 25 Performance reliability and service limits

Set template limits using actual benchmarks for order count, operation count, resources, horizon and constraint complexity. Order count alone does not predict solve duration. Do not contractually promise instantaneous solves or untested volumes.

| **Area** | **Initial design target subject to measurement** | **Acceptance evidence** |
| --- | --- | --- |
| Routine screens | 95th-percentile server response within 2 seconds at agreed pilot load | Documented load test with data and user scope |
| Solve submission | Asynchronous acceptance without holding the connection through computation | Run identifier and queryable state |
| Solving | Configurable initial budget, such as 1 to 5 minutes for the pilot problem | Quality and duration benchmarks on representative samples; no prior guarantee |
| Customer fairness | Per-organization concurrency, memory and time limits | Concurrent operation without starvation or leakage |
| Recovery | Example initial RPO of 24 hours and RTO of 8 hours | Recovery exercise; tighter targets where operational impact requires them |
| Outage | Access to the last approved plan through an agreed mechanism | Outage exercise and operating fallback |

These are planning targets, not a published SLA. Before production, determine RPO, RTO and backup frequency from the customer's cost of disruption; initial figures may be unsuitable for sensitive operations. Require a real restoration test, backup-failure alerts, an escalation owner and a recovery runbook.

# 26 Functional requirements and acceptance criteria

R1 denotes the first release, R2 transportation, R3 inventory and EXT a later extension. These core requirements can become development stories; customer-specific details belong in a separate acceptance appendix.

| **ID** | **Phase** | **Requirement** | **Core acceptance criterion** |
| --- | --- | --- | --- |
| TEN01 | R1 | Organizations and sites | No access to any record outside the authorized scope |
| IAM01 | R1 | Invitations, roles and site scopes | Unauthorized direct server requests are rejected |
| DAT01 | R1 | Import, preview and mapping | Failed input does not modify published data |
| DAT02 | R1 | External identifier updates | Repeating an import does not duplicate orders |
| DAT03 | R1 | Unit and date conversion | Item/case differences are detected or explicitly converted |
| CFG01 | R1 | Versioned rules and objectives | Results preserve the rules used |
| RUN01 | R1 | Background solving and limits | Closing the browser does not interrupt run tracking |
| RUN02 | R1 | Accurate solve states | Timeout without a solution is not reported as proven infeasibility |
| RUN03 | R1 | Independent plan validation | Hard-constraint violations prevent approval |
| PLN01 | R1 | Versions, scenarios and locks | Draft edits do not change approved plans |
| PRD01 | R1 | Feasible production schedule | No overlaps, incompatible lines or unavailable materials |
| PRD02 | R1 | Changeovers and sequencing | A changed sequence affects timing and cost |
| PRD03 | R1 | Events and replanning | Active and completed operations are preserved |
| APR01 | R1 | Concurrency-safe review and approval | Changed inputs require refresh or recorded acknowledgment |
| EXE01 | R1 | Export and recorded manual execution | Every version has clear identity, release and scope |
| KPI01 | R1 | Baseline, planned and actual values | Units, denominators and commitment-date definitions are documented |
| FIN01 | R1 | Benefits, costs and finance approval | Cash released is not recurring profit; costs are not deducted twice |
| INT01 | R1 | Basic exchange interface | Duplicate requests and events do not duplicate effects |
| AUD01 | R1 | Audit trail | Actor, action, time and version are retained |
| OPS01 | R1 | Backups, monitoring and recovery | Restoration and file-access checks pass |
| LOG01 | R2 | Routes, capacities and windows | Load and timing are validated at each route stage |
| LOG02 | R2 | Disruption and replanning | Actual loads and completed stops are preserved |
| LOG03 | R2 | Road travel-time source | Source, timestamp, coverage and cost are documented |
| INV01 | R3 | Time-phased stock balance | No early use of receipts or hidden stock balances |
| INV02 | R3 | Purchasing, transfers and pack rules | Quantities respect multiples, budgets and lead times |
| INV03 | R3 | Shelf life when enabled | Expired batches cannot serve demand |
| ORC01 | R3 | Engine-to-engine handoff | Outputs reference a version and identified downstream input |
| AI01 | EXT | Explanation assistant or prediction | Separate testing and approval for constraint changes |

# 27 Model and product validation

Begin model testing with small cases whose solutions are known or can be enumerated, followed by representative customer data and boundary cases. Use an independent validator for schedules, capacities, times and materials so that tests do not reproduce the solver implementation's own mistakes.

| **Test family** | **Required cases** | **Expected outcome** |
| --- | --- | --- |
| Feasibility | Demand above capacity, missing material or impossible window | Accurate status and clear exceptions without silent violations |
| Quality | Compare a sound simple rule and the planner's current plan | Improvement or explained trade-off; no guarantee of improvement in every case |
| Sensitivity | Change capacity, costs and locks | Understandable changes and stability checks, without assuming universal improvement |
| Security | Other organizations, identifiers, files, exports and queues | Consistent denial and no leakage |
| Import | Duplicates, invalid rows, units and dates | Consistent result, correction report and safe publishing transaction |
| Approval | Concurrent edits, stale data and superseded versions | Conflict prevention or documented reconciliation |
| Integration | Disconnection, retries and late events | No duplicate commands; traceability through reconciliation |
| Operations | Worker crash and backup failure | Recovery, monitoring and no release of incomplete results |

Every template needs a reference acceptance set at small, medium and large sizes relative to agreed scope. Examine solution quality, solve-time distribution and memory consumption. Changes to the model, solver or rounding require regression tests before deployment, with rollback that preserves historical data.

Operational acceptance requires an operations owner to review real plans, track planned-versus-actual differences and sign off constraints and measures. An attractive interface or passing technical tests alone does not authorize production operation.

# 28 Commercial packaging and support

Sell by engine or engine bundle with site, resource and concurrent-solve limits aligned to tested sizes. Setup fees cover assessment, data, rules and training; integrations and customizations are explicitly scoped. Online payments and accounting invoices are not required inside the initial product. Contracts and collection can be handled externally while entitlement status is recorded.

Contracts distinguish projected improvements from verified outcomes and define data sources and correction responsibility, pilot duration and acceptance criteria, support scope, response times and hours, ownership of data, models and changes, termination and data export.

Support records include severity, impact, product version and a run identifier that supports investigation without leaking data. Routine customer changes use configuration; new constraints undergo product, optimization and test review. A separate customer-specific code branch is not the default approach.

# 29 Team responsibilities and coding tools

Execution requires product ownership and operational analysis, mathematical optimization, application and data development, and operations, security and quality responsibilities. One person may cover multiple responsibilities, but model review and operational acceptance remain explicit.

| **Responsibility** | **Expected deliverable** | **Decision not delegated solely to automation** |
| --- | --- | --- |
| Product owner and process analyst | Scope, rules, acceptance and priorities | Supported capabilities and commercial commitments |
| Operations research specialist | Formulation, validator and quality benchmarks | Model correctness and method suitability |
| Application and integration engineering | Screens, permissions, data and plans | Isolation, transactional integrity and integration safety |
| Operations and quality | Deployment, monitoring, recovery and testing | Readiness, releases and restoration |
| Customer operations and finance owners | Approval of rules, plans and impact | Executability and benefit attribution |

Use Claude Code and Codex to implement and review defined components, create tests, document and diagnose. Give them specific requirements and acceptance criteria, and withhold unauthorized secrets and personal data. A tool approving its own generated code is neither mathematical proof nor sufficient independent review.

# 30 Implementation roadmap and release gates

The sequence below is proposed; durations are planning estimates dependent on team, data and integrations. It assumes a dedicated team covering application, optimization, process and testing, plus an available customer owner. Stages overlap and must not simply be added together.

| **Stage** | **Deliverables** | **Gate** | **Indicative estimate** |
| --- | --- | --- | --- |
| Fit assessment | Data, rules, baseline and scope | Agreed process and testable data | 2 to 4 weeks |
| Engine proof | Model, validator and comparison | Correctness and useful results on representative cases | 4 to 8 weeks |
| Platform foundation and pilot | Accounts, data, screens and approval | Security review and limited operational acceptance | 8 to 12 weeks, with overlap |
| Repeatable commercial deployment | Two or three customers with similar operating patterns and support | Same core code with different configurations | Approximately 6 to 12 months from the start |
| Second and third engines | Models, acceptance and separate integration | Value, support and tests for each engine | Estimate after the first is proven |

These estimates do not establish a launch date for all industries. Each new operating family has a validation gate. Repeatable sales require a coverage statement, acceptance test set, configuration documentation, restoration exercise, support records and customer-authorized outcome references.

# 31 End to end use cases

Packaging manufacturer: the planner uploads weekly orders with quantities and due dates, imports material availability and configures alternative lines and changeovers. Validation detects a missing processing rate, which the data steward corrects. The engine calculates a plan with two late orders. The planner duplicates the scenario, adds an authorized shift, compares overtime with lateness cost and submits it for approval. The approved schedule is exported. When a line fails, started work is preserved and remaining work is replanned after review. Actual results are recorded for comparison.

Distributor: the supervisor receives tomorrow's orders, corrects two unverified addresses and selects vehicles and service windows. The engine calculates routes using an agreed road travel-time source and flags an order that cannot be served within the constraints. The supervisor compares an extra vehicle with a customer-agreed appointment change and approves a plan. Route updates carry external identifiers to prevent duplication. Vehicle breakdown replanning starts from actual positions and onboard loads.

Inventory: the owner reviews expected demand, open orders and available batches. The engine proposes purchases and transfers respecting lead times, pack multiples and budget. It identifies short-dated excess and shows projected balances for coming weeks. A quantity is edited and revalidated, then an authorized owner approves and sends the proposal to ERP. External acceptance and status are retained. Impact measurement separates released cash from reduced spoilage and financing costs.

# 32 Deferred capabilities and product limits

Defer a standalone mobile application, chat and multi-agent assistants, dynamic pricing, safety cameras, predictive maintenance, direct PLC and SCADA integration, closed-loop machine control, an unrestricted user equation editor and a broad connector library without customer demand. Add them when need, value and support capability are established.

Inventory and shelf-life features alone do not establish full support for regulated pharmaceutical or food operations. Quality, quarantine, release, traceability and regulatory requirements need customer-specific validation. The platform is not an industrial certification, safety system or substitute for mandatory records.

Document and contract for supported constraints, tested sizes, forecast sources, freshness and numerical approximation. Missing inputs produce warnings or rejection according to impact, not hidden assumptions. Do not promise fixed savings, day-one ROI or instantaneous optimality for every problem.

# 33 Risks and implementation decisions

| **Risk** | **Effect** | **Practical mitigation** |
| --- | --- | --- |
| All-industry scope too early | Superficial models and high support cost | Start with one operating family, then coverage register and staged releases |
| Poor data | Unexecutable plans | Quality gate, data owner and visible assumptions |
| Missing constraints | Attractive results that fail in the factory | Operational review, independent validation and parallel trial |
| Slow solving | Missed decision window | Size and time limits, staged planning and approximation evaluation |
| Unreliable integration | Duplicate commands or conflicting plans | Idempotency, transactional outbox and reconciliation |
| Separate customization per customer | Multiplying maintenance | Templates, versions and change review |
| Inflated ROI | Renewal disputes | Finance sign-off and separate projected, actual and liquidity measures |
| Cross-customer leakage | Commercial and legal harm | Isolation, tests, permissions, audit and authorized support |

Proposed initial decisions: select batch production first; recruit a pilot customer able to provide data and an operations owner; use human-reviewed release; choose one hosting environment; assign an optimization owner; and prove a sample solve before expanding the interface. These are adjustable planning assumptions, not existing customer approvals or committed resources.

# 34 Development team handover instructions

Convert requirements into a backlog linked to identifiers and phases. Begin with a complete vertical slice: isolated organization, data import, small production model, validation, result display, approval and export. Prove the connection between the product and the engine before expanding screens.

Every task defines data, errors, permissions and acceptance. Use clearly labeled synthetic data in development, then authorized customer samples in validation. A mock screen or fixed result is not an implemented engine. A working run button without constraints and a valid plan is not completion.

Before scaling, agree a data dictionary, source-of-truth matrix, rule versions, organization isolation mechanism, solve and plan state definitions and reference cases. Record design decisions, scope changes and their reasons so this document remains a maintained, clearly versioned reference.

# 35 Sources and reference boundaries

This document is a proposed Veltrix product design, not copied specifications from another provider. The references below support domain background and limitations; remaining requirements are recommended design decisions. Source review date retained from the Arabic edition: 22 November 2026.

[1] Google OR-Tools Introduction. Describes optimization problem families and available tools. https://developers.google.com/optimization/introduction

[2] Google OR-Tools Vehicle Routing. Explains routing and computational limits, including good solutions without a guarantee of optimality at every scale. https://developers.google.com/optimization/routing

[3] Jordan Ministry of Digital Economy and Entrepreneurship, personal data protection FAQs. An initial reference for the law's scope; applicable legal texts and instructions require review during implementation. https://modee.gov.jo/EN/Pages/FAQs

[4] Makkook DIOS. A reference for the publicly described product category and platform/engine structure. Its claims are not adopted as performance benchmarks or evidence of internal architecture. https://makkook.ai/dios

# 36 Short glossary

| **Term** | **Meaning in this document** |
| --- | --- |
| Operations research | Systematic formulation of decisions, resources, constraints and objectives |
| Solver | Software that searches for a model solution within method and compute limits |
| MILP | Mixed-integer linear programming with integer and continuous variables |
| CP-SAT | An integer constraint-solving approach suitable for many scheduling applications |
| Feasible solution | A plan satisfying the model's hard constraints |
| Optimal solution | A solution proven best under the model's objectives and boundaries |
| Scenario | A version of assumptions and inputs used for comparison |
| Frozen window | A period or decisions protected from change during replanning |
| Data snapshot | A time-specific version of the inputs that produced a result |
| RPO and RTO | Target maximum data loss and target maximum restoration duration |
| Source of truth | The authoritative system for a specified record or field |
| Idempotency | Preventing a repeated request or event from duplicating a business effect |