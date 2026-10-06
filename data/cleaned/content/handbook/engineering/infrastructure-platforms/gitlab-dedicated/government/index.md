---
title: "GitLab Dedicated for Government"
description: "GitLab Dedicated for Government is a FedRAMP-authorized single-tenant SaaS solution for government agencies."
---

## Overview

GitLab Dedicated for Government is a sub-offering of [GitLab Dedicated](/handbook/engineering/infrastructure-platforms/gitlab-dedicated/), purpose-built for federal agencies that require FedRAMP compliance, complete infrastructure isolation, and managed operations. It delivers the full GitLab Ultimate platform as a single-tenant SaaS solution, hosted exclusively in AWS GovCloud.

Where GitLab Dedicated provides the foundation of single-tenancy and managed operations, GitLab Dedicated for Government extends that foundation with FedRAMP Moderate authorization, government-specific configurations, and a roadmap driven by the unique needs of agency DevSecOps teams.

## Built for central DevSecOps teams

Central DevSecOps teams face a compounding challenge: they must accelerate developer productivity for hundreds to thousands of developers while maintaining strict FedRAMP compliance, managing tool sprawl, and demonstrating measurable value to agency leadership.

GitLab Dedicated for Government consolidates your entire SDLC toolchain into one integrated, compliant solution.

**Our target customer:**

1. A federal agency with a development organization of 1,000 or more users
2. A central DevTools or DevSecOps team with executive sponsorship and a mandate to consolidate tooling
3. An organization actively managing tool sprawl across 5 or more SDLC tools
4. A team seeking to adopt modern DevSecOps workflows within FedRAMP compliance boundaries

## Vision

To be the single, trusted platform that enables government agencies to build, secure, and deploy compliant software at unprecedented speed and scale, empowering central DevSecOps teams to serve their developers more effectively.

### What success looks like

**For central DevSecOps teams:**

- Self-service platform management through a dedicated control plane, with no support tickets for routine configuration
- Real-time visibility into developer productivity and compliance posture
- Platform consolidation reducing many tools to one, significantly reducing operational overhead
- Ability to enable AI-assisted development within agency-approved compliance boundaries

**For government developers:**

- Modern DevSecOps workflows comparable to the commercial sector
- AI assistance for code generation, security scanning, and troubleshooting
- Focus on mission delivery, not infrastructure management

**For agencies:**

- Continuous compliance with automated evidence collection
- Measurable acceleration in software delivery velocity
- Clear ROI from platform consolidation and reduced tool sprawl
- Flexible AI integration that supports agency-approved FedRAMP services

### North star metric

**Number of Customers** measures the total count of federal agencies successfully using GitLab Dedicated for Government.

This metric directly reflects our success in delivering value to government agencies and demonstrates market adoption of our FedRAMP-authorized solution. It captures both our ability to meet compliance requirements and our effectiveness in serving the government sector.

## Current state

GitLab Dedicated for Government launched with FedRAMP Moderate Authorization to Operate (ATO), providing agencies with a fully managed, single-tenant DevSecOps platform in AWS GovCloud.

### Now available: Secure foundation

| Capability | Description |
| --- | --- |
| **FedRAMP Moderate ATO** | Authority to Operate at FedRAMP Moderate, which enables federal agencies to deploy with confidence. |
| **Single-tenant isolation in AWS GovCloud** | Complete infrastructure isolation with a dedicated AWS account boundary; all data remains in AWS GovCloud (US West). |
| **Complete GitLab Ultimate feature set** | Full GitLab Ultimate, including planning, source control, CI/CD, security scanning, and deployment, architected for US government requirements. |
| **Fully managed operations** | GitLab manages all maintenance, security patching, infrastructure, and ongoing FedRAMP compliance. |
| **Enterprise-grade reliability** | High availability with disaster recovery, automated monitoring, and 24/7 operations support. |
| **Enterprise authentication** | SAML 2.0 and OIDC support with private connectivity using AWS PrivateLink within AWS GovCloud. |

### Current challenges

**Limited self-service for central teams.** Central DevSecOps teams today depend on GitLab support tickets for platform configuration, which slows their ability to deliver capabilities to developers. Every customization or workflow adjustment requires coordination with our team.

