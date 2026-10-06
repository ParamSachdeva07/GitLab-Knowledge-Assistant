---
title: "Security Platforms & Architecture"
description: "Security Platforms & Architecture Team Charter"
---

Last Updated: February 6, 2026

## Mission Statement

The Security Platforms and Architecture (SPA) sub-department protects GitLab's platform and products by identifying, prioritizing, and mitigating security risks across the entire product lifecycle. Composed of [Security Architecture](/handbook/security/product-security/security-platforms-architecture/security-architecture/), [Application Security](/handbook/security/product-security/security-platforms-architecture/application-security/), and [Security Research](/handbook/security/product-security/security-platforms-architecture/security-research/), we combine strategic security architecture with operational application security to enable GitLab to be the most secure software factory platform on the market. We work with GitLab engineers and product teams to anticipate and prevent vulnerabilities during design and development, and ensure delivery of high-quality software GitLab customers can trust. We focus on systemic product security risks and operational application security, working cross-functionally to mitigate them while maintaining Engineering's development velocity.

## SPA Teams Guiding Principles

Every SPA team member is expected to operate by our [Guiding Principles](/handbook/security/product-security/security-platforms-architecture/guiding-principles/). They cover how we decide, own work, communicate, support each other, and improve.

## Value Proposition

We provide security expertise and operational support throughout the software development lifecycle so that GitLab and our customers can create quality, secure software with high velocity. Our teams translate security expertise into public and internal thought leadership contributions that establish GitLab as a leader and trusted enabler for secure software development.

## Scope and Responsibilities

### Primary Areas of Ownership

| **Area** | **Description** | **Primary Team** |
| ------- | ------- | ------- |
| **Security Reviews** | Feature-level security reviews, final security reviews prior to release, ongoing design guidance | Application Security |
| **Security Architecture Reviews** | High-level architecture reviews, design reviews for large/complex/strategic initiatives requested by AI, Sec Section, or Core DevOps functional leadership  | Security Architecture |
| **Product Security Risk Register** | Risk identification, assessment, prioritization, and cross-organizational remediation strategies | Security Architecture |
| **Security Research** | Proactive identification of unknown security risks and vulnerabilities in the GitLab ecosystem | Security Research |
| **[Security Interlock](/handbook/security/product-security/security-platforms-architecture/security-interlock/)** | Cross-divisional Customer Zero efforts and dogfooding coordination | Security Architecture |
| **Security Visions and Standards** | Development and communication of security visions and standards to proactively enable teams to make sound security decisions and establish clear expectations for secure software delivery. | Security Architecture and AppSec |
| **Product Security Metrics** | Design and implementation of metrics collection systems | Security Architecture |
| **Direct Product Contributions** | Security feature development, POCs, and engineering contributions to the GitLab product | All SPA Teams |
| **Thought Leadership** | Blog posts, conference talks, or other public and internal thought leadership contributions that establish GitLab as a leader and trusted enabler for secure software development | All SPA Teams |

### Interface Points

- **Product Security Risk Register:**
  - All Product Security teams contribute to the creation, updating, and treatment of risks in the PSRR.
  - We collaborate with the [Security Risk Team](/handbook/security/security-assurance/security-risk/), who owns and operates the broader [Risk Register](/handbook/security/security-assurance/security-risk/storm-program/).
- **Multi-layer Security Reviews**:
  - We partner with InfraSec when initiatives require both application-layer and infrastructure inputs
- **Security Interlock**:
  - All Product Security teams contribute real-world testing of GitLab features and provide feedback to improve product usability, functionality, and effectiveness.
  - SPA consolidates and delivers structured feedback to Security Product Managers and Engineering teams to drive feature enhancements that address actual security team workflows and requirements.
- **Security Team Escalations:** We respond to requests for support in areas including -
  - Vulnerability impact analysis and POC development [Requestor: Vuln Management]
  - [Technical Security Validation](/handbook/security/security-assurance/technical-security-validation/) of high-risk systems used by GitLab [Requestor: Security Risk]
- **Product/Engineering Collaboration:**
  - SPA influences GitLab's security and compliance roadmap, recognizing we are a canary for external enterprise-grade customer needs.
  - Compliance Framework Implementation and Operations: SPA partners with Security Compliance and Engineering Teams on the roadmap to obtain and maintain certifications to customer-required security frameworks.
  - Field Security: SPA supports and leverages Field Security to communicate security guidance and build customer trust.

### Out of Scope

- Security Architecture related to infrastructure/cloud/data security [Team: [InfraSec](/handbook/security/product-security/infrastructure-security/)]
- Routine vendor third-party risk assessments [Team: [Security Risk](/handbook/security/security-assurance/security-risk/)]
- Vulnerability Management Operations [Team: [Vulnerability Management](/handbook/security/product-security/vulnerability-management/) and [Security Compliance](/handbook/security/security-assurance/security-compliance/)]
- Incident Response Management [Team: [SecOps](/handbook/security/security-operations/) and /handbook/security/product-security/psirt/]

