---
title: Detection Engineering Team
---

## Engaging Detection Engineering

Teams can engage Detection Engineering by heading over to the #detection-engineering slack channel. SIRT can also engage Detection Engineering for detection and alert tuning needs by selecting the "report a bug."

## Our Vision

Ensuring cybersecurity incidents never go undetected by building and maintaining a best in class signal development and detection engineering program.

## Our Mission Statement

Build and Mature A Best In Class Detection Engineering Program

- Constantly tracking and pursuing KPI goals, including: Detection coverage, detection precision and sensitivity and time to detection
- Building and maintaining automations with Threat Intelligence and the Red Team to programmatically evaluate detection capabilities and improve our threat resilience

Reducing Time to Detection

- Improving detection context and quality
- Reducing the time to detect through comprehensive detection coverage

Improving Security Observability

- Partnering with the Product, Engineering and Infrastructure teams to improve GitLab security detection coverage
- Partnering with CorpSec and ProdSec to improve security detection capabilities in corporate, cloud, and identity infrastructure

Providing Customer Value

- Improving customer facing detection capabilities and offerings
- Identifying & partnering stakeholders to implement customer observability needs

## The Team & Priorities

### Team Members

| Team Member | Role |
|---|---|
| Matt Coons | [Senior Security Manager](/job-description-library/security/security-leadership/) |
| Harjeet Sharma | [Principal Security Engineer, Detection Engineering](/job-description-library/security/security-engineer/#detection-engineering) |
| Shashi Priyatham Chitakodur | [Associate Security Engineer, Detection Engineering](/job-description-library/security/security-engineer/#detection-engineering) |
| Joanna Rubi | [Senior Security Engineer, Detection Engineering](/job-description-library/security/security-engineer/#detection-engineering) |

### Our Stakeholders

While Detection Engineering has dedicated engineers focussed on advancing projects and handling operational duties, there are a number of stakeholders both within the Security Division and beyond that Detection Engineering collaborates with to drive results.

| Stakeholder | Shared Responsiblities/Dependencies |
|---|---|
| SIRT | Detection tuning, new detections, GUARD DaC framework |
| T&S | Omamori integration |
| Security Logging | Security logging capabilities & collaboration |
| Threat Intel | Threat driven detections, Top threat actor detections |
| GitLab Customers | Consumer of customer facing detections |
| Product team | Collaboration to improve security signal capabilities |
| CorpSec | Collaboration to collect security telemetry from purchased tooling |
| Security Identity Team | Collaboration to collect security telemetry from purchased tooling |
| Red Team | Collaboration to complete purple teams and testing detection capabilities |
| Product Security | Collaboration to build accurate and comprehensive security telemetry |

## What we've Built & Services we Offer

### GUARD

GUARD (GitLab Universal Automated Response and Detection) is the Security Team's Detections as Code (DaC) pipeline and alerting automation framework. GUARD hands off an alert to the SIRT incident handling process stops when an alert is converted into a SIRT incident.

GUARD is a shared responsibility model between Detection Engineering and SIRT - Both SIRT and Detection Engineering build threat detections and have the ability to commit new and maintain existing detections in GUARD.

#### Threat Detection Tuning

When SIRT identifies a threat detection that needs to be tuned, tuning requests are submitted to the Detection Engineering team for improvements.

#### Threat Detection Creation

The Detection Engineering team tracks detection coverage and builds new threat detections based on several needs:

1. Gaps in detection capabilities as identified by SIRT or Detection Engineering
2. Collaboration with T&S to improve the ability to identify potential abuse on the GitLab platform
3. New detections for new log sources that can be queried in GitLab's SIEM
4. New attacker TTPs
5. Collaboration with the Red Team as part of purple team or stealth engagements

### Detection Research

Detection engineers conduct deep dive research into potential observability gaps and security telemetry enhancement opportunities, identified in the GitLab product and 3rd party tools GitLab uses. Such research assignments have a target deliverable of new detections as well as improved observability capabilities.

## How We Measure Success

We measure the success of Detection Engineering by collecting and reporting on key performance indicators, through metrics collected from MRs, issues and alerting metrics.
