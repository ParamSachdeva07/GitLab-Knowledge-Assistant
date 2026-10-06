---
title: "ASE inventory"
description: "A reference to assist ASEs in gathering important information about customer configurations."
---

## Overview

Understanding the way a customer is using GitLab is critical to providing quality support as an ASE.
Each ASE can gather this information as they see fit, and this page serves as a reference and
starting point.

Gathering the information could be approached in several ways, like:

- A sync call to "interview" the customer
- A web form (be sure to consider data classifications!)
- A collaborative markdown doc in the customer collaboration project
- Any combination of the above

Generally, it's helpful to keep the inventory somewhere that any GitLab team-member can access it.
This facilitates quick knowledge transfer for emergencies, ASE transitions, and more!

## Inventory

When inventorying a customer, there are many general items that apply to all customers, as well as
offering-specific items. Feel free to use this as a starting point, and prefill anything you already
know, or discard any items you know aren't relevant.

Please add any items that are missing from the list that you have found helpful.

### General

- User access
  - Access method (basic auth, SSO, LDAP)
  - SSO Identity Provider (like Entra ID, Okta, other)
  - 2FA/MFA enforcement
  - Username format (`first.last`, `flast`, `n12345`...)
- Habits
  - Upgrade cadence (GitLab, Runner, toolkits)
  - Major or notable groups and projects
  - Monorepo
- CI/CD
  - Components
  - [CI/CD inputs](https://docs.gitlab.com/ci/inputs/)
  - Common configurations
- Security
  - SAST
  - DAST
  - Secret push protection
  - Secret detection
  - Compliance policies

### GitLab.com

- Top-level namespace path
- Group owners (reminder: can also be seen with admin/auditor)
- Runners
  - GitLab hosted or self-hosted
  - Review average minute consumption, note highest users of minutes
  - Architecture (if self-hosted)
  - Versions (if self-hosted)

### GitLab Self-Managed

Self-managed customers frequently maintain multiple environments for various purposes, like testing,
QA, and more. Remember to gather information about _all_ environments that will be supported.

- Environment role (prod, pre-prod, dev, QA...)
- Deployment and architecture
  - Type (single/multi-node Omnibus, Docker, Helm...)
  - Install method (manual, custom, GET...)
  - Hosting platform (on-prem, AWS, GCP...)
  - [Reference architecture](https://docs.gitlab.com/administration/reference_architectures/)
    - Additional options (managed Redis, RDS read replicas...)
  - GitLab version
- Runners
  - Runner architecture
  - Versions

### GitLab Dedicated

- Runners
  - [GitLab-hosted runners](https://docs.gitlab.com/ci/runners/hosted_runners/), self-hosted runners,
    or a combination
  - Versions (if self hosted)
- Architecture (can also be seen in Switchboard)

## Maintaining inventory information

After initial collection, it is handy to keep track of changes to customer inventory while working with the customer.
Some ASEs maintain inventories for customers in  `https://gitlab.com/gitlab-com/support/assigned-support-engineers/-/blob/main/Customers/CUSTOMER_NAME/extended_ase_notes/`. Example inventory file:

```yaml
# Detailed customer information

Deployment Platform: "self-managed, AWS."
GitLab Deployment: "Omnibus, modified 20K RA (https://docs.gitlab.com/administration/reference_architectures/20k_users/), not Dedicated"
Runners Deployment: "various executors (such as docker, windows shell), do not have kubernetes runners"
Container registry: "yes"
Package registry: "yes"
GitLab pages: "yes"
GitLab Kubernetes Agent: "n/a"
License: "Ultimate"
Secure features: "merge request approval policies are configured, secret push protection used"
Security policies: "Have MR Approval Policies configured at the top-level group"
Security scanners: "some teams utilise various security scanners"
AI features: "No"
GEO used: "No"
Advanced search solution: "ElasticSearch"
Database solution: "RDS with 2 extra read replicas"
Redis: "AWS managed cluster"
Gitaly deployment type: "2 Gitaly clusters."
Integrations: "Jira, Harness"
Plan stage: "yes"
User access management: "LDAP for group sync, SAML for sign ins"
Zero-downtime upgrade: "yes, it is very important to them"
Zendesk org name: "ZD_ORG_ID CUSTOMER_NAME"
Link to Collaboration project:  https://gitlab.com/gitlab-com/account-management/emea/CUSTOMER_NAME/CUSTOMER_NAME-collaboration-project
Link to org note: https://gitlab.com/gitlab-com/support/assigned-support-engineers/-/blob/main/Customers/CUSTOMER_NAME/Readme.md
Link to Weekly ticket review issue template: "n/a"
```

These inventories are also helpful when used with Duo Agent Platform if you need Duo to have context about customer deployment for troubleshooting, crafting reports, etc.
