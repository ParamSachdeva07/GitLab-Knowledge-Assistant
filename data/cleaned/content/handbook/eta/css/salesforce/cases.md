---
title: 'Cases'
description: 'Documentation on Salesforce Cases'
---

This page documents how Zendesk tickets are synchronized to Salesforce Cases, including the automated workflow, administrator procedures, and troubleshooting guidance.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
- Project repos:
  - [Zendesk Global](https://gitlab.com/gitlab-support-readiness/zendesk-global/salesforce-cases)
  - [Zendesk US Government](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/salesforce-cases)

{{% /alert %}}

## Understanding Salesforce Cases

### What are Salesforce Cases

In Salesforce, a Case is a record that tracks a customer's question, issue, feedback, or request.

### How do tickets become Salesforce Cases

**Note:** Only tickets associated with a Zendesk organization are synced to Salesforce. Tickets without an organization (such as free user inquiries) are not synced.

Whenever a ticket (associated to an organization) is created or closed, a trigger in the Zendesk instance triggers a pipeline (via a Zendesk webhook) in the project for the corresponding Zendesk instance.

This causes the `bin/run` script to run, which does the following:

- Fetch information on the ticket from Zendesk (including organization, requester, and assignee information)
- Fetch a list of Zendesk forms
- Search Salesforce to determine if the case exists

  <details>
  <summary>SOQL used</summary>

  ```sql
  SELECT
    Id,
    Zendesk_Support_Ticket_ID__c,
    Priority,
    Status
  FROM Case
  WHERE
    Zendesk_Support_Ticket_URL__c = 'TICKET_URL'

  ```

  </details>

- Creates a case if one does not exist
- Updates the case if one does exist

The information synced to a Salesforce Case from a ticket is:

- Ticket priority
- Ticket status
- Ticket assignee's name (if one is present)
- Ticket form name
- Ticket requester's email
- Ticket requester's name
- Ticket subject
- Agent accessible ticket URL

## Administrator tasks

Administrator tasks are performed by Customer Support Systems team members with appropriate access to the project repositories.

### Modifying the sync projects

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

To modify the sync that manages Salesforce cases, you will need to create a MR in the corresponding project repo (which one depends on the change being made). The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR. Because this is an `Ad-hoc` deployment type, the changes will be used the next time a ticket is created or closed (which triggers the sync).

## Common issues and troubleshooting

### Case not created in Salesforce

If a Zendesk ticket does not have a corresponding Salesforce case, it indicates the ticket was not associated with an organization in Zendesk at the time of creation. If association occurs on the ticket prior to it closing, a case will be created at the time of ticket closure.
