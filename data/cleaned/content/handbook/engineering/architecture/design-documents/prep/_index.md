---
title: PREP Architecture
status: proposed
creation-date: "2026-02-19"
authors: [ "@pursultani, @sarahwalker, @a_richter" ]
coaches: [ "@WarheadsSE" ]
dris: [ "@product-manager", "@engineering-manager" ]
owning-stage: "~devops::platforms"
participating-stages: []
toc_hide: true
---

<!-- vale gitlab.FutureTense = NO -->

{{< engineering/design-document-header >}}

## Summary

The GitLab product is unique in that we run it in many different ways - Self-Managed, Dedicated, Dedicated for Government, and GitLab.com (SaaS), each with distinct capabilities and constraints. Without guidance, teams can hit platform incapabilities late in development, when fixes are costly and delays become a real risk.

PREP (Platform Readiness Enablement Process) changes that. PREP embeds platform readiness intelligence directly into the GitLab development lifecycle in order to ensure GitLab features ship successfully across all deployment targets by keeping platform requirements visible, assessable, and actionable at every stage.

This document provides a high-level architectural overview of the PREP process and automated toolchain support. It describes system structure, the key entities and processes that comprise it, and how they collaborate to deliver our Platform Readiness Intelligence at scale. More detailed architectural specifications for PREP and the content model will be provided in companion documents.

## Motivation

Platform compatibility is currently a late stage concern. Sometimes features designed to work on GitLab SaaS have different requirements for our self-managed or Dedicated customers, which are only surfaced after design decisions have been made. This has led to rework, delays, and emergency escalations. Given there is a limited number of platform team members with this expertise, we need to democratise this knowledge in order to scale faster.

PREP aims to do just that. By embedding platform requirements directly into the workflows developers already use, PREP distributes platform expertise across the organization without increasing the burden on our Platform teams.

PREP Automation *augments* human judgment within this system, it does not replace it.

### Goals

- Establish the architectural context and motivation for PREP: that there is one paved path to General Availability (GA) across all deployment targets
- Describe PREP four-tier structure; Content, Process, Automation, and Stakeholders, and how they collaborate to deliver platform readiness intelligence
- Show how PREP integrates into GitLab development lifecycle and the broader GitLab process ecosystem, serving as a foundation for the future design
- Outline the AI-assisted toolchain that will support the PREP process
- Provide a stable process foundation that can expand with toolchain evolution
- Support phased delivery, from targeted automation toward a fully AI-driven system

### Non-Goals

- Define GitLab system integration, API specifications, or UI/UX design
- Document exhaustive edge cases
- Outline the governance model for organizational process ownership

### Background

Platform readiness evaluation at GitLab predates PREP. Several independent readiness processes evolved across the organization to address specific deployment contexts:

