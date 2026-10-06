---
title: "Fraud Governance Framework"
description: "Describes the governance model, roles, and RACI for GitLab's enterprise fraud program."
---

This page is the reference for how GitLab structures, governs, and operationalizes its fraud management program. It is intended to give teams a practical, shared view of **who owns what**, **how concerns escalate**, **who leads investigations**, and **which policies and reporting mechanisms support the program**.

## Visual Key

- **Purpose and Scope** — framework objectives, fraud risk categories, and detection methods
- **Governance** — governing bodies, principles, ownership, and oversight model
- **Roles and Responsibilities (RACI)** — program-level, incident-level, and scenario-based investigation ownership
- **Escalation Paths** — intake channels, severity-based escalation, and evidence handling & chain-of-custody
- **Reporting Structure** — incident-level and program-level reporting, Audit Committee updates
- **Policy Structure** — policy reference index, review and governance cycle, and training structure

---

## 1. Purpose and Scope

The Fraud Management Framework is designed to:

- **Provide a centralized governance model** for fraud risk management across GitLab.
- **Clarify roles and responsibilities (RACI)** for fraud prevention, detection, investigation, and reporting.
- **Establish escalation paths** and **investigation ownership** for different fraud scenarios.
- **Define the reporting structure** to executive leadership and the Audit Committee.
- **Organize the policy and training structure** supporting the enterprise fraud program.
- **Serve as the single source of truth (SSOT)** by providing a consolidated policy reference index with direct links to all related GitLab handbook pages and governance documents.

The definition of fraud and examples of fraud incidents can be found in the [Anti-Fraud Policy](/handbook/legal/anti-fraud-policy/).

For the purposes of the framework, a "fraud incident" is a validated report or reasonable indication that an act of the type described in the Anti-Fraud Policy has occurred or been attempted. Not all misconduct or policy abuse constitutes fraud. A matter is in scope only where the elements of fraud in the Anti-Fraud Policy are present.

The following fraud risk categories define the scope of this framework.

| Fraud Risk Category | Description / Examples | Key Detection Methods |
|---|---|---|
| **Financial Statement or SEC-related Fraud** | Revenue manipulation, improper journal entries, reserve misstatement | SOX controls, IA testing, analytics |
| **Team Member Asset Misappropriation** | Expense fraud, payroll ghost team members, theft of IP | Navan expense controls (policy limits, receipt matching, manager approval), expense analytics, access reviews, TMR investigations, IP Theft Detection by Signals Engineering |
| **Bribery & Corruption** | Kickbacks, facilitation payments, improper gifts | Third-party due diligence during vendor onboarding, training, whistleblower hotline, Navan expense controls |
| **Vendor / Procurement Fraud** | Shell vendors, bid-rigging, duplicate invoices, contract manipulation | Vendor master controls, 3-way match (PO ↔ receipt ↔ invoice reconciliation), analytics |
| **Platform Abuse** | Hosting/infrastructure abuse, bandwidth abuse, tier manipulation, seat/license manipulation, free-tier abuse, CI/CD abuse | Automated detection, deny-lists, usage analytics, Abuse monitoring and mitigation (Trust and Safety) |
| **Insider Trading / MNPI** | Trading on material non-public information | Blackout periods, pre-clearance, monitoring |

---

## 2. Governance Model

### 2.1 Governing Bodies

This table addresses each function's standing programmatic responsibilities. The operational first actions each function takes upon intake for any specific matter are described in Section 1 of the Fraud Response Playbook.

