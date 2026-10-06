---
owning-stage: "~devops::tenant_scale"
title: 'ADR-003: A Team Is a Principal, Not a Container'
description: 'A resource never belongs to a Team, and Teams live in their own tables rather than as a namespace type.'
status: accepted
creation-date: "2026-07-28"
authors: [ "@rymai" ]
---

## Context

Two questions about what a Team *is* were answered together, because the answers depend on each other.

**Does a Team own resources?** One proposal modeled Team-owned groups and projects, so that "the Platform Team's projects" would be a real relationship and transferring work between Teams would be a first-class operation. Ownership would make a Team a container, which puts it on the same footing as a group and reintroduces the dual-purpose problem [ADR-001](001-teams_complement_groups.md) set out to avoid, one level up.

**Is a Team a namespace type?** Modeling a Team as a new `namespaces` type would inherit routing, path handling, the `Member` model, the existing membership UI, mentions, and invitations — very little new code for a working roster. It would also inherit everything else a namespace implies: a parent, hierarchy traversal, cascading settings, global path cardinality, and a large amount of code assuming a namespace is a place where work can live. Each of those would need suppressing or special-casing.

## Decision

**A resource never belongs to a Team.** A Team holds a roster and receives access; ownership of groups and projects stays where it is today. A Team granted the Owner role has an Owner's authority over that resource, like any other member at that role — the distinction being drawn is containment, not authority.

- Groups and projects continue to live in the namespace hierarchy, owned as they are today
- Deleting a Team removes access; it never removes, orphans, or reassigns a resource
- There is no "move this project to that Team" operation, because a project never belonged to a Team

**Teams are standalone entities with their own tables**, not a `namespaces` type. A Team is a row with an Organization, a name, and an Organization-unique path; its roster is a separate table of user memberships, each carrying a Team-level role of **admin** or **member**. Teams have no parent-child relationships — a Team granted access high in a hierarchy already covers everything beneath it without being nested. This is a position to hold rather than a default.

Standalone tables are not a standalone bounded context. Teams belong to the **`Organizations`** context, where the boundary in [ADR-002](002-teams_are_organization_scoped.md) already lives, so the classes sit under `Organizations::` and the tables carry the `organization_` prefix.

## Consequences

### Positive

- Deleting a Team is safe: the worst case is lost access, not lost work. This matters given how strongly customers report fear of accidental deletion with cascading effects
- The blast radius of the whole feature is bounded to authorization. No existing ownership, transfer, or deletion path changes
- No suppression work: a Team cannot acquire cascading settings or appear in a hierarchy walk, because it is not in the hierarchy
- Deep-nesting performance problems, the main criticism of hierarchical Team models on other platforms, cannot arise

### Negative

- **A Team cannot aggregate resources horizontally.** Use cases that want a Team-owned space, or a single entity collecting projects from across the hierarchy ([work item 467558](https://gitlab.com/gitlab-org/gitlab/-/work_items/467558)), are not served and still need a container entity of some kind. Alternatively, resources aggregation could happen based on what resources a Team has access to
- Reporting questions of the form "what does this Team own?" have no direct answer; the closest is "what does this Team have access to?"
- Directory synchronization is built around group membership today, so Team membership sync has no existing path to extend
- A flat Team set does not mirror an org chart, and customers who want that shape have to express it in naming. This is the real cost of holding the position, and it is accepted rather than deferred: the platforms surveyed in [Appendix C](../appendices/c-industry_and_competitive_context.md) either nest and propagate access through a hierarchy GitLab already has in its namespaces, or nest and decline to propagate access at all

## Related Documents

- [Teams blueprint](../_index.md)
- [ADR-001: Teams Complement Groups](001-teams_complement_groups.md)
- [ADR-004: Team Membership Is an Ordinary Membership](004-team_membership_is_an_ordinary_membership.md)
