---
title: "Architecture Review Board (ARB)"
description: "Charter, scope, and operating model for GitLab's Architecture Review Board."
---

## Vision & Mission

### Vision Statement

To establish a collaborative architecture governance practice that enables strategic technology investments, eliminates waste, ensures compliance and drives cross-functional alignment—positioning the ARB as a trusted partner that helps the business solve problems and make informed decisions about our technology ecosystem.

### Mission

The Architecture Review Board serves as the central decision-making body and strategic advisor for enterprise technology architecture. We drive focused investments, eliminate duplicative spend, ensure cross-functional alignment, and provide early guidance to teams navigating technology decisions. Through collaborative problem-solving and clear governance, we enable the organization to build a coherent, secure, compliant, scalable, and efficient technology landscape.

## The Business Challenge

Our organization faces measurable challenges that require coordinated architectural governance:

**Software Sprawl & Duplicative Investment:** Without centralized oversight, teams independently procure similar tools, creating redundancy, integration complexity, and unnecessary spend across the enterprise.

**Misaligned Roadmaps:** Business units plan technology initiatives in isolation, resulting in conflicting dependencies, duplicated effort, and missed opportunities for shared solutions.

**Excessive Enterprise Spend:** Uncoordinated purchasing and renewals prevent strategic negotiations, volume discounts, and portfolio optimization.

**Reactive Decision-Making:** Teams select technology solutions late in the process without architectural guidance, leading to integration challenges, technical debt, and rework.

**Limited Cross-Functional Visibility:** No single forum exists where technology decisions can be evaluated holistically across security, compliance, data governance, and business impact.

## How the ARB Adds Value

The ARB serves four interconnected purposes, prioritized in this order:

1. **Collaborative Partner:** We work alongside business and technology teams to understand challenges, explore solutions, and provide architectural guidance early in the planning process. Teams are encouraged to engage the ARB when facing technology decisions, not just when seeking approval.
1. **Value Creation Engine:** We help teams identify existing capabilities, avoid duplicate investments, and align solutions to enterprise standards. Through roadmap reviews and strategic planning sessions, we drive focused investments that maximize business value.
1. **Decision-Making Authority:** We provide clear, timely decisions on software purchases, renewals, and major architectural changes. ARB approval is required before finalizing these commitments, ensuring alignment with enterprise strategy and architectural standards.
1. **Ongoing Governance:** We maintain oversight of the enterprise technology portfolio through regular roadmap reviews, standard setting, and continuous improvement of architectural practices.

## Scope & Authority

### Decision Authority

