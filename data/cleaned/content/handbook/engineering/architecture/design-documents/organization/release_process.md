---
title: "Organizations Release Process"
description: "Release process specific Organization features."
owning-stage: "~devops::tenant scale"
group: Organizations
toc_hide: true
---

This document outlines the release process for specific Organization features and [stages](../../../infrastructure-platforms/tenant-scale/organizations/release-stages.md).

## Beta

### Artifact Registry (design partners)

We will manually onboard a small number of design partners onto Organizations so that they can start using Artifact Registry. This is a interim release process until the [Standalone organizations beta](#standalone-organizations-with-self-serve-onboarding) is available.

#### Step 1 - Enable feature flags

**Owned by:** ~group::organizations

The [Organization flags](https://docs.gitlab.com/development/organizations/release_status/) need to be moved into this state.
This state is only specific to Beta. After Beta these flags can move through other stages.

| Flag                              | Stage        | Description                                                            |
| --------------------------------- | ------------ | ---------------------------------------------------------------------- |
| `org_creation`                    | Experimental | Create an organization from global pages or public APIs.               |
| `org_switcher`                    | Experimental | The organization switcher dropdown component.                          |
| `create_org_from_group_settings`  | Experimental | Create an organization for a top-level group from the group settings.  |
| `org_admin_area`                  | Experimental | Organization admin area for organization owners.                       |
| `org_pages`                       | LA (100%)    | Organization pages that extend `Organizations::ApplicationController`. |
| `your_work_sidebar_org_menu_item` | LA (100%)    | Shows `Organizations` menu item in the `Your work` sidebar.            |

`org_pages` and `your_work_sidebar_org_menu_item` need to move into LA (100%) because they gate pages outside of the organization context and will not work with the `organization` actor, they instead use the `user` actor.

`org_pages` gates the organization pages which are not visible until a user has an active organization. This means that users will not see any changes in the UI until after steps 3 and 4.

`your_work_sidebar_org_menu_item` is also gated by a check that only shows the `Organizations` menu item in the `Your work` sidebar for users that have an Organization with the a [state of `active`](lifecycle.md#states). This means that users will not see any changes in the UI until after steps 3 and 4.

`ui_for_organizations` feature flag - We still have a few instances left behind this flag. Most notably the logic around if a sole owner of an Organization can be deleted. We will need to enable this feature flag globally for all users since it gates pages outside of the organization context and will not work with the `organization` actor.

```shell
/chatops gitlab run feature set ui_for_organizations true
```

#### Step 2 - Identify design partner's top-level groups (TLGs)

**Owned by:** ~devops::package

Identify design partners to be onboarded to Organizations and provide a list of TLG full paths.

#### Step 3 - Backfill TLGs with new Organization

**Owned by:** ~group::organizations

Enable the `root_group_organization_backfill` feature flag for the TLGs using the `group` actor.

```shell
/chatops gitlab run feature set --group=a-customer-group root_group_organization_backfill true
```

This will do the following:

1. Create an Organization with the same name and path as the TLG
1. Transfer TLG into this Organization

#### Step 4 - Confirm Organization and sync TLG members

**Owned by:** ~group::organizations

Enable the `root_group_organization_confirm` feature flag for the TLGs using the `group` actor.

```shell
/chatops gitlab run feature set --organization=a-customer-group root_group_organization_confirm true
```

This will do the following:

1. Confirm the Organization
1. Add TLG members as Organization Members. Owners become Organization Administrators and all other Members become Organization Regular Members.

#### Step 5 - Enable Artifact Registry UI feature flag

**Owned by:** ~group::organizations

Enable the `artifact_registry_ui` feature flag for the organization that was just created and confirmed.

```shell
/chatops gitlab run feature set --organization=a-customer-group artifact_registry_ui true
```

This will show the Artifact Registry UI in the Organization.

#### Step 6 - Notify design partners

**Owned by:** ~devops::package

Notify design partners with a link to documentation that explains how to enable and start using Artifact Registry.

#### Step 7 - Enable Artifact Registry

**Owned by:** ~devops::package

The customer will now see an `Organizations` menu item in the `Your work` sidebar. They can enable under the `Artifacts` menu item in their Organization. Once enabled they can start using Artifact Registry.

#### Rollback

```shell
/chatops gitlab run feature set ui_for_organizations false
/chatops gitlab run feature set --group=a-customer-group root_group_organization_backfill false
/chatops gitlab run feature set --organization=a-customer-group root_group_organization_confirm false
/chatops gitlab run feature set --organization=a-customer-group artifact_registry_ui false
```

### Standalone organizations with self-serve onboarding

#### Step 1

**Owned by:** ~group::organizations

The [Organization flags](https://docs.gitlab.com/development/organizations/release_status/) need to be moved into this state:

| Flag                              | Stage        | Description                                                            |
| --------------------------------- | ------------ | ---------------------------------------------------------------------- |
| `org_creation`                    | Experimental | Create an organization from global pages or public APIs.               |
| `org_switcher`                    | Experimental | The organization switcher dropdown component.                          |
| `create_org_from_group_settings`  | Beta         | Create an organization for a top-level group from the group settings.  |
| `org_admin_area`                  | LA (100%)    | Organization admin area for organization owners.                       |
| `org_pages`                       | LA (100%)    | Organization pages that extend `Organizations::ApplicationController`. |
| `your_work_sidebar_org_menu_item` | LA (100%)    | Shows `Organizations` menu item in the `Your work` sidebar.            |

`create_org_from_group_settings` stays in Beta because it can be used with the `--group` actor. `org_admin_area`, `org_pages`, and `your_work_sidebar_org_menu_item` need to move into LA (100%) because there is no available actor to use on them that will make them available after a customer creates an Organization. These flags gate features that are only available to users that have an Organization so they can safely be in LA (100%) since Organization creation is still gated by the group actor.

#### Step 2 - Identify design partner's top-level groups (TLGs)

**Owned by:** ~group::organizations

Identify design partners to be onboarded to Organizations and provide a list of TLG full paths.

#### Step 3 - Enable the ability to create an Organization from your TLG

**Owned by:** ~group::organizations

Enable the `org_stage_beta` feature flag for design partner's TLGs

```shell
/chatops gitlab run feature set --group=a-customer-group org_stage_beta true
```

#### Step 4 - The customer creates an Organization from their TLG

**Owned by:** ~group::organizations

The customer goes to their TLG -> then selects **Settings > General > Advanced** and uses the `Create an Organization`
UI. This creates an Organization, moves their TLG (and any other owned TLGs they select) into the Organization, and sets the Organization state to `active`.

They then see the `Organizations` menu item in the `Your work` sidebar and can use Organizations.

#### Rollback

Depending on the severity of the issue the following options can be used:

##### Option 1 - bug fix

If it is a low severity issue that can be quickly fixed we should push a fix.

##### Option 2 - disable feature flags

If it is a higher severity issue that is impacting all customers and will take some time to fix we can disable the `org_stage_la_100` feature flag. It is important to note that this will disable Organizations for all customers.

```shell
/chatops gitlab run feature set org_stage_la_100 false
```

##### Option 3 - move TLG(s) back to the Default Organization

If it is a higher severity issue that can not be solved by the above options the TLG(s) should be moved back to the Default Organization. Contact an SRE and have them run the following commands in the Rails console:

```rb
organization = Organizations::Organization.find_by_path("<organization-path>") # replace with the actual organization path
default_organization = Organizations::Organization.default_organization
current_user = ::Users::Internal.in_organization(organization).admin_bot

organization.groups.top_level.find_each do |group|
  Organizations::Transfer::GroupsService.new(
    group: group,
    new_organization: default_organization,
    current_user: current_user
  ).execute
end
```
