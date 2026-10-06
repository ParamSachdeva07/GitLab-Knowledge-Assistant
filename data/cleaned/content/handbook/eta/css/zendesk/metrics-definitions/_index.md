---
title: 'Metrics definitions'
description: 'Documentation on Zendesk metrics definitions'
---

This guide defines common Zendesk ticket metrics. These metrics track ticket lifecycle timing and are used in SLA policies, reporting, and performance measurement.

**Note:** These are Zendesk's official definitions. GitLab may use slightly different calculations or definitions for internal reporting. For more information on SLA policies, please see [our documentation](/handbook/eta/css/zendesk/sla-policies/).

## First Reply Time (FRT)

This is the time a ticket spent from creation until it received its first public reply from an agent.

## Next Reply Time (NRT)

This is the time a ticket spent from a public reply from an end-user until it received a public reply from an agent.

## Requester wait time

**Purpose:** Measures how long customers wait for agent action (including time waiting on outside sources).

This is the total time a ticket spent in the following statuses:

- New
- Open
- On-hold

## Agent work time

**Purpose:** Measures how long tickets spent waiting for direct agent action.

This is the total time a ticket spent in the following statuses:

- New
- Open

## Agent wait time

**Purpose:** Measures how long tickets spent waiting for customers to respond.

This is the total time a ticket spent in the following statuses:

- Pending

## On-hold time

**Purpose:** Measures how long tickets spent waiting for outside sources (i.e. not agent or customer).

This is the total time a ticket spent in the following statuses:

- On-hold

## Total resolution time

**Purpose:** Measures how long tickets from creation to being solved.

This is the total time a ticket spent in the following statuses:

- New
- Open
- Pending
- On-hold

## Periodic update

**Purpose:** Measures the time a ticket spends between public agent replies.

## Pausable update

**Purpose:** Measures the time a ticket spent between public agent replies.

This is the time a ticket spends between public agent replies while in the following statuses:

- New
- Open
- On-hold

## Detailed example

To illustrate how these metrics work together, consider this ticket lifecycle:

**Ticket #12345 timeline:**

| Time | Event | Status Change |
|------|-------|---------------|
| Monday 9:00 AM | Customer creates ticket | → New |
| Monday 2:00 PM | Agent replies publicly | → Open |
| Monday 3:30 PM | Customer replies | → Open |
| Monday 4:00 PM | Agent replies publicly | → Pending |
| Tuesday 10:00 AM | Customer replies | → Open |
| Tuesday 11:00 AM | Agent needs info from Engineering | → On-hold |
| Wednesday 2:00 PM | Engineering provides answer | → Open |
| Wednesday 2:30 PM | Agent replies publicly | → Solved |

**Calculated metrics:**

| Metric | Calculation | Value |
|--------|-------------|-------|
| **FRT** | Mon 9:00 AM → Mon 2:00 PM (first agent reply) | 5 hours |
| **NRT** | Mon 3:30 PM → Mon 4:00 PM (agent reply after customer response) | 30 minutes |
| **Requester wait time** | Time in New + Open + On-hold<br>• New: 5 hours<br>• Open: 8.5 hours total<br>• On-hold: 27.5 hours | **41 hours** |
| **Agent work time** | Time in New + Open<br>• New: 5 hours<br>• Open: 8.5 hours | **13.5 hours** |
| **Agent wait time** | Time in Pending<br>• Mon 4:00 PM → Tue 10:00 AM | **18 hours** |
| **On-hold time** | Time in On-hold<br>• Tue 11:00 AM → Wed 2:00 PM | **27.5 hours** |
| **Total resolution time** | Mon 9:00 AM → Wed 2:30 PM<br>(New + Open + Pending + On-hold) | **53.5 hours** |
| **Periodic update** | Time between any agent public replies<br>• Mon 2:00 PM → Mon 4:00 PM = 2 hours<br>• Mon 4:00 PM → Wed 2:30 PM = 46.5 hours | Latest: **46.5 hours** |
| **Pausable update** | Time between agent replies while in New/Open/On-hold<br>• Mon 2:00 PM → Mon 4:00 PM (in Open) = 2 hours<br>• Tue 10:00 AM → Wed 2:30 PM (in Open + On-hold) = 28.5 hours | Latest: **28.5 hours** |

**Key differences explained:**

- **Periodic update** counts ALL time between agent replies, including Pending status (when waiting for customer)
- **Pausable update** EXCLUDES Pending status, only counting time in New/Open/On-hold (when ticket is on agent/company side)
- **Total resolution time** (53.5 hours) = Agent work (13.5h) + Agent wait (18h) + On-hold (27.5h) - some overlap adjusted
- **Requester wait time** (41 hours) = All time customer is waiting for us (New + Open + On-hold)

## Further reading

- [Understanding which SLA metrics you can measure](https://support.zendesk.com/hc/en-us/articles/4408829459866-Defining-SLA-policies)
- [About native Support time duration metrics](https://support.zendesk.com/hc/en-us/articles/4408834848154-About-native-Support-time-duration-metrics)
