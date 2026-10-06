---
owning-stage: "~devops::tenant scale"
title: 'Organizations ADR 012: Organization is a scoped space'
description: 'Every Organization occupies its own scoped space, independent of isolation and Cell placement.'
creation-date: "2026-06-16"
authors: [ "@alexpooley" ]
toc_hide: true
---

## Context

An Organization is a **logical boundary** — more than a data boundary, it is a
self-contained space that owns its own resources, names, and features. That
boundary shows up in three independent ways:

- **Scoped space** — the boundary in the address space (names, routes). Always
  present.
- **Isolation** — whether the data layer actually prevents data from crossing
  between Organizations (see [Organization Isolation](../isolation.md)). Enforced
  gradually, so a [non-isolated](008_non_isolated_organizations_gitlab_com.md)
  Organization already has its space even if its data boundary is not yet enforced.
- **Cell placement** — the boundary realized in physical infrastructure.

These are orthogonal. Scoped space is the logical boundary made addressable, so
it exists whether or not the data is isolated or the Organization lives on its
own Cell.

## Decision

Every Organization occupies its own scoped space, including non-isolated ones.
Scoping is an addressing and ownership decision, so it does not wait on isolation
being enforced or on a move to a dedicated Cell. Concretely, this means:

1. **Its own namespace.** Today every routable name (e.g. Groups and Projects)
   must be unique across one shared global namespace (cluster-wide on GitLab.com). Two customers cannot both have a "Marketing" group; they
   contend for the same global name. An Organization space partitions that
   namespace, so names need only be unique within the Organization.
2. **A single, predictable point of change.** Legacy URLs are retained, but the
   URL format changes once a resource enters an Organization. We make that change
   at one logical point — entering the Organization — rather than later when the
   Organization moves to a Cell. The path does not encode the Cell, so Cell moves
   never change URLs.
3. **A home for Organization-level features.** Organizations own features, such
   as security dashboards, that need a place to live in the URL space, just as
   Groups, Projects, and Users do.

## Consequences

- Non-isolated Organizations are scoped from creation, not retrofitted later.
- The URL mechanism for this is the `/o/<organization>/` scope decided in
  [ADR 004](004_path_scope.md).
- The transition away from the legacy system to the Organization system does come
  with complications — for example, legacy global routes and scoped routes
  coexisting — but these are essentially unavoidable.
