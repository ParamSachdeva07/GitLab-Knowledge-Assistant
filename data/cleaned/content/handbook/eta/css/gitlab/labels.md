---
title: 'Labels'
description: 'Documentation on labels'
---

This guide explains how Customer Support Systems uses GitLab labels.

## Understanding labels

### What are labels

Labels organize and track work across GitLab features. As projects grow from small teams to large organizations, labels help you track and manage increasing volumes of work. Labels:

- Categorize issues, merge requests, and epics with custom attributes.
- Filter content in lists and boards.
- Prioritize work items with colors and descriptive titles.
- Track priority and severity with scoped labels.
- Structure workflows through organized groupings.

For Customer Support Systems, labels provide structured categorization of requests, enable workflow tracking through issue boards, and help prioritize and route work across the team.

## Labels used by Customer Support Systems

### Stage labels

These are used to indicate what stage an issue is currently at.

| Label | Meaning |
|-------|---------|
| `Stage::Triage` | This is where issues begin. It is here a decision about whether work is going to be accepted will occur |
| `Stage::Planning` | It is here a gameplan for the issue will be created |
| `Stage::Scheduling` | It is here that when to work an issue will be determined |
| `Stage::Queued` | It is here issues being worked in the future wait |
| `Stage::Development` | It is here current development work will be done (traditionally in sandboxes) |
| `Stage::Validation` | It is here validation from the issue requester is obtained |
| `Stage::Implementation` | It is here work will be done to implement it (using work done in the Development stage) |
| `Stage::Completed` | This indicates the issue is completed |
| `Stage::Backlogged` | This indicates an issue is backlogged |
| `Stage::Blocked` | This indicates something is blocking moving forward on an issue |

Note: These are scoped labels, meaning only one of them can ever be present on an issue at a time.

### Validation labels

These are used to indicate the status of validation on an issue (which occurs in the Development stage).

| Label | Meaning |
|-------|---------|
| `Validation::Skipped` | This means no validation was done for an issue |
| `Validation::Awaiting` | This means Customer Support Systems is waiting on validation to be completed |
| `Validation::Received` | This means validation was received |
| `Validation::Rejected` | This means validation was rejected |

Note: These are scoped labels, meaning only one of them can ever be present on an issue at a time.

### Request type labels

These are used to indicate the type of request an issue is.

| Label | Meaning |
|-------|---------|
| `RequestType::Bug` | The issue is concerning a bug |
| `RequestType::Feature` | The issue is concerning a feature request/change |
| `RequestType::Incident` | The issue is concerning an incident |
| `RequestType::Administrative` | The issue is concerning administrative work |

Note: These are scoped labels, meaning only one of them can ever be present on an issue at a time.

### Customer labels

These are used to indicate what team/department made the request.

| Label | Meaning |
|-------|---------|
| `Customer::ETA` | The request is from the ETA team |
| `Customer::Security` | The request is from the Security team |
| `Customer::Engineering` | The request is from the Engineering team |
| `Customer::Finance` | The request is from the Finance team |
| `Customer::People` | The request is from the People team |
| `Customer::Support` | The request is from the Support team |
| `Customer::Field` | The request is from the Field team |
| `Customer::Marketing` | The request is from the Marketing team |

Note: These are scoped labels, meaning only one of them can ever be present on an issue at a time.

### Priority labels

These are used to indicate the priority level of an issue.

| Label | Meaning |
|-------|---------|
| `Priority::1` | It is a priority 1 (urgent) level issue |
| `Priority::2` | It is a priority 2 (high) level issue |
| `Priority::3` | It is a priority 3 (medium) level issue |
| `Priority::4` | It is a priority 4 (low) level issue |

Note: These are scoped labels, meaning only one of them can ever be present on an issue at a time.

### Roadmap labels

These are used to indicate if an issue is tied to a roadmap.

| Label | Meaning |
|-------|---------|
| `roadmap_item` | The issue is pertaining to an item on a roadmap |

## Applying a label

To apply a label to an issue or merge request, you can either click `Edit` next to `Labels` on the right-side panel of the issue/merge request or you can use the [label quick command](https://docs.gitlab.com/user/project/quick_actions/#label):

```plaintext
/label ~"TITLE_OF_LABEL"
```

Note: The tilde (`~`) is required and you should replace `TITLE_OF_LABEL` with the title of the label itself. As an example:

```plaintext
/label ~"Stage::Planning"
```

## Removing a label

To remove a label from an issue or merge request, you can either click `Edit` next to `Labels` on the right-side panel of the issue/merge request or you can use the [unlabel quick command](https://docs.gitlab.com/user/project/quick_actions/#unlabel):

```plaintext
/unlabel ~"TITLE_OF_LABEL"
```

Note: The tilde (`~`) is required and you should replace `TITLE_OF_LABEL` with the title of the label itself. As an example:

```plaintext
/unlabel ~"roadmap_item"
```
