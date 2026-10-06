---
owning-stage: "~devops::tenant scale"
title: "Organizations ADR 013: Warn when creating a Top-Level-Group inside an organization"
description: "Documents the decision to warn users when creating a Top-Level-Group inside an organization, explaining that subscriptions and credits do not transfer between sibling Top-Level-Groups until organization-level billing ships."
creation-date: "2026-04-27"
authors: ["@sxuereb"]
toc_hide: true
---

## Context

Subscriptions (Free, Premium, Ultimate), credits, and related billing entitlements are scoped to a Top-Level-Group, not to an organization.
When a Top-Level-Group is transferred into an organization, its existing license remains attached to that Top-Level-Group. However, if a user creates another Top-Level-Group under the same organization, the new Top-Level-Group does not inherit the sibling Top-Level-Group's subscription or credits.

For example, the owner of the `acmea` Top-Level-Group creates a new organization (also named `acmea`) and transfers the Ultimate-licensed Top-Level-Group into it:

```text
acmea (org)
└── acmea (Top-Level-Group)
```

If the organization owner then creates a new Top-Level-Group called `tlg-new`, they may expect it to behave the same way as `acmea`. It does not, because billing is currently tied to each Top-Level-Group until [organization-level billing](https://gitlab.com/gitlab-org/customers-gitlab-com/-/merge_requests/15263) exists.

```text
acmea (org)
├── tlg-new
└── acmea (Top-Level-Group)
```

As Organizations become the primary structure users interact with, this distinction becomes easier to miss: creating a group directly under an organization produces a sibling Top-Level-Group rather than extending the billing scope of an existing one.

## Decision

When a user creates a Top-Level-Group inside an organization, we surface a warning during that flow. The warning communicates that:

- Subscription tier (Free, Premium, Ultimate) is scoped to each individual Top-Level-Group and is not shared with sibling Top-Level-Groups in the same organization.
- Credits are also scoped per Top-Level-Group, so a new Top-Level-Group does not inherit credits from its siblings.
- Billing for the new Top-Level-Group is separate from its siblings until [organization-level billing](https://gitlab.com/gitlab-org/customers-gitlab-com/-/merge_requests/15263) ships.

The warning remains in place until [organization-level billing](https://gitlab.com/gitlab-org/customers-gitlab-com/-/merge_requests/15263) ships, after which it can be removed.

## Consequences

- Customers retain flexibility to structure their organization with multiple Top-Level-Groups, which is a core value proposition of Organizations.
- Billing remains scoped per Top-Level-Group until [organization-level billing](https://gitlab.com/gitlab-org/customers-gitlab-com/-/merge_requests/15263) ships. The affected population is small today, but expected to grow as Organizations roll out, so surfacing the distinction early reduces avoidable confusion without blocking adoption.
- The broader plan to roll all existing Top-Level-Groups into organizations is unblocked. Multi-Top-Level-Group organizations remain able to adopt new features (such as Artifact Registry) and to be migrated between cells.
- We avoid one-way-door decisions that would later require building organization-merging, registry-merging, or organization-affinity tooling.
- A user may dismiss the warning and still create a Top-Level-Group whose billing differs from its sibling, leading to surprises later. Clear, specific warning copy reinforced in onboarding mitigates this risk but does not eliminate it.

## Alternatives Considered

1. **Do nothing**: users would create new Top-Level-Groups with no signal that licensing and credits are not shared. Rejected because the divergence only becomes visible later when a feature or credit is unexpectedly unavailable, creating UX papercuts and support load.
1. **Share entitlements**: if one Top-Level-Group has credits or a license attached, share those entitlements across all Top-Level-Groups in the same organization. Rejected because entitlements are currently modeled and audited at the Top-Level-Group boundary, and sharing them across sibling Top-Level-Groups would require significant changes in downstream billing and entitlement systems such as CustomersDot.
1. **Block creation of new Top-Level-Groups inside organizations**: prevent the creation of any new Top-Level-Group in an organization until [organization-level billing](https://gitlab.com/gitlab-org/customers-gitlab-com/-/merge_requests/15263) exists. Rejected because:
   - It is inconsistent with the existing path that allows multi-Top-Level-Group customers to reconcile into a single organization.
   - It blocks the broader rollout where existing Top-Level-Groups become organizations, since "you cannot create a Top-Level-Group" is a regression for those customers.
   - It blocks multi-Top-Level-Group organizations from adopting features such as Artifact Registry, and from being migrated between cells.
   - It creates one-way-door decisions: forcing customers into separate organizations would later require building organization-merging, registry-merging, and organization-affinity tooling.
   - It undermines a core value proposition of Organizations: letting customers flexibly structure their groups and projects. Self-Managed and Dedicated customers commonly operate with hundreds or thousands of Top-Level-Groups today, suggesting Top-Level-Groups will become the natural unit of organizational structure inside Organizations.
