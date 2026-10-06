---
title: 'Organization fields'
description: 'Documentation on Zendesk organization fields'
---

This guide covers how to create, edit, and manage Zendesk organization fields at GitLab. Administrators should review the [Administrator tasks](#administrator-tasks) section.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Standard`
- Sync repos
  - [Zendesk Global](https://gitlab.com/gitlab-support-readiness/zendesk-global/organizations/fields)
  - [Zendesk US Government](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/organizations/fields)
- `CustSuppOps Zendesk Test Suite Generator` enabled

{{% /alert %}}

## Understanding organization fields

### What are organization fields

Organization fields are custom fields attached to organizations in Zendesk. Unlike ticket fields (which appear on tickets), organization fields store information about organizations themselves.

### How we manage organization fields

While Zendesk offers a full way to manage organization fields via the UI, we turn to a more version controlled methodology. This allows for a set review process, the ability to perform rollbacks as needed, etc.

That being the case, we utilize sync repos.

### Types of organization fields

The most common types we use at GitLab are:

| Name | API type value | Purpose | Example use case |
|------|----------------|---------|------------------|
| Checkbox | `checkbox` | Single true/false option | "Self-Managed - Ultimate entitlement" |
| Date | `date` | For date selection | "Expiration date" |
| Decimal | `decimal` | For numbers using decimals | "ARR associated" |
| Drop-down | `dropdown` | For drop-downs allowing one selection | "Highest plan level" |
| Multi-select | `multiselect` | For drop-downs allowing multiple selections | "Subscription levels purchased" |
| Numeric | `integer` | For numbers not using decimals | "Number of seats" |
| Regex | `regexp` | For text style fields that need Regex validation | "Salesforce contact ID" |
| Text | `text` | For free-style fields | "Account Manager" |

For a full list, please see [Zendesk documentation](https://support.zendesk.com/hc/en-us/articles/4408838961562-About-custom-fields-and-custom-field-types)

### Current organization fields

For current fields, the source of the data is one of three areas:

- Salesforce: meaning the data comes directly from Salesforce accounts
- Zendesk-Salesforce sync: meaning the data is determined via the [Zendesk-Salesforce sync](/handbook/eta/css/zendesk-salesforce-sync/)
- Agents: meaning it is requested by agents (normally via internal request forms)

<details>
<summary>For Zendesk Global</summary>

| API key value | Field name | Type | Purpose | Source of value |
|---------------|------------|------|---------|-----------------|
| `account_owner` | Account Owner | Text | Displaying the name of the Account Manager (AM) | Salesforce |
| `account_type` | Account Type | Drop-down | Displaying the type of account | Salesforce |
| `am_project_id` | AM Project ID | Text | The gitlab.com project ID for the collaboration project | Agents |
| `aar` | ARR | Decimal | The Annual Recurring Revenue (ARR) of the account | Salesforce |
| `assigned_se` | Assigned SE | Text | The Zendesk user ID of the Assigned Support Engineer (ASE) | Agents |
| `technical_account_manager` | Customer Success Manager | Text | The name of the Customer Success Manager (CSM) | Salesforce |
| `migration_date` | Date to Migrate | Date | The date an organization would migrate to a different instance | Zendesk-Salesforce sync |
| `org_in_escalated_state` | Escalated State | Checkbox | If the organization is in an escalated state | Salesforce |
| `expiration_date` | Expiration date | Text | The latest expiration date of the subscriptions | Salesforce |
| `support_level` | GitLab Plan | Drop-down | The highest level plan from the subscriptions | Salesforce |
| `ignore_deletion` | Ignore deletion | Checkbox | If the deletion process should skip this organization | Zendesk-Salesforce Sync |
| `mark_for_deletion` | Mark for deletion | Checkbox | If the deletion process should review this organization | Zendesk-Salesforce Sync |
| `migrating` | Migrating | Checkbox | If the organization is migration to a new instance | Zendesk-Salesforce Sync |
| `seats_decimal` | Number of Seats | Decimal | The highest number of seats in a subscription | Salesforce |
| `partner_customer` | Partner Customer | Checkbox | If the account is from an OEM partner | Zendesk-Salesforce sync |
| `org_region` | Region | Drop-down | The region the organization belongs to | Salesforce |
| `restricted_account` | Restricted Account | Checkbox | If the account has a legal restriction on it | Salesforce |
| `salesforce_id` | Salesforce ID | Text | The 18 character Salesforce account ID | Salesforce |
| `sales_segmentation` | Sales Segmentation | Text | The size of the account (based off employee size) | Salesforce |
| `sfdc_short_id` | SFDC Short ID | Text | The 15 character Salesforce account ID | Salesforce |
| `solutions_architect` | Solutions Architect | Text | Displaying the name of the Solutions Architect (SA) | Salesforce |
| `sub_edu` | Subscription: Community - EDU | Checkbox | Entitlement information | Salesforce |
| `sub_oss` | Subscription: Community - OSS | Checkbox | Entitlement information | Salesforce |
| `sub_community_other` | Subscription: Community - Other | Checkbox | Entitlement information | Salesforce |
| `sub_consumption_cicd_minutes` | Subscription: Consumption - CI_CD Minutes | Checkbox | Entitlement information | Salesforce |
| `sub_consumption_eap` | Subscription: Consumption - Enterprise Agile Planning | Checkbox | Entitlement information | Salesforce |
| `sub_consumption_duo_enterprise` | Subscription: Consumption - GitLab Duo Enterprise | Checkbox | Entitlement information | Salesforce |
| `sub_consumption_duo_amazon_q` | Subscription: Consumption - GitLab Duo powered by Amazon Q | Checkbox | Entitlement information | Salesforce |
| `sub_consumption_duo_premium` | Subscription: Consumption - GitLab Duo Premium | Checkbox | Entitlement information | Salesforce |
| `sub_consumption_storage` | Subscription: Consumption - Storage | Checkbox | Entitlement information | Salesforce |
| `sub_dotcom_premium` | Subscription: GitLab.com - Premium | Checkbox | Entitlement information | Salesforce |
| `sub_dotcom_ultimate` | Subscription: GitLab.com - Ultimate | Checkbox | Entitlement information | Salesforce |
| `sub_gitlab_dedicated` | Subscription: GitLab Dedicated | Checkbox | Entitlement information | Salesforce |
| `sub_sm_premium` | Subscription: Self-Managed - Premium | Checkbox | Entitlement information | Salesforce |
| `sub_sm_ultimate` | Subscription: Self-Managed - Ultimate | Checkbox | Entitlement information | Salesforce |
| `sub_ss_ase` | Subscription: Support Services - ASE | Checkbox | Entitlement information | Salesforce |
| `sub_ss_growth` | Subscription: Support Services - Success Advanced | Checkbox | Entitlement information | Salesforce |
| `sub_ss_enterprise` | Subscription: Support Services - Success Signature | Checkbox | Entitlement information | Salesforce |
| `support_hold` | Support Hold | Checkbox | If there is a hold on the account | Salesforce |

</details>
<details>
<summary>For Zendesk US Government</summary>

| API key value | Field name | Type | Purpose | Source of value |
|---------------|------------|------|---------|-----------------|
| `emergency_support_24x7` | 24x7 Emergency Support | Checkbox | If they have 24x7 entitlement | Zendesk-Salesforce sync |
| `account_owner` | Account Owner | Text | Displaying the name of the Account Manager (AM) | Salesforce |
| `account_type` | Account Type | Drop-down | Displaying the type of account | Salesforce |
| `am_project_id` | AM Project ID | Integer | The gitlab.com project ID for the collaboration project | Agents |
| `arr` | ARR | Decimal | The Annual Recurring Revenue (ARR) of the account | Salesforce |
| `assigned_se` | Assigned SE | Text | The Zendesk user ID of the Assigned Support Engineer (ASE) | Agents |
| `technical_account_manager` | Customer Success Manager | Text | The name of the Customer Success Manager (CSM) | Salesforce |
| `migration_date` | Date to Migrate | Date | The date an organization would migrate to a different instance | Zendesk-Salesforce sync |
| `org_in_escalated_state` | Escalated State | Checkbox | If the organization is in an escalated state | Salesforce |
| `expiration_date` | Expiration Date | Text | The latest expiration date of the subscriptions | Salesforce |
| `ignore_deletion` | Ignore deletion | Checkbox | If the deletion process should skip this organization | Zendesk-Salesforce Sync |
| `market_segment` | Market Segment | Text | The size of the account (based off employee size) | Salesforce |
| `mark_for_deletion` | Mark for deletion | Checkbox | If the deletion process should review this organization | Zendesk-Salesforce Sync |
| `migrating` | Migrating | Checkbox | If the organization is migration to a new instance | Zendesk-Salesforce Sync |
| `number_of_seats` | Number of Seats | Integer | The highest number of seats in a subscription | Salesforce |
| `restricted_account` | Restricted Account | Checkbox | If the account has a legal restriction on it | Salesforce |
| `salesforce_id` | Salesforce ID | Text | The 18 character Salesforce account ID | Salesforce |
| `sfdc_short_id` | SFDC Short ID | Text | The 15 character Salesforce account ID | Salesforce |
| `solutions_architect` | Solutions Architect | Text | Displaying the name of the Solutions Architect (SA) | Salesforce |
| `sub_consumption_duo_enterprise` | Subscription: Consumption - GitLab Duo Enterprise | Checkbox | Entitlement information | Salesforce |
| `sub_consumption_duo_amazon_q` | Subscription: Consumption - GitLab Duo powered by Amazon Q | Checkbox | Entitlement information | Salesforce |
| `sub_consumption_duo_premium` | Subscription: Consumption - GitLab Duo Premium | Checkbox | Entitlement information | Salesforce |
| `sub_gitlab_dedicated` | Subscription: GitLab Dedicated | Checkbox | Entitlement information | Salesforce |
| `sub_sm_premium` | Subscription: Self-Managed - Premium | Checkbox | Entitlement information | Salesforce |
| `sub_sm_ultimate` | Subscription: Self-Managed - Ultimate | Checkbox | Entitlement information | Salesforce |
| `sub_ss_ase` | Subscription: Support Services - ASE | Checkbox | Entitlement information | Salesforce |
| `sub_usgov_12x5` | Subscription: US Government - 12x5 | Checkbox | Entitlement information | Salesforce |
| `sub_usgov_24x7` | Subscription: US Government - 24x7 | Checkbox | Entitlement information | Salesforce |
| `support_hold` | Support Hold | Checkbox | If there is a hold on the account | Salesforce |
| `support_level` | Support Level | Drop-down | The highest level plan from the subscriptions | Salesforce |

## Administrator tasks

{{% alert title="Note" color="primary" %}}

- All sections in this section require `Administrator` level access to Zendesk.

{{% /alert %}}

### Viewing organization fields

To view the organization fields on Zendesk:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `People > Configuration > Organization fields`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/people/configuration/organization_fields)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/people/configuration/organization_fields)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/people/configuration/organization_fields)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/people/configuration/organization_fields)

