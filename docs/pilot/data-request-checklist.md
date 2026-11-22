# Data request checklist for the pilot (batch production, Release 1)

Ask the pilot customer for 4 to 8 recent weeks. Excel or CSV is fine. Synthetic or anonymized customer names are welcome; we do not need personal data (§24).

| Data | Fields we need | Why | Received |
|---|---|---|---|
| Products | code, name, base unit, unit conversions (case, pallet) | Units must never be guessed (DAT03) | [ ] |
| Orders and lines | order no., product, quantity, due date, priority, status | Demand to schedule | [ ] |
| Routings | product, operation sequence, operation name | Order of steps | [ ] |
| Eligible lines and rates | operation, line, rate per hour, setup time, min/max batch | Where and how fast each step can run | [ ] |
| Changeover matrix | line, from product, to product, minutes (and cost if known) | Sequence-dependent changeovers | [ ] |
| Calendars | shifts per line, breaks, holidays, planned maintenance | When lines are available | [ ] |
| Downtime history | line, start, end, reason | Realistic availability and testing replanning | [ ] |
| Materials | material per unit of product, stock on hand, confirmed receipts with dates | Material availability | [ ] |
| Costs | overtime per hour, lateness penalty or rule, changeover cost | Objective weights and financial impact | [ ] |
| Current plans | the schedule the planner actually used for the same weeks | Baseline for comparison (§7, §20) | [ ] |
| Actual results | what really ran, when, and delays | Planned versus actual (§20) | [ ] |

Handling rules:
- Store only in the approved private location; never in the repository, never in prompts to AI tools unless the customer authorized it.
- Record the date received and the customer contact who approved sharing.
