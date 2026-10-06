---
title: 'Topics'
description: 'Documentation on Zendesk Copilot topics'
---

This guide covers how to create, edit, and manage Zendesk Copilot topics at GitLab.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
- Project repo: [Topics](https://gitlab.com/gitlab-support-readiness/zendesk-copilot/topics)
- `CustSuppOps Zendesk Test Suite Generator` disabled

{{% /alert %}}

## Understanding topics

As per [Zendesk](https://support.zendesk.com/hc/en-us/articles/8903424797722-Setting-up-intelligent-triage-topics):

> topics classify what a ticket is about. You can use the topics that appear in tickets to automate your workflows.

### How we manage topics

We currently manage all topics within Zendesk itself. To ensure we enable non-administrator collaboration and have version control, the source of all topics (and their descriptions) is managed via the [Topics](https://gitlab.com/gitlab-support-readiness/zendesk-copilot/topics) project repo.

### Anatomy of a topic

A topic is an item within a subcategory (which is within a category). Within each topic is a description that Zendesk Copilot uses to help determine if a ticket should use that topic.

As an example, the topic `Product::Geo::Geo replication or failover` :

- Category: `Product`
- Subcategory: `Geo`
- Topic: `Geo replication or failover`
- Description (example used, might not reflect production value):
  > Tickets about GitLab Geo replication, secondary sites, and disaster recovery for distributed self-managed deployments. Symptoms include replication lag, verification failures, site failover or re-sync problems, tracking database issues, and content that is missing or out of date on a secondary node. Use when the issue is specific to Geo behavior rather than general database or storage problems.

### Topic naming restrictions

A topic, as well as its category and subcategory, can only use alphanumeric characters and spaces. No special characters, such as hyphens, slashes, or underscores, are allowed.

## Requesting topic changes

{{% alert title="Note" color="warning" %}}

If you are trying to modify the category or subcategory specifically, please instead create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

{{% /alert %}}

To make changes to topics (such as creating new ones or modifying the description of existing topics), you will want to create a merge request via the [Topics](https://gitlab.com/gitlab-support-readiness/zendesk-copilot/topics) project repo.

After doing so, next steps will be:

1. [Requester actions](#requester-actions)
1. [Customer Support actions](#customer-support-actions)
1. [CSS actions](#css-actions)

### Requester actions

{{% alert title="Note" color="warning" %}}

Please do not enable "auto-merge" on the merge request. This can complicate the process.

{{% /alert %}}

Fill out the default merge request template. After doing so, wait for the CI/CD pipelines to complete.

These pipelines will do validity checking for your merge request. If there are any detected problems, a comment will be added to the merge request detailing what needs to be fixed. After pushing new commits to fix the issues, the CI/CD script will re-run (and update the comment accordingly).

Once the CI/CD has completed and confirmed there are no issues, review the approvers on the merge request to determine who can approve it from `Customer Support`. Assign to any of those listed for further assistance (it is often better to pick multiple persons).

From here, the request moved to [Customer Support actions](#customer-support-actions).

### Customer Support actions

{{% alert title="Note" color="warning" %}}

Please do not enable "auto-merge" on the merge request. This can complicate the process.

{{% /alert %}}

The Customer Support person will review the merge request, checking for anything they do not agree with. If any issues are found, please create a comment on the merge request with your findings (ensuring you ping the requester).

If there are no issues, approve the merge request. After doing so, review the approvers on the merge request to determine who can approve it from `Customer Support systems`. Assign to any of those listed for further assistance (it is often better to pick multiple persons).

From here, the request moved to [CSS actions](#css-actions).

### CSS actions

The CSS person will review the merge request, checking for anything they do not agree with. If any issues are found, please create a comment on the merge request with your findings (ensuring you ping the requester).

If there are no issues, you need to generate a work item to ensure the changes are implemented properly. To do this, open a chat with GitLab Duo, select the agent `Zendesk Copilot - Topic changes`, and run it (the exact messaging you send matter little here). The agent will review the MR and generate a work item to ensure the changes are properly deployed.

You will then work the work item issue to completion. See [Working topic change issues](#working-topic-change-issues) for more information.

Once the issue is worked to completion, you will approve and merge the merge request.

## Working topic change issues

When a work item is created, all of the CSS team should be assigned. If you are working the item, unassign the others (leaving only yourself).

After doing so, you need to implement the changes into the sandbox instances.

After implementing them in the sandbox instances, you should perform tests to ensure the changes are working properly. If you need assistance in doing so, consider reaching out to the requester of the merge request (that created the work item) to help get details of a solid subject/description to use for test tickets.

Once you have confirmed the changes are working properly, you will then implement the changes into the production instance.

After doing so, close out the issue and navigate back to the merge request (to approve and merge it).

### Managing categories and subcategories

These can only be created when creating/modifying a topic. There is not currently a direct way to create/modify a category or subcategory.

If you need to change the name of a category/subcategory, please note this means you need to create the new ones via topic management, and then move all existing topics using the old category/subcategory to the new one.

### Creating a topic

To create a topic:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `AI > Intelligent triage > Topics`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/ai/intelligent-triage/intent)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/ai/intelligent-triage/intent)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/ai/intelligent-triage/intent)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/ai/intelligent-triage/intent)
1. Enter the needed details:
   - Name: The name will appear in Agent Workspace.
   - Description: Details to help classify tickets accurately
   - Category: The category for the topic
     - If you need to create a new category or subcategory, it will be done here.
1. Click `Create custom topic` at the bottom-right of the page

### Modifying a topic

To modify a topic:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `AI > Inteliigent triage > Topics`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/ai/intelligent-triage/intent)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/ai/intelligent-triage/intent)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/ai/intelligent-triage/intent)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/ai/intelligent-triage/intent)
1. Locate the topic in question
1. Click the three vertical dots to the right side of the topic you located
1. Click `Edit topic`
1. Make the needed changes
1. Click `Save changes` at the bottom-right of the page

### Deactivating a topic

To deactivate a topic:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `AI > Inteliigent triage > Topics`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/ai/intelligent-triage/intent)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/ai/intelligent-triage/intent)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/ai/intelligent-triage/intent)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/ai/intelligent-triage/intent)
1. Locate the topic in question
1. Click the three vertical dots to the right side of the topic you located
1. Click `Deactivate`
1. Click `Deactivate topic` to confirm the deactivation in the pop-up modal.

## Common issues and troubleshooting

This is a living section that will have items added to it as needed.
