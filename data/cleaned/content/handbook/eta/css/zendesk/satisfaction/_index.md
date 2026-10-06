---
title: 'Satisfaction'
description: 'Documentation on Zendesk satisfaction'
---

This guide covers satisfaction tracking at GitLab, including the transition from Zendesk's built-in satisfaction surveys to our custom CES (Customer Effort Score) implementation.

## Satisfaction Rating Scores

These are the standardized satisfaction ratings used in Zendesk tickets, whether from the legacy satisfaction system or the current CES surveys:

- Unoffered: No survey has been sent
- Offered: Survey sent but not yet responded to
- Good: Positive satisfaction rating
- Good with comment: Positive rating with customer feedback
- Bad: Negative satisfaction rating
- Bad with comment: Negative rating with customer feedback

## CES Surveys

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`

{{% /alert %}}

### What are CES Surveys

CES (Customer Effort Score) surveys are forms we send out to customers to receive feedback from them on the level of effort required to work with support. A lower score indicates more effort was required while a higher score indicates less effort was required.

CES surveys use a 7-point scale where:

- 1-3: High effort (negative experience)
- 4: Neutral
- 5-7: Low effort (positive experience)

We use them as a replacement for support satisfaction/customer satisfaction.

### Who receives them

We send out the CES survey to those who meet specific criteria. The exact criteria varies by Zendesk instance.

- For Zendesk Global:
  - Must meet all of the following criteria:
    - The organization is not `GitLab`
    - Ticket form is not `GitLab Incidents`
    - Ticket form is not `Billing`
  - Must meet at least one of the following criteria:
    - The ticket contains one of the following tags:
      - `sub_dotcom_ultimate`
      - `sub_dotcom_premium`
      - `sub_sm_ultimate`
      - `sub_sm_premium`
      - `sub_sm_starter`
      - `sub_gitlab_dedicated`
      - `sub_consumption_ai`
      - `sub_consumption_cicd_minutes`
      - `sub_consumption_eap`
      - `sub_consumption_duo_enterprise`
      - `sub_consumption_duo_amazon_q`
      - `sub_consumption_duo_premium`
      - `sub_consumption_storage`
    - The ticket form is `L&R`
    - The ticket form is `Support Ops`
    - The ticket form is `Emergencies`
    - The ticket form is `Support Internal Request`
- For Zendesk US Government:
  - The organization is not `GitLab`
  - The ticket contains none of the following tags:
    - `spam_ticket`
    - `free_customer`
    - `com_embargo`
    - `csat-survey-sent`
    - `needs-org-triggered`

### When are they sent out

We currently send out CES surveys on tickets that have been in the solved state for 24 hours (without status change).

### Components

#### CES Processor

This takes information sent by Workato and processes it. It then checks the information against the ticket itself to determine if the request is valid. It currently checks:

- The ticket ID is present
- The ticket itself exists
- The ticket is not closed
- We have actually sent out a CES survey to them
- The submitter is the same person as the ticket requester

If any of the above fails, it will output a reason for failure and silently exit.

If no validation checks have failed, it will then do the following:

- Add a satisfaction rating (and comment if present) to the ticket
- Add the CES score to the ticket

The location of the project is [here](https://gitlab.com/gitlab-support-readiness/processors/ces-processor)

#### CES Survey Form

This is the actual survey form sent to customers. The exact link received depends on the Zendesk instance the link was sent from:

- [Zendesk Global](https://support.gitlab.io/ces-survey/global-en.html)
- [Zendesk Global sandbox](https://support.gitlab.io/ces-survey/global-sb-en.html)
- [Zendesk US Government](https://support.gitlab.io/ces-survey/us-government.html)
- [Zendesk US Government sandbox](https://support.gitlab.io/ces-survey/us-government-sb.html)

Submissions from the form are sent to Workato.

The location of the source project is [here](https://gitlab.com/gitlab-support-readiness/forms/ces-survey). This is mirrored to [here](https://gitlab.com/support/ces-survey).

#### Zendesk Automations

These are used to send out the actual CES survey.

#### Zendesk Ticket Fields

These are used to store the CES survey numerical score.

#### Zendesk Triggers

These are used to create feedback issues for Support.

#### Workato

This is used to receive submissions from the CES Survey and send them to the CES Processor.

## Satisfaction Surveys

{{% alert title="Note" color="primary" %}}

- Note that as of 2025-05-01, we are no longer using Zendesk satisfaction surveys. We have switched to using [CES Surveys](#ces-surveys).

{{% /alert %}}

### What is the Zendesk satisfaction survey?

As per [Zendesk](https://support.zendesk.com/hc/en-us/articles/4408886194202-Customizing-your-customer-satisfaction-survey):

> One of Zendesk Support’s most popular features is our built-in customer satisfaction survey. Customer satisfaction allows you to track how well your agents and customer service organization as a whole are performing on a ticket by ticket basis. Because of our simplified approach, on average our customers see a roughly 21% response rate - which is fantastic! Zendesk Support provides some great defaults for the survey, but we get a lot of questions about how to further customize the customer satisfaction experience.

## Administrator tasks

### Updating the processor

Making the changes would be done by modifying the files within [the project](https://gitlab.com/gitlab-support-readiness/processors/ces-processor). You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

### Updating the forms

Making the changes would be done by modifying the files within [the project](https://gitlab.com/gitlab-support-readiness/forms/ces-survey). You should also do this in a way that creates a MR. Said MR should always be peer reviewed before merging (the MR should enforce this).

Once the MR is merged, they will then be used to populate the form.
