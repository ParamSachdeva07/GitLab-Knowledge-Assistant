---
title: 'Organization deletion'
description: 'Documentation on organization deletion'
---

This page documents how organization deletion occurs within Zendesk.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
- Projects:
  - [Zendesk Global](https://gitlab.com/gitlab-support-readiness/zendesk-global/organizations/deletion)
  - [Zendesk US Government](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/organizations/deletion)

{{% /alert %}}

## Criteria for standard deletion

As per our [Data Retention policy](https://about.gitlab.com/privacy/#data-retention) and in accordance with various governing laws/regulations, we delete an organization 3 years after their last valid (paid, non-trial) subscription has expired. So if an organization’s last valid subscription expired 2021-12-18, then the date it would be eligible for deletion would be 2024-12-18.

## How it works

Every Saturday at 0045 (UTC for Global, Pacific for US Government), all organizations that have been indicated they need deletion reviewed (by the [Zendesk-Salesforce sync](/handbook/eta/css/zendesk-salesforce-sync/)) are analyzed by the `bin/delete` script. This does the following:

- Fetches a list of organizations to review using the Zendesk search `type:organization mark_for_deletion:true ignore_deletion:false`
- Loops over each organization found, doing the following:
  - Adds the organization to a deletion array if it meets one of the following crtieria:
    - The organization has no tickets
    - The organization has tickets but all are in a closed status
  - Adds the organization to an ignore array if they have tickets in a non-closed status
- Batch deletes all organizations in the deletion array (in batches of 100, as per API limits)
- Batch updates all organizations in the ignore array (in batches of 100, as per API limits) to indicate they have an exception

## Exceptions review

Once a month, The Customer Support Systems team reviews any organizations that are exempt from deletion (via a search `ignore_deletion:true`). If the organization in question should be deleted, they will uncheck the box that granted the exception (ensuring its deletion on the next run). If it should still be exempt, it is left as is.

## Common issues and troubleshooting

This is a living section that will have items added to it as needed.
