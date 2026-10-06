---
title: "AI Coding:DAP Code Review"
description: "The DAP Code Review functional team within AI Coding, focused on AI-powered code review features for merge requests."
---

## Overview

The DAP Code Review team focuses on [Duo Code Review](https://docs.gitlab.com/user/project/merge_requests/duo_in_merge_requests/), the AI-powered code review feature that provides automated insights and feedback on merge requests. This team is part of the broader Code Review organization within AI Coding.

## Features

- AI-generated summaries of merge requests and code changes
- Automated code review comments and suggestions
- Custom instructions for tailored review feedback
- Integration with GitLab's merge request workflow

## Key Information

| | |
|---|---|
| **Slack Channel** | `#g_code-review` |
| **Stage Label** | `devops::ai coding` |
| **Group Label** | `group::code review` |
| **Category Labels** | `Category:DAP Code Review` |

## Dashboards and Monitoring

- [Duo Code Review Monitoring Dashboard](https://log.gprd.gitlab.net/app/r/s/xVFdB) - latency for summarize review, summary merge request, and Duo Code Review (DCR); error rates, metrics for DCR comments, DCR custom instructions, and more (Kibana)
- [Duo Code Review Usage Dashboard](https://app.snowflake.com/ys68254/gitlab/#/francoisrose-duo-code-review-dNsR9ByyW) - usage data and stats per project (Snowflake)
- [DAP Adoption Dashboard](https://10az.online.tableau.com/t/gitlab/views/AgenticAIProductAdoption/Overview/c8ccd819-38b8-491f-859b-407e1f5f7490/8725ee67-495d-4947-a489-dcf6dcb2fb9a) - number of users, sessions, duration, and errors filterable by flow (Tableau)
- [AI Feedback Dashboard](https://10az.online.tableau.com/t/gitlab/views/AiFeedbackDashboard/AiFeedbackDashboard2/7be4a96b-ed04-41f3-85c1-2fe4e0ea0516/c6a77c31-d4f2-4aa1-b5da-ab9a0a868f44) - positive/negative feedback rates for Code Review (Tableau)

## Documentation

- [Duo Code Review documentation](https://docs.gitlab.com/user/project/merge_requests/duo_in_merge_requests/)
- [Original Epic](https://gitlab.com/groups/gitlab-org/-/epics/13008)
- [Updated Epic](https://gitlab.com/groups/gitlab-org/-/epics/18142)
