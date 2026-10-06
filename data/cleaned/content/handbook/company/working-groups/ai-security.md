---
title: "AI Security Working Group"
description: "The charter of this working group is to drive AI Security across GitLab components."
status: disbanded
---

## Attributes

| Property      | Value         |
|---------------|---------------|
| Date Created  | June 12, 2025 |
| End Date      | ~Feb 25, 2026  |
| Slack         | [#wg_ai_security](https://gitlab.enterprise.slack.com/archives/C0912QSD38D) (internal) |
| Google Doc    | [Working Group Agenda](https://docs.google.com/document/d/1sShQ7VH0fsUzA29qsRClbiIel7u-Q1R0-ZOziX1_eAg/edit?usp=sharing) (internal) |
| Epic          | [Main Project Epic](https://gitlab.com/groups/gitlab-org/-/epics/18135) (internal) |
| Handbook Page | [AI Security Working Group](/handbook/company/working-groups/ai-security/) |

## Context

The introduction of the Duo Agent Platform moves from separate GitLab Duo product features to a dedicated platform for AI at GitLab.

Secure development of GitLab Duo features becomes more critical for the business as we launch the Duo Agent Platform. We can
expect to see rapid iteration of this platform and should leverage industry best practices and make features secure by default.

This working group will include a community of team members from Engineering and Security whom strive to make security simple
for users and contributors alike.

## Scope

The scope of this group includes the following GitLab components:

1. [AI Gateway](https://docs.gitlab.com/administration/gitlab_duo/gateway/)
1. [CLI agents](https://docs.gitlab.com/user/duo_agent_platform/agent_assistant/)
1. [Duo Agent Platform](https://docs.gitlab.com/user/duo_agent_platform/)
1. [Editor Extensions](https://docs.gitlab.com/editor_extensions/)
1. [GitLab Language Server](https://docs.gitlab.com/editor_extensions/language_server/)

### Exit Criteria

1. Best practices for implementing AI prompts are documented in our Contributor documentation.
1. Proof-of-concepts are executed and recorded to understand what AI security tooling could
   offer SaaS, Dedicated, and Self-Managed customers.
1. Our CI/CD pipeline will trigger code review of merge requests and provide
   actionable advice for contributors.
1. Our CI/CD pipeline will block merge requests that do not meet secure development standards
   we establish for our AI offerings.
1. Automated scripts are established to setup local working environment and help in testing AI features on the various AI projects.

## Roles and Responsibilities

See the git history of this page to find the team members who were previously involved in this project.
