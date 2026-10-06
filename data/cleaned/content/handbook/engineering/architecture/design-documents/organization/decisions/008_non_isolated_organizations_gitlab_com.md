---
owning-stage: "~devops::tenant scale"
title: 'Organizations ADR 008: Non-isolated organizations on GitLab.com'
creation-date: "2026-03-04"
authors: [ "@tkuah", "@alexpooley" ]
toc_hide: true
---

## Context

Top-level groups (TLGs) on GitLab.com currently exist in a Default Organization
that is controlled by GitLab.
This Default Organization was not designed as a customer-owned entity -
it exists to facilitate pre-existing platform behavior such as cross-namespace forking.

With the introduction of organization-level features, a gap has emerged: new features require an Organization.
[ADR 007](007_self_managed_dedicated_single_organization.md) establishes that self-managed and Dedicated instances have a 1-1 mapping between instance and Organization.
On GitLab.com this does not apply.
The Default Organization is owned by GitLab, not by TLG owners,
so TLG owners cannot configure or control it.

## Decision

Any newly created organization starts as non-isolated.

Upon transferring:

- The TLG owners become the owners of the new Organization.
- All resources owned by the TLG are transferred to the new Organization.
- Resources not owned by the TLG, but by the Default Organization, are **not** transferred.
  This includes Users.

Continuity of access will be preserved across both organizations,
until the isolation is developed.
Features that depend on organization-scoped data must similarly check whether
the current organization is non-isolated before applying organization boundary enforcement.

### Resources owned by the Default Organization

There are some types of resources that are related to the TLG, but
are owned by the Default Organization.
Examples include `User`, `PoolRepository`, and `Projects::Topic`.
These resource types will need to be either:

- Copied to the new organization.
- Transferred to the new organization.
- Do nothing - resource stays with the Default Organization.
- Require the TLG owner and/or new organization owner to perform a manual action.

The above actions can happen during the TLG transfer, or after the TLG is transferred.
As access to these resources are still available to the new non-isolated
organization, users should not see any changes regardless.

## Consequences

- TLG owners gain the ability to own and configure their Organization
  independently of GitLab's Default Organization settings.
- New organization-level features become available to TLGs that have transferred.
- TLGs that remain in the Default Organization do not gain access to these features.
- Users retain access to resources across organization boundaries until isolation is enforced by the owner.
- Multiple TLGs can be transferred into the same Organization,
  supporting enterprises and teams that operate across multiple TLGs.

## Alternatives Considered

1. [Shadow Organizations](https://gitlab.com/gitlab-com/content-sites/handbook/-/merge_requests/18453)

## Rollout options under consideration

### Automatic organization creation per TLG

Automatically create one Organization per TLG, using the TLG `path` and `name` as the organization attributes.

Rejected because:

- Some TLGs want to share an organization (for example, `gitlab-org` and `gitlab-com`).
  It is estimated that 30% of TLGs can be matched to multi-TLG organizations.
  Automatic 1-1 creation forecloses this without an additional merge step.
- The `path` and `name` of the auto-created organization may not reflect owner intent
  and cannot be assumed from the TLG attributes.
- Some features have expensive `organization_id` rewrite costs (for example, Artifact Registry).
  Automatic creation could trigger these rewrites without owner awareness or consent.
- Given there are millions of TLGs on GitLab.com, automatic migration would
  result in a non-trivial amount of churn and incorrect organization assignment.

### Organic adoption

Rejected because:

While we will always allow an TLG be to tranferred by an owner, we cannot rely
solely on organic adoption. This approach does not scale.

### Managed bulk transfer (primary)

We will progressively migrate TLGs into organizations on a schedule we control (much like cohorts).
Migration order is determined by a taxonomy
([Epic 21393](https://gitlab.com/groups/gitlab-org/-/work_items/21393))
that balances migration complexity against business value.
This is not a single big-bang event — it is a sustained, timeboxed program that can be paced, paused, and adjusted
as tooling matures and the team learns from earlier cohorts.

Each TLG is transferred into its own organization (1:1 mapping).
We do not attempt to infer multi-TLG groupings automatically.
Instead, we provide tooling for owners to consolidate multiple TLGs (from different organizations) into a single
organization ([Epic 21394](https://gitlab.com/groups/gitlab-org/-/work_items/21394)) after transfer.

When a TLG is migrated via the bulk path, the resulting organization is created in an `unconfirmed` state.
While unconfirmed:

- The organization exists and the TLG operates normally within it.
- Org-level features (UAM, org-level admin, etc.) are not yet available.

When the organization owner next engages with their organization, they are guided through a mandatory onboarding flow,
which the organization owner can provide information which other TLGs to merge
if necessary.
This ensures customers are never surprised by an org configuration they didn't
choose, without requiring them to initiate the transfer themselves.

### On-demand (secondary)

There might be TLGs where the migration to an organization has not happened yet.

In order to adopt a feature that needs Organization, GitLab will place the TLG
automatically in an organization, if not already.
The organization owner is also guided through a mandatory onboarding flow (see
above).
