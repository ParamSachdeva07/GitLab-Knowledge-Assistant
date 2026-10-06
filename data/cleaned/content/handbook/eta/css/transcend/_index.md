---
title: 'Transcend'
description: 'Documentation on Transcend'
---

## Understanding Transcend

### What is Transcend

Transcend is a tool used for servicing data privacy requests. The primary users are Support Engineers and the Privacy team.

## Working Transcend items

For Customer Support Systems, we may be assigned items from Transcend. When we are assigned items in Transcend, our focus is solely on the users within our Zendesk Global instance.

For these items, you will be notified action is needed by us via email. In the notification email, click the hyperlink to be taking right to the assigned task.

When assigned a task, you need to use the email address of the user in question to locate them in Zendesk. This can be done by doing a search using the query `email:EMAIL_ADDRESS` (replacing `EMAIL_ADDRESS` with the actual email address).

From here, the actions you perform will depend on the status of the user in question:

- If no user is found
  1. Click `Mark as Not Found` in Transcend to complete the task.
- If a user is found AND they are not associated to an organization
  1. Delete or close all non-closed tickets requested by the user
  1. Delete the user
  1. Click `Mark as Complete` in Transcend to complete the task.
- If a user is found AND they are associated to an organization
  - If the organization has active subscriptions
    1. The user is not qualified for deletion (as the organization owns that data, not the user). Click `Mark as Exception` in Transcend to complete the task.
  - If the organization has no active subscriptions (i.e. they are expired)
    1. Delete or close all non-closed tickets requested by the user
    1. Delete the user
    1. Click `Mark as Complete` in Transcend to complete the task.

## Supplemental issues

In some situations, Legal will request the deletion of a user that had filed a data privacy request but was denied due to being part of a paid subscription.

For these issues, you need to use the email address (or addresses) of the user(s) in question to locate them in Zendesk. This can be done by doing a search using the query `email:EMAIL_ADDRESS` (replacing `EMAIL_ADDRESS` with the actual email address) for each email address provided.

- If the user does not exist:
  1. Update the issue to indicate the user does not exist in Zendesk
- If the user does exist:
  - If the user is associated to an organization that has active subscriptions
    1. Update the issue to indicate the user in question is associated to an organization that still has a paid subscription (and we cannot proceed)
  - If the user is associated to an organization that does not have active subscriptions (i.e. they are expired)
    1. Delete or close all non-closed tickets requested by the user
    1. Delete the user
    1. Update the issue to indicate the user has been removed from the Zendesk system
  - If the user is not associated to any organization:
    1. Delete or close all non-closed tickets requested by the user
    1. Delete the user
    1. Update the issue to indicate the user has been removed from the Zendesk system
