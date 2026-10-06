---
title: "Product Security Incident Response Team (PSIRT)"
description: PSIRT home page
---
## Product Security Incident Response Team (PSIRT)

## Mission Statement

PSIRT identifies, assesses, and responds to security vulnerabilities in GitLab's GA (Generally Available) features in production, where customers have production commitments affected. We provide [Coordinated Vulnerability Disclosure](https://about.gitlab.com/security/disclosure/), security releases, and incident response for externally reported vulnerabilities. Through risk-based analysis of business and technical impact, PSIRT enables Engineering to correctly prioritize security fixes in relation to feature development. This ensures vulnerabilities are remediated while preserving development velocity except when security risks are significant. PSIRT contributes during security incidents by supporting as DRIs for coordinating engineering fixes, patch development, and customer communications around vulnerabilities.

## Value Proposition

We provide vulnerability lifecycle management (triage, coordination, remediation, and disclosure) for production features so that Engineering teams can respond to security issues with appropriate urgency aligned to actual risk while maintaining coordinated disclosure practices, customer trust, and compliance requirements. Additionally, we provide insight in lessons learned from vulnerabilities to help inform proactive mitigation.

## Scope and Responsibilities

### Primary Areas of Ownership

**Features in production:** PSIRT is DRI for investigating and communicating the impact of vulnerabilities in GitLab software and services when customers could have production commitments affected by the vulnerability and works with AppSec when reports are received about experimental and beta features.

- **Coordinated Vulnerability Disclosure:** We handle (Coordinated Vulnerability Disclosure) external reports for vulnerabilities within the native code of GitLab software and services received via our bug bounty program as well as publicly known exploitable open source vulnerabilities that are reported via HackerOne or are in the press (Heartbleed, Log4J, etc.).

- **Security Response:** We triage and technically assess critical and exploitable vulnerabilities in features in production and in the supply chain (for example, Log4J), determine company and customer risk, communicate and work with Engineering during remediation.

- **Security Release:** We coordinate external communications regarding vulnerabilities affecting GitLab features with defined release processes during regular patch releases.

- **Variant Hunting:** We search for variants of disclosed vulnerabilities across the codebase to identify similar patterns.

- **Remediation Verification:** We ensure that software remediations are complete and not easily bypassed.

### Interface Points

Our accountability is to triage and technically assess critical and exploitable vulnerabilities, determine company and customer risk, and coordinate external communications regarding these issues. PSIRT has several partners across the company including:

- **Security Team Interlock**
  - **Application Security (AppSec) team**
    - Escalation for specialized product knowledge during incident response
    - Variant hunting insights sharing
    - Knowledge sharing for pre-GA → post-GA transition
  - **Vulnerability Management (VM) Team**
    - Workflow alignment on vulnerability routing
    - Cross-domain vulnerability ownership coordination
  - **Security Platforms and Architecture (SPA) team**
    - PSIRT seeks assistance from SPA for exploitability POC development

- **Security Team Escalations:** We respond to requests for support in areas including:
  - Support for vulnerability mitigation when a 3rd party vulnerability identified by Vulnerability Management is being actively exploited, is high profile, or requires a response to multiple customers [Requestor: Vulnerability Management]
  - Incident support by acting as  DRIs for coordinating engineering fixes, patch development, and customer communications around vulnerabilities and by providing POC/IOC development (supported when required by SPA) to use in threat detection \[Requestor: SecOps\]
  - Knowledge sharing for pre-GA → post-GA transition \[AppSec\]

- **Product/Engineering Collaboration:**
  - Direct routing of vulnerability reports to Development Responsible Individuals (DRIs) and assistance with vulnerability reproduction
  - Verification of vulnerability fixes and coordination of security releases (CVEs, blog posts, communications)

- **Comms/PR Collaboration:**
  - Collaboration for security vulnerability messaging

### Out of Scope

