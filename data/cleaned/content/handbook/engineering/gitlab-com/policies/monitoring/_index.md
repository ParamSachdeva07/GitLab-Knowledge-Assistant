---
title: "Monitoring of GitLab.com"
description: "This policy specifies requirements for monitoring of GitLab.com"
controlled_document: true
tags:
  - security_policy
  - security_policy_caplscsi
---

{{< label name="Visibility: Audit" color="#E24329" >}}

## Purpose

This policy specifies how GitLab ensures continuous monitoring of GitLab.com services, logging and capacity planning are defined.

GitLab implements these measures to ensure compliance with various policies and agreements within the cloud environment, and to ensure that any potential security issues are quickly identified.

## Scope

This policy applies to all GitLab.com monitoring services in support of the statutory, regulatory and contractual requirements of GitLab.

## Roles & Responsibilities

| Role                      | Responsibility                                                                 |
|---------------------------|--------------------------------------------------------------------------------|
| GitLab Team Members       | Responsible for following the requirements in this procedure                   |
| Engineering, Security     | Responsible for implementing and executing this procedure                      |
| Engineering (Code Owners) | Responsible for approving significant changes and exceptions to this procedure |

## Procedure

- GitLab defines how Availability is calculated in the [Service Level Agreement](/handbook/engineering/infrastructure-platforms/service-level-agreement/)
- GitLab defines how logs are collected, and analyzed
- GitLab defines capacity management procedures

### Log management

GitLab.com services emit network, system, and application logs, which are then stored, processed, and searched to provide a basis for incident and security incident investigations.

Logs are stored in a short-term and long-term storage, with their own respective retention policies:

- short-term storage: 30 days
- long-term storage: 365 days

Logs in short-term storage are used to actively monitor application activity, spam events, transient errors, system and network authentication
events, security events, and similar.

Logs in long-term storage are used to comply to the [Records Retention & Disposal](/handbook/security/policies_and_standards/records-retention-deletion/) policy. Logs in long-term storage are less granular and have less detail than those in short-term storage.

Detailed overview of architecture, tooling and workflows are listed on the [Logging](https://gitlab.com/gitlab-com/runbooks/-/blob/master/docs/logging/README.md) page.

### Capacity Planning

In order to scale GitLab.com infrastructure at the right time and to prevent incidents, GitLab employs a capacity planning process.

The focus of the capacity planning process is to perform historical data analysis to predict future growth.
From this analysis, GitLab leverages a process that provides information around saturation points, which are then delivered to service owners.
Service owners then use this process to act on this information.

The data sources used to feed the forecasting tool are historical saturation and utilization data used as part of standard monitoring of GitLab.com.

The output of our capacity planning process is considered ORANGE, and must be treated per [The Data Classification Standard](/handbook/security/policies_and_standards/data-classification-standard/#orange).

Detailed overview of architecture, tooling and workflows are listed on the [Capacity Planning](/handbook/engineering/infrastructure-platforms/capacity-planning/) page.

## Exceptions

Changes and exceptions to this policy must be approved by the appropriate Infrastructure team responsible for monitoring GitLab.com.

## References

- [Records Retention & Disposal](/handbook/security/policies_and_standards/records-retention-deletion/)
