---
title: 'SKU mapping'
description: 'Documentation on Salesforce SKU mapping'
---

This guide covers how to create, edit, and manage SKU mappings at GitLab. Administrators should review the [Administrator tasks](#administrator-tasks) section.

## Understanding SKU mapping

### What is SKU mapping

SKU mapping is the process we use to map a `Product Rate Charge` from Salesforce to a support subscription tier (Ultimate, Premium, ASE, etc.) in Zendesk.

### Why is this needed

Because names can often change in the backend (of Salesforce) and are not always clear what _exactly_ they correspond to. Having a mapping for these allows for backend systems to translate a "name" to an actual subscription tier.

### Current SKU mapping

Due to the large number of them, we document the mapping via the [Product Rate Charge Name mapping google sheet](https://docs.google.com/spreadsheets/d/1bJEq_q3h2fM3E8xWxYoFgZLdryWi_Cn5WLtzGSjuUUI/edit?usp=sharing).

## Administrator tasks

{{% alert title="Danger" color="danger" %}}

- This directly impacts the calculated support entitlement of our customers in Zendesk. You can render a customer with no support entitlement unintentionally. Exercise extreme caution in making changes.

{{% /alert %}}
{{% alert title="Note" color="primary" %}}

- All sections in this section require `Developer` level access to the Zendesk-Salesforce sync [processor project](https://gitlab.com/gitlab-support-readiness/zd-sfdc-sync/processor).
- All sections in this section require `Editor` level access to the [Product Rate Charge Name mapping google sheet](https://docs.google.com/spreadsheets/d/1bJEq_q3h2fM3E8xWxYoFgZLdryWi_Cn5WLtzGSjuUUI/edit?usp=sharing).
- All tasks below should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}
{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
- Project repo: Zendesk-Salesforce sync [processor project](https://gitlab.com/gitlab-support-readiness/zd-sfdc-sync/processor)
- Google sheet: [Product Rate Charge Name mapping](https://docs.google.com/spreadsheets/d/1bJEq_q3h2fM3E8xWxYoFgZLdryWi_Cn5WLtzGSjuUUI/edit?usp=sharing)

{{% /alert %}}

### Adding a new SKU mapping

To add a new SKU mapping:

1. Add an entry to the [Product Rate Charge Name mapping google sheet](https://docs.google.com/spreadsheets/d/1bJEq_q3h2fM3E8xWxYoFgZLdryWi_Cn5WLtzGSjuUUI/edit?usp=sharing)
   1. Set the first column (`Product Rate Plan Charge Name`) to the `Rate Plan Charge Name` value in Salesforce (hyperlinked to the Salesforce URL of the item)
   1. Copy the previous row's second column (`Subscription Tier`) to your new row's second column
   1. Select the correct corresponding subscription tier in the drop-down for your new row's second column
   1. Copy the previous row's third column (`In ZD-SFDC sync?`) to your new row's third column
   1. Select `No` for your row's third column
   1. Set the issue URL you are working from as your row's fourth column (`Notes`)
1. Create a merge request to add the new mapping to the Zendesk-Salesforce sync [processor project](https://gitlab.com/gitlab-support-readiness/zd-sfdc-sync/processor)
   - For this merge request, you will be editing the `data/plans.yaml` file. You need to locate the subscription section it fits into and add a new array entry using the `Rate Plan Charge Name` value in Salesforce
1. Get a peer to review your merge request's changes
1. Merge your merge request
1. Finalize the row on the [Product Rate Charge Name mapping google sheet](https://docs.google.com/spreadsheets/d/1bJEq_q3h2fM3E8xWxYoFgZLdryWi_Cn5WLtzGSjuUUI/edit?usp=sharing)
   1. Set the value of the third column (`In ZD-SFDC sync?`) to `Yes`
   1. Delete the value in the fourth column (`Notes`)

### Editing a SKU mapping

{{% alert title="Note" color="primary" %}}

- It is often better to instead [add a new SKU mapping](#adding-a-new-sku-mapping) instead of editing an existing one. Consider adding a new SKU mapping instead of directly editing an existing one.

{{% /alert %}}

To edit a SKU mapping (i.e. change the Product Rate Charge Name used):

1. Create a merge request to edit the existing mapping to the Zendesk-Salesforce sync [processor project](https://gitlab.com/gitlab-support-readiness/zd-sfdc-sync/processor)
   - For this merge request, you will be editing the `data/plans.yaml` file. You need to locate the existing SKU by its original name and change it to the new `Rate Plan Charge Name` value in Salesforce
1. Get a peer to review your merge request's changes
1. Merge your merge request
1. Edit the entry on the [Product Rate Charge Name mapping google sheet](https://docs.google.com/spreadsheets/d/1bJEq_q3h2fM3E8xWxYoFgZLdryWi_Cn5WLtzGSjuUUI/edit?usp=sharing)
   - Change the value of the first column (`Product Rate Plan Charge Name`) to the `Rate Plan Charge Name` value in Salesforce (hyperlinked to the Salesforce URL of the item)

### Removing a SKU mapping

To remove a SKU mapping:

1. Create a merge request to edit the existing mapping to the Zendesk-Salesforce sync [processor project](https://gitlab.com/gitlab-support-readiness/zd-sfdc-sync/processor)
   - For this merge request, you will be editing the `data/plans.yaml` file. You need to locate the existing SKU by its original name and delete its entry.
1. Get a peer to review your merge request's changes
1. Merge your merge request
1. Delete the entry on the [Product Rate Charge Name mapping google sheet](https://docs.google.com/spreadsheets/d/1bJEq_q3h2fM3E8xWxYoFgZLdryWi_Cn5WLtzGSjuUUI/edit?usp=sharing)
