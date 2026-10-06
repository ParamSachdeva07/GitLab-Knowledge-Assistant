---
title: 'Agents'
description: 'Documentation on Zendesk agents'
---

This guide covers Zendesk agent management at GitLab, including the automated agent sync process and manual agent administration. The agent sync automatically maintains agent metadata from GitLab's team data, while manual processes are used for provisioning and special cases.

Administrators should review the [Administrator tasks](#administrator-tasks) section.

## Understanding Zendesk agents

### What are Zendesk agents

Zendesk agents are team members with access to the agent workspace. Unlike end-users who can only submit and view their own tickets, agents can:

- View and manage all tickets
- Access internal notes and fields
- Use macros and triggers
- Perform administrative tasks (based on role)

We largely manage agents via the agent sync (for the Customer Support Systems and Support teams) and via the [provisioning/deprovisioning](/handbook/eta/css/zendesk/users/provisioning) process.

## Agent sync

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
- Project repos
  - [Zendesk Global](https://gitlab.com/gitlab-support-readiness/zendesk-global/users/agents)
  - [Zendesk US Government](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/users/agents)

{{% /alert %}}

The agent sync manages metadata for Customer Support and Customer Support Systems team members in Zendesk. Other agent accounts (integrations, bots, etc.) are managed manually.

### When does it run

- Zendesk Global: 0000 UTC every day
- Zendesk US Government: 0000 Pacific every day

### What does it manage

Each run will update the following for the agents:

- GitLab.com user ID (a custom [User field](/handbook/eta/css/zendesk/users/fields))
- GitLab.com username (a custom [User field](/handbook/eta/css/zendesk/users/fields))
- Zendesk Group membership
- Manager tag (a custom [User field](/handbook/eta/css/zendesk/users/fields))
- Name
- Out of Office status (a custom [User field](/handbook/eta/css/zendesk/users/fields))
  - US Government only
- Signature
- Select user tags (see [How does it work](#how-does-it-work) for more details)
- User region (a custom [User field](/handbook/eta/css/zendesk/users/fields) for Zendesk Global only)

Any modifications to the agent outside of the sync in Zendesk will be overridden by this.

### How does it work

{{% alert title="Note" color="primary" %}}

- As an `Owner` cannot be modified via API, this does not work for the system owner. They have to manage their user manually.

{{% /alert %}}

When the scheduled pipeline is triggered, two primary actions occur:

- A clone of the [Support team YAML files](https://gitlab.com/gitlab-support-readiness/support-team) occurs
- The `bin/sync` script runs

This script itself acts a bit differently depending on the Zendesk instance it is tied to

#### Zendesk Global

1. It fetches the groups of the Zendesk instance.
1. It reads the contents of the [Support team YAML files](https://gitlab.com/gitlab-support-readiness/support-team)
   - Note it skips select users who should not be in the sync, either because they are not editable (the Owner) or not targets for the sync currently
1. It fetches the user information for each user found in the YAML files via Zendesk
1. It loops over each agent to compare:
   - The Zendesk user data to the YAML user data, specifically:
     - If the organization they are associated to is `GitLab`
     - Their name and email
     - Their alias (alternative display name in Zendesk), if they have opted into using one
     - Their signature
     - Their user fields
     - Their tags, derived from:
       - Their current title
       - Who they report to
       - A shift tag (if their `working_hours` attribute in the YAML files indicates they should have one)
     - Their default group (determined by meeting one of the following criteria, in the order they appear):
       1. `BPO` for those with an email containing `ext@gitlab.com`
       1. `Support AMER` for those with a region containing `AMER`
       1. `Support APAC` for those with a region containing `APAC`
       1. `Support EMEA` for those with a region containing `EMEA`
       1. `General` for anyone not meeting the above criteria
   - It compares the user's current Zendesk group memberships with the groups they should belong to (based on YAML data and default group logic). Groups missing from Zendesk are added; extra groups not in YAML are removed.
1. It then performs updates, using the following API endpoints:
   - [User modification](https://developer.zendesk.com/api-reference/ticketing/users/users/#update-user)
   - [Adding a group membership](https://developer.zendesk.com/api-reference/ticketing/groups/group_memberships/#create-membership)
   - [Removing a group membership](https://developer.zendesk.com/api-reference/ticketing/groups/group_memberships/#delete-membership)

#### Zendesk US Government

1. It fetches the groups of the Zendesk instance.
1. It reads the contents of the [Support team YAML files](https://gitlab.com/gitlab-support-readiness/support-team)
   - Note it skips select users who should not be in the sync, either because they are not editable (the Owner) or not targets for the sync currently
1. It fetches the user information for each user found in the YAML files via Zendesk
1. It fetches a list of those on PTO (as per the `Support - Time Off` calendar's entries)
1. It loops over each agent to compare:
   - The Zendesk user data to the YAML user data, specifically:
     - If the organization they are associated to is `GitLab`
     - Their name and email
     - Their alias (alternative display name in Zendesk), if they have opted into using one
     - Their signature
     - Their user fields
     - Their tags, derived from:
       - Their current title
       - Who they report to
       - A shift tag (if their group memberships indicate they should have one)
     - Their default group (determined by meeting one of the following criteria, in the order they appear):
       1. `General` if they have a role of `Light agent`
       1. `Support` for anyone not meeting the above criteria
   - It compares the user's current Zendesk group memberships with the groups they should belong to (based on YAML data and default group logic). Groups missing from Zendesk are added; extra groups not in YAML are removed.
   - Notes if the user is changing their PTO status (i.e. coming back from or leaving for)
1. It then performs updates, using the following API endpoints:
   - [User modification](https://developer.zendesk.com/api-reference/ticketing/users/users/#update-user)
   - [Adding a group membership](https://developer.zendesk.com/api-reference/ticketing/groups/group_memberships/#create-membership)
   - [Removing a group membership](https://developer.zendesk.com/api-reference/ticketing/groups/group_memberships/#delete-membership)
1. The sync will also update all assigned tickets for team members with changes to their PTO status (so the field `Assignee OOO` reflects the change)

### Requesting changes to the sync

To request the changes to the agent sync, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Administrator tasks

{{% alert title="Note" color="primary" %}}

- All sections in this section require `Administrator` level access to Zendesk.

{{% /alert %}}

### Modifying the agent sync

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

To modify the agent sync, you will need to create a MR in the project repo. The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

### Manually creating an agent

{{% alert title="Warning" color="warning" %}}

- This should never be done unless specified to be done via [provisioning/deprovisioning](/handbook/eta/css/zendesk/users/provisioning).

{{% /alert %}}

To create an agent in Zendesk:

1. Hover over `+ Add` at the top-left of the page (when not on the admin panel)
1. Click `User`
1. Fill out the `Name`
1. Fill out the `Email`
1. Ensure the `User type` is that of `Staff member`
1. Set their `Role` accordingly
1. Click `Add`
