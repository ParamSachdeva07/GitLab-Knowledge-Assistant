---
title: "GitLab Omnibus-Adjacent Kubernetes ADR 005: Zero-downtime upgrades"
description: "Decision on zero-downtime upgrade (ZDU) support for OAK: ZDU is an orchestration concern at the component level, not an Omnibus-specific concern."
owning-stage: "~devops::gitlab delivery"
toc_hide: true
---

## Summary

This ADR documents the decision on zero-downtime upgrade (ZDU) support for OAK. In OAK deployments, Omnibus GitLab runs alongside advanced components in Kubernetes. ZDU for OAK is an orchestration concern at the component level, not an Omnibus-specific concern. Advanced components must be designed to support ZDU independently, without creating mid-upgrade dependencies on GitLab omnibus upgrade sequences.

## Key findings from discovery

Omnibus already has documented ZDU procedures at [Zero-downtime update documentation](https://docs.gitlab.com/update/zero_downtime/). ZDU applies only to multi-node Omnibus deployments; single-node deployments require downtime.

For advanced components, ZDU depends on component design. Each component must support ZDU at the functional level. Full HA and zero-downtime upgrades require multi-node Kubernetes clusters with proper pod draining and rolling update strategies defined in component Helm charts.

Each advanced component's upgrade must be independent of GitLab component upgrade sequences — it must be executable before, after, or outside the Omnibus upgrade cycle. Coupling to mid-upgrade states of Omnibus must be avoided. For example, a component must not require upgrading only after PostgreSQL is upgraded but before Rails.

## Decision

Omnibus ZDU follows existing guidance at [Zero-downtime update documentation](https://docs.gitlab.com/update/zero_downtime/). No Omnibus-specific changes are required for OAK deployments.

Each product team owns ZDU design and documentation for their component, including designing the component to support ZDU independently (multi-node deployment, rolling updates, pod disruption budgets), documenting the upgrade process, and validating ZDU procedures. Components must not create dependencies on Omnibus upgrade sequences.

Omnibus does not provide automation or orchestration for advanced component upgrades.

## Customer workflow

Customers planning zero-downtime upgrades follow this workflow:

1. Refer to ZDU documentation for multi-node Omnibus upgrade procedures.
2. For each advanced component, refer to component-specific ZDU documentation to determine upgrade timing (before, after, or independent of Omnibus).
3. Design an upgrade plan and execute upgrades in the documented order.

OAK documentation provides a high-level overview of this workflow and directs customers to component-specific ZDU guidance.

## References

1. [Zero-downtime update documentation](https://docs.gitlab.com/update/zero_downtime/)
1. [Discovery work item #9692](https://gitlab.com/gitlab-org/omnibus-gitlab/-/work_items/9692)
