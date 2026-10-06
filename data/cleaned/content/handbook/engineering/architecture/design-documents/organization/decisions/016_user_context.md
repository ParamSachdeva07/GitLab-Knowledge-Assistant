---
owning-stage: "~devops::tenant scale"
title: 'Organizations ADR 016: organization_id and Organization-scoped query filtering'
description: "ADR that defines the isolation-based rule for when organization_id creates exclusive membership, and the Organization filter rule, closing a gap the isolated-Organization work knowingly left open."
creation-date: "2026-07-27"
authors: [ "@alexpooley" ]
toc_hide: true
---

## Context

See [Request Context](../contexts.md) for the three contexts every
request or process resolves to: Organization context, User context, and
Nil context.

Today, `organization_id` is required, and membership in that
Organization is always treated as exclusive, whether or not the
Organization is isolated. This blocks User context for every User:
every User's identity is always bound to one Organization.

Today, routing also treats "no Organization" the same as "Default
Organization." This blocks Nil context the same way, and causes bugs
(see [issue #605747](https://gitlab.com/gitlab-org/gitlab/-/issues/605747)).

[ADR 015: Non-isolation is a permanent Organization state](015_non_isolation_is_permanent.md)
established that some Organizations stay non-isolated indefinitely. User
context and Nil context only make sense given that fact: they need
Users whose membership is not exclusive, not just Users who have not
isolated yet.

The isolated-Organization work moved straight from "every User belongs
to one Organization" to "every Organization is isolated." It did not
define the states in between. This decision fills that gap.

## Decision

### Isolation, not presence, decides whether membership is exclusive

`organization_id` stays required. It is also the `users` table's
Cells sharding key, so every User needs a concrete value; that cannot
change.

```text
User.organization_id: org_id
```

What changes is the rule for what that value means. Isolation gates
User context, not whether `organization_id` points at an
Organization — it always does. This field only affects User context —
Nil context has no User to apply it to.

Ownership — `organization_id` itself — is always exclusive: it points
at exactly one Organization. What isolation decides is whether
membership is exclusive too:

1. Points at a **non-isolated** Organization — the User has User
   context. Membership is not exclusive: the User can be a member of
   any number of other non-isolated Organizations too, with the same
   account, and User context aggregates across all of them.
1. Points at an **isolated** Organization — required for every member.
   The User has no User context: the Organization is a real boundary,
   and the User's identity does not exist outside it.

Invariant: membership in an isolated Organization implies
`organization_id` points at it, with no exceptions. A User's
`organization_id` points at, at most, one isolated Organization at a
time. It is reassigned once, at isolation, for members not already
pointing at it. It does not change as memberships change afterward.

### Query scoping

Org-scoped finders apply an Organization filter when the Organization
acts as a real boundary:

```ruby
apply_org_filter = org.present? && org.isolated?
```

This is the core rule. There is a separate, secondary optimization for
instances with only one Organization: when `Organization.count == 1`,
filtering is a no-op, so we skip it. This is a performance detail, not
part of the scoping rule.

Self-managed and Dedicated instances have exactly one Organization, the
Default Organization, so `Organization.count == 1` is true for every
install there, and the filter stays a no-op, at no cost.

### Routing must decide, per route, which context applies

Today, a path with no Organization prefix (for example
`/dashboard/...`) implies the Default Organization. A path with an
Organization prefix (for example `/o/acme/...`) implies that
Organization instead.

User context and Nil context are real, separate values now, not
variants of "no Organization" that fall back to the Default
Organization. An unprefixed path like `/dashboard/...` could mean User
context, or it could still mean Organization context bound to the
Default Organization. A path like `/explore` could mean Nil context, or
it could likewise still mean the Default Organization today.

We must choose, one route at a time, which context applies. Some routes
(for example, a personal to-do list) likely want User context. Some
routes (for example, `/explore`) likely want Nil context. Other routes
may still want the Default Organization. This decision does not resolve
that choice. It only makes the three contexts real enough to choose
between.

## Consequences

On .com, every existing User's `organization_id` already points at
the Default Organization, which is non-isolated. No backfill is needed.
User context is available: a User's to-do list, and other User-context
views, span every non-isolated Organization they are a member of — for
example, an open-source contributor who is also a member of a company
Organization.
