---
title: "Security Incident Severity Matrix"
description: " "
weight: 30
controlled_document: true
---

{{< label name="Visibility: Audit" color="#E24329" >}}

## Purpose

The purpose of this document is to establish a standardized framework for classifying security incidents based on their severity. This classification system enables the Security Incident Response Team (SIRT) to respond appropriately, allocate resources effectively, and ensure consistent communication about incidents across the organization.

## Scope

This document applies to all security incidents affecting GitLab's infrastructure, services, applications, and data. SIRT will use the criteria defined in this document when assessing incident severity and will refer to the [SIRT Escalation Guide](/handbook/security/security-operations/secops-oncall/) for escalation procedures.

## Roles & Responsibilities

| Role | Responsibilities |
| ----- |------------|
| GitLab Team Members | Responsible for following the requirements in this procedure |
| SIRT | Responsible for implementing and executing this procedure |
| SIRT Management (Code Owners) | Responsible for approving significant changes and exceptions to this procedure |

## Procedure

### Severity

The `severity` label is used to indicate the actual or potential impact of a security incident. This label is the single source of truth for determining the required response urgency, communication plan, and resource allocation. The severity should be set during the initial triage and cannot be adjusted.

GitLab uses the following company-wide matrix to determine severity:

| Severity | Impact | GitLab Response | Examples |
|--------|-------------|-------------|---------------------|
| Severity:1 **Critical** | **Customer Impact:** <br> Very high impact on users: their customers or business outputs will be impacted <br><br> **OR** <br><br> **GitLab Impact:** <br> Probable or severe damage to the business |Immediate all-hands response | - Customer-facing service is down <br> - Confirmed data breach or exposure of red/orange data <br> - Customer data loss <br> - Low-complexity, validated exploit scenario to GitLab’s platform or supply chain. <br> - Critical RCE that is actively exploited or that is unpatched, reachable, and has no exploitability telemetry <br> - Critical vulnerability that has public exposure (press, customers, 0-day by researcher) <br> - External actor controls a highly privileged GitLab service account|
| Severity:2 **High** | **Customer Impact:** <br> Significant impact on users: their internal operations will be disrupted <br><br> **OR** <br><br>**GitLab Impact:** <br> Possible or elevated damage to the business | Assigned resources, cross-team coordination, and regular stakeholder updates | - Customer-facing service is unavailable for some customers<br> - Core functionality is significantly impacted<br> - Privilege escalation scenarios requiring account compromise or insider-threat motive and knowledge<br>- High severity vulnerability with evidence of exploitation OR high press attention<br>- Suspected unauthorized access into sensitive GitLab systems<br>- Malware detection in GitLab's cloud infrastructure |
| Severity:3 **Medium** | **Customer Impact:** <br> Moderate impact on users: their internal operations may be hampered <br><br> **OR** <br><br> **GitLab Impact:** <br> Unlikely or mild damage to the business | Resources are diverted to address beyond normal operating procedures | - Slight performance degradation<br>- Non-critical features not performing optimally<br>- Commodity malware detection in non-critical systems  |
| Severity:4 **Low** | **Customer Impact:**: <br> Low impact on users: their internal operations may be altered <br><br> **OR** <br><br> **GitLab Impact:** Minimal damage to the business | Issue is resolved following standard procedures | - An inconvenience to customers, workaround available<br>- Usable performance degradation<br>- GitLab security policy violations that do not impact red/orange data  |

#### Considerations for determining severity

There are a few factors we take into account when determining impact. Every time we are faced with a security incident, we evaluate the scope and exposure of the risk, the confidentiality level, and more. By doing so, we split the issue into multiple, easier to assess, sub-issues. Here are a few examples:

**How many of the following areas of the CIA Triad apply?**

- Confidentiality
- Integrity
- Availability

**Affected Surface** - What is the affected surface?

- GitLab infrastructure
- Customer data
- Cloud accounts
- One particular application
- A customer's instance
- Your own machine
- GitLab Critical Security Control Systems (IDS/IPS, MDMs, EDR, CDR, IAM, SIEM, network security systems, change detection mechanisms, audit logging mechanisms, automated security testing tools, segmentation controls)

**Exploitability** - How easy is it to exploit the issue?

- Very easily - Attacker simply needs to run a command or script to trigger the issue.
- Requires some effort - Attacker requires specific conditions such as someone else to be logged in to exploit the issue.
- Difficult - Attacker requires specific conditions that are difficult to achieve.

**Visibility** - Who can see this issue?

- Everyone
- Someone with specific access
- Only me

The more areas of the CIA Triade that apply combined with the significance of the **Affected Surface**, **Exploitability**, and **Visibility** should be used to determine an estimated **Severity**

## Exceptions

Exceptions to this procedure will be tracked as per the [Information Security Policy Exception Management Process](/handbook/security/controlled-document-procedure/#exceptions).

## References

- [Security Incident Response Guide](/handbook/security/security-operations/sirt/sec-incident-response/)
- [SIRT Escalation Guide](/handbook/security/security-operations/secops-oncall/)
