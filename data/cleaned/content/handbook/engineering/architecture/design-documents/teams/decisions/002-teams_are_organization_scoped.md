---
owning-stage: "~devops::tenant_scale"
title: 'ADR-002: Teams Are Organization-Scoped'
description: 'A Team belongs to exactly one Organization, and that boundary is absolute.'
status: accepted
creation-date: "2026-07-28"
authors: [ "@rymai" ]
---

## Context

Teams need an owning scope: the instance, a group, or an [Organization](../../organization/_index.md).

A group-scoped Team is barely distinguishable from the group itself and cannot span sibling hierarchies, which is precisely the case customers ask about. An instance-scoped Team would cross the customer isolation boundary Organizations exist to establish.

## Decision

Teams are **Organization-scoped**, and that boundary is absolute:

- A Team belongs to exactly one Organization and is created at the Organization level
- A Team's path is unique within its Organization, not globally
- A Team's roster can only contain members of its Organization, and a Team can only be granted access to namespaces in its own Organization
- There is no cross-Organization Team assignment, membership, or visibility

Enterprise identity integration continues to happen at the Organization level, with Teams providing structure inside it.

## Consequences

### Positive

- Teams can span multiple group hierarchies within a customer's boundary, which is the collaboration case groups cannot serve
- Customer isolation holds by construction rather than by check: no code path can assign a Team across Organizations
- Team paths do not consume global namespace cardinality

### Negative

- A group share whose two ends are in different Organizations cannot be converted to a Team, and it is not yet decided whether such shares need any path at all. A group belongs to exactly one Organization, the same as a Team; what crosses the boundary is the *share*, because nothing validates its two ends against each other today
- Customers operating multiple Organizations maintain parallel Teams in each, with no shared roster
- Teams adoption is coupled to Organizations maturity, because Organization-level administration is a prerequisite

## Related Documents

- [Teams blueprint](../_index.md)
- [Organization blueprint](../../organization/_index.md)
- [ADR-007: Parity Before Migration](007-parity_before_migration.md)