- [The Production Readiness Review](/handbook/engineering/infrastructure-platforms/production/readiness/), governing deployments to GitLab.com
- [The Delivery Operational Readiness Review](https://gitlab.com/gitlab-org/gitlab/-/blob/df973a6d104cd94a9fb3f8172696a4944fdbcc46/.gitlab/issue_templates/Operational%20Readiness.md), governing Self-Managed deployments
- [The Feature Readiness Assessment](https://gitlab.com/gitlab-org/architecture/readiness), the direct predecessor to PREP, now superseded by this framework
- [The Dedicated Operational Readiness Review](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team/-/blob/main/.gitlab/issue_templates/operational_readiness.md?ref_type=heads), governing the GitLab Dedicated platform

These frameworks shared a common set of limitations: they were built around large checklists with limited contextual guidance, provided little traceability between requirements and evidence, and placed a coordination burden on feature teams through manual engagement with subject matter experts across multiple groups. As GitLab's platform footprint and feature velocity have grown, the limitations of this checklist-driven approach have become increasingly untenable.

PREP is currently operational as a guided, checklist-driven process for GA promotion, managed through the [`gitlab-org/architecture/readiness` repository](https://gitlab.com/gitlab-org/architecture/readiness/). Product teams complete relevant assessment templates progressively as their feature matures through PoC, Beta, and Pre-GA stages, with infrastructure and platform stakeholders reviewing and approving before GA promotion is granted.

This architecture defines the next evolution of that process from a repository-based checklist to a lifecycle-embedded, AI-assisted readiness system.

## Proposal

PREP consolidates and supersedes these independent processes under a single, coherent framework built around four interconnected elements:

- **Content** — The authoritative body of platform requirements and considerations that define what production readiness means across all deployment targets. Currently maintained as structured checklists; intended to evolve into a curated, AI-accessible knowledge base.
- **Process** — The lifecycle-aligned workflow that governs how readiness is evaluated from initial feature design through to general availability. The process is intentionally independent of the content it operates on, allowing both to evolve separately.
- **Automation** — The AI-enabled toolchain that operationalizes the process, acting as a developer-friendly interface to PREP content and reducing the manual coordination burden that characterized legacy approaches. Described in detail in the companion toolchain architecture document.
- **Stakeholders** — The full set of participants in the PREP ecosystem, including subject matter experts who contribute to and maintain platform requirements content, and feature team members who engage with the assessment process throughout the development lifecycle.

The next iteration of PREP introduces an AI-enabled toolchain architecture that automates and augments the PREP process: the *how* behind detecting platform compatibility issues, delivering contextual guidance to developers, and improving that guidance over time.

The toolchain is a set of AI-assisted components integrated with GitLab's SDLC touchpoints, designed to surface platform readiness requirements at the right moment with the right level of detail, reducing late-stage discovery and emergency escalations.

The PREP process is designed to be embedded alongside the GitLab SDLC, with an event-driven triggering model and decision flow.

![PREP Architecture](/images/engineering/architecture/design-documents/prep/prep.png)

### Architecture Components

#### Content (persistent state)

- Platform Requirements: infrastructure/security/data expectations, owned by platform teams
- PREP Assessments: living records of a feature's readiness, owned by feature teams
- Feature Artifacts: epics, issues, designs, MRs, code; consumed but not owned by PREP
- Architectural Guidelines: standards from the Architecture Board; consumed but not owned by PREP

#### Process (workflows)

- Evaluation Cycle (core): triggered by feature lifecycle changes or requirement updates; evaluates features against requirements, identifies gaps, delivers guidance
- Governance (supporting): keeps Platform Requirements current in response to infrastructure changes
- Quality Control (supporting): monitors Evaluation Cycle performance and surfaces improvement signals

#### Stakeholders

1. Platform Teams, who own and maintain Platform Requirements
2. Feature Teams, who own Feature Artifacts and their assessments

#### Automation (AI tooling)

This architecture consists of several Duo Agents, including but not limited to:

- PREP Assistant Flow will be the next iteration of the current PREP assistant, and act as the human interface into the overall assessment process.
- PREP Governance Flow describes the process by which PREP requirements are maintained and updated as the GitLab platform evolves. This component follows a continuous integration model, incorporating both human input and automated agents to ensure requirements remain current.
- PREP Quality Control is the process by which the accuracy and effectiveness of PREP are monitored. It provides the foundation for success metrics and enables observability into the overall process.

### Development Proposal

### Phase 1 - Foundation

The aim of this phase is to create a first version of our workflows. The PREP AI assistant already exists, so this phase will deliver the scaffolding of our automations:

1. Create a schema for our Requirements Knowledge base. This is the foundation from which we can create Requirements
1. Create a first iteration of our Customiser agent. This agent will access the Requirements to help inform participants which parts of PREP are necessary.
1. Create a first iteration of a Factfinder agent. This will return information about a feature, such as the Epic, Merge Requests, or Design Doc. This will be used to help inform the customiser agent.

### Phase 2 - Intelligence

During this phase, PREP gains the ability to detect, assess, and guide feature teams automatically, then gets smarter over time by learning from past evaluations and building deeper domain expertise. We will iterate on the above workflows as we discover limitations and opportunities in Phase 1.

### Phase 3 - Scale

This phase extends the system across the full breadth of GitLab feature development, introducing specialised agents, each capturing the deeper domain knowledge of a specific platform area, and the Requirements knowledge base growing, eventually allowing PREP to iterate upon itself.

## Alternative Solutions

### 1. Continue with Manual Process and Expanded Checklists

Rather than introducing agentic workflows, we could expand and refine the existing manual checklist-driven approach. This would involve consolidating the current independent readiness processes (PRR, ORR, Feature Readiness Assessment, and Dedicated ORR) into a single, comprehensive checklist maintained in the readiness repository. Teams would continue to navigate the repository, copy templates, and complete assessments manually, but with improved organization, clearer guidance text, and better cross-linking between related requirements.

- Advantages: This approach requires minimal tooling investment and leverages existing team familiarity with the current process. It avoids the complexity of building and maintaining agentic systems and their associated infrastructure.
- Disadvantages: This approach does not address the core limitations that motivated PREP. Manual processes remain difficult to scale as feature velocity increases, discovery burden remains high for teams to self-identify applicable requirements, and there is no mechanism to provide context-aware guidance tailored to specific features or development stages. The coordination overhead on platform stakeholders persists, and without systematic feedback loops, the checklist cannot improve based on real-world outcomes. As GitLab's platform footprint grows, this approach will continue to result in late-stage discovery of platform incompatibilities and emergency escalations.

### 2. Do Nothing: Maintain Status Quo

Continue operating the current fragmented landscape of independent readiness processes without consolidation or enhancement. Teams would continue to navigate separate PRR, ORR, Feature Readiness Assessment, and Dedicated ORR workflows, each with its own repository, templates, and approval gates. No investment would be made in tooling, automation, or process unification.

- Advantages: This approach requires zero engineering effort and avoids any organizational change management. Teams already familiar with existing processes face no disruption.
- Disadvantages: This is the least viable path forward. The current fragmentation actively harms feature delivery: teams must navigate multiple disconnected processes, requirements are duplicated and inconsistent across frameworks, and there is no single source of truth for platform readiness. As documented in the Current Limitations section, the checklist-driven approach has become increasingly untenable as platform footprint and feature velocity have grown. Late-stage discovery of platform incompatibilities will continue to drive rework, delays, and emergency escalations. Without consolidation or improvement, this approach guarantees continued scaling problems and perpetuates the coordination burden on platform teams that PREP is designed to alleviate.
