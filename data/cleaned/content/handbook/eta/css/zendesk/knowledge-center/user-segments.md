---
title: 'User segments'
description: 'Documentation on Zendesk user segments'
---

This guide covers how to create, edit, and manage Zendesk help center user segments at GitLab. Administrators should review the [Administrator tasks](#administrator-tasks) section.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Standard`
- Sync repos
  - [Zendesk Global](https://gitlab.com/gitlab-support-readiness/zendesk-global/help-center-user-segments)
  - [Zendesk US Government](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/help-center-user-segments)
- `CustSuppOps Zendesk Test Suite Generator` enabled

{{% /alert %}}

Note: This is closely tied to [Management permissions groups](/handbook/eta/css/zendesk/knowledge-center/management-permissions-groups)

## Understanding user segments

### What are user segments

As per [Zendesk](https://support.zendesk.com/hc/en-us/articles/4408831908634-Managing-user-segments):

> A user segment is a collection of end users and/or agents, defined by a specific set of attributes, used to determine access to help center content.

Essentially, the use cases of user segments are:

- Restricting article visibility to specific teams
- Controlling who can edit/publish articles (via management permissions)
- Creating team-specific content sections

**Note**: You can belong to multiple user segments.

### How we manage user segments

While Zendesk offers a full way to manage user segments via the UI, we turn to a more version controlled methodology. This allows for a set review process, the ability to perform rollbacks as needed, etc.

That being the case, we utilize sync repos.

## Creating a user segment as a non-admin

For the creation of a user segment, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Editing a user segment as a non-admin

For the modification of a user segment, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Deleting a user segment as a non-admin

For the deletion of a user segment, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Current user segments

### Zendesk Global

| User segment | Tag filters | Organization filters | Group filters | Individual users | System built-in |
|--------------|-------------|----------------------|---------------|------------------|:---------------:|
| Signed-in users | N/A | N/A | N/A | N/A | Y |
| Agents and admins | N/A | N/A | N/A | N/A | Y |
| Support Editors | `article_editor` | None | Support AMER<br>Support APAC<br>Support EMEA | None | N |
| Support Publishers | `article_publisher` | None | Support AMER<br>Support APAC<br>Support EMEA | None | N |

### Zendesk US Government

| User segment | Tag filters | Organization filters | Group filters | Individual users | System built-in |
|--------------|-------------|----------------------|---------------|------------------|:---------------:|
| Signed-in users | N/A | N/A | N/A | N/A | Y |
| Agents and admins | N/A | N/A | N/A | N/A | Y |
| Support Editors | `article_editor` | None | None | None | N |
| Support Publishers | `article_publisher` | None | None | None | N |

## Administrator tasks

{{% alert title="Note" color="primary" %}}

- All sections in this section require `Administrator` level access to Zendesk.

{{% /alert %}}

### Viewing user segments

To see the current user segments in Zendesk:

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

### Creating a user segment

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

For the creation of a user segment, you will need to create a MR in the sync repo. The exact changes being made will depend on the request itself.

**Note**: It will be very rare to use the attributes `added_user_ids`, `or_tags`, and `organization_ids`, so it is likely you will use the value of `[]` for them when you create a user segment.

A starting template you can use would be:

```yaml
---
name: 'Your user segment name here'
previous_name: 'Your user segment name here'
added_user_ids: # Individual user emails to include
- user_email@example.com
- user_email@example.com
group_ids: # Zendesk group names to include
- Group Name 1
- Group Name 2
or_tags: # Tags where ANY match includes the user (OR logic)
- tag_for_filter_1
- tag_for_filter_2
organization_ids:  # Organization Salesforce IDs to include
- salesforce_id_value_1
- salesforce_id_value_2
tags: # Tags where ALL must match (AND logic)
- tag_for_filter_1
- tag_for_filter_2
user_type: 'staff' # All custom user segments should use 'staff'
```

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

### Editing a user segment

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- This can dramatically impact other teams' abilities to manage articles. Exercise caution when proceeding.

{{% /alert %}}

To edit a user segment, you will need to create a MR in the sync repo. The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

#### Changing the name of a user segment

If you need to change the title of a user segment, copy the current value into the `previous_name` attribute and then change the `name` attribute. This allows the sync to still locate the user segment in question to update.

### Deleting a user segment

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- This can dramatically impact other teams' abilities to manage articles. Exercise caution when proceeding.

{{% /alert %}}

As the sync repos do not perform deletions, you will have to do 2 actions to delete a group.

First, you must delete the corresponding file from the sync repo. After a peer reviews and approves your MR, you can merge the MR.

After that is done, you then must delete it from Zendesk itself.

To delete a user segment from Zendesk:

1. Navigate to the [User segments page](#viewing-user-segments)
1. Click the three vertical dots to the right of the name of the user segment you wish to delete
1. Click `Delete`
1. Click `Delete` to confirm the changes

### Performing an exception deployment

To perform an exception deployment for user segments, navigate to the user segments sync project in question, go to the scheduled pipelines page, and click the play button for the sync item. This will trigger a sync job for the user segments.

## Common issues and troubleshooting

### Not seeing user segment changes after a merge

As user segments follow the `Standard` deployment type, they would only be deployed during a normal deployment cycle (or when an exception deployment has been done)

### User not matching expected segment

This would normally indicate you do not meet the criteria defined in the user segment in question. Please speak with the Customer Support Systems team for assistance in this matter.
