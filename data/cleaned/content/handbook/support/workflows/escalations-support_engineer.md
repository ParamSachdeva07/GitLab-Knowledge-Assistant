---
title: A Support Engineer guide to account escalations
description: Guidance to Support Engineers for how to handle account escalations
---

## Overview

This page guides Support Engineers on the Lead Support Engineer role for [Customer Account Escalations](/handbook/customer-experience/csm/escalations/).

An Account Escalation may be initiated by Support Engineering (Support Managers or Engineers) through [converting a customer emergency into an escalation](/handbook/support/workflows/emergency-to-escalation-process), or as the result of a [STAR](/handbook/support/internal-support/support-ticket-attention-requests). The Customer Success Team may also [initiate an Account Escalation](/handbook/customer-experience/csm/escalations/#initiating-managing-and-closing-an-escalation), engaging the Support team for assistance, depending on the escalation type (not all Account Escalations require Support engagement) and [severity](/handbook/customer-experience/csm/escalations/#definitions-of-severity-levels).

### Account Escalation Team

Each escalation will have an [Escalation DRI](/handbook/customer-experience/csm/escalations/#escalation-dri) leading a team of people contributing toward the successful outcome of the escalation. The team will consist of some (at a minimum the Escalation DRI, Lead Support Engineer, and Support Manager DRI) or all of the following roles:

- Escalation DRI (CSM, AE or CSE manager)
- Lead Support Engineer
- Support Manager DRI for the support involvement
- Other CSM Leaders or Account Managers involved
- Product Managers
- Development Engineers
- Secondary or Backup Support Engineer

## Responsibilities of the Lead Support Engineer

The Lead Support Engineer has the following goals:

### Document the system architecture, recent changes, and current issues

During a customer emergency, it can be difficult to keep track of what has been changed and what has already been investigated. As a Customer Account Escalation can last for days or weeks, it is very important to document details of the system architecture, a timeline of events, and any mitigations performed. A Google Document, Field Notes issue, or Request for Help issue may be appropriate.

- Maintain a high level summary for Account Managers and Executives who may be involved.
- Also keep detailed notes on the technical investigation and mitigation efforts so that other engineers can more easily assist in the troubleshooting.

### Identify the customer's desired end goal and criteria for reaching that goal

Build a problem statement that explains the core issue and ensure you are working with the customer towards resolving the problem statement. A customer may raise many different issues and concerns during an escalation, and these concerns will need to be triaged to determine if they will directly impact the resolution of the problem statement or if they are a side issue. While there can be exceptions to ensure customer satisfaction, it is best to remain focused on the key issue driving the escalation and engage with other issues in a new support ticket.

### Determine what technical resources may be needed to assist in resolution

When the core issue is identified, do not hesitate to request assistance from other Support Engineers. An additional set of eyes is always helpful, and getting assistance with the technical investigation will help you focus on guiding the overall escalation. Very often a secondary or backup engineer will be an important contributor to the escalation.

Reach out to the Support Manager DRI to engage the correct resources to assist according to severity, priority, and expertise.

If the scope of the escalation requires the involvement of a second engineer, work with the Support Manager DRI to identify an appropriate resource, define how a Secondary Engineer will assist, and ensure that the Secondary Engineer's existing work is reassigned.

### Coordinate communication with the Support Manager DRI, CSM Leader, and Account Manager

- Determine the best method of providing updates to the customer. This may be regular sync calls, updates in the support ticket, or in an external Slack channel. Consider the [severity level](/handbook/customer-experience/csm/escalations/#definitions-of-severity-levels) when communicating with the customer.
- Determine the level of technical detail to share with the customer. They may want to engage in log analysis together, or they may want to receive only your findings and recommendations.
- Publish internal updates in the escalation Slack channel so that internal stakeholders have up to date status information. There may need to be an update multiple times a day. Include updates from the investigation, the overall progress towards identifying and resolving the root cause, and provide the next steps to be taken by GitLab and the customer.
- The current status also needs to be updated in the escalation document which acts as the single source of truth for the escalation.

### Provide a summary and root cause analysis when finishing the escalation

An escalated customer will generally expect a root cause analysis that can be delivered to their executive team.

- Provide a high level summary of the timeline, investigation, and resolution.
- The [Five Whys technique](https://en.wikipedia.org/wiki/Five_whys) can be helpful in delivering a compelling summary of the issue.
- For a complex issue, an appendix explaining the technical details can be used to provide a more complete explanation.
- Discuss whether a post-escalation retro may be useful with the Support Manager DRI.

### Schedule PTO

Escalations can take significant time and energy. After an escalation has been successfully closed out, consider taking some time off to rest and recover.

## Risk vs. Uncertainty

Throughout your time working on an account escalation, seek to turn uncertainty into manageable risks. For example,

- If a customer is performing a technical change, rather than pointing a customer to documentation and letting the on-call be paged if something goes wrong, proactively engage in forming the plan and sit with the customer as they're going through the operation.
- If a customer is monitoring a situation after a change, rather than letting the on-call get paged if something goes wrong, determine a cadence of check-ins where you and the customer will monitor areas of risk and assess the situation.
- If a customer is experiencing an intermittent problem, rather than letting the on-call get paged if the situation occurs, set up a specific mode of communication to a set of briefed stakeholders who know what diagnostic data to capture.

In short: the customer paging the on-call emergency engineer can happen if an unexpected incident occurs, but if you are relying often on this, you're probably not being proactive enough.

## Communication Tips

These are not unique to account escalations but they may serve you particularly well during this time.

- Say what and when.
  - **Don't**: I'll send you a follow-up message.
  - **Do**: By 8p UTC today, I will send a follow-up message via :ticket: 012345.
    - If there's any concern that you might not be able to get that message out by 8p UTC, instead say that you'll have it by the end of the day and include your time zone. This leaves a small degree of uncertainty but is offered with the thought that it's better to meet a fuzzy deadline than to miss a specific one.
- Communicate.
  - Be active in the escalation channel.
  - It should be clear what Support is doing, when Support is blocked, what Support needs in order to proceed, etc.
  - Consider updating your Slack status to indicate that you are :bulb: focused on the escalated customer.
- Be clear.
  - Say what you are doing and what you are not doing. Don't leave anything for people to assume.
  - Ask questions or clarify what you think you heard if something is unclear.
  - Say what you **can't** do.
    - I don't know **\_**.
    - I have a conflict at **\_**.
    - I am blocked on **\_**.
- Collaborate.
  - You are awesome and amazing. You can't do it _all_. Get help for your tickets.
  - Ask questions. If something is not clear to you...it's not clear. A large portion of our jobs is to take in large amounts of technical information, understand it, prioritize it, rule out what's irrelevant and communicate it to the customer. There are a lot of details and it's better to spend a few moments clarifying something than to introduce further confusion to an already heightened customer.
- Be proactive.
  - It's better to say "this might slip" than to say "this slipped".
- Bias for action.
- It's hard. Lean on the values.
