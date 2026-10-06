---
title: 'Deletion schedules'
description: 'Documentation on Zendesk deletion schedules'
---

This guide covers how to create, edit, and manage Zendesk deletion schedules at GitLab. Administrators should review the [Administrator tasks](#administrator-tasks) section.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Standard`
- Sync repos
  - [Zendesk Global](https://gitlab.com/gitlab-support-readiness/zendesk-global/deletion-schedules)
  - [Zendesk US Government](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/deletion-schedules)

{{% /alert %}}
{{% alert title="Danger" color="danger" %}}

Critical Safety Information:

- Deletion schedules permanently remove data from Zendesk and cannot be undone
- Always test deletion schedules in sandbox environments before deploying to production
- Carefully verify all conditions to ensure you're only deleting intended data
- Consider backing up critical data before activating deletion schedules

{{% /alert %}}

## Understanding deletion schedules

### What are Zendesk deletion schedules?

As per [Zendesk](https://support.zendesk.com/hc/en-us/articles/8301879320474-Managing-deletion-schedules):

> Deletion schedules help you manage data retention by automatically removing data to comply with privacy laws. You can create schedules for end-user data, tickets, attachments, bot-only conversations, and custom object records. Activate, edit, clone, deactivate, or delete these schedules as needed to maintain control over your data storage and ensure compliance with data retention regulations.

### Deletion schedules use condition logic

Deletion schedules use condition logic:

- `all`: ALL of the conditions in the array must be true (AND logic)
- `any`: AT LEAST ONE condition in the array must be true (OR logic)
- You can use either only one set or both sets (but there must be at least one set used)

This condition logic dictates when a deletion schedule runs. When all conditions are met, the object in question will be deleted.

### How we manage deletion schedules

While Zendesk offers a full way to manage deletion schedules via the UI, we turn to a more version controlled methodology. This allows for a set review process, the ability to perform rollbacks as needed, etc.

That being the case, we utilize sync repos and managed content repos.

#### Human readable replacements

{{% alert title="Note" color="primary" %}}

- Only applies to `administrators` creating/editing deletion schedules via YAML files

{{% /alert %}}

Currently, the sync repo can perform replacements of various items from a human readable item to the "Zendesk" equivalent item. This includes:

| Human readable item | Zendesk field item | Condition location | Notes |
|---------------------|--------------------|--------------------|-------|
| `number interval` | `duration_since_created_at` | `value` | Replace `number` with the number and `interval` with the interval |
| `number interval` | `duration_since_last_update` | `value` | Replace `number` with the number and `interval` with the interval |

Valid intervals would include:

- `hour` or `hours`
- `day` or `days`
- `week` or `weeks`
- `month` or `months`
- `year` or `years`

As an example, if you wanted a deletion schedule run 90 days after the last update, you would do the following to use the replacement:

```yaml
- field: 'duration_since_last_update'
  operator: 'greater_than'
  value: '90 days'
```

As another, if you needed a condition to cause the deletion 1 year after the creation date, you would do the following to use the replacement:

```yaml
- field: 'duration_since_created_at'
  operator: 'greater_than'
  value: '1 year'
```

## Administrator tasks

{{% alert title="Note" color="primary" %}}

- All sections in this section require `Administrator` level access to Zendesk.

{{% /alert %}}

### Creating a deletion schedule

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

For the creation of a deletion schedule, you will need to create a MR in the sync repo. The exact changes being made will depend on the request itself. A starting template you can use would be:

```yaml
---
title: 'Your Title Here'
previous_title: 'Your Title Here'
description: ''
object: 'object type (see below)'
active: true
conditions:
  all:
  - field: 'the_condition_to_use'
    operator: 'the_operator_to_use'
    value: 'the_value_to_use'
  any:
  - field: 'the_condition_to_use'
    operator: 'the_operator_to_use'
    value: 'the_value_to_use'
```

Valid object types are:

| Object | What it means | Notes |
|--------|---------------|-------|
| `zen:ticket` | Tickets | |
| `zen:user` | Users | |
| `zen:attachment` | Attachments  | |
| `zen:bot_only_conversation` | Bot conversations | |
| `zen:custom_object:CUSTOM_OBJECT_KEY` | Custom objects | Replace `CUSTOM_OBJECT_KEY` with the custom object's `key` value |

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

### Editing a deletion schedule

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

To edit a deletion schedule, you will need to create a MR in the sync repo. The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

#### Changing the title of a deletion schedule

If you need to change the title of a deletion schedule, copy the current value into the `previous_title` attribute and then change the `title` attribute. This allows the sync to still locate the deletion schedule in question to update.

### Deactivating a deletion schedule

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

To deactivate a deletion schedule, you will need to create a MR in the sync repo. You will be moving the file to the `inactive` folder and changing the `active` attribute to `false`.

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

### Deleting a deletion schedule

{{% alert title="Warning" color="warning" %}}

- You can only delete a deletion schedule if it is deactivated.
- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

As the sync repos do not perform deletions, you will need to do this via Zendesk itself.

To delete a deletion schedule:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `Account > Security > Deletion schedules`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/account/security/deletion_schedules)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/account/security/deletion_schedules)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/account/security/deletion_schedules)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/account/security/deletion_schedules)
1. Locate the deletion schedule you wish to delete and click the three vertical dots by it (at the far right)
1. Click `Delete`
1. Click `Delete schedule` to submit the changes

### Performing an exception deployment

To perform an exception deployment for deletion schedules, navigate to the deletion schedules sync project in question, go to the scheduled pipelines page, and click the play button for the sync item. This will trigger a sync job for the deletion schedules.

## Common issues and troubleshooting

### Not seeing deletion schedule changes after a merge

As deletion schedules follow the `Standard` deployment type, they would only be deployed during a normal deployment cycle (or when an exception deployment has been done)
