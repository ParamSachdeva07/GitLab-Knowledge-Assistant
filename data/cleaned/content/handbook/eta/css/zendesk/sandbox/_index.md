---
title: 'Sandbox'
description: 'Documentation on Zendesk sandboxes'
---

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
  - **Note:** Sandboxes are currently managed manually in Zendesk (no sync repo yet)

{{% /alert %}}

## Understanding sandboxes

### What is the Zendesk Sandbox

As per [Zendesk](https://support.zendesk.com/hc/en-us/articles/4408822049818-Creating-a-sandbox-environment-to-test-changes):

> Sandbox environments provide a test environment that closely mirrors your production instance in configuration and some data. This allows you to accurately test updates to workflows, experiment with integrations, and provide training for new agents in an environment that reflects your production environment.

The Zendesk Sandbox is a replica Zendesk instance you can use to test, learn, replicate, etc. in an environment that is separated from production instances.

We utilize the Zendesk Sandbox in all our change management processes. This allows us a safe and secure place to test changes/updates/etc. so we can ensure the implementations we push into production are both stable and well vetted.

### Common use cases

- Testing trigger and automation changes before production deployment
- Experimenting with new workflows
- Training new team members
- Validating app configurations
- Testing theme modifications

### Where are the sandboxes?

You can locate the sandboxes via:

- [Zendesk Global](https://gitlab1707170878.zendesk.com/agent/)
- [Zendesk US Government](https://gitlabfederalsupport1585318082.zendesk.com/agent)

### How to access the Zendesk Sandbox

For testing end-user workflows (ticket submission, portal access, etc.), use the pre-configured test accounts listed in the [Zendesk Sandbox Test Orgs and Users](https://docs.google.com/spreadsheets/d/1g6lJ3AUS4EYqoBYzAdExp4v1dkzOb3GWKaMIoZikjts/edit?usp=sharing) (internal only) spreadsheet. These accounts simulate different customer scenarios (free users, paid users, various subscription levels, etc.).

You should use the pre-created test organizations and users whenever possible. If for some reason the users there will not work in your case, please contact the Fullstack Engineer for Customer Support Systems.

### Sandbox limitations

- API rate limits may differ from production
- License seat counts differ from production
- Some integrations may not work or have not been setup

## Administrator tasks

{{% alert title="Note" color="primary" %}}

- All sections in this section require `Administrator` level access to Zendesk.

{{% /alert %}}

### Seeing a list of sandboxes

To see a list of current sandboxes for a Zendesk instance:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
1. Go to `Account > Sandbox > Environments`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/account/sandbox/environments)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/account/sandbox/environments)

### Creating a Sandbox

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

To create a sandbox for a Zendesk instance:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
1. Go to `Account > Sandbox > Environments`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/account/sandbox/environments)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/account/sandbox/environments)
1. Click `Create sandbox` at the top-right of the page
1. Enter a name for your sandbox
1. Select how many tickets to copy from production from the drop-down
   - It is recommended the answer you use is `0` for this
1. Check or uncheck the box to copy required organizations (i.e the bare minimum organization information)
   - It is recommended you check this box
1. Click `Create sandbox` at the bottom-right of the page

### Deleting a Sandbox

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- This should be exceedingly rare and only done when absolutely required. Exercise caution in doing this.

{{% /alert %}}

To delete a sandbox from a Zendesk instance:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
1. Go to `Account > Sandbox > Environments`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/account/sandbox/environments)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/account/sandbox/environments)
1. Click the three vertical dots to the right of the sandbox you wish to delete
1. Click `Delete sandbox`
1. Click `Delete sandbox` to confirm the deletion

## Common issues and troubleshooting

This is a living section that will have items added to it as needed.
