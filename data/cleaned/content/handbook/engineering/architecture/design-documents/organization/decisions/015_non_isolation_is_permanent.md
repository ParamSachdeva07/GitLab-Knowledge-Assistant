---
owning-stage: "~devops::tenant scale"
title: 'Organizations ADR 015: Non-isolation is a permanent Organization state'
description: "ADR establishing that a non-isolated Organization is a valid, indefinite state, not a phase every Organization is expected to leave."
creation-date: "2026-07-28"
authors: [ "@alexpooley" ]
toc_hide: true
---

## Context

[Organization Isolation](../isolation.md) assumes every Organization
eventually isolates, and [Non-isolated organizations on GitLab.com](008_non_isolated_organizations_gitlab_com.md) treats
non-isolation only as a starting point on the way there. Whether
non-isolation is temporary or a valid, permanent outcome has been
ambiguous until now. This ADR makes it explicit.

## Decision

A non-isolated Organization is a permanent, valid state. An Organization
is never required to isolate. Isolation is something an Organization's
owner opts into, if and when it makes sense for them — not a
destination every Organization is expected to reach.

## Consequences

1. [Organization Isolation](../isolation.md)'s opening claim, that all
   Organization data will be isolated, is corrected as part of this
   ADR. Its phased rollout further down still describes engineering
   milestones as though every Organization eventually isolates;
   revising that is a separate piece of work.
1. A non-isolated Organization may remain on the legacy Cell
   indefinitely, not only until it isolates. A separate, upcoming
   Organization-scoped request context blueprint works out what this
   means for Cell placement in full.
1. Multi-Organization membership is not a temporary side effect of an
   in-progress migration. It is a permanent capability for any
   Organization that stays non-isolated.

## Alternatives considered

1. **Treat non-isolation as a temporary migration state, with every
   Organization eventually isolating** — rejected. Isolation means no
   data crosses the boundary, so an isolated Organization gives up all
   interop with other Organizations. Many Organizations rely on that
   interop today. Isolating every Organization anyway would break real
   workflows for them; assuming it will happen assumes a replacement
   interop capability that does not exist yet. One idea, sometimes
   called "Org Connect," could someday fill that gap, but it remains a
   long way off.
