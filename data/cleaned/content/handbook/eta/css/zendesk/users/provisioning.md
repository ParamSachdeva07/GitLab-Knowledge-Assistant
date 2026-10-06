---
title: 'Provisioning'
description: 'Documentation on Zendesk user provisioning'
---

This document details the process for provisioning and deprovisioning agents in Zendesk.

{{% alert title="Note" color="primary" %}}

- All sections in this section require `Administrator` level access to Zendesk.

{{% /alert %}}

## Role based entitlement

2 days after someone starts working at GitLab, an access-request issue is generated based off their role based entitlements. We would manually provision users based off the request itself.

To do this, you will need to:

1. Create the user in Zendesk (the role to be used should be included in the role based entitlement access request issue). Ensure their groups and other such settings are accurate (see the access request issue). See [Manually creating an agent](/handbook/eta/css/zendesk/users/agents#manually-creating-an-agent) for more info on creating the user.
1. Associate the correct app in Okta (see [Assigning an app via Okta](#assigning-an-app-via-okta) for more info) if required.

After you have done so, mark off the items in the access request issue.

## Special request

Any special request issues to provision on either Zendesk instance not related to role based entitlements must be done via an access request issue. Do note this will require approval from the Zendesk system owner to proceed.

See [Role based entitlements](#role-based-entitlement) for information on what to do when it comes time to provision it.

## Zendesk Global light agents

This is handled by the requester requesting it via [Lumos](https://app.lumosidentity.com/app_store?domainAppId=1115644&permissionIds=6102631). Doing so creates a CI/CD pipeline in the [Light Agent Provisioning project](https://gitlab.com/gitlab-support-readiness/zendesk-global/users/light-agent-provisioning).

This triggers the `bin/process_via_lumos` script, which does the following:

1. Reviews if the email of the requester has the domain of `gitlab.com`
   - If they do not, it does not proceed
1. Looks if the email is currently in user in Zendesk
1. If a user exists, it then checks if they are already an agent
   - If they are, it outputs a message stating so and does not proceed
1. It will then perform actions to create or update the user to be an agent with the required metadata

### Specialized Zendesk Global light agents

{{% alert title="Note" color="primary" %}}

- Requesters must first have a fully created light agent account. If they do not have one, direct them to have one created first.

{{% /alert %}}

Specialized groups of light agents are allowed to file specific types of Internal Requests. These agents require specific tags to be added or removed based on their team:

| Team | Required Tag |
|------|--------------|
| Partner Support | `partner_support_agent` |
| Order Management | `order_management_team` |
| OEM Management | `oem_management_team` |

You should only ever be asked to either add or remove that tag (and it must be via an access request issue).

## Zendesk US Government light agents

As these require the tech stack provisioner to manually provision these, an [Access Request issue](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new) is required.

Once one has been received and approved, the process will go as follows:

1. Submit a Compass request by selecting `Background Checks` under the People Team dropdown. On the next page, select `Identity Verification` or `Other` from the dropdown `What type of support do you need?` and use the prompt below to fill out your request:
   > Greetings all!
   >
   > Can you verify if NAME is a US Citizen? They are requesting access to the US Government Zendesk instance via ISSUE which does require it.
   >
   > Thanks!
   - Replace NAME with the requester's name
   - Replace ISSUE with the link to the Access Request issue
   - [This should be a quick link to that form](https://app.serval.com/new-request)
1. Note the Access Request issue that you have contacted the People team to verify US citizenship.
1. Depending on the response from the People team, your next actions will vary:
   - If the People team verifies the citizenship:
     - Create the Light Agent manually in the Zendesk US Government instance.
     - Associate Zendesk US Government app in Okta (see [Assigning an app via Okta](#assigning-an-app-via-okta) for more info)
     - Update the issue letting them know it has been provisioned.
   - If the People team cannot verify the citizenship:
     - Comment on the Access Request issue noting citizenship could not be confirmed and that the issue will be closed, as no further action can be taken without verification from the People team.

{{% alert title="Note" color="warning" %}}

The below information is not yet live and in use. For more information, please see [gitlab-com/gl-security/corp/issue-tracker#737](https://gitlab.com/gitlab-com/gl-security/corp/issue-tracker/-/work_items/737)

{{% /alert %}}

This is handled by the requester requesting it via Lumos. Doing so creates a CI/CD pipeline in the [Light Agent Provisioning project](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/users/light-agent-provisioning).

This triggers the `bin/process_via_lumos` script, which does the following:

1. Reviews if the email of the requester has the domain of `gitlab.com`
   - If they do not, it does not proceed
1. Looks if the email is currently in use in Zendesk
1. If a user exists, it then checks if they are already an agent
   - If they are, it outputs a message stating so and does not proceed
1. It will then perform actions to create or update the user to be an agent with the required metadata

## Deprovisioning

You will, from time to time, get a request to deprovision an agent (these will mostly stem from Offboarding tasks). To deprovision an agent, go to that agent's page in Zendesk and do the following:

- Unassign any active tickets (less than Closed) from that agent (assign them to their manager)
- Delete any [Support Team](https://gitlab.com/gitlab-support-readiness/support-team) files associated with the user (if applicable)
- Delete the user from Zendesk
- After doing so, do the following on the issue requesting the deprovisioning
  - Check the corresponding boxes on the request issue

## Assigning an app via Okta

To associate an app via Okta, you will add the person’s email to the corresponding google group as a Member:

- [Zendesk US Government](https://groups.google.com/a/gitlab.com/g/okta-zendeskfederal-users/members)

If you ever need to remove the person, locate them in the group and click the Unassign option.
