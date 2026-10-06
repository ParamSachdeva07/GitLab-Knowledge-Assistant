---
title: 'Groups'
description: 'Documentation on Zendesk group'
---

This guide covers how to create, edit, and manage Zendesk groups at GitLab. Administrators should review the [Administrator tasks](#administrator-tasks) section.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Standard`
- Sync repos
  - [Zendesk Global](https://gitlab.com/gitlab-support-readiness/zendesk-global/groups)
  - [Zendesk US Government](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/groups)
- `CustSuppOps Zendesk Test Suite Generator` enabled

{{% /alert %}}

## Understanding groups

### What are Zendesk groups

As per [Zendesk](https://support.zendesk.com/hc/en-us/articles/4408886146842-About-organizations-and-groups#topic_iny_3jg_sz):

> Groups collect team members together based on criteria those team members have in common. Groups can only contain team members; no end users can be included. All agents must be assigned to at least one group, but they can be members of more than one. Groups can be used to support organizations. You can designate one group as the default group for your account and you can also designate a default group for each team member. All new team members you create will be added to the default group.

### How we manage groups

While Zendesk offers a full way to manage groups via the UI, we turn to a more version controlled methodology. This allows for a set review process, the ability to perform rollbacks as needed, etc.

That being the case, we utilize sync repos.

### How we manage group membership

#### For the Support team

We manage the group membership for those within the Support team via the [Agent sync](/handbook/eta/css/zendesk/users/agents). As such, if you need to modify your group membership, please update your YAML file.

#### For everyone else

As these require the tech stack provisioner to manually perform the changes, please file an [Access Request issue](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new).

## Creating a group as a non-admin

For the creation of a group, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Editing a group as a non-admin

For the modification of a group, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Deactivating a group as a non-admin

To request the deactivation of a group, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Current groups

### Zendesk Global groups

- `Accounts Receivable`
- `ASEs`
- `Billing`
- `BPO`
- `General`
- `Support AMER`
- `Support APAC`
- `Support EMEA`
- `Support Focus: Authentication and Authorization`
- `Support Focus: CMOC`
- `Support Focus: L&R`
- `Support Focus: Secure`
- `Support Managers`
- `Support Ops`

### Zendesk US Government groups

- `General`
- `Security`
- `Support 1st Shift`
- `Support 2nd Shift`
- `Support 3rd Shift`
- `Support Managers`
- `Support Operations`
- `Support`

## Administrator tasks

{{% alert title="Note" color="primary" %}}

- All sections in this section require `Administrator` level access to Zendesk.

{{% /alert %}}

### Viewing groups

To view groups in Zendesk:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `People > Team > Groups`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/people/team/groups)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/people/team/groups)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/people/team/groups)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/people/team/groups)

You can click on the group's name if you need to see the membership of a group.

### Creating a group

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- Keep in mind you may need to edit the Agent sync as well

{{% /alert %}}

For the creation of a group, you will need to create a MR in the sync repo. The exact changes being made will depend on the request itself. A starting template you can use would be:

```yaml
---
name: 'Your group name here'
previous_name: 'Your group name here'
description: 'Your description here'
default: false # If the group is the default one for the account
deleted: false # Deleted groups get marked as such
is_public: true # If true, the group is public. If false, the group is private. You can't change a private group to a public group
```

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

### Editing a group

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- Keep in mind you may need to edit the Agent sync as well

{{% /alert %}}

To edit a group (i.e. its name or description), you will need to create a MR in the sync repo. The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

#### Changing the name of a group

If you need to change the title of a group, copy the current value into the `previous_name` attribute and then change the `name` attribute. This allows the sync to still locate the group in question to update.

### Deleting a group

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- Keep in mind you may need to edit the Agent sync as well

{{% /alert %}}

As the sync repos do not perform deletions, you will have to do 2 actions to delete a group.

First, you must delete the corresponding file from the sync repo. After a peer reviews and approves your MR, you can merge the MR.

After that is done, you then must delete it from Zendesk itself.

To delete a group from Zendesk:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `People > Team > Groups`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/people/team/groups)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/people/team/groups)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/people/team/groups)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/people/team/groups)
1. Click the name of the group you wish to remove the person from
1. Click the `Actions` button at the top of the page
1. Click the `Delete group`
1. Click the `Delete` to confirm the change

### Adding a non-support person to a group

To add someone who is not managed by the Agent sync to a group:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `People > Team > Groups`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/people/team/groups)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/people/team/groups)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/people/team/groups)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/people/team/groups)
1. Click the name of the group you wish to add the person to
1. Use the search on the far-right side to locate the person (searching by email address works best)
1. Click the `+` icon to the right of the person's information
1. Click the `Save` icon to the bottom-right of the page.

### Removing a non-support person from a group

To remove someone who is not managed by the Agent sync from a group:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `People > Team > Groups`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/people/team/groups)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/people/team/groups)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/people/team/groups)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/people/team/groups)
1. Click the name of the group you wish to remove the person from
1. Use the search under the `Group members` section to locate the person (searching by email address works best)
1. Click the trashcan icon to the right of the person's information
1. Click the `Save` icon to the bottom-right of the page.

### Performing an exception deployment

To perform an exception deployment for groups, navigate to the groups sync project in question, go to the scheduled pipelines page, and click the play button for the sync item. This will trigger a sync job for the groups.

## Common issues and troubleshooting

### Not seeing group changes after a merge

As groups follow the `Standard` deployment type, they would only be deployed during a normal deployment cycle (or when an exception deployment has been done)
