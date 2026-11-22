# Data dictionary

Draft data contract for every entity in PRD §9. Each YAML file describes entities, fields, types, units and rules.

- Status: **draft**. The product owner approves it in task P0-04; Claude Code then generates Python and TypeScript types from it.
- Every org-owned entity inherits the `common` fields defined in `common.yaml`.
- Field types: `uuid`, `string`, `text`, `int`, `decimal`, `bool`, `date`, `datetime_utc`, `duration_minutes`, `enum`, `ref:<entity>`, `quantity` (decimal + unit), `money` (decimal + currency).
- Changes after approval go through a pull request reviewed by the product owner (see .github/CODEOWNERS).
