---
title: 'Management permission groups'
description: 'Documentation on Zendesk management permission groups'
---

This guide covers how to create, edit, and manage Zendesk help center management permission groups at GitLab. Administrators should review the [Administrator tasks](#administrator-tasks) section.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Standard`
- Sync repos
  - [Zendesk Global](https://gitlab.com/gitlab-support-readiness/zendesk-global/help-center-management-permissions-groups)
  - [Zendesk US Government](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/help-center-management-permissions-groups)
- `CustSuppOps Zendesk Test Suite Generator` enabled

{{% /alert %}}

Note: This is closely tied to [User segments](/handbook/eta/css/zendesk/knowledge-center/user-segments)

## Understanding management permission groups

### What are management permission groups

As per [Zendesk](https://support.zendesk.com/hc/en-us/articles/4408827952538-Creating-management-permissions-to-define-agent-editing-and-publishing-rights):

> Management permissions define editing and publishing permissions for agents. You apply management permissions to an article to determine agent editing and publishing access for that article.

### How we manage management permission groups

While Zendesk offers a full way to manage management permission groups via the UI, we turn to a more version controlled methodology. This allows for a set review process, the ability to perform rollbacks as needed, etc.

That being the case, we utilize sync repos.

### Permission types

- **Edit**: User segments that can create and edit article drafts
- **Publish**: User segments that can publish articles (make them live)

Typically, a broader group has edit access while a smaller group has publish access for quality control.

## Creating a management permission group as a non-admin

For the creation of a management permission group, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Editing a management permission group as a non-admin

For the modification of a management permission group, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Deleting a management permission group as a non-admin

To request the deactivation of a management permission group, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Current management permission groups

### Zendesk Global

| Permission group | Edit permissions | Publish permissions |
|------------------|------------------|---------------------|
| Administrators | Admins | Admins |
| Support Team | Admins, Support Editors | Admins, Support Publishers |

### Zendesk US Government

| Permission group | Edit permissions | Publish permissions |
|------------------|------------------|---------------------|
| Administrators | Admins | Admins |
| Support Team | Admins, Support Editors | Admins, Support Publishers |

## Administrator tasks

{{% alert title="Note" color="primary" %}}

- All sections in this section require `Administrator` level access to Zendesk.

{{% /alert %}}

### Viewing management permission groups

To see the current management permission groups in Zendesk:

1. [Access the knowledge center](../knowledge-center/#accessing-the-knowledge-center)
1. Click the `User permissions content` icon on the left side:
   - For the primary brand:
     - [Zendesk Global (production)](https://gitlab.zendesk.com/knowledge/user_segments/page/1?brand_id=3252896)
     - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/knowledge/user_segments/page/1?brand_id=12510498177436)
     - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/knowledge/user_segments/page/1?brand_id=360002482351)
     - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/knowledge/user_segments/page/1?brand_id=360003799392)
   - For the internal brand:
     - [Zendesk Global (production)](https://gitlab.zendesk.com/knowledge/user_segments/page/1?brand_id=22781249167132)
     - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/knowledge/user_segments/page/1?brand_id=22687153149724)
     - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/knowledge/user_segments/page/1?brand_id=41824350085780)
     - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/knowledge/user_segments/page/1?brand_id=41389709130900)
1. Click `Management permissions` on the left side:
   - For the primary brand:
     - [Zendesk Global (production)](https://gitlab.zendesk.com/knowledge/permissions/?brand_id=3252896)
     - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/knowledge/permissions/?brand_id=12510498177436)
     - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/knowledge/permissions/?brand_id=360002482351)
     - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/knowledge/permissions/?brand_id=360003799392)
   - For the internal brand:
     - [Zendesk Global (production)](https://gitlab.zendesk.com/knowledge/permissions/?brand_id=22781249167132)
     - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/knowledge/permissions/?brand_id=22687153149724)
     - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/knowledge/permissions/?brand_id=41824350085780)
     - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/knowledge/permissions/?brand_id=41389709130900)

### Creating a management permission group

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

For the creation of a management permission group, you will need to create a MR in the sync repo. The exact changes being made will depend on the request itself. A starting template you can use would be:

```yaml
---
name: 'Your name here'
previous_name: 'Your name here'
edit:
- User Segment Name 1
- User Segment Name 2
publish:
- User Segment Name 1
- User Segment Name 2
- User Segment Name 3
```

**Note:** The `edit` and `publish` attributes use user segment names. To find available user segments, see [User segments documentation](/handbook/eta/css/zendesk/knowledge-center/user-segments).

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

### Editing a management permission group

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

To edit a management permission group, you will need to create a MR in the sync repo. The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

#### Changing the name of a management permission group

If you need to change the title of a management permission group, copy the current value into the `previous_name` attribute and then change the `name` attribute. This allows the sync to still locate the management permission group in question to update.

### Deleting a management permission group

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- This can dramatically impact other teams' abilities to manage articles. Exercise caution when proceeding.

{{% /alert %}}

As the sync repos do not perform deletions, you will have to do 2 actions to delete a group.

First, you must delete the corresponding file from the sync repo. After a peer reviews and approves your MR, you can merge the MR.

After that is done, you then must delete it from Zendesk itself.

To delete a management permission group from Zendesk:

1. Navigate to the [Management permission groups page](#viewing-management-permission-groups)
1. Click the three vertical dots to the right of the name of the management permission group you wish to delete
1. Click `Delete`

**Note**: It does not ask for confirmation, so exercise caution.

### Performing an exception deployment

To perform an exception deployment for management permission groups, navigate to the management permission groups sync project in question, go to the scheduled pipelines page, and click the play button for the sync item. This will trigger a sync job for the management permission groups.

## Common issues and troubleshooting

### Not seeing management permission group changes after a merge

As management permission groups follow the `Standard` deployment type, they would only be deployed during a normal deployment cycle (or when an exception deployment has been done)