ARB approval is required before finalizing software purchases, renewals with scope changes, or major architectural modifications. The ARB operates with clear decision authority while prioritizing collaborative problem-solving and early engagement to ensure the best outcomes for the business. Additionally, all software spend exceeding $100,000 triggers the [Procurement RFP Policy](https://internal.gitlab.com/handbook/finance/procurement/). ARB Approval does not substitute for this requirement - both processes must be satisfied before a purchase is finalized.

### Within ARB Authority

**Software Procurement & Renewals**

- New software purchases (SaaS, licensed, or custom-built solutions)
- Software renewals with scope, cost, or architectural changes
- Proof-of-concepts or trials requiring production data or integration
- AI and ML tools, platforms, and capabilities

**Major Architectural Changes**

- Significant additions or modifications to systems impacting scalability, security, performance, or user experience
- New integrations between internal or external systems
- Platform migrations or technology stack changes
- Data architecture decisions with cross-functional impact

**Strategic Technology Planning**

- Business unit technology roadmap reviews for enterprise alignment
- Evaluation of emerging technologies and innovation initiatives
- Technology rationalization and consolidation efforts
- Standards development and architecture principle definition

**Governance & Oversight**

- System ownership and lifecycle management
- Architectural consistency and adherence to standards
- Technology portfolio reviews and health assessments
- Exception reviews for complex, high-risk, or cross-functional initiatives

### Outside ARB Authority

The ARB does not have authority over:

- Customer-facing product architecture or R&D tools
- Security software; ARB should be consulted, but does not have decision making authority.
- Day-to-day access management or user provisioning
- Minor configuration changes with no architectural impact
- Routine patching, updates, or maintenance following approved procedures
- Budget approvals (Finance/Department responsibility)
- RFP execution and vendor selection process (Procurement responsibility)
- ARB provides architectural input for requirements and evaluation criteria but does not own or replace the sourcing process
- Product feature prioritization (Product Management responsibility)
- Infrastructure operations and incident response (IT Operations responsibility)
- Personnel and organizational decisions (Leadership responsibility)

### Escalation Path

If a stakeholder disagrees with an ARB decision, they may escalate to their E-Group member for review and approval. If their E-Group member approves, it should be discussed with the CIO and CEO for a final decision. The ARB will provide documented rationale and impact analysis to support the E-Group decision process.

## Membership & Governance Structure

### ARB Leadership (Decision Authority)

This core group attends all ARB sessions and holds final decision-making authority:

- **Executive Sponsor:** CIO
- **Chair:** Head of Enterprise Architecture
- Head of Corporate IT
- Head of Data
- Head of Business Systems
- Sr. Director, Corp Sec
- Sr. Director, Procurement

### Core Advisory Members (Regular Attendees)

These members provide business context, surface duplication, and inform decisions. Attendance is expected but flexes based on relevance:

- Business Unit Technology/Operations Leads (Sales Operations, Marketing Technology, etc.)
- Solution/Application Architects
- Data & Analytics Leadership
- Product/Engineering Leadership
- Compliance & Privacy Representatives

### Topic-Based Participants (Ad Hoc)

These members engage for specific submissions requiring specialized expertise:

- Legal (contract terms, licensing, vendor risk)
- Finance (budget implications, cost modeling)
- Domain-specific experts as needed

## Operating Model

The following sections describe how the ARB operates and how teams engage with the board.

### How to Engage the ARB (Intake Process)

All ARB engagement begins through a [GitLab ARB Intake Issue](https://gitlab.com/gitlab-com/arb/intake). This centralized intake method ensures all requests are tracked, contain the necessary context, and are routed appropriately. Whether a team is seeking early guidance or formal approval, the same issue template is used.

### When to Engage

Teams should submit an ARB Intake Issue in two scenarios:

**Early Consultation:** Teams are encouraged to open an intake issue when they are exploring technology options, evaluating vendors, or planning initiatives that may fall within ARB authority. Early engagement allows the ARB to act as a collaborative partner, surfacing existing capabilities, identifying potential conflicts with other initiatives, and providing architectural guidance before significant effort is invested. Early consultation does not require a formal presentation or complete documentation; a summary of the problem, context, and direction is sufficient.

**Formal Approval:** A formal approval request must be submitted before initiating procurement, finalizing software purchases, making major architectural changes, or processing renewals with scope changes. This submission requires complete documentation as outlined in the intake issue template.

### Intake Issue Template Requirements

The GitLab issue template standardizes all ARB submissions. At a minimum, the template captures:

- **Request type:** Early Consultation or Formal Approval
- **Business context:** Problem statement, business need, and sponsoring business unit
- **Proposed solution:** Description of the technology, vendor, or architectural change being considered
- **Alternatives evaluated:** Other options considered and rationale for the proposed direction
- **Impact assessment:** Scope of impact across systems, teams, data, security, and compliance
- **Cost and timeline:** Estimated cost, contract terms, and implementation timeline
- **Alignment to enterprise standards:** Assessment against existing architectural standards and guardrails

For early consultations, not all fields are required. The template clearly indicates which fields are mandatory for each request type.

### Review Process

Once an intake issue is submitted, it follows a two-stage review process. The Chair (Head of Enterprise Architecture) is responsible for routing each request through the appropriate path.

#### Stage 1: Triage

The Chair reviews every incoming intake issue to assess completeness, determine scope, and decide the appropriate review path. During triage, the Chair may consult with relevant Core Advisory Members to gather additional context. The triage step results in one of three outcomes:

- **Fast-track resolution:** For requests that are low-risk, well-aligned with existing standards, and do not require cross-functional discussion, the Chair, in consultation with relevant ARB Leadership members, may approve the request directly. The decision and rationale are documented in the GitLab issue.
- **Scheduled for Full ARB Review:** For requests that are cross-functional, high-spend, architecturally significant, or require broader input, the issue is placed on the agenda for the next ARB session. Any request with estimated spend exceeding $100k will trigger the RFP process upon ARB approval, at which point the business team engages Procurement to begin the applicable RFP process.
- **Returned for additional information:** If the submission lacks critical detail, the Chair returns it to the requesting team with specific guidance on what is needed before the review can proceed.

#### Stage 2: Full ARB Review

Submissions routed to Full ARB Review are presented during a scheduled ARB session. The requesting team (Business Unit or IT Business Partner) presents the request, and the board evaluates it against enterprise strategy, architectural standards, existing capabilities, and cross-functional impact. The process is as follows:

1. **Presentation:** The requesting team presents the business context, proposed solution, and impact assessment.
1. **Discussion:** ARB Leadership and Core Advisory Members ask questions, surface concerns, and identify overlaps or dependencies with other initiatives.
1. **Decision:** ARB Leadership (Decision Authority) renders a decision, which is documented in the GitLab issue.

### Decision Outcomes

Every ARB review, whether fast-tracked or reviewed by the full board, results in one of the following documented outcomes:

- **Approved:** The request proceeds as submitted.
- **Conditionally Approved:** The request may proceed with specific conditions, modifications, or follow-up actions that must be completed.
- **Deferred:** The request requires additional information, further evaluation, or alignment with a pending initiative before a decision can be made.
- **Rejected:** The request does not align with enterprise strategy or architectural standards. The ARB provides documented rationale and, where possible, recommends alternative approaches.

All decisions are recorded in the corresponding GitLab issue with rationale, conditions (if any), and the names of the ARB Leadership members who participated in the decision.

## Meeting Cadence & Governance

**Cadence:** The ARB meets on a regular cadence to review formal submissions, conduct governance activities, and address ongoing oversight items. The Chair sets the agenda based on triaged intake issues and standing governance topics.

**Decision Authority:** ARB Leadership holds final decision-making authority for all in-scope items, as defined in the Membership & Governance Structure section of this charter.

**Attendance:** Core Advisory Members are expected to attend regularly to provide the business and technology context essential for informed decision-making. Topic-Based Participants are invited as needed based on the agenda.

**Documentation:** All decisions, rationale, and conditions are recorded in the corresponding GitLab issue. Meeting notes and action items are captured and made accessible to relevant stakeholders.

## Ongoing Governance & Oversight

Beyond individual request reviews, the ARB maintains continuous oversight of the enterprise technology portfolio through the following activities:

**Roadmap Reviews:** The ARB conducts regular reviews of business unit technology roadmaps to identify misalignment, duplicative investments, and opportunities for shared solutions or consolidation.

**Architectural Standards Management:** The ARB is responsible for defining, maintaining, and evolving enterprise architecture standards and guardrails. The ARB ensures all new and modified architectures adhere to these standards, as well as to mandatory internal security and data governance policies and relevant regulatory requirements (e.g., SOX, GDPR).

**Exception Management:** The ARB formally reviews and documents decisions on exceptions to approved architectural standards, particularly for complex or high-risk initiatives.

**Technology Portfolio Reviews:** Periodic assessments of the technology portfolio are conducted to evaluate health, identify rationalization opportunities, and inform strategic planning.
