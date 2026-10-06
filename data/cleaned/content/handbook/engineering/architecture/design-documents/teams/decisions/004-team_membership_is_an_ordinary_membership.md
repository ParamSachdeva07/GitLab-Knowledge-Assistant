---
owning-stage: "~devops::tenant_scale"
title: 'ADR-004: Team Membership Is an Ordinary Membership'
description: 'A grant materializes real Member rows, one per roster user, so every consumer of membership supports Teams without being taught about them.'
status: accepted
creation-date: "2026-08-17"
authors: [ "@rymai" ]
---

## Context

Granting a Team a role on a group or project could be treated as a new kind of access, with its own rules for how it combines with other access, how far it reaches, and who may manage it. Every one of those rules already exists for members, so writing them again for Teams means a second implementation of behavior the permissions system settles for everyone else.

The aim is the opposite. Integrate with the system that is already there, keep the change footprint as small as the feature allows, and inherit correctness rather than re-earning it. Every path Teams leaves untouched is a path that cannot acquire a Teams-specific bug.

Enforcement is where that choice pays, because GitLab resolves access differently for projects and for groups. Project access has a materialized cache, `project_authorizations`, which already aggregates direct membership, the group hierarchy, and group shares. **Group access has no equivalent.** A user's level on a group is computed on demand as a union of member rows from the group and its ancestors with member rows reached through group shares, memoized only for the life of the request. Anything hooking into enforcement would have to hook in twice, in two different shapes, and keep them agreeing.

One point upstream serves both. **Group abilities and `project_authorizations` alike resolve from `Member` rows, so a grant can create them.** The objection that the code reads a specific table and Teams are not in it is answered by putting rows in the table, rather than by teaching every reader about a second kind of principal.

This was verified rather than assumed. A plain `GroupMember` row at Developer on a group confers group-level access on that group *and* on a descendant subgroup with no per-descendant row, reaches `project_authorizations` at Developer for a project two levels down, and counts toward billable members, with no Teams-specific code in any of those paths.

## Decision

**A grant materializes real `Member` rows.** Granting a Team a role on a namespace creates one `GroupMember` or `ProjectMember` per roster user on that namespace, at that role, recording the Team it came from. Revoking deletes those rows. Roster changes add and remove them across the Team's grants.

A Team membership is therefore an ordinary membership in the literal sense, not only the semantic one. A grant writes the same rows a human invitation writes, so Teams get the existing roles, the existing inheritance, and the existing member-management rules without defining any of them.

Five things follow, and each is load-bearing:

- **The grant row remains, as the declaration.** Member rows are its materialization, not a replacement for it. A Team with an empty roster granted on a resource produces no member rows, so deriving the grant from them would lose it; `granted_by`, the rationale, and the expiry are properties of the assignment rather than of each row; and reconciliation needs a statement of intent to converge toward, or a partially applied grant is indistinguishable from one somebody deleted rows from.
- **Provenance is a foreign key to the Team, not a flag.** `members.ldap` is a boolean and records only *that* a row came from synchronization, never which group. A column pointing at the Team answers attribution directly, with no enum and no fixed set of values to maintain, and it scopes both revocation and reconciliation to one indexed delete.
- **A Team-derived membership is its own row** rather than a level folded into an existing one ([ADR-008](008-a_team_derived_membership_is_its_own_row.md)).
- **A materialized row is not human-editable.** Managing members takes Maintainer, but granting a Team is an Owner's decision. Without a rule, a Maintainer could delete a few materialized rows and quietly un-grant part of a Team. So the update and destroy abilities are prevented on Team-derived rows. There is precedent: a project bot's membership is managed through the token flow rather than the members UI.
- **A grant that does not fit the seat capacity fails whole.** Capacity is checked for the whole roster in the service, before any row is written, which is what the existing seat-overage check already does for an invitation, on the namespaces where it is enabled. Checking row by row instead would fail quietly, because the mechanisms disagree about how: over capacity, one creates a member row in an awaiting state that confers nothing, while another rejects individual rows outright. Either way a half-applied grant would be indistinguishable from a complete one.

No Teams avenue is added to either effective-access computation.

### Roster Fan-Out