- Pre-GA feature security reviews and coordination with Engineering (owned by AppSec)
- Vulnerability Management tooling development or implementation (owned by Vulnerability Management)
- Incident Command and Incident Communication (owned by SIRT)
- Customer Escalations regarding product vulnerabilities (owned by Field Security)
- Compliance violation enforcement/remediation (owned by Security Assurance)
- Disclosure of GitLab-identified third-party vulnerabilities to responsible party (owned by Threat Intelligence)

## Operating Model

tbd

### Core Processes

[**Root Cause Analysis for Critical Vulnerabilities**](/handbook/security/root-cause-analysis)

[**Application Security Engineer Handling priority::1/severity::1 Issues**](/handbook/security/product-security/psirt/runbooks/handling-s1p1/)

[**Application Security Engineer Working With SIRT**](/handbook/security/product-security/psirt/runbooks/working-with-sirt/)

[**CVSS Calculation**](/handbook/security/product-security/psirt/runbooks/cvss-calculation/)

[**General process for PSIRT in patch releases**](/handbook/security/product-security/psirt/runbooks/security-engineer/)

[**PSIRT Case Lifecycle**](/handbook/security/product-security/psirt/runbooks/psirt-case-lifecycle/)

[**HackerOne Process**](/handbook/security/product-security/psirt/runbooks/hackerone-process/)

[**Handling unintended vulnerability disclosures**](/handbook/security/product-security/psirt/runbooks/unintended-vuln-disclosure/)

[**How to handle upstream security patches**](/handbook/security/product-security/psirt/runbooks/upstream-security-patches/)

### Engagement Models

The team meets every other week for a team sync. The [agenda is available](https://docs.google.com/document/d/1MzKzRDNJBm4P1Ww8ieZtr4vtXmbmqYI80NSD8x55WTM/edit?usp=drive_link) to Security Division members.  

Team decisions should be discussed in the project issue tracker; currently PSIRT uses the AppSec issue tracker due to legacy processes but is discussing creating its own.

### Communication Channels

Routine communications with the PSIRT team happen through the following

- GitLab: Mention @gitlab-com/gl-security/product-security/psirt-group
- Slack: Use \#security-help or \#security-discuss and mention @psirt-team

For critical product vulnerabilities that are being actively exploited or have public exposure (press, customers, 0-day by researcher), engage the Security Engineer on-call by using `/security` in Slack; SecOps will engage PSIRT to collaborate on the incident.

### External Outreach

Learn how to identify or remediate security issues using real examples with GitLab's [**Reproducible Vulnerabilities**](/handbook/security/product-security/security-platforms-architecture/application-security/reproducible-vulnerabilities/).

Learn how GitLab is implementing [**Reproducible Builds**](/handbook/security/product-security/security-platforms-architecture/application-security/reproducible-builds/) for our build processes.

## Success Metrics

### Strategic Metrics

PSIRT is building our operational business health metrics in FY26. For many of these, metrics instrumentation and reporting mechanisms are still forthcoming. As the team matures, these metrics will evolve and be shared on this page.

### Current Roles

PSIRT consists of Security Engineers and Security Analysts.

Security Engineers are responsible for:

- Technical assessment of security vulnerabilities
- Support for engineering teams in reproducing, triaging, and addressing security vulnerabilities
- Vulnerability validation and patch review
- Support for security releases through checklist task preparation and tooling automation.
- Development and validation of security mitigations and temporary workarounds for vulnerabilities prior to patch availability
- Variant hunting and proactive searches for similar vulnerabilities to ensure complete remediation and prevent security bypasses
- Development and enhancement of automation for security releases, vulnerability assessment workflows, and operational processes

Security Analysts are responsible for:

- PSIRT-owned vulnerability management including management of researchers, communication, release communications  
- Support incident management by coordination with engineering and customer vulnerability communication
- Support for security releases through checklist task preparation, communication, and process enhancements
- Operations Management of runbooks, workflows and metrics
- Metrics tracking and reporting on PSIRT operational health, vulnerability trends, and team performance

## Content Review and Updates

This page will be reviewed quarterly to ensure alignment with company and divisional priorities, the GitLab Security product roadmap, and relevant business and operational changes. Updates may occur more frequently as business operations evolve.
