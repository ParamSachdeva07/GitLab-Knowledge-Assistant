---
title: 'Procedures'
description: 'Documentation on Zendesk Copilot procedures'
---

This guide covers how to create, edit, and manage Zendesk Copilot proceudres at GitLab.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
- Project repo: [Procedures](https://gitlab.com/gitlab-support-readiness/zendesk-copilot/procedures)
- `CustSuppOps Zendesk Test Suite Generator` disabled

{{% /alert %}}

## Understanding procedures

As per [Zendesk](https://support.zendesk.com/hc/en-us/articles/7924047699738-Creating-procedures-for-auto-assist):

> Procedures are the sets of written steps that auto assist should follow when making suggestions. You can think of defining procedures as similar to explaining to a new agent how a specific problem should be solved within your company.

### How we manage procedures

We currently manage all procedures within Zendesk itself. To ensure we enable non-administrator collaboration and have version control, the source of all procedures (and their descriptions) is managed via the [Procedures](https://gitlab.com/gitlab-support-readiness/zendesk-copilot/procedures) project repo.

## Requesting procedure changes

To make changes to procedures (such as creating new ones or modifying existing ones), you will want to create a merge request via the [Procedures](https://gitlab.com/gitlab-support-readiness/zendesk-copilot/procedures) project repo.

After doing so, next steps will be:

1. [Requester actions](#requester-actions)
1. [CSS actions](#css-actions)

### Requester actions

{{% alert title="Note" color="warning" %}}

Please do not enable "auto-merge" on the merge request. This can complicate the process.

{{% /alert %}}

Fill out the default merge request template. After doing so, wait for the CI/CD pipelines to complete.

These pipelines will do validity checking for your merge request. If there are any detected problems, a comment will be added to the merge request detailing what needs to be fixed. After pushing new commits to fix the issues, the CI/CD script will re-run (and update the comment accordingly).

Once the CI/CD has completed and confirmed there are no issues, review the approvers on the merge request to determine who can approve it from `Customer Support Systems`. Assign to any of those listed for further assistance (it is often better to pick multiple persons).

From here, the request moved to [CSS actions](#css-actions).

### CSS actions

The CSS person will review the merge request, checking for anything they do not agree with. If any issues are found, please create a comment on the merge request with your findings (ensuring you ping the requester).

If there are no issues, you need to generate a work item to ensure the changes are implemented properly. To do this, open a chat with GitLab Duo, select the agent `Zendesk Copilot - Procedure changes`, and run it (the exact messaging you send matter little here). The agent will review the MR and generate a work item to ensure the changes are properly deployed.

You will then work the work item issue to completion. See [Working procedure change issues](#working-procedure-change-issues) for more information.

Once the issue is worked to completion, you will approve and merge the merge request.

## Working procedure change issues

When a work item is created, all of the CSS team should be assigned. If you are working the item, unassign the others (leaving only yourself).

After doing so, you need to implement the changes into the sandbox instances.

After implementing them in the sandbox instances, you should perform tests to ensure the changes are working properly. If you need assistance in doing so, consider reaching out to the requester of the merge request (that created the work item) to help get details of a solid subject/description to use for test tickets.

Once you have confirmed the changes are working properly, you will then implement the changes into the production instance.

After doing so, close out the issue and navigate back to the merge request (to approve and merge it).

### Creating a procedure

To create a procedure:

1. Navigate to the knowledge admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/knowledge/home/)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/knowledge/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/knowledge/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/knowledge/home)
1. Go to `Content > Customert objects > Procedures`
   - [Zendesk Global](https://gitlab.zendesk.com/knowledge/procedures)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/knowledge/procedures)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/knowledge/procedures)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/knowledge/procedures)
1. Click the `Create procedure` at the top-right of the page
1. Enter the needed details
1. Click `Save draft` at the bottom-right of the page

### Modifying a procedure

To modify a topic:

1. Navigate to the knowledge admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/knowledge/home/)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/knowledge/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/knowledge/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/knowledge/home)
1. Go to `Content > Customert objects > Procedures`
   - [Zendesk Global](https://gitlab.zendesk.com/knowledge/procedures)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/knowledge/procedures)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/knowledge/procedures)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/knowledge/procedures)
1. Locate the procedure in question and click its name
1. Make the needed changes
1. Click `Save draft` at the bottom-right of the page

### Publishing a procedure

1. Navigate to the knowledge admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/knowledge/home/)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/knowledge/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/knowledge/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/knowledge/home)
1. Go to `Content > Customert objects > Procedures`
   - [Zendesk Global](https://gitlab.zendesk.com/knowledge/procedures)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/knowledge/procedures)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/knowledge/procedures)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/knowledge/procedures)
1. Locate the procedure in question
1. Click the three vertical dots to the right side of the procedure you located
1. Click `Publish` in the drop-down menu
1. Click `Publish` on the pop-up modal

### Unpublishing a procedure

1. Navigate to the knowledge admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/knowledge/home/)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/knowledge/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/knowledge/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/knowledge/home)
1. Go to `Content > Customert objects > Procedures`
   - [Zendesk Global](https://gitlab.zendesk.com/knowledge/procedures)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/knowledge/procedures)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/knowledge/procedures)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/knowledge/procedures)
1. Locate the procedure in question
1. Click the three vertical dots to the right side of the procedure you located
1. Click `Unpublish` in the drop-down menu

### Deleting a procedure

To delete a topic:

1. Navigate to the knowledge admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/knowledge/home/)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/knowledge/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/knowledge/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/knowledge/home)
1. Go to `Content > Customert objects > Procedures`
   - [Zendesk Global](https://gitlab.zendesk.com/knowledge/procedures)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/knowledge/procedures)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/knowledge/procedures)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/knowledge/procedures)
1. Locate the procedure in question
1. Click the three vertical dots to the right side of the procedure you located
1. Click `Delete` in the drop-down menu
1. Click `Delete procedure` on the pop-up modal

## Common issues and troubleshooting

This is a living section that will have items added to it as needed.
