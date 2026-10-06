---
title: Working on tickets
category: Handling tickets
description: How to find, select, and begin work on support tickets
---

## Introduction

This page helps guide Support Engineers (SEs) to [find](#zendesk-views), [select](#selecting-new-tickets), and [work](#first-response-and-ongoing-communication) support tickets.

## Zendesk views

The default views in Zendesk for Support Engineers (SEs).

| Name | Purpose |
|------|---------|
| [My Assigned Tickets](https://gitlab.zendesk.com/agent/filters/360062369834) | Tickets assigned to you that are not `Solved` or `Closed`. |
| The Global Support Ticket View| Shows all unassigned tickets, sorted by ticket weight. This is the primary view for all support engineers to work from. |
| Assigned Support Engineer Tickets | Tickets from organizations that have an Assigned Support Engineer (ASE). |
| L&R | Licensing & Renewals tickets |
| All FRT and Emergencies | `New` tickets in the FRT stage.|
| All NRT | Non-new tickets in the NRT stage.|

## Selecting new tickets

Employ the following workflows for:

 Choosing Tickets:

- Work from the top of `The Global Support Ticket View`. Tickets are sorted by `Ticket Weight` to prioritize the highest-impact tickets first. Tickets receive additional weight as they progress through their FRT and NRT life-cycles, ensuring that soon to breach tickets do not remain low in the view.  When everyone aims to start from the top of the queue, it supports our ability to achieve our SLAs.
- Take and keep assignment of tickets that have your region as the preferred one.
  For tickets with other preferred regions, work them by putting out a quality
  first response. Then follow the guidelines for
  [rehoming tickets](/handbook/support/workflows/ticket-transfers/#ticket-rehome-transfer-to-the-preferred-region) to transfer
  them to the customers' stated preferred region. (NOTE: APAC may also maintain
  assignment of low priority tickets with a preferred region of AMER.)
- Both FRT and NRT tickets that do not have an assignee are presented in this view.
  Consider assigning tickets that have a status of `open` or `pending` and that
  have your region as the preferred one. These all need owners within the preferred region on the same day they are rehomed from other regions. Refer to the [receiving a ticket rehome](/handbook/support/workflows/ticket-transfers/#receiving-a-ticket-rehome) section of this page for guidelines on working these tickets.
- For handover tickets prioritize open tickets first then pending tickets.
- Ensure tickets rehomed from other regions get assigned within the same day.
- Ensure customers' choice of preferred region is honored or questioned within 8 business hours of ticket creation.
- Tickets should be taken and self-assigned as they come in by one of the team members responsible for that time segment, regardless of region specified. The first response should happen
  with the goal of targeting 100% FRT SLA achievement during your coverage hours, with a stretch goal of greater than 70% of tickets replied to within half of the FRT SLA clock.
- The customer contact region should only be considered at the end of the assignee's day, at which point the assignee decides, based on customer input, if the ticket should be handed over or retained.

## Assigning Tickets

- Assign tickets to yourself using the "Take It" button and update status to `Open` or `Pending`.
- Please note that the SLA clock continues to run until you've sent a public response to the user.
- Keep in mind that the status will change from New `n`, to Open `o`, as soon as you assign the ticket. It won't be obvious that it is still at FRT stage.
- Manually CC yourself on the ticket so that if it gets reassigned, you can still track it.
- Hand over tickets to other regions within 2 hours of each region's start of day.

## Managing ticket load

- Regularly review your `open`, `pending`, and `on-hold` tickets under
      [My Assigned Tickets](https://gitlab.zendesk.com/agent/filters/360062369834)
      to maintain a balanced workload.
- Aim for a manageable number of tickets, adjusting based on daily demands
     and personal capacity.
- Aim to adhere to the support ticket SLA/SLOs:
  - Urgent FRT 30m, NRT 4h
  - High FRT 4h, NRT 4h
  - Normal FRT 8h, NRT 24h
  - Low FRT 24h, NRT 24h

## Managing Zendesk attachments

When working with Zendesk tickets, you may need to download attachments to your laptop. While [our laptops have full disk encryption](/handbook/eta/corporate-it/end-user-services/laptop-management/laptop-security/encryption), we need to be careful with downloaded attachments as they can contain [RED data (customer data)](/handbook/security/policies_and_standards/data-classification-standard/#red)):

1. Keep downloads in a dedicated folder for easier management, for example with [Zendesk Download Router](https://gitlab.com/gitlab-com/support/toolbox/zd-dl-router)
1. Automate the deletion of downloaded attachments as soon as possible after resolving the ticket
1. Take extra care with sensitive information (tokens, passwords, credentials). If needed, [remove the sensitive information](../providing_excellent_customer_service.md#removing-information-from-tickets) directly from the ticket as well

The [Zendesk Download Router](https://gitlab.com/gitlab-com/support/toolbox/zd-dl-router) web browser extension can be used
to download attachments from Zendesk. By default, the extension will download all Zendesk attachments to `~/Downloads/zd-%TICKET_ID%`.
Note that this assumes your browser is using its default download location - you may need to adjust paths if you've customized your browser's download settings.

If you are using the Zendesk Download Router, you can set up automatic cleanup using `crontab`:

1. Open your crontab for editing:

   ```shell
   crontab -e
   ```

1. Add the following line (adjust the path if needed):

   ```shell
   # Automatically delete any Zendesk attachments older than 30 days
   0 12 * * * find ~/Downloads -type d -name "zd-*" -mtime +30 -exec rm -rf {} +
   ```

## First response and ongoing communication

When starting work on a ticket, prioritize these steps to effectively address
the customer's needs and streamline the resolution process:

1. **Start Working Immediately:** Begin troubleshooting or send clarification responses immediately upon taking a ticket.
2. **Confirm Understanding:** Begin by confirming in the first response your
   understanding of the customer's situation, needs, and the problem or question
   they need resolved. If unsure, request clarification or propose a brief
   meeting to discuss details.
3. **Review Past Interactions:** Check the customer's recent tickets for related
   issues or useful background information. Confirm any relevant environmental
   details with the customer and review any organizational notes in Zendesk that
   might dictate specific actions or communication methods.
4. **Adjust Priorities:** If the ticket's priority doesn't align with our
   [Definitions of Support Impact](https://about.gitlab.com/support/#gitlab-support-service-levels),
   discuss and adjust the priority with the customer using the
   `General::Changed priority` macro.
5. **Prepare for Emergencies:** If the ticket could escalate to an emergency,
   alert the on-call engineer(s).
6. **Manage Time Effectively:** If an extensive response is required or the SLA
   is near breaching, send an initial brief response. Outline the actions you
   will take and when the customer can expect an update. Adjust timelines as
   necessary based on customer feedback.
7. **Use Tools:** Set the ticket to Open and use 'Due Date' and 'Reminder' apps
   to keep track.

By following these steps, you ensure a structured approach to ticket handling that can save time and enhance customer satisfaction.

## Responsiveness

- Contact customers promptly when tickets are close to breaching.
- When tickets are awaiting updates from other departments, provide updates to customers at least weekly.
- Frequency of updates should be agreed upon with the customer.
- Calls are not the exception, and are used not only for troubleshooting and data collection, but also for clarification, guidance, and providing comfort.

## Elevating Tickets

Elevate tickets (seeking assistance from a Peer/Senior/Pod/Development – Request for help) based on agreed criteria:

- Time constraints
- Skill level requirements
- Meeting customer expectations

By following these steps, you ensure a structured approach to ticket handling that can save time and enhance customer satisfaction.

## Working with Internal Requests

Support tickets submitted by GitLab team members will appear in Zendesk under the GitLab organization with the Brand "GitLab - Internal".
These tickets should be treated like any other ticket. Provide public responses.

**Important:** If you don't provide a public response, the SLA clock will continue to run and may breach.

### Handling the Zendesk Warning

When you attempt to create your first public response on an internal request ticket, Zendesk will display this warning:

> This ticket has no public comments, so the requester can't see it. If you add a public comment, they'll start to be notified (but internal notes will stay private). Do you want to add a public comment?

Click `OK` to proceed with your public response. This warning can be safely ignored.

## Closure Process

When closing a ticket:

- Attempt to gain customer agreement before closing tickets.
- Provide a **closure summary** outlining steps taken to resolve the ticket.
- Apply appropriate closure codes when solving tickets.
- Populate the [Product Category](/handbook/support/workflows/product_category_field.md) field
- Link tickets to knowledge articles or documentation that helped with resolution.
- Link tickets to RFH issues, bug issues or feature requests by adding the associated issue URL to the `GitLab Issues` text field.
- Create or update knowledge articles based on ticket resolutions when appropriate.
- Add an email signature to final emails encouraging customers to complete satisfaction surveys, such as: "Your feedback is important to us. Please take a moment to complete the satisfaction survey you'll receive after this ticket is closed."

## Contacting the Customer Success or Account team

Support can connect with the Customer Success and/or Account team for reasons such as discussing architecture, Professional
Services, or support collaboration. If escalation is required, follow the
designated workflow. If no CSM is available, contact the AM, identified in
Zendesk as `Account Owner`. During FY26Q1 (Feb25-Apr25), APAC are participating in a pilot to reach the CSE (Customer Success engineer) for customers that are `TAM Scale` and don't have a dedicated CSM.  See below if you are in APAC. To involve a CSM or AM, use the following methods:

1. Zendesk: Add the CSM/AM as a CC on the ticket, inform the customer, and add
   an internal note for context.
2. Slack: Notify the CSM/AM with one of the following:
   - Mention them in an existing ticket discussion.
   - Start a new thread in the customer's channel
     (#a_customerName-internal).
   - Post a message in a relevant support channel (`#support_leadership`,
     `#support_gitlab-com`, or `#support-self_managed`).

### Helping with a ticket that has an Assigned Support Engineer

Some customers have an Assigned Support Engineer (ASE) who will own their
tickets. This will be apparent from the org note in the ticket. For such
customers, see [the ASE workflow](../enhanced-support-offerings/offering-assigned-support-engineer/working-with-ases/global-support-and-ases.md).

### Weekend focus for Shift engineers

Be familiar with the responsibilities of being on-call for High Priority tickets for GitLab's [Success Signature](https://gitlab.zendesk.com/agent/search/1?copy&type=organization&q=sub_ss_enterprise%3Atrue) and [Success Advanced](https://gitlab.zendesk.com/agent/search/1?copy&type=organization&q=sub_ss_growth%3Atrue) customers.

Over the weekend, Shift engineers will focus on *meeting First Response Times (FRT) for high-priority tickets for Signature and Advanced Customers*.

List of responsibilities to cover during your shift (Hours to cover is the same as the CEOC hours):

1. Meet FRT for high priority Signature and Advanced tickets
1. Assist the On-call Engineer (CEOC) with their workload
1. Meet NRT for Signature and Advanced tickets that are at risk of breaching
1. Document common issues and solutions to build knowledge base
1. Work on Next Response Times (NRT) for existing tickets adding internal comments (no public replies allowed)

## FAQ

### How many new tickets should I pick up each week?

Each week, every Support Engineer should aim at least to meet, and preferably to exceed, [the appropriate baseline](/handbook/support/support-engineer-responsibilities/#ticket-baseline)
from the following list for the number of first responses:

| Ticket type   | Assigned tickets goal   |
| ------------- | ---------- |
| Self-managed  | 7 tickets  |
| SaaS          | 7 tickets  |
| SaaS Accounts | 28 tickets  |
| L&R           | 14 tickets |

These goals represent the average number of new tickets you should provide a first substantive response to each week for the ticket types that apply to your role. The intent is to ensure a fair distribution of tickets across the team, while still allowing for variation week‑to‑week based on workload, escalations, and project work. Intermediate and senior engineers, excluding those in core L&R and Associate SE roles, are expected to develop as well‑rounded contributors by consistently working on a balanced mix of Self‑managed, SaaS, and Dedicated tickets.
These assigned ticket baselines are one of the two primary ticket‑related baselines for Support Engineers. The second is Median Time to Resolve (TTR/MTTR) with ticket‑type specific targets:

- Median TTR – Self‑Managed: target 141 hours
- Median TTR – SaaS: target 76 hours
- Median TTR – SaaS Account: target 25 hours
- Median TTR – L&R: target 7 hours

These expectations are informed by overall ticket volume, team size, and an average PTO rate of 15%. We continuously monitor ticket volume, staffing levels, and performance indicators to ensure these guidelines remain accurate and appropriate. For further details, including how these baselines are used in performance indicators and dashboards, please review the Support Engineer Performance Indicators FY26 work item, the [Support Engineer Performance Indicators FY26 issue](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/6635#note_2498022715) and the [Median TTR dashboard](https://gitlab.zendesk.com/explore/studio#/dashboards/5CB98A840DDD3FFF1A274944BCC070229D377C1D23901AF90988FBD0CA79C706).

**Please Note:** EMEA Support Engineers should follow the [Shift Chair](/handbook/support/workflows/team/shift_chair/) workflow when selecting tickets.

#### What if I can't meet baseline?

There will be times when you may be leading an escalation, working through
challenging tickets, or focusing on non-ticket work, and you cannot take on new
ticket assignment. This is okay! The key is to make sure you have coordinated
with your regional team and Manager so they are aware of the risks to our team.

### What can I do when I'm stuck and I really need help?

Follow the [how to get help](/handbook/support/workflows/how-to-get-help/)
workflow for guidance.

### I'm going to be absent, what do I do with my assigned tickets?

Please see the [Support Team Member Time Off](/handbook/support/support-time-off/)
page for guidance on taking time off.

### What if the customer is absent and wants to keep the ticket open until they return?

In this scenario:

1. Acknowledge the customer's request and inform them of your plan.
1. Set the ticket status to `on-hold`.
1. Change the ticket type to **Task**.
1. Set a reminder for yourself to check in with the customer 1-2 days after
   their planned return date.

Because of the [behavior of `On-Hold` tickets](/handbook/support/workflows/zendesk-ticket-basics/#behavior-of-on-hold-tickets)
the ticket will remain in the `on-hold` state until the customer returns. This
is useful if the customer will be unavailable for 1-2 weeks. If a customer will
be unavailable for a longer period of time, consider asking them to handover the
ticket to a colleague, or open a new ticket upon their return.

### May I reassign a ticket to someone else?

There are some situations in which it is appropriate to reassign a ticket. A few
common situations are listed below, but others may arise. If you encounter a
scenario where you need to reassign a ticket that isn't detailed in the
handbook, please discuss with your manager, and then add it below!

#### If you'll be out of office

If you're out of office, either planned or unplanned, follow the guidance in
[Support Team Member Time Off](/handbook/support/support-time-off/).

#### If you need an expert

If you've determined that specific expertise outside your own is required to
resolve the ticket, pair with an expert so that you can get the ticket resolved
and learn in the process. If that person determines that they need to take the
lead due to the advanced or complex nature of the problem, then:

1. Send a message to the customer informing them:
   - You've asked another support engineer with relevant expertise to take the
     ticket
   - You've reviewed the ticket with that engineer
   - You'll stay involved in order to help in any way you can
1. Assign the ticket to the expert

#### If you have too many tickets

If you've become overloaded with tickets, you may look to find one or more other
SEs to take some of your tickets. Be sure you discuss each ticket before
reassigning it to gain agreement and so that the other support engineers don't
have to start from scratch.

Once you've found a new assignee:

1. Add an internal note summarizing the ticket and noting the reassignment
1. Send a public reply to the customer informing them of the reassignment
1. Reassign to the new engineer

### What if a customer has confirmed a ticket can be closed but the ticket has no assignee?

While we should ensure that all tickets always have an assignee from FRT to
close, there are some scenarios where a ticket is ready to be closed but has no
assignee. For example, a customer may open a ticket and inform us that they have
resolved the issue before we send an FRT. In these scenarios:

1. Inform the customer that you are changing the ticket status to solved
1. Assign the ticket
   - If a solution was provided, assign to the engineer who provided the
     solution
   - If the issue was not solved as the result of a direct suggestion, assign it
     to an engineer who has significantly contributed to the ticket throughout
     its life cycle
   - If the customer solved the ticket before we could respond, take assignment
     of the ticket yourself. After all, you're doing the work of acknowledging
     the customer's update, and solving the ticket!
1. Mark the ticket as `solved`

### How many issues or incidents should I handle in a single support ticket?

As detailed in [Support General Policies](https://about.gitlab.com/support/general-policies/#we-handle-each-incident-within-a-single-support-ticket)
it is GitLab's policy to handle each unique issue or incident within a single
support ticket.

### How can I open a new ticket on behalf of a customer?

As detailed in the [Support General Policies](https://about.gitlab.com/support/general-policies/#we-handle-each-incident-within-a-single-support-ticket)
it is GitLab policy to handle each individual incident, problem or issue within
a single support ticket. If a situation arises where you need to open a new
ticket on behalf of a customer, you **must** use the [Create new ticket plugin](/handbook/eta/css/zendesk/apps/global#zendesk-super-app)
within the Zendesk Super App
to ensure proper routing and SLA assignment:

1. Within a ticket, navigate to the Zendesk Super App and select the Create new
   ticket plugin.
1. Select the appropriate form type. This will most likely match the request
   type of the originating ticket.
1. Enter the customer's details like subject, problem description and other
   relevant information. Use the customer's existing Zendesk Ticket to obtain
   the necessary customer information to complete the form.
1. Submit the ticket using the `Create Ticket` button.

Once the new ticket has been submitted, the app will provide you with the
corresponding ticket ID. You can click the ticket ID to directly navigate
to the newly created ticket.

If you plan to immediately start working the ticket, please assign the ticket to
yourself.

### Can I use output from an LLM in ticket replies?

While you can use a tool like GitLab Duo to help when researching and when writing a reply to a customer, there are a few important things to keep in mind:

- Verify the information provided by the LLM to ensure that it is accurate using the docs and the source code or by checking with a human [subject matter expert](https://gitlab-com.gitlab.io/support/team-pages/skills-by-subject.html)
  - You should pay special attention to making sure whether things like environment variables, configuration options, UI settings and documentation URLs actually exist
  - You should double check that any bugs or feature availability identified aligns with the GitLab version/edition/tier/install method that the customer is using
  - You should make sure that you can understand, can explain and have tested any commands or code snippets generated by an LLM and shared with a customer
  - You should not send text from an LLM to a customer verbatim without ***at least*** verifying it for technical accuracy first
- Be mindful of GitLab's [Data Classification Standard](/handbook/security/policies_and_standards/data-classification-standard/) and the [kind of input](https://internal.gitlab.com/handbook/legal-and-corporate-affairs/ai-tool-usage-guidelines/#input) you have in mind when selecting a tool
  - When working with customer data, always consider whether you need to anonymize information before sharing with any LLM
  - Take special care with customer screenshots, logs, and configuration files which may contain sensitive or identifying information
- LLMs can be useful for refining and improving a response you have drafted to a customer (such as checking for clarity, completeness, and tone), however responsibility for the final response always lies with the Support Engineer, not the tool.

Read the [General Purpose AI Tool Usage Guidelines](https://internal.gitlab.com/handbook/legal-and-corporate-affairs/ai-tool-usage-guidelines/) for additional guidance.