| Function | Primary Fraud Responsibilities |
|---|---|
| **Legal & Corporate Affairs (LACA)** | • Owns the **Anti-Fraud Policy**, Code of Business Conduct & Ethics, whistleblower hotline.<br>• Administers enterprise ethics and compliance-related training, including the Code of Conduct course, which includes a module devoted to **financial integrity** and fraud.<br>• Coordinates the **Ethics and Compliance Program** as the operational framework for fraud governance.<br>• Maintains the **enterprise fraud-related case register**, in coordination with Internal Audit, ensuring all related investigations are logged. |
| **Internal Audit** | • Performs the **annual operational fraud risk assessment** covering non-financial statement fraud risks (e.g., asset misappropriation, vendor fraud, platform abuse, bribery & corruption, etc.). Coordinates with SOX PMO to ensure comprehensive fraud risk coverage across both financial reporting and operational domains.<br>• Provides **independent assurance and advisory** over the fraud program and related internal controls.<br>• Advises on governance design (e.g., program structure, ownership model, etc.) and incident response protocols (e.g., investigation, escalation procedures, etc.). |
| **SOX PMO** | Owns the **annual financial statement fraud risk assessment** as part of the SOX compliance program. Evaluates fraud risks related to financial reporting, including revenue recognition, journal entry manipulation, and reserve misstatement. |
| **Finance (including Accounts Payable, Treasury, and Procurement)** | • Owns key **financial process controls** (e.g., expense reimbursement, vendor payments, treasury activities, etc.) that prevent and detect fraud.<br>• Implements and monitors corrective actions addressing identified high-risk fraud scenarios (e.g., expense fraud).<br>• Procurement team enforces **vendor onboarding controls, segregation of duties, and contract management** fraud safeguards. |
| **Team Member Relations (TMR)** | • Leads **team-member-related conduct investigations**, including fraud-related matters, with guidance from Security and LACA, including Employment, Corporate and Compliance, and Privacy teams within LACA, as appropriate.<br>• Manages **disciplinary actions, terminations, and exit protocols**, in consultation with LACA Employment and Corporate and Compliance teams when fraud is substantiated. |
| **Security (Security Operations including Trust & Safety, CorpSec, and Security Assurance)** | • Owns **technical and platform controls** for fraud and abuse (e.g., data loss prevention, monitoring for large downloads, platform abuse controls, deny-lists, trust & safety actions, etc.).<br>• Maintains the **Security Incident Response process** and coordinates with SIRT for fraud-related security events. |
| **Audit Committee** | Provides **board-level oversight** of fraud risk involving management and key financial reporting personnel, including review of investigation outcomes, remediation effectiveness, and escalated fraud reports from Internal Audit and LACA. |

### 2.2 Governance Principles

**Centralized design, distributed execution:** One coherent framework with clearly assigned DRIs; execution remains with specialist teams (LACA, Finance, Security, TMR, etc.).

**RACI-based clarity:** Each major fraud activity has a single Accountable DRI and defined Responsible/Consulted/Informed roles, consistent with GitLab's DRI and RACI guidance.

**Independence of Internal Audit:** Internal Audit provides advisory input, independent assurance, and, depending on the nature of the fraud concern, may lead or support investigations per the RACI matrices described herein. Internal Audit does not own business processes or disciplinary decisions. Per the Internal Audit Charter, Internal Audit has a mandate to oversee the adequacy of fraud governance as a whole by assessing whether fraud risks, controls, and reporting are appropriately designed and operating, and by communicating significant fraud-related risk exposures and control issues to the Audit Committee and E-Group.