Note: You might need to change the active filter by clicking the `Filter` button if wanting to view non-active organization fields

### Creating an organization field

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- **Note**: the `key` and `type` attribute cannot be changed once a field is created, so choose carefully

{{% /alert %}}

For the creation of an organization field, you will need to create a MR in the sync repo. The exact changes being made will depend on the request itself. The exact content can vary depending on the type of organization field.

**Note:** Templates shown for common field types. For other types (date, decimal, textarea, multiselect, regexp), modify the `type` attribute accordingly and refer to [Zendesk field documentation](https://support.zendesk.com/hc/en-us/articles/4408838961562-About-custom-fields-and-custom-field-types) for type-specific requirements.

**Tip:** Click each field type below to see its template.

<details>
<summary>checkbox</summary>

```yaml
---
title: 'Your Title Here'
previous_title: 'Your Title Here'
description: 'Your description here'
key: 'Your API key name here'
type: 'checkbox'
active: true
position: 1 # Integer representing organization field position, controls display order on organization page (lower numbers appear first)
tag: 'tag_to_add_when_checked' # Added onto the organization when the checkbox is checked, field is not present for other types
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
key: 'Your API key name here'
type: 'text'
active: true
position: 1 # Integer representing organization field position, controls display order on organization page (lower numbers appear first)
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
key: 'Your API key name here'
type: 'integer'
active: true
position: 1 # Integer representing organization field position, controls display order on organization page (lower numbers appear first)
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
key: 'Your API key name here'
type: 'dropdown'
active: true
position: 1 # Integer representing organization field position, controls display order on organization page (lower numbers appear first)
regexp_for_validation: null # Always null unless "regexp"
custom_field_options:
- name: 'Name of option'
  value: 'tag_option_uses'
- name: 'Name of option 2'
  value: 'tag_option_uses_2'
```

</details>

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

### Editing an organization field

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- **Note**: the `key` and `type` attribute cannot be changed once a field is created

{{% /alert %}}

To edit an organization field, you will need to create a MR in the sync repo. The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

#### Changing the title of an organization field

If you need to change the title of an organization field, copy the current value into the `previous_title` attribute and then change the `title` attribute. This allows the sync to still locate the organization field in question to update.

### Deactivating an organization field

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

To deactivate an organization field, you will need to create a MR in the sync repo. In this MR, you should do the following to the corresponding actions:

1. Move the file from the `active` folder to the `inactive` folder
1. Change the value of the `active` attribute to `false`

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

### Deleting an organization field

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

As the sync repos do not perform deletions, you will need to do this via Zendesk itself.

To delete an organization field:

1. Go to the [organization fields page](#viewing-organization-fields)
1. Locate the organization field you wish to delete and click on the name
   - You might need to change the active filter by clicking the `Filter` button
1. Click `Actions` at the top-right of the page
1. Click `Delete`
1. Click `Delete` on the pop-up to submit the changes

### Performing an exception deployment

To perform an exception deployment for organization fields, navigate to the organization fields sync project in question, go to the scheduled pipelines page, and click the play button for the sync item. This will trigger a sync job for the organization fields.

## Common issues and troubleshooting

### Not seeing organization field changes after a merge

As organization fields follow the `Standard` deployment type, they would only be deployed during a normal deployment cycle (or when an exception deployment has been done)
