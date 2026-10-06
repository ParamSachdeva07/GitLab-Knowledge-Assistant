---
owning-stage: "~devops::tenant_scale"
title: 'ADR-008: A Team-Derived Membership Is Its Own Row'
description: 'A materialized Team membership is a separate member row rather than a level folded into an existing one, because the aggregate paths already tolerate several rows per user and folding needs a recompute that nothing can do correctly.'
status: accepted
creation-date: "2026-08-17"
authors: [ "@rymai" ]
---

## Context

[ADR-004](004-team_membership_is_an_ordinary_membership.md) decides that a grant materializes real `Member` rows. That immediately meets an invariant. `Member` validates one row per user per source, so a user cannot hold two memberships on the same group or project. Three ordinary situations violate it: a user is a direct member of a resource and also on a Team granted there; a user is on two Teams both granted on the same resource; and a user on a granted Team is later added directly.

The constraint is enforced in Rails, not in PostgreSQL. The `members` table has no unique index over its source and user, so duplicate rows are physically possible and the question is which behavior to choose rather than what the database allows.

Two shapes were available.

**Fold into one row.** Keep one membership per user per source, whose level is the maximum over the manual row and every Team grant, recomputed whenever any contributor changes. This is what SAML group synchronization does: it picks the highest of several group links and writes one row, overwriting whatever was there.

**Separate rows.** A Team-derived membership is its own row, carrying the Team it came from, and the uniqueness scope widens to admit it.

## Decision

**A Team-derived membership is its own member row.** The uniqueness scope widens by the Team reference, so a user may hold one manual membership plus one row per granted Team on the same resource.

The reason is that *several member rows per user is already the normal case, not an exception.* A user's level on a group is already resolved from rows spread across the group, its ancestors, and the groups shared into it, so the aggregate paths take a maximum by construction rather than assuming a single row. Folding would introduce a recompute in order to satisfy an invariant that the reading code does not depend on.

This was verified before deciding. With two member rows for one user on one group, group access resolves to the maximum on both the group and a descendant; `project_authorizations` holds exactly one row for the project at the maximum, with no duplicate and no oscillation across refreshes; billable members counts the user **once**; and the members finder returns one row, deterministically, because it applies `DISTINCT ON` per user ordered by access level with three tiebreakers. Nothing double-counts and nothing thrashes.

Separate rows also make the write paths trivial. Revoking a grant deletes the rows for that Team on that resource. Removing somebody from the roster deletes their rows for that Team. Both are idempotent and convergent, and neither has to remember or restore a level a human chose.

Folding, by contrast, would need all of the following to be correct: a place to remember the manual level so it can be restored when a Team grant is withdrawn, a rule for which contributor a single provenance column names when there are several, and a recompute on every roster and grant change. Synchronization needed the `override` column precisely because folding cannot tell a human's decision from its own, and that column exists to let a human win an argument the design should not have started.

## Consequences

### Positive

- **No recompute, no restore, and no override semantics.** A revoke is a delete. The manual membership is never written to, so it cannot be clobbered or lost
- **Attribution is exact.** Each row names one Team, so "why does this person have access here" is answered by the row rather than by reconstruction. Folding could not answer it for a user reached by two Teams
- **The aggregate paths need no change at all**, which is most of the authorization surface
- The members read surface already collapses several rows per user at the maximum, deterministically, so a person is not listed twice

### Negative

- **About fifteen single-row lookups become ambiguous** and have to be audited rather than mechanically fixed. Two are authorization-critical: the custom-role protected-branch check, which compares the role of the one row it finds and is deliberately ordered to prevent privilege escalation, and the token claim builders in secrets management. A third, the project team's member lookup, feeds the members UI
- **Relaxing a validation is a change to a model every part of GitLab uses**, so the blast radius is wider than the Teams feature even though the new rows only appear where a Team is granted
- **Row count grows with grants multiplied by roster size**, where folding would have kept one row per user per resource. This is the smaller of the two amplification stories — the propagation engine it replaces grew with subtree size — but it is growth on a table that is already among the largest
- One read path skips the collapsing: a members query filtered by custom role bypasses the per-user `DISTINCT ON`, so duplicates surface there and it needs handling

## Related Documents

- [Teams blueprint](../_index.md)
- [ADR-004: Team Membership Is an Ordinary Membership](004-team_membership_is_an_ordinary_membership.md)
- [ADR-007: Parity Before Migration](007-parity_before_migration.md)
