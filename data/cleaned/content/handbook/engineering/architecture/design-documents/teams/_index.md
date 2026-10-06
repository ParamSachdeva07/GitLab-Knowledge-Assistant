---
title: Teams
description: 'A Team is an Organization-scoped roster of users that can be granted a role on a group or project, the same way any other member is.'
status: proposed
creation-date: "2025-12-09"
authors: [ "@lohrc", "@jblack7", "@rymai" ]
dris: [ "@jblack7", "@rymai" ]
owning-stage: "~devops::tenant scale"
participating-stages: []
toc_hide: true
---

{{< engineering/design-document-header >}}

## Summary

GitLab's groups do two jobs at once: they organize projects into a namespace hierarchy, and they organize people and control their access. [Organizations](../organization/_index.md) will provide customer isolation, but the dual purpose lives *inside* each customer's boundary. Customers whose reporting lines and repository layout differ — which is most large customers — have no way to express that except by creating groups that exist only to hold people.

A **Team** is an Organization-scoped entity that holds a roster of users and can be granted a role on a group or project. **A Team is a new kind of member**: the grant uses the same authority, the same role semantics, and the same inheritance as inviting a user, and Teams change none of it. Teams grant access; a resource never belongs to a Team.

This page is the entry point. Background is in the [appendices](#related-documents), and each architectural choice has its own [decision record](#decisions).

## Status

A proof of concept exists, and nothing is generally available. Teams ship through the Organizations [release stages](../../../infrastructure-platforms/tenant-scale/organizations/release-stages.md) and their [release process](https://docs.gitlab.com/development/organizations/release_process/), gated by a `teams` organization flag declared in `config/organizations_release.yml`. Code asks `Organizations::Release.enabled?(:teams, actor)` with the Organization as the actor, which is the same boundary [ADR-002](decisions/002-teams_are_organization_scoped.md) draws.

## Problem

Nothing distinguishes a group used to organize work from a group used to organize people, so customers who need those structures to differ create member-bag groups and share them into the groups that hold work. Around **15% of groups contain no projects at all**, which is the clearest signal that a separate entity for people is missing.

Three consequences follow, and they are what customers report: inheritance producing unexpected access levels, sharing behavior that includes different populations depending on the target, and cognitive load from inheritance that is invisible until it surprises someone.

Full detail: [Appendix A](appendices/a-dual_purpose_group_problem.md), [Appendix B](appendices/b-customer_pain_points_research.md), and [Appendix C](appendices/c-industry_and_competitive_context.md).

## Goals

1. **Separate user management from project organization** within an Organization, so people hierarchies and project hierarchies can evolve independently, and enterprise identity can integrate with the first without disturbing the second.
2. **Make access assignment visible and auditable**, including a consistent answer to group-to-group and group-to-project sharing, and support for both hierarchical and flat cross-functional collaboration.
3. **Meet enterprise scale**: Organizations with 10,000+ users and thousands of projects, audit trails suitable for NIST 800-53, ISO 27001, and SOX, and bulk administrative operations.
4. **Enable cross-functional work coordination** — aggregating issues, merge requests, and epics for a Team across the Organization. The current architecture does not advance this goal; it delivers the access-control half of Teams.

Secondary goals are just-in-time access for sensitive operations, temporary elevation, service-account management, API-first automation, and self-service access requests.

## Non-Goals

- **Replacing groups, or restructuring the hierarchy.** Teams complement groups ([ADR-001](decisions/001-teams_complement_groups.md))
- **Replacing or reinterpreting roles and permissions.** A Team grant carries an existing role and behaves like any other membership ([ADR-004](decisions/004-team_membership_is_an_ordinary_membership.md)). Changing how roles combine or how inheritance works is a separate proposal about the permissions system
- **Aggregating resources horizontally.** A Team is not a container and cannot collect projects from across the hierarchy ([ADR-003](decisions/003-a_team_is_a_principal_not_a_container.md))
- **Nesting Teams.** Teams are flat. Nesting would create complexity that we want to avoid for now. Based on future requests, we might reconsider this
- **Disrupting existing workflows.** Group-based management, existing API contracts, and customer automation keep working, and mixed environments are supported for as long as customers need them. Group sharing is deprecated over the long term ([ADR-001](decisions/001-teams_complement_groups.md)), on a horizon set by parity rather than by a date

## What a Team Is

A Team holds a roster of users and is granted a **role on a namespace** — a group or a project namespace. Granting a Team is granting a member: it carries an existing role, it resolves the way any other membership resolves, and anyone who can manage members on a resource can grant or remove a Team's access to it ([ADR-004](decisions/004-team_membership_is_an_ordinary_membership.md)).

Enforcement asks nothing new of the permissions system, because **a grant materializes real member rows** — one per roster user, on the target namespace, carrying the Team they came from ([ADR-004](decisions/004-team_membership_is_an_ordinary_membership.md)). Project access, group abilities, seat counting, and audit events all read member rows already, so they support Teams without being taught about them, and a row on a group reaches every descendant the way any other membership does.

| Entity | Purpose |
| --- | --- |
| Team | Organization-scoped, with a name and an Organization-unique path |
| Team user membership | The roster. Each row carries a Team-level role: **admin** or **member** |
| Team namespace membership | The grant: a Team, a target namespace, and a resource role. A declaration, materialized as member rows |
| Member (existing) | The materialization. An ordinary member row referencing the Team it came from |

Two properties of the grant are load-bearing. **Grants target a namespace, not a project**, so one grant shape covers both groups and projects ([ADR-005](decisions/005-grants_target_namespaces.md)). And **the grant is the declaration rather than the access**, so it survives an empty roster, states who granted it and why once, and gives reconciliation something to converge toward.

## Decisions

| Decision record | In one line |
| --- | --- |
| [ADR-001: Teams Complement Groups](decisions/001-teams_complement_groups.md) | An additive layer over groups rather than a restructuring — a two-way door, with group sharing sunset long-term |
| [ADR-002: Teams Are Organization-Scoped](decisions/002-teams_are_organization_scoped.md) | A Team belongs to one Organization and never crosses customer isolation |
| [ADR-003: A Team Is a Principal, Not a Container](decisions/003-a_team_is_a_principal_not_a_container.md) | A resource never belongs to a Team; own tables, and flat |
| [ADR-004: Team Membership Is an Ordinary Membership](decisions/004-team_membership_is_an_ordinary_membership.md) | A grant materializes real member rows, so every consumer of membership supports Teams untouched |
| [ADR-005: Grants Target Namespaces](decisions/005-grants_target_namespaces.md) | A real foreign key, not a polymorphic target; external enforcers need a replicated principal |
| [ADR-006: The Teams API Surface](decisions/006-the_teams_api_surface.md) | GraphQL and REST both; grants ship now, organization-scoped management waits on a token boundary |
| [ADR-007: Parity Before Migration](decisions/007-parity_before_migration.md) | Features must learn Teams before their groups become convertible |
| [ADR-008: A Team-Derived Membership Is Its Own Row](decisions/008-a_team_derived_membership_is_its_own_row.md) | A separate member row per Team, not a level folded into one row |

## User Experience Surfaces

Teams appear in two places, keeping two concerns apart: *who is on a Team* is an Organization-level question, and *where a Team has access* is a resource-level one.

**The Organization Teams section** is a new sidebar entry with a Teams list and a Team detail page carrying the roster. Organization owners get create, delete, and roster management; other members see the same pages read-only.

**The members page** gains a Teams tab listing each Team with access to the group or project, its role, where the assignment came from, who granted it, when, and when it expires. It reads from the GraphQL Teams surface rather than the existing REST and Vuex members store, so it is a self-contained component ([ADR-006](decisions/006-the_teams_api_surface.md)). The Members tab gains read-only rows for people who reach the resource through a Team, with a pointer to the Teams tab. Lowering a grant's role takes access away from everyone who held it only through that Team, so it is confirmed rather than applied from a select.

A cross-resource access-attribution view, bulk assignment, custom roles, Team avatars, notifications, and email invitations are follow-ups.

## Migration From Group Shares

Roughly **35% of all group shares** in the `gitlab-org` hierarchy are Teams in all but name. These are converted by an opt-in, per-candidate assistant that creates a Team, seeds the roster, reassigns the grants, and removes the migrated links, with deletion of the emptied group as a separate step using adjourned deletion.

Eligibility is narrow, and the sharpest rule is that the group must not be referenced anywhere as a principal in its own right — protected branches, approval rules, CODEOWNERS, the CI job token allowlist, and others resolve a group's members themselves and would not see a migrated Team. Each of those features has to be taught to accept a Team before the groups it references become convertible ([ADR-007](decisions/007-parity_before_migration.md)).

## Scale

Customers hit practical degradation well before documented caps, so the architecture is designed to observed thresholds rather than hard limits: hierarchy depth of **5 levels or fewer**, **under 1,000 members per Team**, **under 100 direct children per parent**, and token-size awareness of **150 to 200 groups**. Warnings should arrive before a threshold rather than errors after it.

Three of those four sit at the conservative end of the cross-platform ranges in [Appendix C](appendices/c-industry_and_competitive_context.md) rather than being derived from them by a formula. The children-per-parent figure is a GitLab observation that appendix does not yet have a citation for.

## Known Limitations

- **Materialized rows carry the member-created side effects.** An activity event, a notification, and a system hook fire per row, and no suppression flag exists yet
- **For now, Teams reach no organization-level resource**, because those are enforced outside PostgreSQL ([ADR-005](decisions/005-grants_target_namespaces.md))
- **Deleting a Team removes many member rows**, so the operation is larger than removing a few grants even though it still removes only access

## Open Questions

- **Seat capacity and roster additions.** A grant that does not fit the capacity fails whole, but what to do when somebody is added to a Team that already holds grants on capacity-limited namespaces? There is a precedent to weigh: the automated provisioning paths — SAML, SCIM, and LDAP group sync — resolve this, behind a feature flag, by creating the member at a non-billable minimal-access level with an audit event rather than refusing. So the choice is between refusing the roster addition, accepting it with a warning, and following that precedent ([ADR-004](decisions/004-team_membership_is_an_ordinary_membership.md))
- **Which users a Team contributes to a group-principal feature.** When a feature names a *group* as a principal — "these groups may push to this protected branch" — it resolves that group's members itself, and features disagree about which ones count: most take direct members only, while protected environments let you choose direct or all (direct + inherited + shared). A Team's roster is flat, so that choice has nothing to select between. Two things follow, and neither is settled: does a direct-versus-all control still makes sense when the principal is a Team, and which population a conversion has to seed so the feature keeps behaving as it did ([ADR-007](decisions/007-parity_before_migration.md))
- **Enterprise identity.** The mapping gets simpler: a SAML or LDAP group link today ties an identity-provider group to a *role on a specific GitLab group*, whereas a Team roster carries no role, so an identity-provider group can map to a Team one-to-one. The plumbing is what is missing — group links and SCIM are built on `Member` records and a roster row is not one. Team-to-namespace grants would stay manual, which is defensible because identity providers rarely model the group hierarchy anyway
- **Fan-out for enforcers outside Rails.** For a resource enforced in IAM or OpenBao, does GitLab write one assignment per member, or does the Team become a set-valued subject in the enforcing service? ([ADR-005](decisions/005-grants_target_namespaces.md))
- **Horizontal aggregation.** Collecting resources from across the hierarchy under one entity ([work item 467558](https://gitlab.com/gitlab-org/gitlab/-/work_items/467558)) still has no answer, and Teams are not it ([ADR-003](decisions/003-a_team_is_a_principal_not_a_container.md))

## Success Criteria

**Performance and scale.** Effective access resolves under 1 second at p95 with 1,000+ Teams and 1,000+ projects; grant creation and revocation return under 500 ms at p95 with propagation completing asynchronously; both effective-access computations agree on every level as a verified test property; 99.95% uptime for permission-related operations.

**Administration and compliance.** Time-to-grant-access under 5 minutes, bulk operations across 100+ Team-resource relationships, a 50% reduction in inheritance-related support issues, 100% audit-trail coverage for permission changes, and passing NIST 800-53, ISO 27001, and SOX audits.

**Qualitative.** More than 80% of administrators correctly predicting inheritance patterns in user research, more than 70% developer satisfaction with the access request experience, and Fortune 500 customers implementing Teams.

## Dependencies

- **Organizations** — Organization-level user management, identity provider synchronization, audit scope, and isolation enforcement ([ADR-002](decisions/002-teams_are_organization_scoped.md))
- **Group-as-principal parity** — the largest body of dependent work ([ADR-007](decisions/007-parity_before_migration.md))
- **Billing** — billable-member computation needs a Team avenue before general availability
- **Enterprise identity** — LDAP and directory synchronization, SAML assertion processing, and OIDC provisioning for Team membership, none of which exists yet
- **External enforcement services** — reaching IAM and OpenBao means replicating Teams through the existing IAM outbox, whose allowed entity types would have to grow ([ADR-005](decisions/005-grants_target_namespaces.md))
- **The organization permission boundary** — `organization` is not an authorization boundary in code, so a granular token cannot authorize an organization-scoped endpoint. This blocks token access independent of Teams and can proceed in parallel. It is also what defers REST Team and roster management ([ADR-006](decisions/006-the_teams_api_surface.md))
- **The CE and EE seam** — no `ee/` Teams code exists, and creating it is part of whichever of audit events and custom roles lands first

## Relationship to the Functional Roadmap

A parallel, product-owned functional roadmap defines a foundational MVC and four releases. It agrees with this blueprint on nearly everything it calls foundational and diverges on five things that are hard conflicts, and three findings recorded here have no counterpart in it at all. The comparison is [Appendix D](appendices/d-proposal_reconciliation.md).

## Related Documents

### Appendices

Background and evidence. No decisions are made in these.

- [Appendix A: The Dual-Purpose Group Problem](appendices/a-dual_purpose_group_problem.md) — what is wrong today, and how Teams relate to roles, Organizations, groups, and projects
- [Appendix B: Customer Pain Points and Research Findings](appendices/b-customer_pain_points_research.md) — interviews, support analysis, and the patterns across them
- [Appendix C: Industry and Competitive Context](appendices/c-industry_and_competitive_context.md) — market pressure, how other platforms solved this, and the scale evidence
- [Appendix D: Reconciling the Blueprint With the Functional Roadmap](appendices/d-proposal_reconciliation.md) — where this architecture and the product roadmap diverge

### Related Blueprints

- [Organization](../organization/_index.md)
- [Group and project operations and state management](../group_and_project_operations_and_state_management/_index.md)
