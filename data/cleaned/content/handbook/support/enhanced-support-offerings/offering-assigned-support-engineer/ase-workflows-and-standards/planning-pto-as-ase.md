---
title: Planning PTO as ASE
description: Planning PTO for Assigned Support Engineers
---

## ASE PTO planning

As defined in the Assigned Support Engineer (ASE) contract, our customers expect to have a named engineer covering
for their ASE when the ASE is unavailable. This means that when an ASE
plans to take some time off, appropriate coverage needs to be identified. This
workflow describes the recommended process an ASE must follow to arrange
coverage for planned time off (PTO).

### Planning PTO

At least two weeks in advance of your time off, find people to cover for you
during the full length of that time.

If another ASE is able to cover for you, they should be your first choice. Next,
consider SEs who have expressed an interest in the ASE role. Finally, consider
any other SEs who you believe would be a good fit.

Once you have found suitable backups, create an issue in the
[Assigned Support Engineer project](https://gitlab.com/gitlab-com/support/assigned-support-engineers/-/issues).
Tag your manager and your backups in the issue. State clearly the dates you
will be out.

### The week before PTO

- Review the accounts and open tickets with your backups
- Inform the customers and account teams of your upcoming absence and your
  coverage plan
- Use the [Delegate Tasks feature of `Time Off by Deel` in Slack](https://help.letsdeel.com/hc/en-gb/articles/11901927070737-How-To-Request-Time-Off-With-Deel-Plugin#h_01GNY1Q325CCDEMASHZCMMY4RS)
  to indicate who is covering for each of your accounts

### Returning from PTO

When you return, meet with your backups to review the work they did on your
behalf. And notify your customers and account teams of your return.

Add any lessons learned from this process to the issue that you created in the
[Assigned Support Engineer project](https://gitlab.com/gitlab-com/support/assigned-support-engineers/-/issues),
and then close the issue. Consider improving this Handbook page, too.

## The PTO regional coverage pod pilot (AMER)

Following discussion in
[RFC - Discuss options for PTO planning workflow update](https://gitlab.com/gitlab-com/support/assigned-support-engineers/-/issues/92#two-option-2-regional-coverage-pod-clustered-pool),
starting **2025-11-15**, ASEs will run a pilot program to test out a new format for handling PTO
coverage using regional coverage pods.

When a single ASE is on PTO, the remaining two ASEs will cover **only high-priority accounts**. On
average, covering ASEs should expect to spend around 8 hours each week on coverage duties.

The current pod assignments are detailed in the [current pod assignments](#current-pod-assignments)
section below.

### Overview

- Status: Pilot program
- Start date: `2025-11-15`
- Check-in: `2025-12-15`

The ASE team experienced burnout from inability to enjoy PTO, unclear coverage creating stress,
micromanagement of every absence, and lack of structured processes. This pilot aims to address these
issues by restructuring how ASEs plan their time off.

The AMER ASEs are organized into coverage pods. Each group covers for their members during PTO. 
When a pod can't handle coverage within their group for any reason, they will
use the guidance defined in [when your pod can't cover](#when-your-pod-cant-cover).

Pods are loosely aligned by time zone to maintain consistent coverage for accounts.

### How it works

Each coverage pod has several ASEs, with 1 ASE acting as the pod lead. Pods rotate membership twice a
year. ASEs will plan their PTO based on how many people are already out during the same timeframe:

- **1 person out**: Enter in Workday, coordinate with your coverage group
- **2 people out**: Enter in Workday, post in `#support_assigned-support-eng` for visibility
- **3+ people out**: Post in `#support_assigned-support-eng` and tag the ASE manager before entering
in Workday. The manager will evaluate if coverage is feasible and work with the ASE on next steps.

For now, use the guidance in the [planning PTO](#planning-pto) section to document work and prepare
for your time off.

### When your pod can't cover

Post in `#support_assigned-support-eng` to request coverage from another pod. Other ASEs should
volunteer to take 1-2 accounts. If there are no volunteers within 48 hours (for planned PTO) or 4
hours (for emergency PTO), the ASE manager will assign coverage.

### Current pod assignments

Pods are leaderless. Members should act as [managers of one](/handbook/leadership/#managers-of-one) when supporting their
shared accounts, and make decisions as a group.

#### Pod alpha

- {{< member-by-gitlab "michwalker" >}} - 4 accounts - United States
- {{< member-by-gitlab "dbass90" >}} - 4 accounts - Canada
- {{< member-by-gitlab "erisrenee" >}} - 1 accounts - United States

#### Pod beta

- {{< member-by-gitlab "adamlauzon" >}} - 4 accounts - Canada
- {{< member-by-gitlab "magomez3" >}} - 3 accounts - United States
- {{< member-by-gitlab "m_lussier" >}} - 4 accounts - United States
- {{< member-by-gitlab "japokatanidis" >}} - 2 accounts - Canada

#### Pod gamma

- {{< member-by-gitlab "a.conrad" >}} - 4 accounts - United States
- {{< member-by-gitlab "pselva" >}} - 2 accounts - Canada
- {{< member-by-gitlab "dhickman" >}} - 2 accounts - United States
