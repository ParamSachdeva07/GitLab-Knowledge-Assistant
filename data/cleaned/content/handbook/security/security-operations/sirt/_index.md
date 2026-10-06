---
title: Security Incident Response Team - SIRT
description: GitLab Security Incident Response Team Overview
---

The Security Incident Response Team (SIRT) is GitLab's dedicated team for detecting, responding to, and investigating security events that impact GitLab.com and GitLab the company, protecting the business, our platform, and the trust of our users.

## <i class="fas fa-rocket" id="biz-tech-icons"></i> Our Vision

To be the first and last line of defence protecting GitLab, our platform, and our users, proactively identifying threats before they materialise and responding decisively when they do.

### Our Mission Statement

Protect GitLab's business and the trust of our users by delivering effective security incident response, forensic analysis, and continuous detection capability. We reduce risk through rapid containment, thorough investigation, and the operational improvements we drive from every incident we handle.

## <i class="fas fa-users" id="biz-tech-icons"></i> The Team

### Team Members

| | |
|---|---|
|Manny Mulatu|[Director SIRT](/job-description-library/security/security-leadership/#director-security)|
|Mitra Jozenazemian|[Security Manager - APAC](/job-description-library/security/security-incident-response-team/#manager-security-incident-response-team)|
|Laurens Van Dijk|[Security Manager - EMEA](/job-description-library/security/security-incident-response-team/#manager-security-incident-response-team)|

| | |
|---|---|
|Austin Bollinger|[Security Engineer](/job-description-library/security/security-incident-response-team/#security-incident-response-team-engineer-intermediate)|
|Bala Allam|[Senior Security Engineer](/job-description-library/security/security-incident-response-team/#senior-security-incident-response-team-engineer)|
|Chathura Kuruwita|[Senior Security Engineer](/job-description-library/security/security-incident-response-team/#senior-security-incident-response-team-engineer)|
|Ellis Coulson|[Security Engineer](/job-description-library/security/security-incident-response-team/#security-incident-response-team-engineer-intermediate)|
|Hasan Chawich|[Security Engineer](/job-description-library/security/security-incident-response-team/#security-incident-response-team-engineer-intermediate)|
|Janina Roppelt|[Senior Security Engineer](/job-description-library/security/security-incident-response-team/#senior-security-incident-response-team-engineer)|
|Leslie Anzures|[Security Engineer](/job-description-library/security/security-incident-response-team/#security-incident-response-team-engineer-intermediate)|
|Natalie Laundergan|[Security Engineer](/job-description-library/security/security-incident-response-team/#security-incident-response-team-engineer-intermediate)|
|Neil McDonald|[Senior Security Engineer](/job-description-library/security/security-incident-response-team/#senior-security-incident-response-team-engineer)|
|Saksham Anand|[Security Engineer](/job-description-library/security/security-incident-response-team/#security-incident-response-team-engineer-intermediate)|
|Dylan Stephenson|[Security Engineer](/job-description-library/security/security-incident-response-team/#security-incident-response-team-engineer-intermediate)|
|Joel Clarke|[Security Engineer](/job-description-library/security/security-incident-response-team/#security-incident-response-team-engineer-intermediate)|
|Josh Boyce|Principal Incident Commander|

## <i class="fas fa-stream" id="biz-tech-icons"></i> Services We Provide

1. Reactive - Services design to respond to active incident handling, including but not limited to
    - Incident analysis
    - Incident response support and coordination
    - Incident response resolution
    - Detection and response engineering
1. Proactive - Services designed to improve the infrastructure  and security  processes of GitLab before any incident occurs or is detected. The main goals are to avoid incidents and to reduce the impact and scope when they do occur.
    - Cyber Threat Analysis of vulnerability warnings and security advisories
    - Monitor Adversaries' activities and related trends to help identify future threats
    - Configuration and maintenance of security tools, applications, and infrastructure
    - Detection and response engineering
1. Administrative - Services design to assist with requests from GitLab's Legal and HR Departments.

## <i class="fas fa-bullseye" id="biz-tech-icons"></i> Engaging SIRT

The SIRT is on-call [24/7/365](/handbook/engineering/infrastructure-platforms/incident-management/on-call/#security-team-on-call-rotation) to assist with any security incidents. If an urgent security incident has been identified or you suspect an incident may have occurred, please refer to [Engaging the Security Engineer On-Call](/handbook/security/security-operations/sirt/engaging-security-on-call/).

Information about SIRT responsibilities and incident ownership is available in the [SIRT On-Call Guide](/handbook/security/security-operations/secops-oncall/).

## <i class="fas fa-receipt" id="biz-tech-icons"></i> Incident Management and Review

As part of the incident management and review process the SIRT maintains a recurring meeting that takes place on Monday of each week. During this meeting all of the previous weeks incidents, and any incidents that are currently open are reviewed. The review process covers the incident's scope, impact, the work performed to mitigate and remediate the incident, next steps, blockers, and current status. These meetings are also an opportunity to discuss mishandled incidents and process improvements.

## Limited Access

Information about security incidents or investigations is considered [limited access](/handbook/communication/confidentiality-levels/#limited-access) and is not shared with all team members by default. Security incidents are handled with appropriate confidentiality protocols to protect potentially sensitive information and maintain operational security.

The workflow for security incident handling is:

```mermaid
graph TD
    A[Security incident occurs] --> |Incident reported| B[SIRT automation creates a private project]
    B -->C[SIRT automation creates issue in new project]
    C -->D[Reporter added to the issue/project]
    D -->E[Other team members are added as needed*]
```

\*A pre-defined list of team members are automatically added when the incident is `~severity::1`.
