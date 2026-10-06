---
title: "Database Health Team"
description: "The Database Health team ran from early FY27 until September 2026, when its scope was split between Self-Managed Database Experience and Database Automation."
---

The Database Health team was one of the three teams created in the FY27-Q1 reorganization, from a split of the [Database Frameworks Team](/handbook/engineering/data-engineering/database-excellence/database-frameworks/). In September 2026 it wound down and its scope was split along the line that had always run through it: GitLab.com and self-managed.

## Where the work went

* **Self-managed health frameworks**, along with the upgrade and migration work that had been planned for a separate Database Migrations team, went to the new [Self-Managed Database Experience](/handbook/engineering/data-engineering/database-excellence/self-managed-database-experience/) team.
* **GitLab.com health monitoring, shift-left saturation identification, and managed Postgres monitoring** went to [Database Automation](/handbook/engineering/data-engineering/database-excellence/database-automation/), together with the engineers doing that work.

Identifying and mitigating active saturation points remains a shared responsibility across all Database Excellence teams, as it was when this team existed.

## What the team did

Database Health's mission was to maintain operational runway for GitLab's databases by proactively identifying and mitigating saturation points before they impacted customers, and to provide the visibility, tooling, and frameworks that keep databases healthy across both GitLab.com and self-managed deployments. Its scope was:

* **Database health monitoring and observability**: dashboards, metrics, and monitoring systems for database health across GitLab.com and self-managed instances.
* **Shift-left saturation identification**: tooling and processes that detect potential saturation points earlier in the development cycle, before they reach production.
* **Self-managed health frameworks**: frameworks that give self-managed customers insight into the health and operability of their GitLab database.
