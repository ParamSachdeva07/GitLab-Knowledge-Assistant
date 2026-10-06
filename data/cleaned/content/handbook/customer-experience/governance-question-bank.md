---
title: "AI Governance Discovery Question Bank by Industry"
description: "A structured question bank of industry-specific AI governance, risk, and compliance (GRC) discovery questions designed to help organizations identify regulatory, safety, and accountability requirements before deploying AI tools"
---

## Overview

The Industry AI Governance Discovery Question Bank is a tool designed to proactively address the governance, risk, and compliance (GRC) issues associated with deploying AI and software tooling across various sectors. It contains eight specific, governance-focused questions for 25 different industries (such as Aerospace & Defense, Banking, Healthcare, etc.)

The purpose of the document is to help organizations identify potential blockers related to regulations, safety, data protection, and accountability before they build or deploy an AI solution.

### Shifting Governance Discovery Left

The concept of "shifting left" means moving essential non-functional requirements, in this case, AI governance, risk assessment, and compliance questions from later in the adoption lifecycle to the very beginning (the discovery or design phase).

This shift is critical to prevent delays and slow adoption for the following reasons:

- **Avoids Costly Rework and Deployment Blockers**: If regulatory and security questions (e.g., "Who is the Authorizing Official," "Are there restrictions on using cloud AI services," "What audit logs are required") are only asked late in the process, the resulting AI tool may be architecturally non-compliant, unsafe, or unable to meet regulatory standards like HIPAA or ISO 26262. Discovering this late forces expensive, time-consuming rework, which is the primary cause of slowing down or halting adoption
- **Enforces Compliance by Design**: By asking the questions in the Discovery Question Bank upfront, teams can design the AI system with required controls built in from the start. For example, a financial services team asking about SR 11-7 model risk management (MRM) frameworks early can immediately define the required model versioning and auditability controls, making the final deployment frictionless
- **Establishes Clear Accountability**: The questions force early identification of the owners and approvers ("Who approves AI tools," "Who is accountable"). This ensures that security authorities (like ISSMs in Aerospace & Defense) or governance bodies (like an AI risk committee in Banking) sign off on the intent and architecture rather than acting as a final, surprised gatekeeper for a completed system
- **Manages Data and IP Risks**: Questions address sensitive issues like data residency, IP constraints, and the segregation of client-confidential information. Addressing these restrictions early (e.g., confirming whether proprietary data can be shared with external AI services) prevents potential legal or contractual breaches that would immediately halt adoption.

In summary, the document facilitates the "shift left" strategy by providing a structured, industry-specific checklist, ensuring that necessary governance checks are integrated into the initial planning stages, thereby enabling faster, safer, and compliant AI adoption.

### General Questions

1. Scope & policy: What formal policies or frameworks govern how your organization evaluates and approves new AI or developer tools?
2. Ownership: Who is the accountable owner (team/role) for AI governance decisions, and how are exceptions or escalations handled?
3. Data access: How do you classify data, and which classes are AI tools explicitly allowed or prohibited from accessing (code, logs, customer data, regulated data, etc.)?
4. Vendors & hosting: What requirements apply to AI vendors and hosting locations (e.g., security certifications, data residency, third-party risk reviews)?
5. Controls & approvals: What controls do you require before production use (e.g., security review, privacy review, legal review, risk sign-off, change-management)?
6. Logging & auditability: What level of logging, traceability, and evidence do you need (who used which tool, on what data, with what outcome) for audit or investigations?
7. Lifecycle & monitoring: How do you manage the lifecycle of AI tools and models (onboarding, updates, monitoring for drift/incidents, decommissioning)?
8. Safety, bias & misuse: How do you assess and monitor AI tools for bias, safety, and misuse, and what is your process for pausing or rolling back a tool if issues are found?

[Download the full AI Governance Discovery Question Bank (PDF)](/pdfs/customer-experience/industry-ai-governance-question-bank.pdf)

---
