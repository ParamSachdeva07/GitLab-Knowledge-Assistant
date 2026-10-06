---
title: 'Pagerduty'
description: 'Documentation on Pagerduty'
---

This guide covers how Customer Support Systems works with and uses with Pagerduty at GitLab.

## Understanding Pagerduty

### What is Pagerduty

PagerDuty is a SaaS-based incident management platform that helps IT, DevOps, and security teams prevent and resolve business-impacting issues by automating alerts, orchestrating responses, and providing real-time visibility into operations, ensuring the right people are notified at the right time to minimize downtime and improve customer experience. It collects alerts from monitoring tools, uses on-call schedules and escalation policies, and offers AI for incident summarization and automation.

### How we manage items in Pagerduty

We currently manage all Pagerduty items within Pagerduty itself.

For information on paging Customer Support Systems or being oncall for Customer Support Systems, please see our [Oncall documentation](/handbook/eta/css/pagerduty/oncall).

## Customer Support Systems Pagerduty components

### Schedules

We currently utilize the following schedules:

- [Customer Support Operations](https://gitlab.pagerduty.com/schedules/PXYIFEP)
  - Timezone: UTC
  - Layers:
    - AMER
      - Rotation type: weekly
      - Handoff time: Monday 04:00 PM
      - Restrict on-call shifts to specific times:
        - from 04:00 PM to 12:00 AM
    - APAC 1
      - Rotation type: weekly
      - Handoff time: Monday 12:00 AM
      - Restrict on-call shifts to specific times:
        - from 12:00 AM to 4:00 AM
    - APAC 2
      - Rotation type: weekly
      - Handoff time: Monday 04:00 AM
      - Restrict on-call shifts to specific times:
        - from 04:00 AM to 08:00 AM
    - EMEA
      - Rotation type: weekly
      - Handoff time: Monday 08:00 AM
      - Restrict on-call shifts to specific times:
      - from 08:00 AM to 04:00 PM

### Escalation Policies

We currently utilize the following escalation policies:

- [Customer Support Operations](https://gitlab.pagerduty.com/escalation_policies/PKNCI0R)
  - Immediately after an incident is triggered
  - Notify the following users or schedules
    - [Customer Support Operations](https://gitlab.pagerduty.com/schedules#PXYIFEP)
    - escalates after 10 minutes
  - Notify the following users or schedules
    - Jason
    - escalates after 10 minutes
  - Notify the following users or schedules
    - Dylan
    - escalates after 10 minutes
  - If no one acknowledges, repeat this policy 5 times

### Services

We currently utilize the following services:

- [Customer Support Operations](https://gitlab.pagerduty.com/service-directory/PIETVIG)
  - Integrations
    - None
  - Workflows
    - None
  - Settings
    - Assign and Notify
      - Assign to escalation policy: [Customer Support Operations](https://gitlab.pagerduty.com/escalation_policies/PKNCI0R)
      - How should responders be notified: High-urgency notifications, escalate as needed
      - When incidents are not actioned, automatically:
        - All options unchecked
    - Reduce Noise
      - Currently not grouping alerts on this service.
    - Coordinate Responders and Stakeholders
      - Conference Bridge Dial-In Number: none
      - Conference Bridge Meeting URL: none
    - Event Management
      - Not used
    - Remediate
      - Documentation link: No documentation link listed for this service
      - Custom Incident Actions: No custom incident actions on this service
    - Service Dependencies
      - None
