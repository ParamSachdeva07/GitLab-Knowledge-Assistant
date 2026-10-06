---
title: 'Mid-ticket feedback'
description: 'Documentation on Zendesk mid-ticket feedback'
---

This guide covers mid-ticket feedback at GitLab, including customer submission and processing workflows.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
- Form repos:
  - [Zendesk Global](https://gitlab.com/gitlab-com/support/customer-feedback)
    - **NOTE**: Not managed by Customer Support Systems
  - [Zendesk US Government](https://gitlab.com/gitlab-support-readiness/forms/us-government-customer-feedback-form)
- Processor repos:
  - [Zendesk Global](https://gitlab.com/gitlab-support-readiness/zendesk-global/customer-feedback-processor)
  - [Zendesk US Government](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/customer-feedback-processor)
- Feedback project: [Customer Feedback](https://gitlab.com/gitlab-com/support/feedback)

{{% /alert %}}

## Understanding mid-ticket feedback

### What is mid-ticket feedback

Mid-ticket feedback is a system of forms and processors that takes feedback from customers (intended to come after ticket creation but before the [CES survey](/handbook/eta/css/zendesk/satisfaction/#ces-surveys)).

### Components of mid-ticket feedback

#### Form

This is the actual survey form used by customers. The exact link used depends on the Zendesk instance the customer is utilizing:

- [Zendesk Global](https://gitlab-com.gitlab.io/support/customer-feedback/)
- [Zendesk US Government](https://support.gitlab.io/us-federal-customer-feedback/)

Submissions from the form are sent to Workato.

#### Processor

This is what receives the responses from the form and processes them.

### How mid-ticket feedback works

Once a customer submits the feedback form, the submission is sent to Workato. This is then used to trigger a CI/CD pipeline in the processor project for the corresponding Zendesk instance. This CI/CD pipeline then runs the `bin/process` script, which does the following:

- Checks if a ticket URL was provided
  - If one was not, it exits with a 0 status code
- Checks if the feedback type provided is valid
  - If one was not, it exits with a 0 status code
- Checks if the ticket is closed
  - If it is, it exits with a 0 status code
- Adds an internal comment to the ticket (including adding a feedback tag)
- Creates an issue in the [Customer Feedback project](https://gitlab.com/gitlab-com/support/feedback)
- Posts to Slack
  - If for Zendesk US Government, all feedback submissions are posted to Slack
  - If for Zendesk Global, only feedback submissions requesting manager contact are posted to Slack

## Requesting changes as a non-admin

To make changes to the Zendesk Global mid-ticket feedback form, you will want to speak with the Customer Support team for their workflows.

For anything else, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Administrator tasks

{{% alert title="Note" color="primary" %}}

- This action requires `Developer` level access to the projects.

{{% /alert %}}

### Modifying the form

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- This only applies for Zendesk US Government, as Zendesk Global is managed by the Customer Support team.

{{% /alert %}}

To modify the mid-ticket feedback form, you will need to create a MR in the project repo. The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR. Being this is an `Ad-hoc` deployment type, the changes will be live immediately.

### Modifying the processor

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

To modify the mid-ticket feedback processor, you will need to create a MR in the project repo. The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR. Being this is an `Ad-hoc` deployment type, the changes will be live immediately.

## Common issues and troubleshooting

This is a living section that will have items added to it as needed.
