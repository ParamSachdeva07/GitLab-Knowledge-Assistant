---
title: Support Training Specialised Domain Tracks
description: Structured learning pathways grouping related training modules into domain tracks for building deep expertise
---

## Overview

{{% alert title="Note" color="info" %}}
This page is a work in progress as part of the [Create role-based learning paths & curriculum initiative](https://gitlab.com/gitlab-com/support/support-experience-strategy/-/work_items/2) within Support. Module statuses marked as "To be created" are planned but not yet available. This page will be updated as new modules are developed.
{{% /alert %}}

Specialised domain track areas group related training modules into structured learning pathways. Each domain track provides a logical progression of modules, from foundational concepts to advanced troubleshooting, enabling engineers to build deep expertise in a specific area. Tracks leverage existing modules where possible and identify gaps where new modules are needed.

{{% alert title="Note" color="info" %}}
The ordering of modules within each track indicates the recommended pathway, but in no way dictates an explicit order in which these modules must be taken. Engineers are encouraged to follow the suggested progression where possible, but may adapt the order to suit their experience and learning needs.
{{% /alert %}}

## Domain Tracks

### Database

A pathway covering PostgreSQL internals, performance and troubleshooting as they relate to GitLab.

| Order | Module | Status |
|-------|--------|--------|
| 1 | Database Fundamentals (PG settings, PgBouncer, connection pooling) | To be created |
| 2 | [PostgreSQL Locks](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=Postgresql_locks&issue[title]=YOUR%20NAME%20-%20PostgreSQL%20Locks) | Exists |
| 3 | Database Performance & Troubleshooting (vacuum, analyze, index bloat, slow queries) | To be created |
| 4 | Database Migrations & Upgrades (PG major version upgrades, migration debugging) | To be created |
| 5 | Partitioned Tables & Advanced Schema Topics | To be created |

### CI/CD

A combined track covering pipeline configuration and runner infrastructure.

| Order | Module | Status |
|-------|--------|--------|
| 1 | [Continuous Integration](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=Continuous%20Integration&issue[title]=YOUR%20NAME%20-%20Continuous%20Integration) | Exists |
| 2 | [GitLab Runner](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=GitLab%20Runner&issue[title]=YOUR%20NAME%20-%20GitLab%20Runner) | Exists |
| 3 | [Runner-Job-Lifecycle](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=Runner-Job-Lifecycle&issue[title]=YOUR%20NAME%20-%20Runner-Job-Lifecycle) | Exists |
| 4 | CI/CD Troubleshooting (pipeline failures, job logs, debugging strategies) | To be created |
| 5 | [GitLab Runner Infrastructure Toolkit (GRIT)](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=GitLab%20Runner%20Infrastructure%20Toolkit%20%28GRIT%29&issue[title]=YOUR%20NAME%20-%20GitLab%20Runner%20Infrastructure%20Toolkit%20%28GRIT%29) (optional) | Exists |

### Security Scanning and Security Policies

A pathway covering security scanning and security policies.

| Order | Module | Status |
|-------|--------|--------|
| 1 | Dependency Scanning | To be created |
| 2 | [SAST](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=SAST&issue[title]=YOUR%20NAME%20-%20SAST) | Exists |
| 3 | [DAST](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=DAST&issue[title]=YOUR%20NAME%20-%20DAST) | Exists |
| 4 | Security Policies | To be created |
| 5 | Advanced SAST | To be created |

### GitLab Installation and Administration

A deep-dive track for engineers supporting self-managed deployments, covering installation methods, scaling and architectural understanding.

| Order | Module | Status |
|-------|--------|--------|
| 1 | [Introduction to GitLab Architecture](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=Introduction%20to%20GitLab%20Architecture&issue[title]=YOUR%20NAME%20-%20Introduction%20to%20GitLab%20Architecture) | Exists |
| 2 | [GitLab Installation and Administration Basics](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=GitLab%20Installation%20and%20Administration%20Basics&issue[title]=YOUR%20NAME%20-%20GitLab%20Installation%20and%20Administration%20Basics) | Exists |
| 3 | [GitLab Intermediate Topics](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=GitLab%20Intermediate%20Topics&issue[title]=YOUR%20NAME%20-%20GitLab%20Intermediate%20Topics) | Exists |
| 4 | [GitLab Omnibus](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=GitLab%20Omnibus&issue[title]=YOUR%20NAME%20-%20GitLab%20Omnibus) | Exists |
| 5 | [GitLab Upgrades](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=GitLab%20Updates&issue[title]=YOUR%20NAME%20-%20GitLab%20Upgrades) | Exists |
| 6 | [Docker](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=Docker&issue[title]=YOUR%20NAME%20-%20Docker) | Exists |
| 7 | [Helm and GitLab Charts](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=Helm%20and%20GitLab%20Charts&issue[title]=YOUR%20NAME%20-%20Helm%20and%20GitLab%20Charts) | Exists |
| 8 | [GitLab Environment Toolkit](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=GitLab%20Environment%20Toolkit&issue[title]=YOUR%20NAME%20-%20GitLab%20Environment%20Toolkit) | Exists |
| 9 | [Openshift](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=Openshift&issue[title]=YOUR%20NAME%20-%20Openshift) | Exists |
| 10 | [Scaled And High Availability](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=Scaled%20And%20High%20Availability&issue[title]=YOUR%20NAME%20-%20Scaled%20And%20High%20Availability) | Exists |

### Geo

A focused track for Geo, which frequently appears in complex support tickets and emergencies.

| Order | Module | Status |
|-------|--------|--------|
| 1 | [Geo](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=Geo&issue[title]=YOUR%20NAME%20-%20Geo) | Exists |

### Gitaly

A focused track for Gitaly and Praefect, which frequently appears in complex support tickets and emergencies.

| Order | Module | Status |
|-------|--------|--------|
| 1 | [Gitaly](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=Gitaly&issue[title]=YOUR%20NAME%20-%20Gitaly) | Exists |

### Authentication & Identity

A track grouping all identity-related modules into a coherent pathway.

| Order | Module | Status |
|-------|--------|--------|
| 1 | [SAML](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=SAML&issue[title]=YOUR%20NAME%20-%20SAML) | Exists |
| 2 | [SCIM](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=SCIM&issue[title]=YOUR%20NAME%20-%20SCIM) | Exists |
| 3 | SAML/SCIM Troubleshooting (combined real-world scenarios) | To be created |
| 4 | [LDAP](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=LDAP&issue[title]=YOUR%20NAME%20-%20LDAP) | Exists |
| 5 | [OmniAuth](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=OmniAuth&issue[title]=YOUR%20NAME%20-%20OmniAuth) | Exists |

### Observability & Log Analysis

A track focused on monitoring, performance analysis and the log analysis skills that underpin effective troubleshooting across all domains.

| Order | Module | Status |
|-------|--------|--------|
| 1 | Kibana & OpenSearch for Log Analysis | In progress |
| 2 | [GitLab Performance](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=GitLab%20Performance&issue[title]=YOUR%20NAME%20-%20GitLab%20Performance) | Exists |
| 3 | [Competent Strace module](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=Competent%20Strace%20module&issue[title]=YOUR%20NAME%20-%20Competent%20Strace%20module) | Exists |

### GitLab Duo & AI Usage

A track covering GitLab's AI-powered features for both supporting customers and engineers' own productivity.

| Order | Module | Status |
|-------|--------|--------|
| 1 | [GitLab Duo](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=GitLab%20Duo&issue[title]=YOUR%20NAME%20-%20GitLab%20Duo) | Exists |
| 2 | [Using AI in Support](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=Using%20AI%20in%20Support&issue[title]=YOUR%20NAME%20-%20Using%20AI%20in%20Support) | Exists |
| 3 | [GitLab Duo Agent Platform](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=GitLab%20Duo%20Agent%20Platform&issue[title]=YOUR%20NAME%20-%20GitLab%20Duo%20Agent%20Platform) | Exists |
| 4 | [GitLab Duo Self Hosted Models](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=Gitlab%20Duo%20Self%20Hosted%20models&issue[title]=YOUR%20NAME%20-%20GitLab%20Duo%20Self%20Hosted%20Models) | Exists |

### GitLab.com (SaaS)

A track for engineers supporting GitLab.com.

| Order | Module | Status |
|-------|--------|--------|
| 1 | [GitLab-com SaaS Account Basics](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=GitLab-com%20Saas%20Account%20Basics&issue[title]=YOUR%20NAME%20-%20GitLab-com%20SaaS%20Account%20Basics) | Exists |
| 2 | [GitLab-com SaaS Basics](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=GitLab-com%20SaaS%20Basics&issue[title]=YOUR%20NAME%20-%20GitLab-com%20SaaS%20Basics) | Exists |
| 3 | [GitLab-com Admin](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=GitLab-com%20Admin&issue[title]=YOUR%20NAME%20-%20GitLab-com%20Admin) | Exists |
| 4 | [GitLab-com Console](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=GitLab-com%20Console&issue[title]=YOUR%20NAME%20-%20GitLab-com%20Console) (optional) | Exists |

### GitLab Dedicated

A track for engineers supporting GitLab Dedicated.

| Order | Module | Status |
|-------|--------|--------|
| 1 | [GitLab Dedicated](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=GitLab%20Dedicated&issue[title]=YOUR%20NAME%20-%20GitLab%20Dedicated) | Exists |
| 2 | [Hosted Runners Dedicated](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=Hosted%20Runners%20Dedicated&issue[title]=YOUR%20NAME%20-%20Hosted%20Runners%20Dedicated) | Exists |
| 3 | [GitLab Dedicated for Government](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=GitLab%20Dedicated%20for%20Government&issue[title]=YOUR%20NAME%20-%20GitLab%20Dedicated%20for%20Government) (optional) | Exists |

### Licensing and Renewals

A track for the commercial/account side of support.

| Order | Module | Status |
|-------|--------|--------|
| 1 | [Subscriptions License and Renewals](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=Subscriptions%20License%20and%20Renewals&issue[title]=YOUR%20NAME%20-%20Subscriptions%20License%20and%20Renewals) | Exists |
| 2 | [Customers Console](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=Customers%20Console&issue[title]=YOUR%20NAME%20-%20Customers%20Console) | Exists |
| 3 | [Downtime Credits](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=Downtime%20Credits&issue[title]=YOUR%20NAME%20-%20Downtime%20Credits) | Exists |
