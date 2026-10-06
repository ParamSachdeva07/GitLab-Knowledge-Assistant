---
title: "Communication and Confidentiality"
description: "How the Cloud Cost Utilization team communicates, and how FinOps/CCU data is classified across public, internal, and confidential levels"
---

## Overview

This page describes how the Cloud Cost Utilization (CCU) team communicates and how we classify information in the FinOps/CCU space. It complements the guidance in the [team overview](_index.md) and builds on GitLab's [communication handbook](/handbook/communication/) and [confidentiality levels](/handbook/communication/confidentiality-levels/).

CCU follows GitLab's [public by default](/handbook/values/#public-by-default) value: unless there is a specific reason to restrict access, information defaults to internal (visible to all team members), and preferably to public.

## Why this matters

Private conversations create inefficiency. They exclude people who could contribute, make it hard to pick up context, and force the same questions to be repeated. Moving discussion into public channels and issues improves team throughput and reduces mental overhead for individual team members.

Transparency is most valuable when it feels hardest. Defaulting to confidential feels safer and avoids the "everyone has an opinion" problem, but that is exactly where the cost of private communication accumulates. When something is marked confidential, state *why*: "This is confidential because …". If no reason applies, default to internal.

## Data classification for CCU/FinOps

We classify CCU/FinOps data into three levels, aligned with GitLab's [SAFE framework](/handbook/legal/safe-framework/) and [confidentiality levels](/handbook/communication/confidentiality-levels/).

### Public (handbook)

Methods, frameworks, and definitions — **no values, no customers, no margins**.

- CCU mission and scope
- [Labeling strategy](labeling-strategy.md) and cost allocation approach
- Formulas and definitions for unit economics (what we measure and how, with dimensions and examples)

### Internal (SAFE data)

All cloud cost numbers and non-margin aggregates, visible to all GitLab team members.

- Cloud cost numbers by vendor, account, service, or product
- Unit economics aggregates without margin or customer context (for example, cost per `gl_service`, cost per environment)
- `gl_service`-level cost budgets and savings targets (technical budgets we set and discuss with owning teams)

### Confidential / MNPI

Restricted to specific audiences. Examples include:

- Margin views (hosting margin, product/segment margin, margin bridges)
- Customer-level or customer-segment economics (for example, hosting cost per customer, margin per plan, Duo unit margins)
- Company-level hosting AOP/Budget
- Forward-looking financials

## Communication channels

| Channel | Purpose |
|---|---|
| [`#g_cloud-cost-utilization`](https://gitlab.enterprise.slack.com/archives/C09MUMXRECC) | CCU team channel — team work and topics **driven or owned by** CCU |
| `#g_finops` | Wider FinOps space — CCU participates or is affected, but is not the primary driver |
| `#g_hosting_exec` | Confidential/MNPI topics in a VP/Exec context |
| [CCU issue tracker](https://gitlab.com/gitlab-com/gl-infra/finops/team/-/issues) | Tracked work and requests |

`#g_cloud-cost-utilization` is the default for CCU team discussion.

Use `#g_finops` when the topic spans the broader FinOps space, e.g. for hosting cost questions.

Use the confidential channels only when the content actually requires the confidential classification above.

## Handling direct messages and private groups

CCU does not take work requests via direct messages or private group chats. The GitLab handbook gives the same guidance: [do not use group direct messages](/handbook/communication/#do-not-use-group-direct-messages) and [use public channels](/handbook/communication/#use-public-channels).

If you receive a private message asking CCU to take an action, spend time on a topic, or weigh in on a decision:

1. Acknowledge the message and redirect it to a public forum — `#g_cloud-cost-utilization`, `#g_finops`, or an issue in the [CCU issue tracker](https://gitlab.com/gitlab-com/gl-infra/finops/team/-/issues).
2. Link to [do not use group direct messages](/handbook/communication/#do-not-use-group-direct-messages) rather than explaining the reasoning yourself.
3. Do not spend time on the topic until it has been redirected.

This applies regardless of who is asking. When prioritization is the real question, the request can be routed to CCU's Engineering Manager.

For discussions that don't fit an issue, take the conversation into the appropriate public Slack channel and respond in-thread. The context is often useful to the wider audience, and others can chime in.