A grant becomes one member row per roster user, and a roster change reaches every namespace the Team is granted on. Adding somebody to a Team holding 200 grants touches 200 namespaces, so the work is asynchronous.

The member rows are not the end of it. Writing a member row on a group enqueues a `project_authorizations` refresh for the projects beneath it, so a roster change fans out twice: into member rows, and then into the project access cache for every affected subtree. The second fan-out is the one every membership change already pays; Teams pays it at roster scale.

How durable it has to be follows from an asymmetry: **a lost addition delays access, while a lost removal leaves access that should be gone.** Removal is a correctness requirement, not a latency one.

It does not need an outbox, because **the grant and the roster are together a complete specification of the member rows that should exist.** Drift is one indexed query joining the two and looking for rows that are missing or surplus. So the state lives on the declaration rows: a grant records whether it has been materialized, and a revocation passes through a pending state so a lost job cannot leave access behind — the rows go first, the declaration goes last, with a reconciliation cron as the backstop.

Directory synchronization is the closest existing analogue, because it also materializes member rows from a declaration. This design follows its shape and adds the durability it lacks.

## Consequences

### Positive

- **Seat counting, audit events, and the membership UI stop being Teams work.** Billable members are computed from member rows; member changes already generate audit events; the members page already renders member rows. Each was a separate epic
- **Custom roles and expiry ride along.** A member row carries `member_role_id` and `expires_at`, so two constraints recorded as gated or deferred become properties the row already has
- **Role-based rules gain Teams for free.** A rule naming a role rather than a principal, such as "Maintainers can push", resolves through a maximum aggregation, so a Team-materialized row satisfies it with no per-feature work. This reduces the parity surface in [ADR-007](007-parity_before_migration.md) to rules that name a *group* as a principal
- Member reuse returns: mentions, invitations, and the existing membership UI are available rather than forgone, reversing a consequence of [ADR-003](003-a_team_is_a_principal_not_a_container.md)

### Negative

- **Member sprawl becomes real, and it is visible through the API.** Granting a 500-person Team puts 500 rows on the resource. The complaint Teams exist to answer is that people manage hundreds of individual memberships, and this answers it with automation rather than elimination. The rows being real is inseparable from the benefits above: they are *why* seats and group abilities work
- **A Rails invariant has to be relaxed.** `Member` validates one row per user per source, and about fifteen single-row lookups become ambiguous once that is widened. Two are authorization-critical: the custom-role protected-branch check, whose own comment explains it is ordered to prevent privilege escalation, and the secrets-management token claim builders. These are security fixes, not cleanups
- **Seat capacity and roster additions.** A grant that does not fit the capacity fails whole, but what to do when somebody is added to a Team that already holds grants on capacity-limited namespaces? Refuse the roster addition, accept it but display a warning, something else?
- **Billing changes as soon as the rows exist.** Team-granted users become billable. This is the correct outcome and it is a customer-visible pricing consequence rather than a scheduled step
- **Every materialized row carries the member-created side effects.** An activity event, an access-granted notification, and a `:create` system hook fire per row, and no suppression flag exists today, so one is needed before this can be enabled at scale
- **Deleting a Team becomes a large destructive member operation** rather than the removal of a few grant rows, which raises the stakes on the safety [ADR-003](003-a_team_is_a_principal_not_a_container.md) claims for Team deletion
- Two existing behaviors have to be suppressed for materialized rows: the validation refusing a level below what a user inherits from an ancestor, which would otherwise make materialization depend on the order of unrelated changes, and the member-destroy cascade into sub-resources, which would otherwise delete unrelated memberships beneath a revoked grant
- A materialized Owner row can satisfy the last-owner guard, so revocation has to refuse to orphan a resource

## Related Documents

- [Teams blueprint](../_index.md)
- [Roles and permissions](https://docs.gitlab.com/user/permissions/)
- [ADR-003: A Team Is a Principal, Not a Container](003-a_team_is_a_principal_not_a_container.md)
- [ADR-005: Grants Target Namespaces](005-grants_target_namespaces.md)
- [ADR-007: Parity Before Migration](007-parity_before_migration.md)
- [ADR-008: A Team-Derived Membership Is Its Own Row](008-a_team_derived_membership_is_its_own_row.md)
