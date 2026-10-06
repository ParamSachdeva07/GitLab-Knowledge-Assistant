---
owning-stage: "~devops::tenant scale"
title: 'Organizations ADR 009: State machine for organization lifecycle'
description: Why we use the state_machine gem backed by organizations.state and organization_details.state_metadata for the Organization lifecycle.
toc_hide: true
---

## Context

Organizations sit at the top of the resource hierarchy and own groups, projects, users, and settings. Their lifecycle needs explicit, machine-enforced control:

- An Organization must not be usable before confirmation.
- Deletion is two-tiered: reversible soft-delete for owners, irreversible hard-delete for admins.
- Every transition must be auditable (who, when, why — including the error on failures).
- Failed transitions must leave the row in a consistent, recoverable state.

The deletion workflow is tracked in [Add ability to delete an Organization](https://gitlab.com/groups/gitlab-org/-/work_items/21433).

## Decision

We manage the Organization lifecycle with the [`state_machine` gem](https://github.com/state-machines/state_machines), backed by:

- `organizations.state` (SMALLINT) — the authoritative state value.
- `organization_details.state_metadata` (JSONB) — the audit trail, validated against a strict JSON Schema on every save.

Low-level infrastructure (metadata writes, logging, transition-user validation) is shared with `Namespaces::Stateful` through four `Gitlab::TenantContainerLifecycle::Stateful` modules.

This ADR records the *mechanism* only. The state catalog, transitions, and conventions for adding new states live in the [Organization Lifecycle](../lifecycle.md) blueprint, which is the single source of truth.

## Consequences

- All state changes go through the state machine — direct assignment to `organizations.state` is invalid.
- `state_metadata` uses `additionalProperties: false`: any MR adding a metadata field must update `organization_detail_state_metadata.json` in the same MR, or saves will fail validation.
- Transition services must pass `transition_user:`; the machine enforces this through `ensure_transition_user`.
- The shared `TenantContainerLifecycle::Stateful` modules must stay backward-compatible with both `Organizations::Stateful` and `Namespaces::Stateful`.
- New states and transitions do not require new ADRs — they ship in the blueprint, the schema, and the state machine. A new ADR is only needed when the mechanism itself changes.

## Alternatives

### Single boolean flag (`active` / `deleted`)

Rejected: a boolean cannot represent intermediate states (confirmation, in-flight hard deletion). No audit trail, no guards.

### Separate columns per concern (`is_confirmed`, `confirmed_at`, `soft_deleted_at`, …)

Rejected: nothing enforces mutual exclusivity, so an Organization could appear simultaneously `confirmed` and mid-hard-deletion. Guards and audit become ad-hoc per-feature code. This is the approach the legacy namespace deletion used (`group_deletion_schedules`, `marked_for_deletion_at`) and that we are moving away from — see the [Group and Project Operations blueprint](../../group_and_project_operations_and_state_management/_index.md).

### Renamed intermediate state (`confirmation_in_progress` / `activation_in_progress`)

Discussed in the [intermediate-state naming thread](https://gitlab.com/gitlab-com/content-sites/handbook/-/merge_requests/19655/diffs#note_3313088904).

Rejected: the `_in_progress` convention in the namespace lifecycle names the background process performing the operation (user says "delete" → `deletion_in_progress`). Here the user is confirming the Organization's structure, not kicking off a "confirmation" process; `confirmation_in_progress` would imply the user is mid-action. `confirmed` + `active` keep the user's completed action and the system's completed activation as two distinct, durable states.

### Reuse `Namespaces::Stateful` directly

Rejected: Organizations are not namespaces — no parent, no inheritance, no archival, no transfer. Sharing the full namespace machine would mean conditional branching for org-specific behavior throughout. The current design shares only the low-level infrastructure modules.
