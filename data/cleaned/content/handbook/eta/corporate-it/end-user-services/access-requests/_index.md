---
title: Access Requests (ARs)
controlled_document: true
tags:
  - security_standard
  - security_standard_acia
---

{{< label name="Visibility: Audit" color="#E24329" >}}

Access Requests are owned by the IT team, while onboarding, offboarding and internal transition requests are owned by the People Operations Team.

If you have any access requests related questions, please contact us via the Compass app in Slack (type "Compass" in the top search bar to find it) or it-help@gitlab.com.

## Requesting Access in Lumos

Most access requests are now made through the [Lumos App Store](https://app.lumosidentity.com/app_store) rather than by opening an issue. Lumos automatically routes the request to your manager, the system owner, and any other required approvers, and provisions the app automatically where automation exists.

### Create an access request

1. Open Lumos from the Okta tile or the Slack sidebar.
1. Select the app from the list.
1. Provide the following:
   - Who the access is for
   - Permission needed
   - Access length
   - Business justification — "why" the access is needed

You can also request access directly in Slack: find the Lumos app, click **Request Access**, then select the app, permission, and target user. Lumos notifies you when all approvals are complete and access is granted.

### Check the status of a request

Open the *Messages* tab of the Lumos Slack app. Every request you have made appears there and updates dynamically as its status changes.

### Approve a request

Open the notification in Slack or email, or visit Lumos from the Okta tile, then approve, comment, or deny. You can click **Edit** on the Slack approval to change which groups the user is being added to before approving.

Not every application is in Lumos yet — we are migrating the tech stack iteratively, prioritising apps with provisioning automation and high request volume. If the app you need is not listed, use the issue templates below.

See the [Lumos Access Request Guide](/handbook/security/corporate/systems/lumos/ar/) for screenshots and the full process, including how to request that an app be added to the Lumos App Store.

## Access requests related pages

- [Frequently asked questions](/handbook/eta/corporate-it/end-user-services/access-requests/#application-specific-templates)
- [Tech Stack](https://gitlab.com/gitlab-com/www-gitlab-com/-/blob/master/data/tech_stack.yml)
- [Baseline Entitlements](https://internal.gitlab.com/handbook/eta/corporate-it/end-user-services/access-request/baseline-entitlements/)
- [Temporary service providers access requests and onboarding](https://internal.gitlab.com/handbook/eta/corporate-it/end-user-services/access-request/temporary-service-providers/)

## Get Started

All open and closed ARs can be found in the [access-requests project](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/), and you can create a new issue [here](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new).

When creating a new AR, you'll be given the option to chose from various templates to help you figure out exactly what additional information is needed to fulfil your request and if additional approvals are required.
**We made sure to add all the required lables for each issue type, it's possible that we missed something so please make sure to double check your request before submitting it**

While there are a large number of templates available, they typically fall into one of the categories below.

*A full list of all available templates cane be found [here](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/tree/master/.gitlab/issue_templates)*

### Individual or Bulk Access Request

[Individual or Bulk Access Requests](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?description_template=Individual_Bulk_Access_Request) should be used if none of the other templates match what you are looking for.

You can use this template to request access for individuals or multiple people, as long as all the people are requesting access to the same systems. Create multiple issues if multiple people require access to different systems.

### Access Change Request

[Access Change Requests](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?description_template=Access_Change_Request) are logged when a team member no longer requires access to a currently provisioned system or no longer requires the same level of access (downgraded access from admin to user etc).
Refer to [`For Total Rewards Analysts: Processing Promotions & Compensation Changes`](/handbook/people-group/promotions-transfers/) section of the GitLab handbook for additional information.

It is important to note that while Okta has provisioning/deprovisioning automation in place, this is not a complete/accurate reflection of access provisioning and deprovisioning.
Okta has been configured to assign integrated/implemented applications based on a user's role/group.
This makes applications accessible via Okta but users may still have the ability to access the systems directly.
Refer to [Okta Application Stack](https://gitlab.com/gitlab-com/www-gitlab-com/-/blob/master/data/tech_stack.yml) for a list of applications set up in Okta.

### Application-Specific Templates

These issues relate to access to or withing specific applications and services. For example, you can use the [1Password Request Form](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?description_template=1Password_Request) to modify existing vaults and groups, or to create new ones.

### Admin (Black) Accounts

We support the provisioning of admin access to various core services, such as Okta, 1Password, and Google Workspace. This proccess typically first involves requesting the [creation of an admin account](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?description_template=Admin_Black_Account_Creation) with a new email address.
Once the admin account has been created, additional ARs need to be submitted for admin access to specific services.

- [Admin (Black) Acount](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?description_template=Admin_Black_Account_Creation)
- [1Password Admin](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?description_template=Admin_Black_Account_Role_1Password)
- [AWS Admin](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?description_template=Admin_Black_Account_Role_AWS)
- [Google Workspace Admin](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?description_template=Admin_Black_Account_Role_GoogleWorkspace)
- [Okta Admin](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?description_template=Admin_Black_Account_Role_Okta)

### Name Change Request

You can use [this template](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/blob/master/.gitlab/issue_templates/Name_change_request.md) when you want to change your preferred name. We will then work with the People Ops team to update your name across all systems and provide you with a new email address.

### Baseline Entitlements

These issues help us assign the appropriate access to new-hires. These are created automatically for many roles and don't typically require additional approvals. However, if the automation does not create the issue, it is the responsibility of the new-hire's manager to manually create the issue.

A list of baseline issue templates can be found [here](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/tree/master/.gitlab/issue_templates/role_baseline_access_request_tasks) and can be freely customized.

For additional support when creating Baseline Entitlement Requests, please contact us via the Compass app in Slack (type "Compass" in the top search bar to find it) or it-help@gitlab.com.

## Working on Access Requests

### Department Access Request Boards

- If you need additional labels or have suggestions for improving the process until we can fully automate, please [open an issue](https://gitlab.com/gitlab-com/it/end-user-services/issues/it-help-issue-tracker/-/issues/new).
- ARs are auto-assigned and auto-labeled when possible by department. In some cases, there are multiple provisioners per tool. If a template cannot be auto-assigned, Business Technology will provide a board where the provisioners can review their department's issues by label (ie `dept::to do`. It is up to the department to manage the workflow on who works the issues to completion.
- **Moving an issue from one column to another will remove the first label (per the column header) and add the second label. Please use caution when moving issues between columns.**
- Departments can check their outstanding access request issues by viewing their board below.

{{% panel header="**AR boards: to-do:**" header-bg="success" %}}

1. [Data](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/boards/1319045)
1. [Finance](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/boards/1319048)
1. [Infra](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/boards/1262513)
1. [IT](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/boards/1262521)
1. [Legal](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/boards/1319051)
1. [PeopleOPs](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/boards/1318841)
1. [Prod+Eng](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/boards/1319057)
1. [Marketing](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/boards/1284066)
1. [Sales](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/boards/1262518)
1. [Security](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/boards/1319052)
1. [Support](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/boards/1319053)
{{% /panel %}}

## Adding Access Request Process for a new item in the Tech Stack

If you need to initiate an Access Request process for a new item in the tech stack:

1. Confirm the tool is added to the [tech stack](https://gitlab.com/gitlab-com/www-gitlab-com/-/blob/master/data/tech_stack.yml)
1. Confirm a team member is included as the `provisioner` `deprovisioner`
1. Document the requirement to submit an Access Request in any relevant handbook pages

## Additional help

- Please @ mention `@gitlab-com/gl-security/corp/helpdesk` in the issue, with no particular SLA.
- If your request is urgent, please contact us via the Compass app in Slack (type "Compass" in the top search bar to find it) or it-help@gitlab.com.
