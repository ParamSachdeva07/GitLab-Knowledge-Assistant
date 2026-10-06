---
owning-stage: "~devops::tenant_scale"
title: 'Appendix D: Reconciling the Blueprint With the Functional Roadmap'
description: 'Where this architecture and the product-owned functional roadmap diverge, and who has to resolve each difference.'
status: accepted
creation-date: "2026-07-29"
authors: [ "@rymai" ]
---

A second Teams proposal exists: a product-owned **functional roadmap** in the `gitlab-com/tenant-scale/product/teams` project (internal), defining a foundational MVC and four releases (R1 to R4, as that project names them). A cross-resource **Direct Access Only** proposal owned by the Authorization group is an input to it. This appendix records where they and this blueprint disagree. It is background: no decisions are made here, but it records where decisions are needed.

Neither document referenced the other before this appendix, which is why the overlap is agreement and the edges are contradiction. The two agree on nearly everything the roadmap calls foundational — no ambient access from Team membership, a grant that records its rationale and authority, no upward inheritance, an organization that is not a permission root, flat Teams, absolute Organization boundaries — and diverge on much of what this blueprint treats as settled.

## Hard Conflicts

Resolving any of these changes either the architecture or the roadmap. There is no version where both stand as written.

| # | Conflict | Positions | Owner |
| --- | --- | --- | --- |
| 1 | **Polymorphic grant targets or a real foreign key** | Both documents now agree Teams should eventually reach organization-level resources ([ADR-005](../decisions/005-grants_target_namespaces.md)), so the disagreement is how, not whether. The roadmap's decision brief recommends a polymorphic association at MVC, covering projects and Artifact Registry resources. [ADR-005](../decisions/005-grants_target_namespaces.md) decides namespaces only, and holds findings the brief does not: the registry has no table, model, or policy in Rails, and there is no organization equivalent of `project_authorizations`. Polymorphism here is cheap and ineffective | Teams, Authorization and Artifact Registry  |
| 2 | **Teams materializes, or authorization consults** | The roadmap commits that Teams does not enforce permissions and that authorization consults the grant record. ADR-004 adds no avenue to either effective-access computation, but it materializes real `Member` rows, which is membership rather than derived state. The conflict inverts rather than closing: a cache write would have been easier to call an implementation detail than writing the table authorization reads as its source of truth. Cheap if the commitment is about adding no authorization code paths, expensive if it forbids Teams writing membership | Architectural review, where the commitment is a launch bar |
| 3 | **Custom roles: layering on, or a build-out** | Both agree a custom role belongs to an assignment rather than to a Team. The cost estimate conflicts, but by less than it did: a materialized member row carries `member_role_id` ([ADR-004](../decisions/004-team_membership_is_an_ordinary_membership.md)), so the data model is no longer the obstacle and R2 needs re-estimating **down**. What remains is real — member roles are EE-only with no CE Teams seam to extend, and a member role must belong to a single top-level namespace while a Team is Organization-scoped and can be granted across several | Product, to re-scope R2 |
| 4 | **Rollback** | The roadmap promises a flag-off state indistinguishable from before the MVC, as a numbered exit criterion. The [Organizations release process](https://docs.gitlab.com/development/organizations/release_process/) defines rollback as lowering a stage, one at a time, and makes no claim about data: enforcement is gated by the member rows a grant materializes, not by the flag, so regressing a stage hides the interface while access already conferred keeps working. Restating the guarantee in the process's own terms is far cheaper than a revoke-everything path, which would mean a destructive pass over `members` on a stage change | Product, to restate |
| 5 | **Does a resource belong to a Team?** | [ADR-003](../decisions/003-a_team_is_a_principal_not_a_container.md) decides that it never does: containment would put a Team on the same footing as a group and reintroduce the dual-purpose problem one level up. A recent product discussion favours Team-owned resources as the better model. Half of this was our own wording error, now fixed — a Team granted the Owner role *does* hold an Owner's authority, so "a Team never owns a resource" was never the right claim. What remains is genuinely open, and [ADR-001](../decisions/001-teams_complement_groups.md) records that Team ownership can be added later without a migration, so it is a two-way door rather than a foreclosed option | Product and Engineering, together |

## Out of Scope for Teams

- **May a resource refuse inherited access?** Direct Access Only would let a node stop inherited and shared access reaching it. That is a change to GitLab's inheritance model for every member rather than a Teams feature, so Teams does not answer it, and [ADR-004](../decisions/004-team_membership_is_an_ordinary_membership.md) is unaffected either way: a Team-materialized row is an ordinary member row, so whatever the inheritance model does to member rows it does to these. The roadmap's "explicit and enumerable", Authorization's "explicit over implicit", and this blueprint's position are the same argument reaching opposite conclusions, but the argument belongs to Authorization and needs no Teams session

## Resolved in This Revision

- **End state.** [ADR-001](../decisions/001-teams_complement_groups.md) committed to permanent coexistence, against the roadmap's deprecation horizon for legacy group sharing at R4+. ADR-001 now adopts the horizon: coexistence is how Teams arrive, and group sharing is deprecated, sunset, and eventually removed in favour of Team grants. Two qualifications carry into the roadmap — group *membership* is not deprecated, because a group's own members are how its projects are reached; and the sunset is gated on the group-as-principal parity in [ADR-007](../decisions/007-parity_before_migration.md) rather than on a date, because a group referenced as a principal cannot be converted until its feature accepts a Team

## Findings Absent From the Roadmap

Each of these gates a roadmap release and has no line in it. They need roadmap entries rather than debate.

- **Seat counting.** Billable members are computed entirely from `Member` rows, and a grant now creates them ([ADR-004](../decisions/004-team_membership_is_an_ordinary_membership.md)), so Team-granted users become billable the moment a grant lands. Nothing has to be built; what the roadmap lacks is a line for the pricing consequence, because granting a 500-person Team bills 500 seats on that namespace. The unresolved part is capacity — a grant that does not fit fails whole, but a roster addition against an existing capacity-limited grant cannot be refused the same way
- **Group-as-principal parity.** Roughly a dozen tables hold direct group references and none see a migrated Team ([ADR-007](../decisions/007-parity_before_migration.md)). R3's guided conversion is gated on a program the roadmap does not budget for, and R4's Teams-first default on more of it
- **The CE and EE seam.** No `ee/` Teams code exists, so audit events at MVC cannot be met as written. The same missing seam blocks custom roles, so whichever lands first pays for it — an argument for sequencing them together that neither document makes. It also exposes a direct conflict between the roadmap's principle that governance must not sit behind a tier boundary and audit events being Premium and above

## Resolved by Treating a Team as an Ordinary Member

Several roadmap items describe Teams-specific permission behavior. ADR-004 removes them from the comparison rather than answering them: role mutability, per-member exceptions, and whether attribution renders one row per source or collapses to the direct row are all properties of the members system, and Teams follow whatever it does. Where the roadmap wants different behavior, it wants it for every member.

Two related items are real and remain:

- **Removal is not immediate.** The roadmap states that removing a user from a Team revokes their access on every granted resource immediately. The subtree propagation engine is gone, but roster fan-out remains: removing somebody from a Team holding 200 grants deletes rows on 200 namespaces asynchronously, with the durability carried on the declaration rows rather than in an outbox. The roadmap needs to describe eventual consistency in customer-facing terms
- **Explaining access is a launch bar on one side and a follow-up on the other.** The roadmap requires an access explanation panel, a cross-cutting matrix, and an auditor view at MVC. What exists is per-assignment attribution on the members-page Teams tab. Because every inherited row carries its source, this is additive interface work rather than a re-architecture, which answers the roadmap's open question about attribution cost at scale

## Straightforward

The blueprint answers three open roadmap questions outright: Team object storage is standalone tables ([ADR-003](../decisions/003-a_team_is_a_principal_not_a_container.md)); per-Organization gating is not only feasible but prescribed, because Teams ships through the [Organizations release process](https://docs.gitlab.com/development/organizations/release_process/); and grant expiry exists today rather than waiting for R1. One is naming: Owner and Member against admin and member for Team-level roles. Flag naming is no longer open — an organization flag is an entry in `config/organizations_release.yml` and its stage is the rollout state. One is evidence — this blueprint holds the numbers the roadmap argues without, in [Appendix B](b-customer_pain_points_research.md).

## Process Observation

The two places the roadmap makes specific schema recommendations are the two places the proposals conflict hardest. Routing those questions into this document tree, which already existed, would have avoided conflicts 1 and 3. Conflicts 2 and 4 touch commitments the roadmap treats as settled, so they need a route back into the foundation document rather than into a release-scope discussion.

Suggested order: conflict 1 first, because a session is already scheduled and it now turns on how rather than whether; then conflict 5, which needs Product and Engineering together and decides how ADR-003 reads; then conflict 2, which is cheap if terminological; then the three absent findings; then conflicts 3 and 4. The inherited-access question no longer needs a Teams session at all.

## Related Documents

- [Teams blueprint](../_index.md)
- [ADR-004: Team Membership Is an Ordinary Membership](../decisions/004-team_membership_is_an_ordinary_membership.md)
- [ADR-005: Grants Target Namespaces](../decisions/005-grants_target_namespaces.md)
- [ADR-007: Parity Before Migration](../decisions/007-parity_before_migration.md)
