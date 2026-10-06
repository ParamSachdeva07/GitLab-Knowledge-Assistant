---
title: 'Shared organizations'
description: 'Documentation on Zendesk shared organizations'
---

By default, organizations are configured with private ticket visibility - users within an organization can only see and comment on their own tickets, not tickets submitted by other users in the same organization.

For some organizations, shared ticket visibility is more appropriate, allowing all organization members to view (and potentially comment) on each other's tickets. This is useful for small teams or organizations requiring internal ticket transparency.

## Types of shared organizations

There are two types of shared organizations:

- `Read only`: All associated users can see all tickets under the organization (but cannot comment on any other than their own)
- `Read+write`: All associated users can see and comment on all tickets under the organization

## Pre-checks

{{% alert title="Danger" color="danger" %}}

- There is a security and legal component to this feature. As such, you must ensure all pre-checks are done every single time. When in doubt, get a Customer Support Systems, Fullstack Engineer to review the situation.

{{% /alert %}}

Before we can proceed to enable a shared organization, three criteria must be met:

- The requester has confirmed which type of shared organization is desired
- The requester, on behalf of their organization, has approved the inherent security risk shared organizations present
  - **Note** The approval must be clear in their response. If it is not, ask them to verify they are approving the security risk
  - The message sent to the customer specifically about the security risk is as follows:
    > Please keep in mind that using a shared organization entails a potential security risk. Namely, if all users can view and comment on all tickets, that means the degree of privacy and security from separating the tickets is gone. This won't mean those outside your organization can see your tickets, only those within your organization.
- There is not an organization note/detail stating we will not enable a shared organization for them

Before performing any changes to the organization, make sure to update the ticket metadata to indicate the request information. The fields to focus on are:

- `Support Ops Problem Type` (should be `Shared organization requests`)
- `Shared Org type`
- `Confirm security risk`

If any of those criteria have not been met, we cannot proceed.

If all of those criteria are met, you may proceed with the changes.

## Enabling a shared organization

To enable a shared organization:

1. Navigate to the organization
1. Click the text next to `Users` at the top-left (it is actually a tab)
1. Select `Can view all org tickets`
1. On the drop-down below, select the correct option depending on the type they requested
1. Add a new item in the `Details` field containing the following:

   > Shared organization (TYPE) enabled DATE as per TICKET

   - Replace `TYPE` with either `Read only` or `Read+write`
   - Replace `DATE` with today’s ISO formatted date (`YYYY-MM-DD`)
   - Replace `TICKET` with the ticket’s URL
1. Add a public comment on the ticket confirming it has been enabled
1. Mark the ticket as `Solved`

## Disabling a shared organization

To disable a shared organization:

1. Navigate to the organization
1. Click the text next to `Users` at the top-left (it is actually a tab)
1. Select `Can view own tickets only`
1. Add a new item in the `Details` field containing the following:

   > Shared organization disabled DATE as per TICKET

   - Replace `DATE` with today’s ISO formatted date (`YYYY-MM-DD`)
   - Replace `TICKET` with the ticket’s URL
1. Add a public comment on the ticket confirming it has been disabled
1. Mark the ticket as `Solved`
