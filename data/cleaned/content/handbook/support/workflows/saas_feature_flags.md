---
title: Enabling and disabling feature flags for projects or groups on GitLab.com
category: GitLab.com
description: "Workflow to follow when customers request that a feature flag be enabled for a GitLab.com project or group"
---

## Overview

This workflow covers cases where a customer requests support to enable [feature flags](https://docs.gitlab.com/development/feature_flags/controls/) on their GitLab.com groups, projects, or users.

Enabling feature flags can be done using ChatOps. Before you can use ChatOps, you will need to [request access](https://docs.gitlab.com/development/chatops_on_gitlabcom/#requesting-access).

## Process

When a customer requests a feature flag:

1. If the feature flag issue does not already say it can be enabled for customers, comment on the feature flag issue to confirm that the product and development teams are comfortable with Support turning on the feature flag for customers.
1. Add the customer's Account Owner/Customer Success Manager found in ZenDesk as a CC on the ticket so that they are aware of the request.
1. Run the appropriate [ChatOps command](#chatops) to enable it.
1. Once enabled, add an internal comment on the feature flag issue with:

- A screenshot of the ChatOps response on the feature flag issue. This should include the group, project, or user that the feature flag is scoped to.
- The relevant ZenDesk ticket.

If Engineering recommends that a feature flag be enabled for a customer:

1. Inform the customer that we would like to enable a feature flag that will assist with debugging or enable a feature that is anticipated to fix the issue.
1. Link the customer to the Feature Flag issue so they are aware of the change the flag controls
1. Enable the feature flag once the customer confirms the change can be made.
1. Add the customer's Account Owner/Customer Success Manager found in ZenDesk as a CC on the ticket so that they are aware of the request.
1. Run the appropriate [ChatOps command](#chatops) to enable it.
1. Once enabled, add an internal comment on the feature flag issue with:

- A screenshot of the ChatOps response on the feature flag issue. This should include the group, project, or user that the feature flag is scoped to.
- The relevant ZenDesk ticket.

Declining a feature flag means may prevent further troubleshooting. Let the customer know when we expect the feature covered by the flag will be released.

Customers may request a feature flag that was previously be enabled be disabled.

1. Validate that the Feature Flag is still active. If it is not, let the cusstomer know the feature flag is no longer active and the feature covered by the flag is live.
1. Add the customer's Account Owner/Customer Success Manager found in ZenDesk as a CC on the ticket so that they are aware of the request.
1. Run the appropriate [ChatOps command](#chatops) to disable it.
1. If we had created an internal comment on the feature flag issue when enabling the flag, update the thread with:

- A screenshot of the ChatOps response on the feature flag issue. This should include the group, project, or user that the feature flag is scoped to.
- The relevant ZenDesk ticket.

## ChatOps

To enable a feature flag using ChatOps, follow [the process](https://docs.gitlab.com/development/feature_flags/controls/#process) described in the Feature Flags documentation.

Typically you will want to set the Feature Flag by actor and run one of the following in the #production Slack channel. Be sure to replace the placeholders.

- For project-actor: `/chatops run feature set --project=<path/to/project_1,path/to/project_2> feature_flag_to_be_enabled true`
- For group-actor: `/chatops run feature set --group=<group_namespace> feature_flag_to_be_enabled true`
- For user-actor: `/chatops run feature set --user=<username> feature_flag_to_be_enabled true`

If you are unsure how it should be applied, reach out to the appropriate owner or team on the Feature Flag issue. You can also test against your own group, project, or user but should ensure to disable the feature flag once you are done testing.
