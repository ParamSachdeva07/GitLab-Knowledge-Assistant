---
owning-stage: "~devops::tenant_scale"
title: 'ADR-006: The Teams API Surface'
description: 'Teams ship in both GraphQL and REST. The split is by scope rather than by protocol: grants live on groups and projects, and Team management waits for an organization authorization boundary.'
status: accepted
creation-date: "2026-07-28"
authors: [ "@rymai" ]
---

## Context

Teams need an API, and both of GitLab's protocols have a claim on it. GraphQL is where new surfaces are built. REST is where the members API lives, and customers with large-scale administrative needs automate against it heavily — for a feature aimed at enterprises, script-driven grant management is an early request rather than a later nicety. What each protocol can carry is not a question of effort, and the line does not fall where the protocol boundary falls.

**Granular tokens have no organization boundary.** Endpoint authorization declares a permission and a boundary type, and the boundary types in use are project, group, instance, and user. There is no organization — the same finding the blueprint records as an external dependency. That splits the surface by scope:

- **Grants live on a group or a project**, so they declare a group or project boundary and can ship today
- **Team and roster management is organization-scoped**, so it has no honest boundary to declare. `POST /organizations` solves this with an instance boundary, which means a token permitted to manage Teams in one organization has to be scoped to the whole instance. Arguably proportionate for creating an organization; not for a routine roster edit

A second question is how a grant is expressed in REST. [ADR-004](004-team_membership_is_an_ordinary_membership.md) makes a Team a new kind of member, which suggests extending `POST /:id/members` with a Team parameter. That breaks down in practice: one call would create a member row per roster user, so there is no single member to return, and it changes the contract of the most heavily automated endpoint in the API.

## Decision

**Teams ship in both GraphQL and REST, and the boundary between them is scope, not protocol.** Everything that can declare a group or project boundary exists in both. Organization-scoped management is GraphQL-only until the boundary exists.

### GraphQL

- **Organization surface** — querying an Organization's Teams and their members, and mutations to create, update, and delete a Team and to add and remove members
- **Namespace surface** — querying a group's or project's Team grants, including the source namespace, granting user, grant time, and expiry, and mutations to assign, change a role, and revoke
- Team-derived member rows are exposed through their own relation rather than mixed into the members connection

### REST

Grants are a sub-resource on groups and projects, mirroring the shape of `POST /groups/:id/share` without borrowing its name, because a Team grant is not a share:

| Method and path | Purpose |
| --- | --- |
| `GET /groups/:id/teams` | Teams granted a role directly on this group |
| `GET /groups/:id/teams/all` | Including grants inherited from ancestor groups |
| `GET /groups/:id/teams/:team_id` | One grant |
| `POST /groups/:id/teams` | Grant a Team a role. Takes `team_id`, `access_level`, and optionally `expires_at` and `member_role_id` |
| `PUT /groups/:id/teams/:team_id` | Change the role or the expiry |
| `DELETE /groups/:id/teams/:team_id` | Revoke |

The same six exist under `/projects/:id/teams`. The direct-versus-all split mirrors `/members` and `/members/all` rather than inventing a parameter, because it is the same distinction and callers already know it.

**Team-derived member rows are opt-in on the members endpoints.** `GET /:id/members` and `GET /:id/members/all` gain a parameter to include them, matching the GraphQL choice to expose them through a relation rather than in the default response. Such a row carries the Team it came from, or the response cannot be interpreted.

**The abilities are the member abilities**, on both surfaces, not a parallel Teams vocabulary. ADR-004 makes granting a Team use the same authority as granting a user, so these endpoints declare the permissions the members endpoints declare. A token that may manage members may manage Team grants, which is the intended consequence rather than an oversight.

REST also grows Team support wherever the parity work in [ADR-007](007-parity_before_migration.md) requires an existing endpoint — protected refs, protected environments, approval rules — to accept a Team alongside a group. Those endpoints are already REST, and changing their contract is not optional.

### Deferred, and Why

Team creation, update, and deletion, and roster management, all under `/organizations/:id/teams`. The shape is not in question; the blocker is that a granular token cannot be scoped to an organization, and shipping with an instance boundary would hand out far more than the operation needs. This is tracked as blocked on a named dependency rather than as unplanned.

## Consequences

### Positive

- The operation that matters most for automation is available in the protocol automation uses. Granting and revoking is the repetitive administrative act; creating a Team is rare by comparison
- Grant endpoints carry an honest token boundary, so a token can be scoped to the group or project it administers
- No existing contract changes. The members endpoints gain an optional parameter and an optional field, and nothing in a current response moves
- Field-level permission exposure in GraphQL comes for free, so the UI can hide controls a user cannot use without a second authorization round trip
- The deferred half has a named blocker that is already an external dependency of the program, so it is schedulable rather than open-ended

### Negative

- **Coverage is uneven, and the unevenness is invisible in the API.** A script that provisions a Team and then grants it access needs both surfaces. Nothing in `/organizations` explains why there is no `teams` sub-resource, so the absence reads as an omission rather than a constraint, and documentation has to carry that
- A second write path to the same state means the grant services must be the only place authorization and materialization live, or REST and GraphQL will drift
- Reusing the member abilities means a change to member-management permissions silently changes who can grant Teams. That is correct under ADR-004, and it is a coupling worth stating
- Two surfaces are two things to design, review, document, and deprecate, on a data model that is still settling

## Related Documents

- [Teams blueprint](../_index.md)
- [ADR-002: Teams Are Organization-Scoped](002-teams_are_organization_scoped.md)
- [ADR-004: Team Membership Is an Ordinary Membership](004-team_membership_is_an_ordinary_membership.md)
- [ADR-007: Parity Before Migration](007-parity_before_migration.md)
