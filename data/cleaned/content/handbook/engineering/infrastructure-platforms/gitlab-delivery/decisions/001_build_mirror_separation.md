---
title: "Delivery ADR 001: New components use security mirror, not dev.gitlab.org"
owning-stage: "~group::release-and-deploy"
toc_hide: true
---

## Context

GitLab historically built and published release artifacts from a dedicated, separate GitLab instance
([dev.gitlab.org](https://dev.gitlab.org)). This provided a control plane boundary distinct from
GitLab.com and a fallback in the event of a GitLab.com outage.

As GitLab moves toward a more modular release architecture, the question arose whether new services
must continue using this separate instance or could instead use the security mirror on GitLab.com.
The full discussion is recorded in
[gitlab-com/gl-infra/delivery#21976](https://gitlab.com/gitlab-com/gl-infra/delivery/-/work_items/21976).

The core compliance question was: do SOC 2, FedRAMP, SLSA, and related frameworks require a separate
GitLab instance for builds, or do they require logical separation between build infrastructure and
production environments?

After consultation with Security and Compliance ([@madlake](https://gitlab.com/madlake),
[@jhebden](https://gitlab.com/jhebden)):

- No compliance framework mandates a separate GitLab instance. The requirement is **logical separation**
  between where software is built and where it runs in production.
- GitLab CI runners execute on compute infrastructure that is separate from GitLab.com application
  servers. This dedicated runner fleet constitutes the "build infrastructure" for compliance purposes.
- The Security mirror operates with its own restricted access model, separately auditable from the
  Canonical project. Builds triggered from it are scoped to that context.
- This combination, dedicated runners outside the production environment triggered from the
  access-controlled Security mirror, satisfies SOC 2 (CC8.1, CC6.1, CC6.6), FedRAMP, and SLSA L2+
  logical separation requirements.

## Decision

**New modular services and components do not need to use dev.gitlab.org.** They build and publish
release artifacts from the Security mirror on GitLab.com, using the dedicated CI runner fleet.

Existing processes that use dev.gitlab.org continue unchanged and are migrated gradually as the
broader release architecture evolves. This decision does not affect them.

## Consequences

- New components have a simpler, lower-maintenance build path. Repository mirroring to dev.gitlab.org
  is not required for new services.
- Logical separation between build infrastructure and production is maintained and auditable.
- Existing dev.gitlab.org tooling and processes are unaffected; migration is gradual and not required
  for compliance.
- The "chicken-and-egg" availability concern (GitLab.com outage blocking GitLab builds) remains a
  consideration for existing processes on dev.gitlab.org. For new modular components, this risk is
  acceptable by their service teams.  Should later this be deemed inappropriate, we may continue creating a third mirror as we do today.
- This reduces scope for which we need to audit with less instances in scope for monitoring.
