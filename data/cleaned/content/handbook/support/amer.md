---
title: Support Team AMER
description: Support Team AMER home page
---

## Welcome to Support Team AMER's Handbook page

This page documents items specific to the AMER Support Team which we have not yet
found a home for in the wider Support Team Handbook.

The intent is to enable AMER Support team members to contribute to results for
AMER-specific initiatives, policies, processes and workflows by prioritizing:

1. Transparency, through being [handbook first](/handbook/about/handbook-usage/#why-handbook-first)
   and providing a single source of truth for AMER-specific information.
1. Iteration, through providing a safe space where AMER Support team members can
   introduce or update AMER-specific policies, workflows and processes without
   creating confusion and uncertainty for the wider Support Team.

Where appropriate, we should always look to move content from this page into
other pages of the wider Support Team Handbook.

## General policies

### AMER Support Timezone-Aligned Ticket Distribution

#### Overview

AMER Support ticket work is organized into three distinct, timezone-aligned windows.
This model ensures new ticket assignments match your preferred working hours,
reduces overhead associated with constant queue monitoring, and improves
assignment predictability.

Engineers are expected to take new ticket assignments only during your
designated shift window. Outside of this time you are welcome to continue
collaborating with ticket work but are not expected to take tickets.

#### Shift Schedule

| Shift  | Local Time Window | Team Size  | Duration | Note |
| :---- | ----- | :---: | :---: | ----- |
| East  | 8:00 AM–12:00 PM ET | \~20 | 4 h |  |
| Central  | 11:00 AM–2:00 PM CT | \~11 | 3 h | Designed to flex support for East or West shifts as needed |
| West  | 12:00 PM–4:00 PM PT | \~11  | 4 h |  |

#### How It Works

Ticket assignment during a shift is a collaborative process managed by the rotating shift chair. Usually a manager but engineers are welcome to participate.

1. At the start of the window, the shift chair posts the current ticket queue to the shift’s Slack channel.
2. Engineers pull tickets via self-selection.
3. The shift chair assigns any remaining tickets after engineer self-selection is complete.

{{< note >}}
West Shift Engineers, if your workday ends at 4 p.m. PT, prioritize picking up tickets at the start of the West window (12 p.m. PT).
{{< /note >}}

##### Engineer Expectations

During your assigned shift window, you adhere to the following expectations:

* **Slack Presence:** Be active and responsive in your shift’s slack channel
* **Actively Collaborate** on getting tickets assigned.
* **Proactively communicate** if you are stepping out of your workspace.
* **Ensure no tickets go below the 1-hour FRT SLA** after your shift ends.

##### Shift Chair Responsibilities

The shift chair runs the distribution window by completing the following tasks:

* Post the ticket queue to the shift channel at the start of each window.
* Run the Shift [Ticket Priority List](https://gitlab.com/gitlab-com/support/toolbox/shift-ticket-priority-list) script.
* Highlight any tickets that are about to breach SLA

##### Shift Assignments

Shifts are assigned based on your preferred working hours. To request a change to your assigned shift, reach out to your manager.

These channels are used for queue posting and active collaboration during the designated shift window:

* [`#spt_amer_shift_east`](https://gitlab.enterprise.slack.com/archives/C0AN614HSG3)
* [`#spt_amer_shift_central`](https://gitlab.enterprise.slack.com/archives/C0AN619A3V1)
* [`#spt_amer_shift_west`](https://gitlab.enterprise.slack.com/archives/C0ANR9X6TLZ)

##### Success Metrics

The following metrics are tracked to evaluate the effectiveness of the timezone-aligned ticket distribution model:

* FRT SLA attainment % is maintained at or above target.
* Ticket distribution is even across all AMER support engineers.
* Engineers have dedicated time for backlog and project work.

### AMER Holiday Coverage Targets

The table below sets the minimum coverage we aim to maintain on upcoming
holidays where there is a risk of too many people being off at once.
Targets are based on historical ticket volume for each holiday. Use it, together
with the [Support OOO - AMER calendar](https://calendar.google.com/calendar/embed?src=c_9166d2302886c4ae23f34099eeb4015e2d520e1dd4029711becd8370be996513%40group.calendar.google.com),
as a quick self-check before requesting a holiday off.

#### Coverage targets

"Target % working" is the minimum percentage of the AMER team that should be
working that day. Regardless of forecast volume, we always maintain a minimum
coverage of 15%.

| Holiday | Date | Day | Region | Target % working |
| ----- | ----- | :---: | ----- | :---: |
| Civic Holiday | 2026-08-03 | Mon | Canada | 67% |
| Labor Day | 2026-09-07 | Mon | US + Canada | 60% |
| National Day for Truth & Reconciliation | 2026-09-30 | Wed | Canada | 67% |
| Thanksgiving (Canada) / Indigenous Peoples' Day | 2026-10-12 | Mon | US + Canada | 64% |
| Remembrance Day / Veterans Day | 2026-11-11 | Wed | US + Canada | 62% |
| Thanksgiving (US) | 2026-11-26 | Thu | US | 55% |
| Day after Thanksgiving | 2026-11-27 | Fri | US | 47% |
| Christmas Eve | 2026-12-24 | Thu | US + Canada | 15% |
| Christmas Day | 2026-12-25 | Fri | US + Canada | 15% |
| Boxing Day (observed) | 2026-12-28 | Mon | Canada | 21% |
| New Year's Eve | 2026-12-31 | Thu | US + Canada | 15% |
| New Year's Day | 2027-01-01 | Fri | US + Canada | 15% |
| Martin Luther King Jr. Day | 2027-01-18 | Mon | US | 65% |

If a holiday you feel should be included is missing, let your manager know
and we will review the data and add a target for it.

#### Before requesting a holiday off

1. **Check the table above** for the target coverage on the day you want off.
1. **Check the [Support OOO - AMER calendar](https://calendar.google.com/calendar/embed?src=c_9166d2302886c4ae23f34099eeb4015e2d520e1dd4029711becd8370be996513%40group.calendar.google.com)**
   for that day's summary event, which shows the percentage of the team
   available (for example, `AMER: at 94%`). See
   [Support Time Off calendars](/handbook/support/support-time-off/#support-time-off-calendars)
   for subscription steps.

If the calendar percentage is above the target, go ahead and submit your
request. If it is at or below the target, check with your manager before
submitting — if it's a day you really need, say so and we'll work it out.

As a general rule, Canadian holidays are for Canada-based engineers to take
and US holidays for US-based engineers.

{{< note >}}
The calendar updates nightly with submitted time off, so new requests appear
after the next refresh. All existing
[holiday and time off guidance](/handbook/support/support-time-off/) still
applies; this check does not replace it.
{{< /note >}}
