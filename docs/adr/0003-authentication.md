# ADR-003: Authentication approach

- Status: Proposed (decide in task P0-03)
- Date: 2026-11-22
- Deciders: Tech lead, product owner
- PRD: §6, §24

## Context

Users need invitations, sign-in, MFA for sensitive roles, throttling and session revocation. Shared passwords are not allowed. Enterprise customers may later ask for single sign-on.

## Options considered

1. Built-in: argon2id password hashing, TOTP MFA, server-side sessions.
2. Self-hosted OIDC provider (Keycloak): SSO-ready, more operations work.
3. Hosted identity provider (Auth0, Cognito, Entra ID): fastest SSO, recurring cost, data location questions for Jordan.

## Recommended decision

Option 1 for Release 1, behind an interface that allows adding OIDC later without changing authorization code.

## Consequences

The team owns security-sensitive code, so P1-02 gets a deep-tier model and a careful review. SSO becomes a later change request.

## Evidence required before acceptance

Threat review of the design in P11-01. Throttling and session revocation tests pass.

## Revisit when

When the first customer requires SSO, or if security review finds the built-in approach too risky.
