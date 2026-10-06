---
title: 'Automations'
description: 'Documentation on Zendesk automations'
---

This guide covers how to create, edit, and manage Zendesk automations at GitLab. Administrators should review the [Administrator tasks](#administrator-tasks) section.

Unlike [macros](../macros/) which agents apply manually, or triggers which fire immediately on ticket events, automations run on a time-based schedule.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Standard`
- Sync repos
  - [Zendesk Global](https://gitlab.com/gitlab-support-readiness/zendesk-global/automations)
  - [Zendesk US Government](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/automations)
- Managed content repos
  - [Zendesk Global](https://gitlab.com/gitlab-com/support/zendesk-global/automations)
  - [Zendesk US Government](https://gitlab.com/gitlab-com/support/zendesk-us-government/automations)
- `CustSuppOps Zendesk Test Suite Generator` enabled

{{% /alert %}}

## Understanding Automations

### What are automations

As per [Zendesk](https://support.zendesk.com/hc/en-us/articles/4408832701850-About-automations-and-how-they-work):

> Automations are similar to triggers because both define conditions and actions that modify ticket properties and optionally send email notifications to customers and agents. Where they differ is that automations execute when a time event occurs after a ticket property was set or updated, rather than immediately after a ticket is created or updated.

The simpler way to think of it is automations are triggers that do not run instantly. They are time based rather than event based.

### When do automations run in Zendesk

Officially, automations in Zendesk run once per hour. While the exact timing is not set in stone, our use of Zendesk has shown this to occur at the beginning of each hour (within 5 or so minutes) in the instance's timezone.

### Automations use condition logic

Automations use condition logic:

- `all`: ALL of the conditions in the array must be true (AND logic)
- `any`: AT LEAST ONE condition in the array must be true (OR logic)
- You can use either only one set or both sets (but there must be at least one set used)

### How we manage automations

While Zendesk offers a full way to manage automations via the UI, we turn to a more version controlled methodology. This allows for a set review process, the ability to perform rollbacks as needed, etc.

That being the case, we utilize sync repos and managed content repos.

### How the sync repo works

The sync repo workflow follows this process:

```mermaid
graph TD;
  A-->C;
  B-->C;
  C-->D;
  A(Scheduled time for pipeline to run)
  B(Scheduled pipeline triggered manually)
  C(bin/sync runs)
  D(Changes synced to Zendesk)
```

#### Human readable replacements

{{% alert title="Note" color="primary" %}}

- Only applies to `administrators` creating/editing automations via YAML files

{{% /alert %}}

Currently, the sync repo can perform replacements of various items from a human readable item to the "Zendesk" equivalent item. This includes:

| Human readable item | Zendesk field item | Condition/Action location | Notes |
|---------------------|--------------------|-----------------|-------|
| `'Brand: XXX'` | `brand_id` | `value` | Replace `XXX` with the `name` of the brand |
| `'Field: XXX'` | `custom_fields_xxx` | `field` | Replace `XXX` with the `title` of the ticket field |
| `'Group: XXX'` | `group_id` | `value` | Replace `XXX` with the `name` of the group |
| `'XXX'` | `role` | `value` | Replace `XXX` with the `name` of the role type OR the email address of the requester |
| `'Form: XXX'` | `ticket_form_id` | `value` | Replace `XXX` with the `name` of the ticket form |
| `'Schedule: XXX'` | `set_schedule` | `value` | Replace `XXX` with the `name` of the schedule |
| `'Schedule: XXX'` | `schedule_id` | `value` | Replace `XXX` with the `name` of the schedule |
| `'XXX'` | `organization_id` | `value` | Replace `XXX` with the `salesforce_id` attribute of the organization |
| `'XXX'` | `assignee_id` | `value` | Replace `XXX` with the email address of the agent |
| `'XXX'` | `satisfaction_reason_code` | `value` | Replace `XXX` with the `name` of the satisfaction reason |
| `'XXX'` | `via_id` | `value` | Replace `XXX` with the `name` of the via type |
| `'XXX'` | `requester_role` | `value` | Replace `XXX` with the `name` of the requester role type |
| `'Target: XXX'` | `notification_target` | `value` | Replace `XXX` with the `name` of the target |
| `'Webhook: XXX'` | `notification_webhook` | `value` | Replace `XXX` with the `name` of the webhook |

As an example, if you wanted an automation to change the value of the field `Preferred Region for Support` to `AMER`, you would do the following to use the replacement:

```yaml
- field: 'Field: Preferred Region for Support'
  value: 'AMER'
```

As another, if you needed a condition to check if the form of a ticket is not the `SaaS` form, you would do:

```yaml
- field: 'ticket_form_id'
  operator: 'is_not'
  value: 'Form: SaaS'
```

#### When creating MRs in the sync repo

When a MR is created on the sync repo, it performs the compare actions (via the `bin/compare` script), which does the following:

1. Performs a clone of the managed content repo
1. Fetches all automations, brands, groups, satisfaction reasons, schedules, targets, ticket fields, ticket forms, and webhooks from the Zendesk instance
1. Reviews all YAML files within the sync repo to generate an automation object
   - It also checks to ensure none of the following problems exist in the sync repo files:
     - A title is missing
     - A file with the `active` attribute of `false` is not in the `active` folder
     - A file with the `active` attribute of `true` is not in the `inactive` folder
     - There is not a duplicate use of a `title` attribute
     - Any file with the `contains_managed_content` attribute of `true` has a matching managed content file
     - Any file with the `contains_managed_webhook` attribute of `true` has a matching managed content file
1. Compares all automation objects from the YAML files to a matching Zendesk item (determined by checking the value of the attributes `title` and `previous_title`)
   - If none exists, it will store a create object in a variable to be used later
   - If one exists but has different attribute values, it will store an update object in a variable to be used later
1. Output a comparison report

#### Syncing to Zendesk

The sync repo performs its sync task when the scheduled pipeline runs for the project (either via the correct timing or when performed manually).

When either action occurs, the sync performs the [compare actions](#when-creating-mrs-in-the-sync-repo) and then uses the objects generated to perform the needed creates and updates via a loop hitting the needed Zendesk endpoint:

- [Creates](https://developer.zendesk.com/api-reference/ticketing/business-rules/automations/#create-automation)
- [Updates](https://developer.zendesk.com/api-reference/ticketing/business-rules/automations/#update-automation)

#### Reporting orphaned managed content files

On the 1st of February, May, August, and November, a [scheduled pipeline](https://docs.gitlab.com/ci/pipelines/schedules/) will have the sync repo create an issue for the support leadership team to review all orphaned managed content files.

This is done via the `bin/find_orphaned_files` script in the sync repo, which does the following:

1. Performs a clone of the managed content repo
1. Reviews every file within the `active` and `inactive` folders of the managed content repo to determine the `state` (i.e. `active` or `inactive`, the `path`, and the `title`)
1. Reviews every file within the `active` and `inactive` folders of the sync repo itself to determine:
   - If the file is using a managed content file
   - If there is a managed content file
1. If it has located managed content files without a sync repo file, it then creates an issue reporting it to Customer Support leadership

## Creating an automation as a non-admin

For the creation of an automation, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Editing an automation as a non-admin

### Changing the comment wording used in an automation

To edit the comment wording in an automation, you will modify the corresponding file in the managed content repo. After it is merged to the `master` branch, it will be picked up at the next deployment cycle to deploy to Zendesk.

### Changing the payload used in an automation

To edit the payload in an automation (that is using a managed webhook), you will modify the corresponding file in the managed content repo. After it is merged to the `master` branch, it will be picked up at the next deployment cycle to deploy to Zendesk.

### Changing title, non-comment wording actions, and so on

To change anything else in an automation, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Deactivating an automation as a non-admin

To request the deactivation of an automation, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Administrator tasks

{{% alert title="Note" color="primary" %}}

- All sections in this section require `Administrator` level access to Zendesk.

{{% /alert %}}

### Seeing automation usage information

To see the usage information on automations:

1. Navigate to the admin panel for the Zendesk instance
1. Go to `Objects and rules > Business rules > Automations`
1. Click the icon to the left of the "Add automation" button (looks like a circle with AZ in it)
1. Click the usage columns you wish to see

### Creating an automation

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- If creating an automation that will use a managed content file, you must create said managed content file first.

{{% /alert %}}

For the creation of an automation, you will need to create a MR in the sync repo. The exact changes being made will depend on the request itself. A starting template you can use would be:

```yaml
---
title: 'Your::Title::Here'
previous_title: 'Your::Title::Here'
description: 'Your description here'
active: true
position: 1 # Integer representing automation position
actions:
- field: 'the_action_to_perform'
  value: 'the_value_to_use'
conditions:
  all:
  - field: 'the_action_to_perform'
    operator: 'the_operator_to_use'
    value: 'the_value_to_use'
  any:
  - field: 'the_action_to_perform'
    operator: 'the_operator_to_use'
    value: 'the_value_to_use'
contains_managed_content: false
contains_managed_email: false
contains_managed_webhook: false
```

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

### Editing an automation

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- If changing the automation's `contains_managed_content` or `contains_managed_webhook` attribute from `false` to `true`, you must create said managed content file first.
- If changing the automation's `contains_managed_content` or `contains_managed_webhook` attribute from `true` to `false`, you should create a follow-up MR to delete the corresponding managed content file.

{{% /alert %}}

To edit an automation, you will need to create a MR in the sync repo. The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

#### Changing the title of an automation

If you need to change the title of an automation, copy the current value into the `previous_title` attribute and then change the `title` attribute. This allows the sync to still locate the automation in question to update.

### Deactivating an automation

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- If the automation was using a managed content file (i.e. `contains_managed_content` or `contains_managed_webhook` attribute in the YAML file was previously set to `true`), you likely will need to also move the corresponding file from the `active` to the `inactive` location in the managed content repo.

{{% /alert %}}

To deactivate an automation, you will need to create a MR in the sync repo. In this MR, you should do the following to the corresponding automation's YAML file:

1. Move the file from the `active` to `inactive` path
1. Modify the value of the `active` attribute to `false`
1. Change the value of `actions` to the following:
   - For Zendesk Global:

     ```yaml
     - field: 'current_tags'
       value: 'missing_brand'
     ```

   - For Zendesk US Government:

     ```yaml
     - field: 'current_tags'
       value: 'missing_brand'
     ```

1. Change the value of `conditions` to the following:
   - For Zendesk Global:

     ```yaml
       all:
       - field: 'brand_id'
         operator: 'is_not'
         value: 'GitLab Support'
       - field: 'brand_id'
         operator: 'is_not'
         value: 'GitLab - Internal'
       - field: 'current_tags'
         operator: 'not_includes'
         value: 'missing_brand'
       - field: 'status'
         operator: 'is_not'
         value: 'closed'
       any: []
     ```

   - For Zendesk US Government:

     ```yaml
       all:
       - field: 'brand_id'
         operator: 'is_not'
         value: 'GitLab'
       - field: 'brand_id'
         operator: 'is_not'
         value: 'GitLab - Internal'
       - field: 'current_tags'
         operator: 'not_includes'
         value: 'missing_brand'
       - field: 'status'
         operator: 'is_not'
         value: 'closed'
       any: []
     ```

1. Change the value of the `contains_managed_content` attribute to `false`
1. Change the value of the `contains_managed_webhook` attribute to `false`

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

### Deleting an automation

{{% alert title="Warning" color="warning" %}}

- You can only delete an automation if it is deactivated.
- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- When deleting an automation, you likely will need to also remove the file from the sync and managed content repos.

{{% /alert %}}

As the sync repos do not perform deletions, you will need to do this via Zendesk itself.

To delete an automation:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `Objects and rules > Business rules > Automations`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/objects-rules/rules/automations)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/objects-rules/rules/automations)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/objects-rules/rules/automations)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/objects-rules/rules/automations)
1. Locate the automation you wish to delete and click on the name (in the `Inactive` tab)
1. Scroll to the bottom of the page
1. Click drop-down next to the `Submit` button
1. Click `Delete`
1. Click `Submit` to submit the changes

### Performing an exception deployment

To perform an exception deployment for automations, navigate to the automations sync project in question, go to the scheduled pipelines page, and click the play button for the sync item. This will trigger a sync job for the automations.

## Common issues and troubleshooting

### Not seeing automation changes after a merge

As automations follow the `Standard` deployment type, they would only be deployed during a normal deployment cycle (or when an exception deployment has been done)
