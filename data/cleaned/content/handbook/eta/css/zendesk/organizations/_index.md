---
title: 'Organizations'
description: 'Documentation on Zendesk organizations'
---

This guide covers how we manage Zendesk organizations at GitLab. Administrators should review the [Administrator tasks](#administrator-tasks) section.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`

{{% /alert %}}

## Understanding organizations

### What are organizations

As per [Zendesk](https://support.zendesk.com/hc/en-us/articles/4408882246298-Creating-organizations):

> Organizations are typically collections of your end users, but they can also include agents.

In other words, organizations are simply a collection of users in Zendesk (much like groups). They contain a list of users (both end-users and agents can be in an organization).

We also use them to store metadata (synced from Salesforce), which is used to determine such things as SLA, ARR, etc. (see [Organization fields](/handbook/eta/css/zendesk/organizations/fields) for more information). Because of this, they play a key role in how our customers receive entitlement to paid support.

### How we manage organizations

As organizations (and the metadata within) play such a key role in our routing, we have complex methods in place to manage them.

- For organization creation and modification, please see the [Zendesk-Salesforce sync](/handbook/eta/css/zendesk-salesforce-sync/).
- For organization deletion, please see [Organization deletion](/handbook/eta/css/zendesk/organizations/deletion).
- For associating users to an organization, please see [Organization association](/handbook/eta/css/zendesk/organizations/association).

### Locating an organization

The easiest way to locate an organization is by searching for it via the Salesforce account tied to the organization.

Outside of that, you would need to use alternative searching means to locate the organization. See our [Searching documentation](/handbook/eta/css/zendesk/searching/) for more information.

### Permissions

By default, organizations are configured with private ticket visibility - users within an organization can only see and comment on their own tickets, not tickets submitted by other users in the same organization.

For some organizations, shared ticket visibility is more appropriate, allowing all organization members to view (and potentially comment) on each other's tickets. This is useful for small teams or organizations requiring internal ticket transparency.

For more information on expanded permissions or managing permissions, see our [Shared organizations](/handbook/eta/css/zendesk/organizations/shared-orgs) documentation.

### Domain matching

While Zendesk does have the functionality to do domain matching, we have determined that the security risks inherent in this feature outweigh the benefits that would be received from its use.

Because of this decision, as of August 2020, GitLab will no longer apply a domain on a Zendesk organization. Any organization that had this applied prior to this date will have it as a legacy feature.

## Organization notes

### Zendesk Global

There are two forms of organization notes we utilize:

- Customer Support Systems organization notes
  - Managed via Zendesk in the `Notes` and `Details` fields on the organization itself.
- Support Team organization notes
  - Managed via Support's [Zendesk Global Organizations project](https://gitlab.com/gitlab-com/support/zendesk-global/organizations).

When an organization has a ticket created, the [ticket processor](/handbook/eta/css/zendesk/tickets/processor) runs to parse both of these into internal comments on the ticket itself.

If you need to modify an organization's notes, the action you take will depend on the team you are on:

- Customer Support Systems: see [Modifying an organization's notes or details](#modifying-an-organizations-notes-or-details)
- Anyone else: Create a merge request on Support's [Zendesk Global Organizations project](https://gitlab.com/gitlab-com/support/zendesk-global/organizations)

### Zendesk US Government

As there is a citizenship requirement for data within this instance, we manage organization notes a bit differently for the US Government instance. We manage all internal notes on Zendesk itself due to data privacy concerns. As such, we separate them as such:

- `Notes` are for Support Team organization notes
- `Details` are for Customer Support Systems organization notes

When an organization has a ticket created, the [ticket processor](/handbook/eta/css/zendesk/tickets/processor) runs to parse both of these into internal comments on the ticket itself.

If you need to modify an organization's notes, the action you take will depend on the team you are on:

- Customer Support Systems: see [Modifying an organization's details](#modifying-an-organizations-notes-or-details)
- Anyone else: Reach out to Customer Support Systems via Slack for assistance

## Administrator tasks

{{% alert title="Note" color="primary" %}}

- All sections in this section require `Administrator` level access to Zendesk.

{{% /alert %}}

### Modifying an organization's notes or details

To modify an organization's notes:

1. Locate the organization within Zendesk
1. Click in the relevant textarea
   - `Notes` for notes
   - `Details` for details
1. Make the changes needed
1. Click outside of relevant textarea

### Changing an organization's permissions

See our [Shared Organizations documentation](/handbook/eta/css/zendesk/organizations/shared-orgs) for more information.

## Common issues and troubleshooting

This is a living section that will have items added to it as needed.
