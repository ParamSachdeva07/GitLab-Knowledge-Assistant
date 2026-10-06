---
owning-stage: "~devops::tenant_scale"
title: 'ADR-005: Grants Target Namespaces'
description: 'A grant points at a namespace with a real foreign key. Resources enforced outside Rails are reached by replicating the Team to the service that enforces them.'
status: accepted
creation-date: "2026-07-29"
authors: [ "@rymai" ]
---

Teams should eventually be assignable to organization-level resources such as the Artifact Registry. No decision record covers how, and this one fixes only the boundary an implementation must respect until one does.

## Context

A grant targets a namespace, so an organization-level resource is out of reach. The Artifact Registry is the motivating case, and investigating it turns out not to be a schema question.

**Both organization-level resources with real per-principal access are enforced outside Rails.** The Artifact Registry delegates to the IAM service: its roles are UUIDs owned by a shared library and mirrored in IAM, assignments are written through a relationships client, and there is no registry table, model, or policy in Rails at all. Secrets Manager delegates to OpenBao, where the permission class has no table and identity is a policy path.

Every organization access decision is an existence check against `organization_users`, which has two levels. Nothing at organization level is enforced in PostgreSQL, so there is no aggregation point for a grant to fold into — which is the whole enforcement strategy of [ADR-004](004-team_membership_is_an_ordinary_membership.md).

Making the grant's target polymorphic would therefore trade away a real foreign key, against [the database guidelines](https://docs.gitlab.com/development/database/polymorphic_associations/), to gain a target type with no table to point at and no enforcement behind it.

## Decision

**Team grants target namespaces only.** The grant's `namespace_id` keeps its real foreign key, and the primitive stops at the namespace tree. A Team reaches a resource enforced elsewhere by being known to whatever enforces it, not by the grant table growing a target type.

The replication path already exists: `Authn::IamOutbox` is a transactional outbox for replicating entity changes to IAM, sharded by `organization_id`. Teaching IAM about Teams means adding entity types and emitting from the Teams services.

What remains open is **where the roster expands into assignments** — GitLab writing one assignment per member, or the Team becoming a set-valued subject in the enforcing service. The first needs nothing from anyone else but makes GitLab resolve collisions in a store that holds one assignment per subject and object. The second keeps membership resolution in the service that enforces, and needs support GitLab does not own. This should be settled before anything else here, because it decides everything downstream.

## Consequences

### Positive

- The grant keeps one target type and a real foreign key, so every query, index, and cascade stays as designed
- Teams remains a principal rather than a permissions platform, which is what keeps it a small feature with a bounded blast radius
- The fan-out question is answered next to the service that enforces, by the people who own it, rather than pre-empted by a schema choice in GitLab

### Negative

- **Teams reach nothing at organization level today.** A customer using both Teams and the Artifact Registry gets no Team-based access to the registry, and the reason — that the two are enforced in different systems — will read as an arbitrary hole
- This is a second per-integration cost after [ADR-007](007-parity_before_migration.md), and the generic principal abstraction that answers ADR-007 does not help, because it unifies principals inside Rails and these enforcers are outside it
- The end goal is stated but unspecified: no record says how a Team reaches an organization-level resource, so the findings above will age before anything acts on them

## Related Documents

- [Teams blueprint](../_index.md)
- [ADR-004: Team Membership Is an Ordinary Membership](004-team_membership_is_an_ordinary_membership.md)
- [ADR-007: Parity Before Migration](007-parity_before_migration.md)
- [Organization blueprint](../../organization/_index.md)