**AI adoption barriers.** Agencies want AI-assisted development, but the current offering does not yet provide connections to agency-approved FedRAMP AI services.

**Platform management overhead.** Without a self-service control plane, central teams lack real-time visibility into platform health and usage patterns, which limits their ability to optimize the platform and demonstrate value to leadership.

**Migration complexity.** Agencies with existing GitLab instances face friction migrating to Dedicated for Government, particularly when coordinating across distributed teams and geographic regions.

## Where we're going

Our roadmap is organized around enabling central DevSecOps teams to deliver value to their developers. We prioritize based on:

1. **Developer productivity** — accelerate deployment velocity
2. **Central team enablement** — reduce operational overhead
3. **Compliance & security** — automate compliance
4. **Scale & automation** — extend impact across multiple agencies

> **Note:** Future capabilities are proposed and not commitments. Timing is subject to change based on customer demand and technical dependencies.

### In development: Empowering central teams

**Self-service control plane (Switchboard for Government)**

Central DevSecOps teams will manage their platform without support ticket dependencies, configuring workflows, monitoring platform health, viewing usage metrics, and customizing environments at their own pace.

_Impact: Removes the biggest friction point central teams face today, which is dependency on GitLab support for routine platform management._

**Agency-approved AI services (Duo integration)**

Enable GitLab Duo features using agency-approved FedRAMP AI services (Azure AI, AWS Bedrock) while maintaining data residency and security boundaries. Developers get AI-assisted development without compromising compliance.

_Impact: Unlocks modern developer productivity tools within government compliance requirements, with flexibility to use the agency's approved AI provider._

**Enhanced service level commitments**

Clear, measurable SLA improvements for mission-critical platforms:

| Commitment | Target |
| --- | --- |
| Recovery Point Objective (RPO) | 4-hour maximum data loss |
| Recovery Time Objective (RTO) | Prioritized restoration by mission impact |
| Availability (SLO) | Targets aligned with FedRAMP requirements |

### Coming next: Scaling & connectivity

**Cloud connectivity toolkit**

Secure data migration across geographic regions using Site-to-Site VPN connectivity, which reduces latency for distributed teams and enables smoother transitions to Dedicated for Government.

_Impact: Removes major barriers for agencies with existing GitLab instances or geographically distributed development teams._

**IPv6 support**

IPv6 networking capabilities to meet federal networking requirements and modernization mandates (OMB M-21-07).

_Impact: Enables agencies to comply with federal networking standards while modernizing infrastructure._

**Advanced Geo capabilities**

Expanded multi-region deployment options and additional connectivity methods for agencies with complex geographic or data residency requirements.

### Future capabilities under consideration

The following are being evaluated based on customer demand and mission impact:

| Capability | Description |
| --- | --- |
| **Agency-approved AI services (DAP integration)** | GitLab Duo Agent Platform features with FedRAMP authorization and maintained data residency |
| **Hosted CI/CD runners** | GitLab-managed runners eliminate the need for agencies to provision and maintain CI/CD infrastructure |
| **FedRAMP High authorization** | Higher security authorization for agencies with more stringent requirements or classified workloads |
| **Multi-cloud support** | Deployment options beyond AWS GovCloud (Azure Government, Google Cloud for Government) |
| **Additional compliance certifications** | DoD Impact Levels, StateRAMP, and other government-specific compliance frameworks |
| **Managed AI gateway** | Centralized gateway for AI integrations with governance, monitoring, and multi-model support |

## Pricing

GitLab Dedicated for Government follows the [GitLab Dedicated pricing model](https://about.gitlab.com/pricing/?deployment=dedicated) with government-specific considerations.

| Component | Details |
| --- | --- |
| **GitLab Ultimate licenses** | Per user |
| **Instance infrastructure & management** | Tiered by instance size (S, M, L, XL, XXL) |
| **Storage** | Based on data volume |

**Government accommodations:** Pricing is structured to support federal budget planning cycles, GSA Schedule purchasing vehicles, and flexible payment terms aligned to fiscal year cycles.

---

Questions about roadmap timing or specific capabilities? Contact your GitLab account team or reach out in [#f_gitlab_dedicated](https://gitlab.slack.com/archives/f_gitlab_dedicated).
