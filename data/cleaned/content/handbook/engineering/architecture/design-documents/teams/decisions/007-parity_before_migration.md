---
owning-stage: "~devops::tenant_scale"
title: 'ADR-007: Parity Before Migration'
description: 'Features holding a direct group reference must learn Teams before their groups become convertible, and conversion of clean-replacement group shares is opt-in per candidate.'
status: accepted
creation-date: "2026-07-28"
authors: [ "@rymai" ]
---

## Context

Roughly **35% of all group shares** in the `gitlab-org` hierarchy are Teams in all but name: a group with members but no projects and no subgroups, created purely so it could be shared. These are the customers Teams was built for, and they already did the work of separating people from places with the only tool available. Offering them an assisted path is the difference between a feature they might eventually adopt and one they adopt now.

Conversion is not uniformly safe, because a group grants access in three structurally different ways:

- **Through membership.** Membership and both kinds of share resolve into member rows and the effective-access cache, and a grant materializes real member rows, so a converted Team is indistinguishable from the group it replaced ([ADR-004](004-team_membership_is_an_ordinary_membership.md))
- **Through a rule that names a role.** "Maintainers may push to this branch" resolves through a maximum over the user's memberships, so a materialized Team member satisfies it with no per-feature work. This category needs nothing
- **Through a direct group reference held by a feature.** The feature stores a group ID and resolves that group's members itself — "these groups may push to this protected branch", "an approval from this group is required". A Team is not a Group, so these features do not see a migrated Team at all. This is the only category that needs parity work

The second category is a catalog, not an edge case:

| Category | Features |
| --- | --- |
| Group as actor | Protected branch push, merge, and unprotect access; protected tag creation; protected environment deploy access and deployment approval; Branch Rules, transitively |
| Group as approver | Merge request approval rules at project, MR, and group level, on both approval-rule models; scan result and merge request approval policies; CODEOWNERS group references, and reviewer suggestions derived from them |
| Other subsystems | CI job token allowlist, Kubernetes agent CI and user access authorizations, Secrets Manager principals |

Approval rules are the one entry with two implementations rather than one: the newer `MergeRequests::ApprovalRule` holds its group approvers in a table of its own. Both rails have to be counted, and neither is reached by widening the other.

The catalog is finite and, unlike a prose list, checkable. Every entry is a table holding a foreign key to a group used as a principal, so the set is derivable by scanning the schema for those columns, and that derivation could be diffed against this catalog in CI so a new group-principal feature cannot land unnoticed. No such check exists today; it is proposed here because the alternative is a list that silently rots. The exclusion check in the Decision below is the same catalog in executable form. Tracking follows the shape used for Organizations feature parity: one sub-epic per cluster of features, with a further one for the generic principal abstraction.

Converting a group referenced this way would leave the reference pointing at a group that is now empty. Approvals would stop being satisfiable, or a protected branch would stop accepting pushes, with nothing in the conversion flow indicating it.

## Decision

**Parity precedes migration, feature by feature, and conversion is opt-in per candidate.**

- A group referenced anywhere as a principal is **excluded from conversion**, enforced by a check against the tables above
- Each feature in the catalog is extended to accept a Team alongside a group, on its own schedule. Each one that lands makes another population of groups eligible
- The long-term target is a **generic principal abstraction**, so a feature accepts a user, a group, or a Team uniformly instead of each one growing a third foreign key, resolution path, and selector
- Conversion of an eligible candidate is offered as a recommendation with a before-and-after preview, behind its own organization flag, so conversion can sit at an earlier stage than Teams itself. It creates a Team from the shared-with group, seeds the roster with that group's direct members, grants the Team the same role and expiry on each target, and removes the migrated share links. Deleting the emptied source group is a **separate, explicitly opt-in step** using adjourned deletion
- Eligibility also requires both ends in the same Organization ([ADR-002](002-teams_are_organization_scoped.md)), base roles only, and a pure member bag with no projects and no subgroups

Ordering is the point: the exclusion check is what makes opt-in conversion safe to offer before parity is complete. Automatic migration was rejected on risk — nobody should discover a broken approval rule from a background job.

"First-class principal" is a claim about the **assignment** layer, not the ability-evaluation layer. A feature should be able to record that a Team is an approver the way it records a group. It does not follow that a Team appears where abilities are evaluated: a Team decides *which users*, and then the existing per-user path runs unchanged. That distinction is what bounds the work to one more principal kind per join table and selector.

## Consequences

### Positive

- Conversion cannot silently strip access or approvals, which is the failure mode that would have discredited the migration assistant permanently
- The dependency runs the right way round: migration coverage grows as parity lands, rather than parity being chased after customers hit the gap
- Risk is bounded per candidate — the smallest unit of change is one share, reviewed by a human — and adjourned deletion gives the most consequential step a recovery window
- A generic principal abstraction pays back beyond Teams

### Negative

- **This is the largest body of dependent work in the Teams program**, spanning a dozen tables. Until much of it lands, Teams are a second-class principal in practice, however ordinary the member rows they materialize
- **Adoption is the risk this creates.** Outside the clean 35%, conversion is either unavailable or lossy, and a converted Team stays second-class until the features referencing its old group have landed. The first customers to try Teams may reasonably conclude it does less than the groups they already have. Closing that gap needs bulk conversion tooling and a documented migration pathway, not parity alone
- Three gaps in the exclusion check are known: the CI job token allowlist is in a different database and cannot be joined, CODEOWNERS is file-based rather than table rows, and the newer approval-rule approver table is simply absent from the check
- **Narrow eligibility caps reach.** The 35% figure is the ceiling for the clean cases, within a single Organization. Groups doing two jobs at once are the harder and more common enterprise reality and get nothing here
- Custom-role shares are excluded, because whether a grant may carry a custom role is a roadmap decision that has not been taken. The materialized row can hold a `member_role_id` ([ADR-004](004-team_membership_is_an_ordinary_membership.md)), so the data model is no longer what stands in the way; a member role must belong to a single top-level namespace, while a Team is Organization-scoped and can be granted across several. The customers most invested in custom roles convert last either way
- One-at-a-time conversion does not scale to hundreds of candidates, and conversion is not reversible as a single operation
- Per-feature parity means per-feature semantic decisions, because a Team's roster is flat while group-principal features vary in whether they resolve direct or all members
- **The abstraction reaches only as far as Rails.** A resource enforced in an external service needs the Team replicated to it instead ([ADR-005](005-grants_target_namespaces.md)), so parity is two programs and only the first has an exit

## Related Documents

- [Teams blueprint](../_index.md)
- [ADR-004: Team Membership Is an Ordinary Membership](004-team_membership_is_an_ordinary_membership.md)
- [ADR-005: Grants Target Namespaces](005-grants_target_namespaces.md)
- [ADR-006: The Teams API Surface](006-the_teams_api_surface.md)
