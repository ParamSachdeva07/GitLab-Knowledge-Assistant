---
title: 'User fields'
description: 'Documentation on Zendesk user fields'
---

This guide covers how to create, edit, and manage Zendesk user fields at GitLab. Administrators should review the [Administrator tasks](#administrator-tasks) section.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Standard`
- Sync repos
  - [Zendesk Global](https://gitlab.com/gitlab-support-readiness/zendesk-global/users/fields)
  - [Zendesk US Government](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/users/fields)
- `CustSuppOps Zendesk Test Suite Generator` enabled

{{% /alert %}}

## Understanding user fields

### What are user fields

User fields are custom fields attached to user profiles in Zendesk. Unlike ticket fields (which appear on tickets), user fields store information about users themselves.

### How we manage user fields

While Zendesk offers a full way to manage user fields via the UI, we turn to a more version controlled methodology. This allows for a set review process, the ability to perform rollbacks as needed, etc.

That being the case, we utilize sync repos.

### Types of user fields

The most common types we use at GitLab are:

| Name | API type value | Purpose | Example use case |
|------|----------------|---------|------------------|
| Checkbox | `checkbox` | Single true/false option | "User on PTO" |
| Date | `date` | For date selection | "Expiration date" |
| Decimal | `decimal` | For numbers using decimals | "ARR associated" |
| Drop-down | `dropdown` | For drop-downs allowing one selection | "Highest plan level" |
| Multi-line | `textarea` | For free-style fields needing multiple lines | "Account manager notes" |
| Multi-select | `multiselect` | For drop-downs allowing multiple selections | "Subscription levels purchased" |
| Numeric | `integer` | For numbers not using decimals | "GitLab.com user ID" |
| Regex | `regexp` | For text style fields that need Regex validation | "Salesforce contact ID" |
| Text | `text` | For free-style fields | "Preferred nickname" |

For a full list, please see [Zendesk documentation](https://support.zendesk.com/hc/en-us/articles/4408838961562-About-custom-fields-and-custom-field-types)

## Administrator tasks

{{% alert title="Note" color="primary" %}}

- All sections in this section require `Administrator` level access to Zendesk.

{{% /alert %}}

### Viewing user fields

To view the user fields on Zendesk:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `People > Configuration > User fields`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/people/configuration/user_fields)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/people/configuration/user_fields)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/people/configuration/user_fields)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/people/configuration/user_fields)

Note: You might need to change the active filter by clicking the `Filter` button if wanting to view non-active user fields

### Creating a user field

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

For the creation of a user field, you will need to create a MR in the sync repo. The exact changes being made will depend on the request itself. The exact content can vary depending on the type of user field.

**Note:** Templates shown for common field types. For other types (date, decimal, textarea, multiselect, regexp), modify the `type` attribute accordingly and refer to [Zendesk field documentation](https://support.zendesk.com/hc/en-us/articles/4408838961562-About-custom-fields-and-custom-field-types) for type-specific requirements.

**Tip:** Click each field type below to see its template.

<details>
<summary>checkbox</summary>

```yaml
---
title: 'Your Title Here'
previous_title: 'Your Title Here'
description: 'Your description here'
type: 'checkbox'
active: true
position: 1 # Integer representing user field position, controls display order in user profile (lower numbers appear first)
tag: 'tag_to_add_when_checked' # Added onto the user when the checkbox is checked
regexp_for_validation: null # Always null unless "regexp"
custom_field_options: null # Always null unless "dropdown" or "multiselect"
```

</details>
<details>
<summary>text</summary>

```yaml
---
title: 'Your Title Here'
previous_title: 'Your Title Here'
description: 'Your description here'
type: 'text'
active: true
position: 1 # Integer representing user field position, controls display order in user profile (lower numbers appear first)
regexp_for_validation: null # Always null unless "regexp"
custom_field_options: null # Always null unless "dropdown" or "multiselect"
```

</details>
<details>
<summary>integer</summary>

```yaml
---
title: 'Your Title Here'
previous_title: 'Your Title Here'
description: 'Your description here'
type: 'integer'
active: true
position: 1 # Integer representing user field position, controls display order in user profile (lower numbers appear first)
regexp_for_validation: null # Always null unless "regexp"
custom_field_options: null # Always null unless "dropdown" or "multiselect"
```

</details>
<details>
<summary>dropdown</summary>

```yaml
---
title: 'Your Title Here'
previous_title: 'Your Title Here'
description: 'Your description here'
type: 'dropdown'
active: true
position: 1 # Integer representing user field position, controls display order in user profile (lower numbers appear first)
regexp_for_validation: null # Always null unless "regexp"
custom_field_options:
- name: 'Name of option'
  value: 'tag_option_uses'
- name: 'Name of option 2'
  value: 'tag_option_uses_2'
```

</details>

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

### Editing a user field

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

To edit a user field, you will need to create a MR in the sync repo. The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

#### Changing the title of a user field

If you need to change the title of a user field, copy the current value into the `previous_title` attribute and then change the `title` attribute. This allows the sync to still locate the user field in question to update.

### Deactivating a user field

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

To deactivate a user field, you will need to create a MR in the sync repo. In this MR, you should do the following to the corresponding actions:

1. Move the file from the `active` folder to the `inactive` folder
1. Change the value of the `active` attribute to `false`

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

### Deleting a user field

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

As the sync repos do not perform deletions, you will need to do this via Zendesk itself.

To delete a user field:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `People > Configuration > User fields`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/people/configuration/user_fields)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/people/configuration/user_fields)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/people/configuration/user_fields)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/people/configuration/user_fields)
1. Locate the user field you wish to delete and click on the name
   - You might need to change the active filter by clicking the `Filter` button
1. Click `Actions` at the top-right of the page
1. Click `Delete`
1. Click `Delete` on the pop-up to submit the changes

### Performing an exception deployment

To perform an exception deployment for user fields, navigate to the user fields sync project in question, go to the scheduled pipelines page, and click the play button for the sync item. This will trigger a sync job for the user fields.

## Common issues and troubleshooting

### Not seeing user field changes after a merge

As user fields follow the `Standard` deployment type, they would only be deployed during a normal deployment cycle (or when an exception deployment has been done)
