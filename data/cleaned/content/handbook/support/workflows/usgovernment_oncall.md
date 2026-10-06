---
title: How to Perform U.S. Government On-Call Duties
category: On-call
description: "Describes the role and responsibilities for U.S. Government On-Call rotation in Support Engineering"
---

## Introduction

Support Engineers in the U.S. Government Emergencies rotation coordinate operational emergencies from GitLab customers.

The U.S. Government Emergencies rotation is one of the rotations that make up [GitLab Support On-call](/handbook/support/on-call/).

This page is a high-level view of various workflows for being in the U.S. Government On-Call rotation, more detailed guides for working emergency calls, etc, can be found in the [PATRIOT project](https://gitlab.com/gitlab-com/support/us-government/patriot).

## Things to Know

### U.S. Government On-call

All customers that have purchased U.S. Government support receive "12x5 Emergency Support". Customers may purchase a "24x7 Emergency Support" add-on.

"12x5" Customers can page for [severity one](https://about.gitlab.com/support) issues on their Production instances Monday through Friday between the hours of 0500 and 1700 Pacific Time.

"24x7" customers can page for severity one or two issues on their Production instances at any time.

The current on-call schedule can be viewed in [PagerDuty](https://gitlab.pagerduty.com/schedules#P89ZYHZ)(Internal Link). The schedule is currently split into two 12 hour shifts: 5a-5p / 5p-5a (Pacific):

- Day shift: 05:00 - 17:00 PT
- Overnight: 17:00 - 05:00 PT

Day shift engineers are scheduled for On-Call shifts on weekends and holidays. Weekday emergencies are handled with the Slack Bot workflow. Overnight engineers are scheduled every day of the week, typically in week-long blocks running Friday through Thursday.

Customers are permitted to submit emergencies by email or the emergency form in the U.S. Government support portal.

#### On-call Shift Coverage in U.S. Government

In the event that a Support Engineer needs coverage for a scheduled On-call shift, open an issue in Support Team Meta using the `us-gov-oncall-coverage` template, and share the link with the team in Slack.

#### Emergencies outside working hours

If a 12x5 customer submits an emergency case outside the [working hours of Government Support](https://about.gitlab.com/support/us-government-support/#hours-of-operation) the following will occur:

- A slack notification will trigger in the #spt_us-government channel alerting the team to an off hours emergency and indicating follow-up is needed at the start of business hours
- The `Off hours emergency request` trigger will inform the ticket submitter that it is after hours and that U.S. Government support will follow up at the next start of business hours.

##### Responding to after hours emergencies

Team members who are working after the 12x5 hours may opt to provide support for customers who are having a production emergency at the engineer's own discretion. When addressing these it is important to ensure the following is clear with the customer:

- They are not entitled to 24x7 support based on their subscription
- Emergency support is being provided as a one off exception based on the engineer's availability and future after hours support is not guaranteed

The responding engineer should also add their manager as a follower and indicate in an internal note that after hours support is being provided. This will help ensure the appropriate follow-up occurs with the customer's account team.

### PagerDuty

We use PagerDuty to keep track of emergencies raised by GitLab customers. For any customer emergency, there will be a notification in `#support_us-government`.

### PagerDuty Status

- **Triggered** - "A customer has requested the attention of the on-call engineer"
- **Acknowledged** - "I have seen the page and am reviewing the ticket"
- **Resolved** - "I've engaged with the customer by sending a reply to the emergency ticket"

**Note:** "Resolved" in PagerDuty does not mean the underlying issue has been resolved.

## Getting Alerted of an Emergency Case

There are two ways of being alerted to an Emergency that _may be_ your responsibility

1. **PagerDuty notifications**

These come as [configured](#configuring-your-pagerduty) when you are the Engineer On-Call

1. **The Slack Bot**

These come during dayshift hours during the week and will ping all _available_ engineers to alert to the emergency case.

![U.S. Gov Slack Bot Emergency Example](/images/support/usgov_pd_bot_alert.png)

### Examples of flow

These examples will address the flow from the customer filing the emergency to an engineer responding in the ticket.  How to triage and work the case will be addressed elsewhere.

#### Day Shift, bot flow

When an emergency is filed during business hours on a weekday, two messages will appear in the [#spt_us-government](https://gitlab.enterprise.slack.com/archives/C03RTN3JEJ2) channel. First a PagerDuty alert, then a message from the 'Support Readiness Bot' tagging all available engineers, alerting to the emergency.
Once pinged, the available engineers review the ticket, and `acknowledge` the PagerDuty alert. (Unacknowledged PagerDuty Alerts will escalate).
When one or two engineers have agreed to work the ticket, reply to the ticket and `resolve` the PagerDuty alert.

#### Day Shift Engineer On-call flow

If an emergency is filed while you are the On-Call Engineer, you will get a PagerDuty notification according to your [configuration](#configuring-your-pagerduty). Once you have received the notification, `acknowledge` the page--either in Slack or in the PagerDuty app--to forestall the escalation. Then, begin reviewing the ticket. Once you have responded to the customer, `resolve` the PagerDuty alert.

#### Night Shift flow

Nightshift engineers go through a rotation of week long On-Call shifts. For an individual rotation, the first shift begins on **Friday** night (5:00 PM Pacific Time), and ends on **Saturday** morning (5:00 AM Pacific Time). The remaining shifts follow this same schedule until the rotation ends on **Friday** morning (5:00 AM Pacific Time). If an emergency is filed while you are the On-Call Engineer, you will get a PagerDuty notification according to your [configuration](#configuring-your-pagerduty). Once you have received the notification, `acknowledge` the page--either in Slack or in the PagerDuty app--to forestall the escalation. Then, begin reviewing the ticket. Once you have responded to the customer, `resolve` the PagerDuty alert.

### If no one Acknowledges an alert

If a U.S. Government Customer emergency is filed, PagerDuty will notify the On-Call Engineer, the Bot, and the Shadow--if there is one. If the alert is not `acknowledged` after 15 minutes, a manager will be paged. If still not `acknowledged` after 15 more minutes, Sr. Manager will be paged. 

## Configuring your PagerDuty

Individual PagerDuty notification settings are configurable, under `Notification Rules` in your profile. You should set these to ensure you receive / hear notifications and respond accordingly. You can configure SMS Messages, Phone Calls, Emails, and PagerDuty App alerts at various minute intervals. 

## Post-resolution ticket handling

Post-resolution ticket handling is outside the scope of this on-call page. After the emergency condition has been addressed, follow the post-resolution ticket workflow in [Working with U.S. Government Support tickets](/handbook/support/workflows/usgovernment_tickets/#emergency-ticket-handling).

That section documents when to merge an emergency ticket into an existing non-emergency ticket, when to solve or close the emergency ticket, and the rare exception where the ticket continues as a non-emergency with a manual weight adjustment.
