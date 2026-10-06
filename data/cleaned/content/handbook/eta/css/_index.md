---
title: Customer Support Systems
description: GitLab Customer Support Systems
---

## Purpose

The purpose of Customer Support Systems is to enable GitLab to provide delightful customer experiences by:

- equipping the Customer Support team with knowledge, tools, and data to optimize productivity and efficiently solve customer problems.
- equipping our customers and wider GitLab with the data, knowledge, and insights to prevent customer problems before they occur.
- delivering delightful experiences to both our own internal and external customers.

## Meet the team

| Name | Role |
|------|------|
| [TJ Pais](https://gitlab.com/tjpais) | Director - Customer Support Systems |
| [Jason Colyer](https://gitlab.com/jcolyer) | Fullstack Engineer, Customer Support Systems |
| [Dylan Tragjasi](https://gitlab.com/dtragjasi) | Senior Customer Support Systems Specialist |
| [Sarah Cole](https://gitlab.com/Secole) | Customer Support Systems Specialist |

## Working with us

We're here to help! Here's a quick guide on the best way to reach us depending on what you need:

🙋 **Requesting Something New or a Change**

> **Heads up before you file**: Each request type has specific roles that are authorized to submit it. To avoid delays, connect with the right person first - issues filed outside the appropriate role will be closed and you'll be directed to them anyway!

- **Global Support team requests** should be filed by a [SIG team](https://gitlab.com/support-innovation-group) member using [this template](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?issuable_template=Feature)
- **US Government Support team requests** should be filed by a US Government Support manager/director using [this template](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?issuable_template=Feature)
- **Knowledge Base updates (any Zendesk instance)** should be filed by a Support Senior Technical Program Manager using [this template](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?issuable_template=Feature)
- **Everything else** should be filed by a manager/director of the requesting team using [this template](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?issuable_template=Feature)

🐛 **Found a Bug?**

Please file an issue using [this template](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?issuable_template=Bug). We appreciate you taking the time to report it!

💬 **Something Else?**

Feel free to reach out to us directly in Slack at [#customer_support_systems](https://gitlab.enterprise.slack.com/archives/C018ZGZAMPD). We're always happy to chat!

## Issue flowchart

```mermaid
graph TD;
  Start--> Triage;
  Triage--> Type;
  Type-->|Bug| BugDevelopment
  Type-->|Feature| FeaturePlanning
  BugDevelopment--> BugValidation
  BugValidation--> BugValidated
  BugValidated-->|No| BugDevelopment
  BugValidated-->|Yes| Implementation
  FeaturePlanning--> FeatureScheduling
  FeatureScheduling--> FeatureIsItTime
  FeatureIsItTime-->|No| FeatureQueued
  FeatureIsItTime-->|Yes| FeatureDevelopment
  FeatureDevelopment--> FeatureValidation
  FeatureQueued--> FeatureIsItTime
  FeatureValidation--> FeatureValidated
  FeatureValidated-->|No| FeatureDevelopment
  FeatureValidated-->|Yes| Implementation
  Implementation--> Completion
  Completion--> End
  Start(Issue created)
  Triage(Triage stage)
  Type{Request type?}
  BugDevelopment(Development stage)
  BugValidation(Validation stage)
  BugValidated{Was it validated?}
  FeaturePlanning(Planning stage)
  FeatureScheduling(Scheduling stage)
  FeatureIsItTime{Is it being worked in the current iteration?}
  FeatureQueued(Queued stage)
  FeatureDevelopment(Development stage)
  FeatureValidation(Validation stage)
  FeatureValidated{Was it validated?}
  Implementation(Implementation stage)
  Completion(Completion stage)
  End(Issue closed)
```