## Communication Channels

Routine communications with the SPA team happen through the following:

- Slack: Use #security_help or #security_discuss and tag `@security-platforms-architecture` or `@appsec-team`
- GitLab Tags for Issue/MR discussion: `@gitlab-com/gl-security/security-research`, `@gitlab-com/gl-security/product-security/security-architecture`, or `@gitlab-com/gl-security/product-security/appsec`

In the event of an emergency, GitLab Team Members should page the Security Incident Response Team in any channel using the command `/security`.

## FY27 Primary Focus Areas

- Merge Security Architecture, Application Security, and Security Research into one team
- Deliver operational excellence for security reviews of new features
- Implement scaling investments to maximize security coverage and support and reduce risk
- Key Risk Areas: AI Security, Software Supply Chain Security, and AuthN/Z

## FY27 Metrics

SPA maintains metrics at many levels. The following are SPA-level strategic and operational metrics we intend to build and report on in FY27. These metrics are _in addition_ to Key Risk Indicators, project-level metrics, or sub-team specific metrics. For many of these, metrics instrumentation and reporting mechanisms are still forthcoming.

Note: These tables require horizontal scrolling to see completely.

### Strategic Metrics

The following are key metrics we will start tracking in FY27 to measure the SPA team's success delivering upon our charter, with E-Group as our intended audience. These reflect the reality that our ultimate success lies not in our individual activity, but requires working across teams and driving results that directly benefit our customers.

| **FY27 Key Metric** | **Why It Matters** | **How it's Calculated** | **Target Thresholds** | **Measurement Frequency** | **Reporting Mechanism** | **Additional Notes** |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| **Security Review Coverage** | Validates delivery of our team's primary value stream by confirming features requing security review receive appropriate coverage | TBD | 90%+ | Quarterly | End-of-Quarter Readout Issue | |
| **Security Findings Incorporation Rate** | Measures whether our team's work (vulns from Research, findings from security reviews, etc.) is being prioritized and incorporated into the product | TBD | 75% | Quarterly | End-of-Quarter Readout Issue | |
| **Customer Zero Feedback Delivered** | This metric tracks our effectiveness at partnering with product teams to validate that new security features meet real-world requirements and deliver value before they reach our customers | Manual count of C0 Issues completed and their outcomes | Baseline Required | End of Milestone | [FY26 Security Interlock Epic Comments](https://gitlab.com/groups/gitlab-com/gl-security/-/epics/350) (internal) | This metric is dependent upon submissions from Product and Engineering |
| **Thought Leadership Contributions** | This metric tracks our active efforts to position GitLab as a security thought leader, influencing both internal practices and the industry | Count of public blog posts, conference talks, interviews, or other public works | 2+/Quarter | Quarterly | End-of-Quarter Readout Issue | |
| **Direct Security Feature Contributions** | This metric tracks our team's delivery of security features and improvements that enhance our security posture, reduce platform risk, and enable GitLab and its customers to create secure software | [The count of merged MRs by SPA with the label "ProdSec-SPA-Contribution" applied](https://gitlab.com/groups/gitlab-org/-/merge_requests/?sort=created_date&state=merged&label_name%5B%5D=ProdSec-SPA-Contribution) | Baseline Required | Quarterly | End-of-Quarter Readout Issue | This likely needs to mature and take into account MR weight/complexity. We will iterate over time after we start tracking. |

### Operational Metrics

| **FY27 Key Metric** | **Why It Matters** | **How it's Calculated** | **Target Thresholds** | **Measurement Frequency** | **Reporting Mechanism** | **Additional Notes** |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| **PSRR Operational Metrics:** | These metrics provide comprehensive visibility into our Product Security Risk Register's contents, hot spots, and priority | Issue Counts with PSRR Labels | 1 Risk per functional leader prioritized each quarter | Quarterly | [Internal Dashboard](https://10az.online.tableau.com/#/site/gitlab/views/ProductSecurityRiskRegister/Dashboard?:iid=1) | |
| **Security Research Identified Vulnerabilities** | This metric tracks our Security Research Team's effectiveness at proactively identifying vulnerabilities before they can impact GitLab or our customers | Count of bug::vulnerability identified by Security Research over time, weighted by severity ([sample GLQL](https://gitlab.com/gitlab-com/gl-security/security-research/sec-research/-/issues/250#note_2245509822)) | Baseline Required | Quarterly | End-of-Quarter Readout Issue | |

## Review and Updates

This charter will be updated quarterly to ensure alignment with company and divisional priorities, the GitLab Security product roadmap, and critical risks in the StORM and Product Security Risk Registers.

Next scheduled review: May 1, 2026
