---
title: "AI Coding:DAP Events"
description: "The DAP Events functional team within AI Coding, building the event platform and trigger capabilities for GitLab Duo Flows."
---

## Overview

The DAP Events team is building the event platform and trigger system that enables GitLab Duo Flows to run automatically in response to events across the development lifecycle. [Flow Triggers](https://docs.gitlab.com/user/duo_agent_platform/triggers/) are database objects that associate projects with flows and a dedicated service account, firing when matching events occur. The platform supports internal GitLab event types (code pushes, issue and MR changes, CI/CD pipeline results, deployments, and more) as well as custom external events from third-party tools like Jira, Jenkins, and Slack, published via gRPC CloudEvents to GitLab Relay. Events are streamed through a pluggable message broker (e.g., Redis, NATS) and executed asynchronously via Sidekiq workers.

## Key Information

| | |
|---|---|
| **Slack Channel** | `#g_dap-events` |
| **Stage Label** | `devops::ai coding` |
| **Group Label** | `group::dap events` |
| **Category Labels** | `Category:DAP Event Platform`, `Category:DAP Triggers` |

## Documentation

1. [Duo Flow Triggers documentation](https://docs.gitlab.com/user/duo_agent_platform/triggers/)
1. [Design document](https://gitlab.com/gitlab-com/content-sites/handbook/-/merge_requests/18106) (in progress)
1. [Event Platform Epic](https://gitlab.com/groups/gitlab-org/-/work_items/21338)
   1. [Phase 1](https://gitlab.com/groups/gitlab-org/-/work_items/21345): Using the existing EventStore
   1. [Phase 2](https://gitlab.com/groups/gitlab-org/-/work_items/21346): Building a new message broker
1. [DAP Triggers Epic](https://gitlab.com/groups/gitlab-org/-/work_items/21997)
