# ADR-006: File storage

- Status: Proposed (decide in task P0-03)
- Date: 2026-11-22
- Deciders: Tech lead, product owner
- PRD: §21, §22, §24

## Context

Imports, exports and large snapshots need private storage, size limits, malware scanning and short-lived download links that recheck permissions.

## Options considered

1. S3-compatible object storage (MinIO locally, provider storage in production).
2. Database large objects.
3. Local disk on the API server.

## Recommended decision

Option 1 with org-prefixed keys, private buckets, versioning and links issued through an API endpoint that rechecks authorization.

## Consequences

Needs a malware scan step and lifecycle rules for retention (§24).

## Evidence required before acceptance

Upload and download tests in P2-07, including a revoked user's saved link failing.

## Revisit when

If the hosting environment offers a better managed option.
