# Definition of Done

A task is done only when all of these are true. The PR template repeats this list.

1. All acceptance criteria in the task file are automated tests and pass in CI.
2. Cross-tenant tests cover any new route, job, file or export (TEN01).
3. Server-side authorization and audit events exist for every new mutating action (IAM01, AUD01).
4. Migrations upgrade and downgrade cleanly; historical data is never destroyed.
5. OpenAPI and the generated TypeScript client are updated; breaking changes are versioned.
6. User-facing strings exist in Arabic and English; RTL layout is verified for new screens.
7. Errors are actionable (what happened and how to fix it); empty and loading states exist.
8. Documentation is updated: data dictionary, ADR, runbook or formulation where relevant.
9. The reviewer agent approved, any listed human gate is signed, and the tech lead merged.
10. The task file in docs/tasks has Status: done and the PR link.
