---
title: 'Dynamic content'
description: 'Documentation on Zendesk dynamic content'
---

This guide covers how to create, edit, and manage Zendesk dynamic content at GitLab (only used on Zendesk Global). Administrators should review the [Administrator tasks](#administrator-tasks) section.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Standard`
- Sync repo: [Zendesk Global](https://gitlab.com/gitlab-support-readiness/zendesk-global/dynamic-content)

{{% /alert %}}

## Understanding dynamic content

### What is dynamic content?

As per [Zendesk](https://support.zendesk.com/hc/en-us/articles/4408882999066-Providing-multiple-language-support-with-dynamic-content):

> Dynamic content is a combination of a default version of the text (typically in the same language as your default language) and variants for every other language that you support.

### How we manage dynamic content

While Zendesk offers a full way to manage dynamic content via the UI, we turn to a more version controlled methodology. This allows for a set review process, the ability to perform rollbacks as needed, etc.

That being the case, we utilize sync repos and managed content repos.

### Using dynamic content in themes

To call on a dynamic content item in a theme, use the following helper:

```plaintext
{{dc 'item_to_call'}}
```

Replacing `item_to_call` with the `placeholder` attribute of the item (minus the curly brackets and `dc.` component).

### Using dynamic content in other areas

To call on a dynamic content item outside of a theme, use the `placeholder` attribute of the dynamic content item in the `raw` attribute.

The exact `raw` attribute to use varies from item to item, but the most common areas are:

- `raw_display_name` on ticket forms to show the form's name as the dynamic content item
- `raw_title_in_portal` for ticket fields to show the dynamic content item as the field's title
- `raw_description` for ticket fields to show the dynamic content item as the field's description
- `raw_name` on entries under the `custom_field_options` attribute of ticket fields to show the drop-down option as the dynamic content item

For insertion into text (such as comments or emails), simply insert the `placeholder` attribute of the dynamic content item in the text itself.

## Administrator tasks

{{% alert title="Note" color="primary" %}}

- All sections in this section require `Administrator` level access to Zendesk.

{{% /alert %}}

### Creating a dynamic content item

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

For the creation of a dynamic content item, you will need to create a MR in the sync repo. The exact changes being made will depend on the request itself. A starting template you can use would be:

```yaml
---
name: 'Name of item here'
placeholder: 'placeholder item (see below)'
default_locale_id: 1 # English
variants:
- content: 'content_to_use'
  locale_id: 1 # English
  active: true
  default: true
```

The `placeholder` attribute is formatted as follows:

1. Convert the name to lowercase
1. Replace spaces with underscores
1. Prefix with `dc.`
1. Wrap in double curly brackets: `{{dc.placeholder_name}}`

An example would be `Preferred Region for Support` becoming `{{dc.preferred_region_for_support}}`.

If you are unsure of what your placeholder would be, a neat trick is to go into the Zendesk instance’s Sandbox and create the dynamic content item in the admin panel, then look at what it generates (make sure if you do this to delete it afterwards).

If you need to know more about locales for the `default_locale_id` or `locale_id`, you can get a list of active locales using the [Zendesk API](https://developer.zendesk.com/api-reference/ticketing/account-configuration/locales/#list-locales).

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

### Editing a dynamic content item

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

To edit a dynamic content item, you will need to create a MR in the sync repo. The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

### Deleting a dynamic content item

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

As the sync repos do not perform deletions, you will need to do this via Zendesk itself.

To delete a dynamic content item:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
1. Go to `Workspaces > Agent tools > Dynamic content`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/workspaces/agent-workspace/dynamic_content)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/workspaces/agent-workspace/dynamic_content)
1. Locate the dynamic content item you wish to delete and click `delete` by it (at the far right)
1. Click `OK` to submit the changes

### Performing an exception deployment

To perform an exception deployment for dynamic content, navigate to the dynamic content sync project in question, go to the scheduled pipelines page, and click the play button for the sync item. This will trigger a sync job for the dynamic content.

## Common issues and troubleshooting

### Not seeing dynamic content changes after a merge

As dynamic content follows the `Standard` deployment type, they would only be deployed during a normal deployment cycle (or when an exception deployment has been done)
