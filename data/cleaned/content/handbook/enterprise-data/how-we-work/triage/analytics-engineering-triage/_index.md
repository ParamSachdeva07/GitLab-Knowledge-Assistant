---
title: "Analytics Engineering Triage Guide"
---

## Overview

Analytics Engineers rotate weekly through triage duties. While the rotation is assigned by week, the triager is responsible for **daily monitoring**, **issue processing**, and **communication** throughout their shift. This guide outlines what needs to happen each day, how to handle issues, and what to complete at the end of the rotation.

**Triage is the priority during your rotation.** Focus your time and effort on triage responsibilities. Only when there are no active triage issues should you work on business operations or OKR-related tasks.

## Triage Rotation Schedule

Triage is organized on an annual basis with all Analytics Engineers participating in the rotation. New team members are added to the rotation after one to two quarters on the team, depending on their seniority and team needs.

If you cannot complete triage during your assigned week, you are welcome to coordinate a swap with another team member.

## Daily Responsibilities

### Monitor pipeline health

Check the **#analytics-pipelines** channel each day for:

- Airflow failures  
- Monte Carlo anomalies  

When you encounter a failure:

1. [**Search existing issues**](https://gitlab.com/gitlab-data/analytics/-/issues?sort=created_date&state=opened&label_name%5B%5D=Triage%3A%3AAnalytics&first_page_size=20) to confirm whether the failure is already tracked
2. **Create or update issues**:
   - Group related failures under a single issue when they share a root cause
   - Add context to existing issues rather than duplicating them
   - For new failures, create one issue per distinct root cause using the [AE Triage Errors](https://gitlab.com/gitlab-data/analytics/-/issues/new?issuable_template=Triage:%20Errors%20AE%20) template
3. **Link to the weekly triage issue**:
   - Link all new and existing relevant issues to the current week’s triage issue
   - If an issue spans multiple weeks, link it to each relevant triage issue

#### Processing Issues from Triage

When an issue is created during triage:

1. **Assign to yourself**: All issues created from detected failures begin assigned to the triager
2. **Complete triage & validation**:
   - Document the problem clearly using logs, error messages, or monitoring alerts
   - Investigate the scope and identify the root cause
   - Paste relevant SQL queries and outputs in the issue to preserve context for future owners
3. **Investigate and attempt resolution**
   - Your primary responsibility as a triager is to determine the possible root cause of the issue
   - Debug, test, and explore potential fixes within your skill set
   - If the fix is expected to be [**less than 3 issue points**](/handbook/enterprise-data/how-we-work/#issue-pointing), you should implement the fix yourself
   - Document your investigation as you go, including attempted approaches, findings, and any SQL queries (with sensitive/MNPI data removed)
4. **Escalate**
   - Reassign the issue if the root cause or required fix is clearly beyond your domain expertise **or** if the work exceeds **3 issue points**
   - If the fix is **3+ issue points**, tag the Analytics Engineering Manager to determine assignment and prioritization
   - When escalating, include a concise summary of what you’ve investigated, what you’ve ruled out, what you believe the root cause may be, and why the issue requires reassignment

#### Communication with stakeholders

When pipeline failures occur, proactive communication with stakeholders is essential. Our goal is to notify stakeholders before they encounter the problem themselves.

Not all failures qualify as incidents. Review the [incident criteria](/handbook/enterprise-data/data-governance/incident-management/) to determine whether the failure requires the formal incident management process. If you're uncertain, err on the side of over-communicating.

### Review new issues created by stakeholders

1. Monitor new issues and requests in the analytics project with the `Team::Analytics Engineering` and the `workflow::1 - triage and validation` labels. You can find do so by filtering the [analytics issues](https://gitlab.com/gitlab-data/analytics/-/issues?sort=created_date&state=opened&label_name%5B%5D=Team%3A%3AAnalytics%20Engineering&label_name%5B%5D=workflow%3A%3A1%20-%20triage%20%26%20validation&first_page_size=100) by label and created date. If you have the necessary context, provide answers or direction. If the request requires a different owner, notify the team manager so they can assign an owner and schedule it for an iteration. Once an issue has been triaged, it can be moved to `workflow::2 - waiting for prioritization`
2. Monitor issues created with the `clean-up::review` label in order to [help our stakeholders route issues to the correct team](/handbook/enterprise-data/how-we-work/triage/#label-enforcement). You can use [this board](https://gitlab.com/gitlab-data/analytics/-/boards/9924098?label_name[]=clean-up%3A%3Areview) to find the issues

### End of day communication

Post a brief end-of-day update in #analytics-pipelines. This ensures that if an incident occurs after your workday ends, other team members have context and can respond appropriately.

## End-of-Week Wrap-Up

At the end of your triage week:

- Close any issues that have been resolved during your rotation
- Provide updates on any issues that remain open, including current status and next steps
- Post an end-of-week handoff message in **#analytics-pipelines** so the next triager knows where to pick up when they start their week
