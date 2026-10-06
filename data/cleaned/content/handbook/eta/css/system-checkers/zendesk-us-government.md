---
title: 'Zendesk US Government'
description: 'Documentation on the Zendesk US Government system checker'
---

<sup>Introduced via [gitlab-com/support/support-ops/support-ops-project#1890](https://gitlab.com/gitlab-com/support/support-ops/support-ops-project/-/issues/1890)</sup>

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
- Project repo: [gitlab-support-readiness/system-checkers/zendesk-us-government](https://gitlab.com/gitlab-support-readiness/system-checkers/zendesk-us-government)

{{% /alert %}}

## Understanding the Zendesk US Government system checker

### What is the Zendesk US Government system checker

The Zendesk US Government system checker is a setup using scheduled pipelines to check the status of Zendesk US Government. It posts to the [#feed_status-zendesk-usgov Slack channel](https://gitlab.enterprise.slack.com/archives/C08PBULKRUH).

### How does it work

At the top of every hour UTC (`0 * * * *`), a scheduled pipeline causes the `bin/run` script to execute. This does the following:

- Gathers the current Zendesk status information from the following API endpoints:
  - [List Active Incidents](https://developer.zendesk.com/api-reference/status_api/status_api/#list-active-incidents)
  - [List Maintenance Incidents](https://developer.zendesk.com/api-reference/status_api/status_api/#list-maintenance-incidents)
- Compares the current Zendesk status information for incidents to that of the stored information from `data/incidents.yaml` file
  - If the Zendesk status information for an incident is not within the stored information (and it is not already resolved), the information is stored as a new incident
  - If the Zendesk status information for an incident is within the stored information (but there are differences between the two), the information is stored as an updated incident
    - If the update is it being resolved, the item will later be deleted from the `data/incidents.yaml` file
- Compares the current Zendesk status information for maintenances to that of the stored information from `data/maintenances.yaml` file
  - If the Zendesk status information for a maintenance is not within the stored information (and it is not already completed), the information is stored as a new maintenance
  - If the Zendesk status information for a maintenance is within the stored information (but there are differences between the two), the information is stored as an updated maintenance
    - If the update is it being resolved, the item will later be deleted from the `data/maintenances.yaml` file
- Creates a new commit to the project updating the `data/incidents.yaml` and `data/maintenances.yaml` files (if there are any new or updated items)
- Makes posts to the [#feed_status-zendesk-usgov Slack channel](https://gitlab.enterprise.slack.com/archives/C08PBULKRUH) detailing any new or updated items

## Changing the Zendesk US Government system checker

{{% alert title="Note" color="primary" %}}

- This requires at least `Developer` access to the project.
- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

To make changes to the Zendesk US Government system checker, you will need to create a MR in the project repo. The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR (which will have them applied on the next triggered run).

## Common issues and troubleshooting

This is a living section that will have items added to it as needed.
