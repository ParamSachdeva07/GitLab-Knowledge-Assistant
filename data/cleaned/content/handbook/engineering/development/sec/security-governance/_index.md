---
title: Security Governance Stage
description: >-
  The Security Governance stage builds policy, compliance, and AI governance
  capabilities so customers can define security rules once and enforce them
  across the platform.
---

The Security Governance engineering stage owns how security and compliance rules are
expressed, stored, evaluated, and audited across GitLab, including the governance surface
for AI workloads.

This stage was formed in the FY27 Sec reorg from the former Security Risk Management stage
plus the Compliance group.

## Leadership

| Role | Person |
| --- | --- |
| Stage lead | Mohamed Waseem (`@mwaseem5`) |
| Senior Staff Engineer | Mehmet Emin Inaç (`@minac`) |

## Teams

| Group | Engineering Manager | Tech Lead | Label |
| --- | --- | --- | --- |
| [Policy Engine](policy-engine/) | Alan Paruszewski (`@alan`) | Martin Cavoj (`@mcavoj`) | `group::policy engine` |
| [Policy Management](policy-management/) | Alan Paruszewski (`@alan`) | Alexander Turinske (`@aturinske`) | `group::policy management` |
| [Security Controls](security-controls/) | Alan Paruszewski (`@alan`) | Gal Katz (`@gkatz1`) | `group::security controls` |
| [Compliance](compliance/) | Nathan Rosandich (`@nrosandich`) | Huzaifa Iftikhar (`@huzaifaiftikhar1`) | `group::compliance` |
| [AI Governance](ai-governance/) | Nathan Rosandich (`@nrosandich`) | Jean van der Walt (`@jeanvdw`) | `group::ai governance` |
| [AI Control Plane](ai-control-plane/) | Abhimanyu Singh (`@asingh73`) | To be hired | `group::ai control plane` |

Group membership is sourced from Workday and published on the
[product categories page](/handbook/product/categories/#sec-section).

Renamed groups still link to their previous handbook location. Those pages move under this
stage in a follow-up merge request, tracked in the
[Sec reorg project](https://gitlab.com/gitlab-org/software-supply-chain-security/reorg-act2-2026-06/-/issues).

## Labels

Work in this stage carries the `devops::security governance` stage label plus the owning
group's `group::` label. Both are scoped labels and exist in the `gitlab-org` and
`gitlab-com` top-level groups.

## Slack

- `#sec-security-governance` - stage channel.

Per-group channels are listed on each group page. Several channel renames are still in
progress, tracked in
[Sec reorg issue 2](https://gitlab.com/gitlab-org/software-supply-chain-security/reorg-act2-2026-06/-/issues/2).
