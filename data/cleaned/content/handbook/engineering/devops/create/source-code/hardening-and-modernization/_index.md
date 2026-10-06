---
title: "Create:Source Code Hardening and Modernization Team"
description: A temporary team that addresses systemic security and frontend problems in Source Code, hands the results over to the feature teams, and disbands.
---

## Why

Source Code is one of the oldest parts of GitLab's codebase, and most of its engineering capacity goes to maintenance. Two problems are systemic rather than tied to any single feature: security vulnerabilities with recurring root causes, and a fragmented, partially migrated frontend. This team exists to fix them, hand the results over, and disband.

## Scope

- **Security root causes.** Find the recurring root causes behind Source Code vulnerabilities and fix each as a class, with a shared layer or check used by every affected surface.
- **Frontend modernization.** Finish the Vue 3 migration on Source Code pages, add an integration test harness, clear the flaky-spec quarantine, and unify the many small Vue roots on the busiest pages into coherent applications.
- **Feature categories.** Split Source Code's single feature category so each Source Code team has its own error budget.

## What this team does not own

- **The Source Code security backlog.** Security issues stay with the team that owns the feature; we take on classes of issues we can fix systemically.
- **Feature maintenance.** Every Source Code feature has an owner among the other Source Code teams. We work in their code, with their review.
- **Microfrontends.** We unify Vue roots into fewer, well-structured apps; microfrontends are a separate team's direction.

## This team is temporary

The team runs **2026-09-21 → 2027-09-10** (end of milestone 20.4), with a go/no-go review after 6 months (19.10). It maintains no surface area of its own, so once the systemic problems are fixed and handed over there is nothing left for it to own.

### Team members

{{< team-by-manager-role role="Engineering Manager(.*)Create:Source Code Hardening and Modernization" team="Create:Source Code Hardening and Modernization" >}}

### Return teams

| Name | Role | Returns to |
|---|---|---|
| Vladimir Shushlin | Engineering Manager | Plan |
| Kerri Miller | Staff Backend Engineer | [Create:Repository Services](/handbook/engineering/devops/create/source-code/repository-services/) |
| Emma Park | Backend Engineer | [Create:Repository Services](/handbook/engineering/devops/create/source-code/repository-services/) |
| Chaoyue Zhao | Frontend Engineer | Create:Source Code Investigation |
| Anastasia Khomchenko | Senior Frontend Engineer | Plan:Portfolio Planning |

## Stable counterparts

{{< engineering/stable-counterparts manager-role="Engineering Manager(.*)Create:Source Code Hardening and Modernization" role="(Product Manager|Product Designer|Security Engineer|Technical Writer)(.*)Create:Source Code(,|$)|Director of Engineering(.*), Plan$" >}}

## How we measure success

| Measure | Target |
|---|---|
| Source Code security intake (new issues per quarter) — primary | Flat or falling for two consecutive quarters |
| Source Code security backlog — secondary | No past-due issues; the classes we took on closed |
| Frontend modernization | Metrics to be defined with the team |
| Feature categories | Each Source Code team has its own error budget |

## Links

- [Team board](https://gitlab.com/groups/gitlab-org/-/work_items/views/1032326)
- [Tracking issue](https://gitlab.com/gitlab-org/create-stage/-/work_items/13313) (confidential)
- [Create:Source Code teams](/handbook/engineering/devops/create/source-code/)
- Slack: [#g_create_source-code-hardening-and-modernization](https://gitlab.enterprise.slack.com/archives/C0C37CWJHMM)
