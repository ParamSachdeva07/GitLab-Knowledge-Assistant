---
title: 'Roles'
description: 'Documentation on Zendesk user roles'
---

This guide covers how to create, edit, and manage Zendesk user roles at GitLab. Administrators should review the [Administrator tasks](#administrator-tasks) section.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
  - **Note:** Roles are currently managed manually in Zendesk (no sync repo yet)

{{% /alert %}}

## Understanding roles

### What are Zendesk user roles

Zendesk uses Roles as a way to maintain permission sets for agents.

### How we manage roles

We currently manage all roles within Zendesk itself.

### Current roles in use

{{% alert title="Note" color="danger" %}}

This should be the single source of truth for the roles used. Never make changes outside of approved workflows.

Always be cautious of changes. Many of these can have significant downstream impacts.

{{% /alert %}}

For more information on what permissions the roles have, please see [this doc](https://docs.google.com/spreadsheets/d/1geQ3AYmlAUVFdgLusQVCaoNacV2yOHULjN2L7LP8rT0/edit?usp=sharing) (internal).

#### Zendesk Global

- [Admin](https://gitlab.zendesk.com/admin/people/team/roles/360004957599)
- [BPO](https://gitlab.zendesk.com/admin/people/team/roles/21960449459868)
- [Chat-only agent](https://gitlab.zendesk.com/admin/people/team/roles/11757383830044)
- [Contributor](https://gitlab.zendesk.com/admin/people/team/roles/360006947540)
- [GitLab Staff](https://gitlab.zendesk.com/admin/people/team/roles/360005625453)
- [GitLab Staff - Explore](https://gitlab.zendesk.com/admin/people/team/roles/360001716320)
- [Light agent](https://gitlab.zendesk.com/admin/people/team/roles/360004984553)
- [Security Staff](https://gitlab.zendesk.com/admin/people/team/roles/8869988210972)
- [Support Managers](https://gitlab.zendesk.com/admin/people/team/roles/360001716340)
- [Support Staff](https://gitlab.zendesk.com/admin/people/team/roles/1288263)
- [Support Staff - CMOC](https://gitlab.zendesk.com/admin/people/team/roles/8869919308956)
- [Support Staff - Explore](https://gitlab.zendesk.com/admin/people/team/roles/360001525560)
- [Tech Support](https://gitlab.zendesk.com/admin/people/team/roles/360001532679)

#### Zendesk US Government

- [Admin](https://gitlab-federal-support.zendesk.com/admin/people/team/roles/360016820032)
- [Chat-only agent](https://gitlab-federal-support.zendesk.com/admin/people/team/roles/20528982631700)
- [Contributor](https://gitlab-federal-support.zendesk.com/admin/people/team/roles/360016669231)
- [GitLab Staff](https://gitlab-federal-support.zendesk.com/admin/people/team/roles/360008466212)
- [Light agent](https://gitlab-federal-support.zendesk.com/admin/people/team/roles/360008074111)
- [Support Managers](https://gitlab-federal-support.zendesk.com/admin/people/team/roles/33687078022676)
- [Support US Federal Staff](https://gitlab-federal-support.zendesk.com/admin/people/team/roles/360008098572)
- [Support US Federal Staff w/ Explore](https://gitlab-federal-support.zendesk.com/admin/people/team/roles/360009925712)

## Creating a role as a non-admin

For the creation of a role, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Editing a role as a non-admin

For the modification of a role, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Deleting a role as a non-admin

To request the deactivation of a role, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Requesting a role change

All Zendesk role changes follow this approval process:

1. **Submit Request**: File an [access request issue](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?description_template=Individual_Bulk_Access_Request)
1. **Manager Approval**: The requester's manager must approve the request
1. **Security Review**: A Fullstack Engineer, Customer Support Systems reviews the business justification
1. **Decision**: If approved, Customer Support Systems will make the needed changes

## Administrator tasks

{{% alert title="Note" color="primary" %}}

- All sections in this section require `Administrator` level access to Zendesk.

{{% /alert %}}

### Viewing roles in Zendesk

To view roles in Zendesk:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `People > Team > Roles`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/people/team/roles)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/people/team/roles)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/people/team/roles)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/people/team/roles)

You can click on the role's name if you need to see the permissions and membership of a role.

### Creating a role

{{% alert title="Danger" color="danger" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

To create a role in Zendesk:

1. Access the [roles page](#viewing-roles-in-zendesk)
1. Click `Create role` at the top-right of the page
1. Fill out a name for the new role
1. Fill out a description for the new role (optional)
1. Fill out the various permission information as needed for the new role
1. Click `Create role` on the bottom-right of the page.

### Editing a role

{{% alert title="Danger" color="danger" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- This can severely impact agents' ability to do their jobs. Exercise caution in doing this.
- Never change a role's name. It can have many severe downstream effects.

{{% /alert %}}

To edit a role in Zendesk:

1. Access the [roles page](#viewing-roles-in-zendesk)
1. Click the name of the role to edit
1. Make the needed changes on the role
1. Click `Save` on the bottom-right of the page.

### Changing an agent's role

{{% alert title="Danger" color="danger" %}}

- This requires an access request issue. Do not proceed without one.
- This requires the requester's manager's approval to proceed. Do not proceed without one.

{{% /alert %}}
{{% alert title="Note" color="primary" %}}

- If this is for a Support or Customer Support Systems team member, you might need to also update their [Support team YAML file](https://gitlab.com/gitlab-support-readiness/support-team).

{{% /alert %}}

To change the role of an agent in Zendesk:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `People > Team > Team members`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/people/team/members)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/people/team/members)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/people/team/members)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/people/team/members)
1. Search for the person in question using their email address
1. Click their name
1. Click the drop-down to the right of the `Support` product and select the new role to use
1. Click `Save` at the bottom-right of the page

### Deleting a role

{{% alert title="Danger" color="danger" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- Keep in mind you may need to edit the [Agent sync](/handbook/eta/css/zendesk/users/agents/#agent-sync) as well
- This can severely impact agents' ability to do their jobs. Exercise caution in doing this.

{{% /alert %}}

To delete a role in Zendesk:

1. Access the [roles page](#viewing-roles-in-zendesk)
1. Click the name of the role to delete
1. Click `Actions` on the top-right of the page
1. Click `Delete role`
1. Click `Delete role` on the confirmation pop-up to confirm the deletion

## Common issues and troubleshooting

This is a living section that will have items added to it as needed.
