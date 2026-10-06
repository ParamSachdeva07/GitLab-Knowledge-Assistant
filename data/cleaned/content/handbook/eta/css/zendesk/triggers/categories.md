---
title: 'Categories'
description: 'Documentation on Zendesk trigger categories'
---

This guide covers how to create, edit, and manage Zendesk trigger categories at GitLab. Administrators should review the [Administrator tasks](#administrator-tasks) section.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
  - **Note:** Trigger categories are currently managed manually in Zendesk (no sync repo yet)

{{% /alert %}}

## Understanding trigger categories

### What are trigger categories

Trigger categories are used to both group triggers and fine tune the run order (position) of triggers.

Common use cases for trigger categories include:

- Grouping by function
- Grouping by team
- Grouping by region
- Grouping by priority
- Further fine-tuning run-order (positioning)

When you assign a trigger to a category (via the `category_id` attribute in the trigger's YAML file), it appears under that category heading in the Zendesk triggers list, making it easier to navigate large numbers of triggers.

### Trigger categories impact run order

When triggers run, they run in "groups" based off the trigger categories. And in those groups, the position of the trigger category is taken into effect.

So in a setup of the following (shown in order of positions):

- Category 1
  - Trigger 1
  - Trigger 6
- Category 2
  - Trigger 2
  - Trigger 5
- Category 3
  - Trigger 3
  - Trigger 4

The run order would be:

1. Trigger 1
1. Trigger 6
1. Trigger 2
1. Trigger 5
1. Trigger 3
1. Trigger 4

### How we manage trigger categories

We currently manage all trigger categories within Zendesk itself.

## Creating trigger categories as a non-admin

For the creation of a trigger category, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Editing trigger categories as a non-admin

For the modification of a trigger category, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Deleting trigger categories as a non-admin

For the deletion of a trigger category, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Administrator tasks

{{% alert title="Note" color="primary" %}}

- All sections in this section require `Administrator` level access to Zendesk.

{{% /alert %}}

### Creating a trigger category

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

To create a trigger category in Zendesk:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `Objects and rules > Business rules > Triggers`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/objects-rules/rules/triggers)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/objects-rules/rules/triggers)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/objects-rules/rules/triggers)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/objects-rules/rules/triggers)
1. Click the down caret next to the `Create trigger` button
1. Click `Create category`
1. Enter the trigger category's name
1. Click the `Create` button

### Editing a trigger category

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- Exercise caution in doing this as it can have significant downstream impacts.

{{% /alert %}}

To edit a trigger category (i.e change its name) in Zendesk:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `Objects and rules > Business rules > Triggers`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/objects-rules/rules/triggers)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/objects-rules/rules/triggers)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/objects-rules/rules/triggers)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/objects-rules/rules/triggers)
1. Hover over the trigger category to edit and click the three vertical dots to the right of it
1. Click `Rename`
1. Enter the new trigger category name to use
1. Click the `Update` button

### Reordering trigger categories

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- Exercise caution in doing this as it can have significant downstream impacts.

{{% /alert %}}

To reorder the trigger categories (i.e. change their position) in Zendesk:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `Objects and rules > Business rules > Triggers`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/objects-rules/rules/triggers)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/objects-rules/rules/triggers)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/objects-rules/rules/triggers)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/objects-rules/rules/triggers)
1. Click the `Edit order` button (to the left of the `Create trigger` button)
1. Click the up and down arrows to the right of the trigger categories to change their order
1. Click the `Save` button at the bottom-right of the page

### Deleting a trigger category

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- This can only be done if no triggers exist in the category (active or inactive)

{{% /alert %}}

To delete a trigger category in Zendesk:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `Objects and rules > Business rules > Triggers`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/objects-rules/rules/triggers)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/objects-rules/rules/triggers)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/objects-rules/rules/triggers)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/objects-rules/rules/triggers)
1. Hover over the trigger category to edit and click the three vertical dots to the right of it
1. Click `Delete`

## Common issues and troubleshooting

This is a living section that will have items added to it as needed.
