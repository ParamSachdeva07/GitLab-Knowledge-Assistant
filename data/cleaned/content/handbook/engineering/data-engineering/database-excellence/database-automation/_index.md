---
title: "Database Automation Team"
description: "The Database Automation team owns the automation frameworks, tools, and templates that make GitLab's Postgres databases easier to operate at scale, including configuration management, upgrade automation, and infrastructure provisioning."
---

The Database Automation team is the result of a reorganization of the [Database Operations Team](/handbook/engineering/data-engineering/database-excellence/database-operations/) and [Database Frameworks Team](/handbook/engineering/data-engineering/database-excellence/database-frameworks/).

## Mission

Replace manual, bespoke database operations with standardized, repeatable automation — transitioning GitLab's database infrastructure from individually managed systems to scalable, automated processes. The Database Automation team owns the automation frameworks, tools, and templates that make GitLab's PostgreSQL databases easier to operate at scale. While all three Database Excellence teams contribute automations and operational changes, Database Automation owns the underlying frameworks and manages the planning load for infrastructure changes.

Today, the team's primary focus is GitLab.com, with a longer-term goal of extending these capabilities to support Dedicated and self-managed deployments as well.

## Scope

The Database Automation team is responsible for:

* **Automation frameworks** — Owning the frameworks, tools, and templates that all three Database Excellence teams use to automate database operations, including managing the planning and prioritization of infrastructure changes.
* **Configuration management** — Standardizing and automating PostgreSQL configuration across clusters, replacing ad-hoc tuning with repeatable, version-controlled processes.
* **Upgrade automation** — Owning the tooling and frameworks that make PostgreSQL version upgrades safe, predictable, and increasingly automated. All three teams contribute to upgrade work using these frameworks.
* **Infrastructure provisioning** — Owning the patterns and tooling for creating and managing database clusters, replicas, and related infrastructure. All three teams contribute provisioning changes through standardized processes.

## Team

The team is composed primarily of reliability engineers, with backend engineers to help achieve its tooling and framework development goals. Regardless of team, all team members share stage-level role responsibilities including database reviews, oncall rotations, and operational needs alongside the other Database Excellence teams.

{{< group-by-slugs dazhu1 bshah11 jon_jenkins meiyang pmistry2 rhenchen.gitlab saadullah707 >}}