**LACA visibility and ACP:** LACA maintains visibility to all fraud investigations through the enterprise fraud-related case [register](https://docs.google.com/spreadsheets/d/1EjJxCwTe2S5K52DoVpASJwj1rEIJB0H2c9M2ulmzhfk/edit?gid=2067029915#gid=2067029915)  and related communications, regardless of which team leads the investigation. This ensures consistent application of attorney-client privilege and engagement with outside counsel, when needed.

**TMR ownership of employee discipline:** Regardless of which function leads the fraud investigation, Team Member Relations (TMR) must be engaged whenever the matter may result in disciplinary action involving a team member. TMR leads all disciplinary decisions and actions including warnings, terminations, and exit protocols in consultation with Employment Legal and LACA Corporate and Compliance teams. Investigation ownership and disciplinary ownership are distinct: the expert function owns the investigation; TMR owns any resulting employee discipline.

**Learning orientation:** Outcomes from investigations, whistleblower cases, and risk assessments are fed back into policies, training, and controls.

**Single Source of Truth:** All fraud governance artifacts are published in the GitLab handbook where appropriate, providing a single source of truth for all team members. Confidential investigation details are protected consistent with applicable legal and privacy requirements.

---

## 3. Roles and Responsibilities (RACI Overview)

This list is the single source for functional DRI titles.

**Legend:** R = Responsible | A = Accountable | C = Consulted | I = Informed

> *For the purposes of this framework, the following individuals represent each function as the primary DRI:*
>
> - *LACA: Director of Legal, Compliance & Ethics (or delegate)*
> - *Internal Audit: VP, Internal Audit (or delegate)*
> - *Finance: CAO (or delegate)*
> - *TMR: VP, Team Member Relations (or delegate)*
> - *Security: CISO (or delegate)*
> - *Procurement: Director, Procurement (or delegate)*
> - *SOX PMO: Director, SOX PMO (or delegate)*
> - *Audit Committee: Audit Committee Chair*

The following section provides a high-level RACI for core fraud program activities.

### 3.1 Program-Level RACI

| Activity | LACA | Int. Audit | Finance (AP) | TMR / Emp. Legal | Security | Procurement | Audit Comm. |
|---|---|---|---|---|---|---|---|
| Design & maintenance of enterprise fraud governance framework | A / R | C | C | C | C | C | I |
| Anti-Fraud Policy & Code of Conduct (ownership & annual review) | A / R | C | C | C | C | C | I |
| Whistleblower / hotline administration | A / R | C | I | C | I | I | I |
| Annual operational fraud risk assessment / Annual financial statement fraud risk assessment | C | A / R C* | C | C | C | C | I |
| Fraud risk controls in financial processes (e.g., expenses, AP, etc.) | C | C | A / R | C | C | C | I |
| Fraud risk controls in security & platform | C | C | I | C | A / R | I | I |
| Fraud Training & Awareness | A / R | C | I | I | I | I | I |
| Enterprise fraud program reporting | A / R | A / R | C | C | C | C | I |
| Reporting significant fraud matters to Audit Committee | A/R | A / R | C | C | C | C | I |
| Vendor/third-party fraud controls | C | C | C | I | C | A / R | I |

*\* The annual financial statement fraud risk assessment is owned (A/R) by the SOX PMO. Internal Audit is consulted and provides independent assurance over the assessment. SOX PMO is not shown as a separate RACI column to keep the framework concise; detailed responsibilities are maintained in SOX PMO program documentation.*

### 3.2 Incident Response RACI

This RACI covers the fraud case lifecycle and responsible teams. See section 3.3 for investigation leads by fraud type.

| Activity | LACA | Int. Audit | Finance (AP) | TMR / Emp. Legal | Security | Procurement | Audit Comm. |
|---|---|---|---|---|---|---|---|
| Intake & registration of fraud incidents* | A/R | C | I | I | I | I | I |
| Case triage & determination of lead investigator** | C | C | A/R | A/R | A/R | A/R | I |
| Employee disciplinary action arising from any fraud investigation | C | I | I | A/R | I | I | I |
| Case closure | A/R | C | C | C | C | I | I |

*\* LACA owns the enterprise fraud-related register and is accountable for intake and case registration for all fraud incidents. To enable this, the relevant investigation lead - regardless of the team - is responsible for: (1) notifying LACA promptly when a fraud concern is identified, (2) keeping LACA informed of material developments throughout the investigation, and (3) confirming case closure, allowing LACA to accurately maintain the enterprise fraud-related case register.*

*\*\* When a fraud concern is reported, the team that receives it first is responsible for determining who should lead the investigation based on the scenario types in Section 3.3, and for notifying LACA to log the case. Where the appropriate investigation lead is not immediately clear, Internal Audit should be consulted and will determine the appropriate lead.*

### 3.3 Investigation-Level RACI (Scenario-Based Ownership)

This table is the sole source for assigning investigation ownership by fraud type. Section 2 of the Fraud Response Playbook describes the first operational actions for each fraud type, once the investigation lead has been confirmed.

| Scenario / Fraud Type | Investigation Lead (A/R) | Consulted (C) | Informed (I) |
|---|---|---|---|
| Team members asset misappropriation / expense fraud | TMR / Employment Legal | Finance (AP), Security (if technical evidence), Internal Audit, LACA | AC |
| Vendor / third-party procurement fraud | Procurement + Finance (AP) | Security, Internal Audit, LACA | AC |
| Bribery / corruption / improper payments | Internal Audit, in partnership with LACA as needed | Finance, Sales Leadership, Procurement | CLO, CFO, AC if material or regulatory |
| Financial statement or SEC-related fraud | Finance + LACA, with external counsel | CFO/CAO, Internal Audit, Security | CEO, Audit Committee, external auditors |
| Platform Abuse | Security | LACA, Product, Engineering, Internal Audit | CISO, CLO, AC if material |
| Insider trading / MNPI misuse | LACA with external counsel, as necessary | Finance, Security, Internal Audit | CLO, CEO, Audit Committee, SEC counsel |

> *In all scenarios, Internal Audit and/or the relevant investigation lead is responsible for notifying LACA at intake, providing updates on material developments, and confirming case closures, enabling LACA to accurately maintain the enterprise fraud-related case register.*
>
> *In any scenario where a team member may be subject to disciplinary action, TMR must be consulted and will lead the disciplinary process in consultation with LACA Employment, regardless of which function leads the investigation.*

---

## 4. Escalation Paths

Escalation paths ensure that suspected or confirmed fraud is handled quickly, consistently, and at the right level of seniority, including the Audit Committee where required.

### 4.1 Intake Channels

For most fraud concerns, team members should refer to the [Whistleblowing Policy](https://drive.google.com/drive/folders/1kB3k5FRnR3OUBP0Eyo3SxxyPKeiRFfUk) for the appropriate reporting channels, including anonymous reporting options and protections against retaliation.

For suspected platform abuse, concerns may be reported directly via Security and Trust & Safety channels, including using the `/Security` command on Slack, `#security_help`, `#abuse`, `abuse@gitlab.com`, or the GitLab abuse report function. These channels are staffed to respond to technically-oriented fraud (e.g., credential misuse, data exfiltration, CI/CD abuse, automated account creation, etc.) and may enable a faster initial response.

> *All validated reports will be logged centrally (LACA-owned enterprise fraud-related case register) with a unique identifier and minimal necessary details.*

### 4.2 Severity-Based Escalation

Fraud incidents are classified as CRITICAL, HIGH, MODERATE, or LOW. Severity level definitions based on fraud type, scoring factors, notification audience, and response targets are defined in, and governed exclusively by, Section 2 of the Fraud Response Playbook. Triage procedures for assigning and updating severity are addressed in Section 4 of the Fraud Response Playbook (TBD).

### 4.3 Evidence Handling & Chain-of-Custody

All fraud-related investigation records and evidence must be classified as RED per GitLab's Data Classification Standard, retained for a minimum of 7 years (or as required by applicable law), and managed on a need-to-know basis by the team leading the investigation. Detailed evidence handling procedures, including chain-of-custody protocols are maintained in the Fraud Response Playbook (TBD).

---

## 5. Reporting Structure

### 5.1 Incident-Level Reporting

**Case-level reporting**

LACA maintains a consolidated fraud register (including hotline cases, policy violations with fraud indicators, and significant control exceptions). All fraud investigation leads - regardless of team - are responsible for promptly notifying LACA when a fraud concern is identified and for providing status updates through case closure. This enables LACA to maintain complete visibility to the enterprise fraud case register and apply ACP protections consistently across all investigations. Where the appropriate lead is not immediately clear, Internal Audit will assess the initial facts, determine the appropriate lead based on the Scenario-based RACI matrix in Section 3.3, and notify LACA of the case details for registration before or concurrent with that determination.

As investigations develop, leads must coordinate with LACA to maintain documentation that summarizes, for example, the allegation (anonymized where appropriate), scope and status of investigation, preliminary and final conclusions, disciplinary actions (managed by TMR, in consultation with Employment Legal), and control remediations (with DRIs in Finance, Security, or other teams), as appropriate for the nature and severity of each investigation.

**Escalation to Audit Committee**

The Audit Committee receives briefings on: allegations involving management or key finance roles; significant fraud incidents with material financial, regulatory, or reputational impact; and themed or repeated issues indicating systemic fraud control gaps.

Internal Audit and LACA jointly coordinate these updates, consistent with the Audit Committee charter and internal audit reporting protocols.

### 5.2 Program-Level Reporting

At least annually, and more frequently as needed, Internal Audit will produce an **Enterprise Fraud Program Report** in coordination with LACA and functional stakeholders (Finance, Security, Procurement, TMR). The report is presented to the Audit Committee and a summary is shared with E-Group. The report includes:

- Summary of fraud risk assessment results and residual risk themes.
- Volume and characteristics of hotline and internal fraud cases (aggregated, anonymized).
- Key training and policy metrics (e.g., Code of Conduct and Anti-Fraud Policy acknowledgments, completion tracking, etc.).
- Control enhancement and remediation status for high-risk fraud scenarios.
- Planned roadmap items for the next 12 months.
- External regulatory developments and their impact on the fraud program.

---

## 6. Policy Structure

The fraud program is underpinned by a set of core policies and related procedures. This section defines how these policies fit together and who owns them.

### 6.1 Policy Reference Index

Please refer to GitLab's [Ethics and Compliance Program handbook page](/handbook/legal/ethics-compliance-program/) for a list of fraud-related policies, including:

1. Anti-Fraud Policy
2. Anti-Corruption Policy
3. Anti-Retaliation Policy
4. Code of Business Conduct & Ethics
5. Gifts & Entertainment, Political Activities & Contributions, and Charitable Contributions Policy
6. Insider Trading Policy
7. Related Party Transactions Policy
8. SAFE Framework
9. Third Party Risk Management Process

### 6.2 Annual Policy Reviews

- The Director of Legal, Compliance & Ethics (or delegate) coordinates the annual review of the policies outlined above using the existing policy change management process.
- As and when required, the VP, Internal Audit (or delegate) is formally included in the review workflow, with documented evidence of participation in a GitLab issue or equivalent tracker.
