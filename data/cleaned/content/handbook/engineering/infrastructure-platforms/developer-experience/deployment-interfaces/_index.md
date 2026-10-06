---
title: "Deployment Interfaces"
description: "The Deployment Interfaces team owns the common contract between the teams that build GitLab and the people who operate it."
---

## Mission

The Deployment Interfaces team owns the common contract between the teams that build GitLab and the people who operate it. The interface guarantees a consistent deployment experience everywhere GitLab operates: an engineer's laptop, GitLab.com, Dedicated, Cells, and every Self-Managed customer.

We build the paved roads that make the easy way to ship the right way to ship, so that the work teams take on deploys well for every customer by default.

Deployment Interfaces is part of the wider [Theseus initiative](../../../architecture/design-documents/theseus_platform_vision/).

## Team Members

{{< team-by-manager-slug manager="mkomor1" team="Deployment Interfaces(.*)" >}}

## Primary Projects

| Name | Description |
|------|-------------|
| [Fairway](https://gitlab.com/gitlab-com/gl-infra/platform/runway/fairway) | Generates a self-contained Helm chart from a `FairwayManifest` that declares a service's deployment shape and its infrastructure dependencies. Fairway is the concrete implementation of the Deployment Interfaces contract for Kubernetes-based targets. |

## Common Links

| What | Links |
|------|-------|
| **Slack** | [`#g_deployment-interfaces`](https://gitlab.enterprise.slack.com/archives/C0BJ19WFZV3) *(planned)* |
