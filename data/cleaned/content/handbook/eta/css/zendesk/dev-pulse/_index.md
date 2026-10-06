---
title: 'Dev Pulse'
description: 'Documentation on Dev Pulse'
---

<sup>Introduced via [support-ops-project#970](https://gitlab.com/gitlab-com/support/support-ops/support-ops-project/-/issues/970)</sup>

This guide covers Dev Pulse, a custom setup we have created for use in Zendesk. If you are an agent looking to use it, please see [How do I use Dev Pulse](#how-do-i-use-dev-pulse). Administrators should review the [Administrator tasks](#administrator-tasks) section.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
- Project repos:
  - [Zendesk Global](https://gitlab.com/gitlab-support-readiness/zendesk-global/dev-pulse)
  - [Zendesk US Government](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/dev-pulse)

{{% /alert %}}

## Understanding Dev Pulse

### What is Dev Pulse

Dev Pulse is the name for a set of scripts and Zendesk setups we utilize to actively monitor various types of issues and merge requests in relation to bug resolution, feature request resolution, and requests for help (or RFH for short).

Through all the components, Dev Pulse allows a Zendesk ticket to stay in the On-hold status while waiting on an issue or merge request to reach a specific state.

When the specific state is reached, the tickets within Zendesk using Dev Pulse are updated to indicate there has been a state change on the issue or merge request they were waiting on.

### What are the components of Dev Pulse

The components of Dev Pulse are:

- The Dev Pulse project
- Zendesk macros
  - 3 for Zendesk Global environments
  - 1 for Zendesk US Government environments
- 3 Zendesk views
- 1 ticket field
- 1 trigger
- 1 webhook

While not anything directly stemming from Dev Pulse, it does utilize [problem and incident tickets](https://support.zendesk.com/hc/en-us/articles/4408835103898-Working-with-problem-and-incident-tickets) as a whole. For bugs and feature requests, a “parent” problem ticket is created. Using this problem ticket, you can update all the attached incident tickets to do one bulk update and solve.

### How do I use Dev Pulse

To utilize Dev Pulse on a Zendesk ticket:

1. Fill out the `Waiting on issue or merge request` ticket field with the link to your issue, merge request, or epic
   - Do not include any anchor links or the like (just use the full item's web URL)
1. Run the macro appropriate for your situation
   - `Waiting on bug resolution` (Zendesk Global environments only)
     - For tickets waiting on a bug resolution
   - `Waiting on feature request resolution` (Zendesk Global environments only)
     - For tickets waiting on a feature
   - `Waiting on RFH`
     - For tickets waiting on a request for help (RFH) issue
1. Submit the ticket with all the changes you did plus what the macro did

### How does Dev Pulse work

On the project side, there are 3 components to Dev Pulse:

- [Analyzing a ticket](#analyzing-a-ticket)
- [Analyzing problem tickets](#analyzing-problem-tickets)
- [Analyzing RFH tickets](#analyzing-rfh-tickets)

#### Analyzing a ticket

This is triggered when an agent [uses Dev Pulse on a ticket](#how-do-i-use-dev-pulse). The actions they perform causes the Zendesk trigger to run, which in turns sends a payload to the project (via a Zendesk webhook).

The payload contains:

| Key | Value in Production | Value in Sandbox | What it does |
|-----|---------------------|------------------|--------------|
| `variables[SANDBOX]` | Not set in production | `true` | Tells the script if this is for a sandbox environment |
| `variables[TICKET_ID]` | `{{ticket.id}}` | `{{ticket.id}}` | Tells the script the ticket's ID |
| `variables[TASK]` | `Analyze Ticket` | `Analyze Ticket` | Tells the script which task to run |

This results in the project's `bin/analyze_ticket` script to run (via CI/CD).

This script then:

- Checks to determine if the ticket is in the `closed` status
  - If it is, it exits as there is nothing to be done
- Fetches a list of Zendesk views
- Fetches a list of Zendesk ticket fields
- Fetches a list of Zendesk ticket forms
- Fetches the Zendesk Customer Support Operations bot user
- Verifies the validity of the value in the ticket's `Waiting on issue or merge request` ticket field
  - Checks to confirm it is an issue, merge request, or epic
  - Checks if it exists on gitlab.com
  - Checks if the item is in an non-closed and non-merged state
- If the link is determined to be invalid:
  - The ticket is minimally updated to stop Dev Pulse running
  - An internal comment is added stating the provided link was invalid
- If the link is determined to be valid, it checks if this is concerning a waiting on a bug or feature via the tags
  - If not _or_ it is a Zendesk US Government environment, the script exits as no further action is needed
- If it is _and_ this is on a Zendesk Global environment, it checks for an existing problem ticket matching the ticket's `Waiting on issue or merge request` ticket field
- If one does not exist, one is created for it
- The ticket is linked to the problem ticket (either an existing one or the newly created one)

#### Analyzing problem tickets

{{% alert title="Note" color="primary" %}}

- This only occurs on Zendesk Global environments

{{% /alert %}}

This is triggered via GitLab [scheduled pipelines](https://docs.gitlab.com/ci/pipelines/schedules/) on the project. It runs every third Wednesday of the month at 1600 UTC.

This results in the project's `bin/analyze_problems` script to run (via CI/CD).

This script then:

- Fetches a list of Zendesk views
- Fetches a list of Zendesk ticket fields
- Fetches a list of Zendesk ticket forms
- Fetches a list of all problem tickets within the `Links to bugs and feature requests` Zendesk view
- Loops through all found problem tickets, doing the following:
  - Fetches a list of attached tickets
    - If it has no attached tickets, the problem ticket is closed out and the loop moves to the next iteration
  - Analyzes the GitLab item the problem ticket was created for (checking if it is in a closed or merged state)
    - If it is, it does the following actions:
      - Posts in the #support_leadership Slack channel to notify about the change
      - Updates all attached incident tickets by doing the following:
        - Sets the `Ticket Stage` ticket field to NRT
        - Sets the ticket's type to `Task`
        - Sets the ticket's status to Open
        - Makes an internal comment indicating the GitLab item being waited on has resolved

#### Analyzing RFH tickets

This is triggered via GitLab [scheduled pipelines](https://docs.gitlab.com/ci/pipelines/schedules/) on the project. It runs every hour at the 0 minute mark.

This results in the project's `bin/analyze_rfhs` script to run (via CI/CD).

This script then:

- Fetches a list of Zendesk views
- Fetches a list of Zendesk ticket fields
- Fetches a list of tickets within the `RFH tickets` Zendesk view
- Fetches team data information from the [Support Team project](https://gitlab.com/gitlab-support-readiness/support-team)
- Loops through all found tickets, doing the following:
  - Checks if someone other than issue's author replied AFTER the last ticket update
  - If the check passed, the ticket is updated in the following way:
    - The ticket's status is set to Open
    - The ticket's type is set to `Task`
    - The ticket's `Ticket Stage` ticket field to NRT
    - An internal comment is added indicating the RFH issue has been updated

## Administrator tasks

{{% alert title="Note" color="primary" %}}

- This action requires `Developer` level access to the Dev Pulse projects.

{{% /alert %}}

### Modifying the Dev Pulse project

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

To modify the Dev Pulse project, you will need to create a MR in the project repo. The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR. Being this is an `Ad-hoc` deployment type, the changes will be live immediately.

### Removing Dev Pulse from a ticket

{{% alert title="Warning" color="warning" %}}

- This should only be done when requested specifically from an agent.
- Be very careful and proceed only as detailed here. The changes done here, when not done all together, can result in tickets being removed from all views (i.e. being "lost to the void").

{{% /alert %}}

If you need to stop Dev Pulse from running on a ticket (i.e. "unDev Pulse a ticket"), do the following:

1. Remove the the following tags from the ticket (if present):
   - `waiting_on_bug`
   - `waiting_on_feature_request`
   - `waiting_on_rfh`
   - `process_waiting_on_issue_or_mr`
1. Change the ticket's type to `Task`
1. Change the `Ticket Stage` field to `NRT`
1. Submit your changes on the ticket (with all of the above changes done in one single update)

After doing so, check the `Links to bugs and feature requests` view in the Zendesk instance to locate the problem ticket (if one exists). It's subject will be the previously used value of the ticket's `Waiting on issue or merge request` field. If you see one **and** there are not other attached tickets, delete the problem ticket you located.

## Common issues and troubleshooting

This is a living section that will have items added to it as needed.

### How do I stop Dev Pulse from running on my ticket

As this can be a complex (and very specific) process, it is best to reach out to the Customer Support Systems team via Slack for assistance with this matter.
