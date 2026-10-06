---
title: Security Platform Stage
description: >-
  The Security Platform stage builds the authentication, authorization, abuse
  prevention, secrets management, and software supply chain foundations of the
  GitLab platform.
---

The Security Platform engineering stage owns the platform primitives that every other part
of GitLab depends on for identity and trust: authentication, authorization, abuse
prevention, secrets management, and the software supply chain.

This stage was formed in the FY27 Sec reorg from the former Software Supply Chain Security
stage plus the Dynamic Analysis group.

## Leadership

| Role | Person |
| --- | --- |
| Stage lead | Mark Mishaev (`@mmishaev`) |
| Senior Staff Engineer | James Hebden (`@jhebden`) |

## Teams

| Group | Engineering Manager | Tech Lead | Label |
| --- | --- | --- | --- |
| [Authentication](authentication/) | Mike Eddington (`@mikeeddington`) | Smriti Garg (`@sgarg_gitlab`) | `group::authentication` |
| [GATE Infra](gate-infra/) | Mike Eddington (`@mikeeddington`) | Matthias Käppler (`@mkaeppler`) | `group::gate infra` |
| [GATE Core](gate-core/) | Mike Eddington (`@mikeeddington`) | Shilpa Kundapur (`@skundapur`) | `group::gate core` |
| [Authorization](authorization/) | Jordon Proctor (`@jpr0c`) | Ian Anderson (`@imand3r`) | `group::authorization` |
| [Abuse Engineering](abuse-engineering/) | Jordon Proctor (`@jpr0c`) | Jay Swain (`@jayswain`) | `group::abuse engineering` |
| [Build Security](build-security/) | Mark Mishaev (`@mmishaev`, interim) | To be hired | `group::build security` |
| [Dependency Firewall](dependency-firewall/) | Mike Eddington (`@mikeeddington`) | Mike Eddington (`@mikeeddington`) | `group::dependency firewall` |
| [Secrets Manager (Application)](secrets-manager/application/) | Connor Fleming (`@cfleming3`) | Erick Bajao (`@iamricecake`) | `group::secrets manager application` |
| [Secrets Manager (OpenBAO)](secrets-manager/openbao/) | Connor Fleming (`@cfleming3`) | Fabien Catteau (`@fcatteau`) | `group::secrets manager openbao` |

Group membership is sourced from Workday and published on the
[product categories page](/handbook/product/categories/#sec-section).

## Labels

Work in this stage carries the `devops::security platform` stage label plus the owning
group's `group::` label. Both are scoped labels and exist in the `gitlab-org` and
`gitlab-com` top-level groups.

## Slack

Per-group channels are listed on each group page. Several channel renames are still in
progress, tracked in
[Sec reorg issue 2](https://gitlab.com/gitlab-org/software-supply-chain-security/reorg-act2-2026-06/-/issues/2).

## On-call

Teams in this stage participate in the Sec on-call rotation. See the
[Sec on-call handbook](/handbook/engineering/development/sec/oncall/).
