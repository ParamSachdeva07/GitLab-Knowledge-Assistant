---
title: 'Issue boards'
description: 'Documentation on issue boards'
---

## Understanding issue boards

### What are issue boards

As per [GitLab](https://docs.gitlab.com/user/project/issue_board/):

> Issue boards provide a visual way to manage and track work in GitLab. Issue boards:
>
> - Display issues as cards in customizable lists based on labels, milestones, or assignees.
> - Track issues through different stages of your workflow.
> - Support agile methodologies like Kanban and Scrum.
> - Organize multiple boards for different teams and projects.
> - Visualize workload and progress across your entire process.

Customer Support Systems uses our issue boards to:

- get an overview of issues we have to work
- move issues quickly between stages
- plan upcoming workloads and iterations

## Current issue boards

Customer Support Systems use issues boards to get a quick overview of our workload. Here we detail the primary ones we use and how they are setup.

### Stages

<sup>[Source](https://gitlab.com/groups/gitlab-com/eta/css/-/boards/11453656)</sup>

This is the primary board the Customer Support Systems team works from. It shows all non-closed issues grouped together by the `Stage` scoped label.

- Configuration
  - Title: `Stages`
  - List options
    - [ ] Show the Open list
    - [ ] Show the Closed list
  - Scope
    - Milestones: Don't filter milestones
    - Iteration: Any iteration
    - Labels: Any label
    - Assignee: Any assignee
    - Weight: Any weight
- Lists
  - `Stage::Triage`
    - Label: `Stage::Triage`
    - Work in progress limit: None
  - `Stage::Planning`
    - Label: `Stage::Planning`
    - Work in progress limit: None
  - `Stage::Scheduling`
    - Label: `Stage::Scheduling`
    - Work in progress limit: None
  - `Stage::Queued`
    - Label: `Stage::Queued`
    - Work in progress limit: None
  - `Stage::Deployment`
    - Label: `Stage::Deployment`
    - Work in progress limit: None
  - `Stage::Validation`
    - Label: `Stage::Validation`
    - Work in progress limit: None
  - `Stage::Implementation`
    - Label: `Stage::Implementation`
    - Work in progress limit: None
  - `Stage::Blocked`
    - Label: `Stage::Blocked`
    - Work in progress limit: None
  - `Stage::Backlogged`
    - Label: `Stage::Backlogged`
    - Work in progress limit: None

### Customers

<sup>[Source](https://gitlab.com/groups/gitlab-com/eta/css/-/boards/11453690)</sup>

This is a less used board by Customer Support Systems. It shows all non-closed issues grouped together by the `Customer` scoped label.

- Configuration
  - Title: `Customers`
  - List options
    - [ ] Show the Open list
    - [ ] Show the Closed list
  - Scope
    - Milestones: Don't filter milestones
    - Iteration: Any iteration
    - Labels: Any label
    - Assignee: Any assignee
    - Weight: Any weight
- Lists
  - `Customer::Support`
    - Label: `Customer::Support`
    - Work in progress limit: None
  - `Customer::ETA`
    - Label: `Customer::ETA`
    - Work in progress limit: None
  - `Customer::Security`
    - Label: `Customer::Security`
    - Work in progress limit: None
  - `Customer::Engineering`
    - Label: `Customer::Engineering`
    - Work in progress limit: None
  - `Customer::Field`
    - Label: `Customer::Field`
    - Work in progress limit: None
  - `Customer::Finance`
    - Label: `Customer::Finance`
    - Work in progress limit: None
  - `Customer::Marketing`
    - Label: `Customer::Marketing`
    - Work in progress limit: None
  - `Customer::People`
    - Label: `Customer::People`
    - Work in progress limit: None

### Request Type

<sup>[Source](https://gitlab.com/groups/gitlab-com/eta/css/-/boards/11453704)</sup>

This is a less used board by Customer Support Systems. It shows all non-closed issues grouped together by various labels we use to indicate the type of request.

- Configuration
  - Title: `Request Type`
  - List options
    - [ ] Show the Open list
    - [ ] Show the Closed list
  - Scope
    - Milestones: Don't filter milestones
    - Iteration: Any iteration
    - Labels: Any label
    - Assignee: Any assignee
    - Weight: Any weight
- Lists
  - `RequestType::Bug`
    - Label: `RequestType::Bug`
    - Work in progress limit: None
  - `RequestType::Incident`
    - Label: `RequestType::Incident`
    - Work in progress limit: None
  - `RequestType::Feature`
    - Label: `RequestType::Feature`
    - Work in progress limit: None
  - `RequestType::Administrative`
    - Label: `RequestType::Administrative`
    - Work in progress limit: None
