---
title: Proof of Value (POV)
description: Proof of Value (POV)
---

## Proof of Value (POV) and Trial

> **Status:** Working draft for SA leadership, Sales, Fulfillment, Professional Services, and Product review.
>
> **Purpose:** Replace the current POV page with one operating model for customer evaluations, using a common lifecycle and two execution modes: **Simple** and **Extended**.

## Executive summary

A Proof of Value (POV) is a qualified, outcome-led technical evaluation that gives a customer and GitLab evidence for a commercial or implementation decision.

A trial is the product access mechanism; a POV is the managed business and technical motion around that access. Every formal POV should have a reason to evaluate, named participants, defined scope, measurable success criteria, an execution owner, a decision date, and a recorded result. The standard is intentionally lightweight for commercial and lower-complexity motions, while enterprise, strategic, usage-sensitive, and multi-team evaluations use stronger planning and measurement.

## 1\. What is a POV?

A **Proof of Value** is a time-bound, qualified evaluation in which GitLab and the customer agree on:

* The customer problem or business outcome being addressed.
* The technical capabilities and use cases to be validated.
* The measurable criteria that determine success.
* The people, environment, timeline, and responsibilities required.
* The decision that follows the evaluation: technical win, technical loss, or inconclusive.

A POV is not:

* A generic demo.
* A no-commitment sandbox with no success criteria.
* A substitute for discovery, architecture, implementation, training, or paid consulting.
* A catch-all label for every free trial or technical question.

Use **trial** when the primary purpose is feature or capability validation. Use **POV** when the evaluation is qualified, outcome-led, and tied to a technical or commercial decision. A trial can be customer-initiated and self-guided; a POV normally requires explicit scoping and an accountable GitLab owner.

## 2\. The standard POV model

GitLab uses one lifecycle with two execution modes.

### Simple execution

Best for customer self-guided, commercial, lower-complexity, or lightly assisted evaluations.

Required assets are a concise scope, a pre-checklist, a use-case playbook or smoke test, a named owner, lightweight progress tracking, and an outcome check. The goal is speed and repeatability without removing qualification or measurement.

### Extended execution

Best for enterprise, strategic, multi-team, higher-risk, usage-sensitive, or transformation-oriented evaluations.

Required assets include a scope document, success-criteria table, participant list, prerequisites, risks log, schedule, collaboration project, use-case playbook, baseline and target metrics, midpoint check, final readout, and complete system-of-record hygiene.

Commercial does not always mean Simple, and Enterprise does not always mean Extended. Segment is the starting bias; complexity, risk, number of stakeholders, deployment model, and usage economics determine the final mode.

## 3\. Types of POVs and trials

| Type | Primary owner | Typical mode | Customer experience | Minimum standard |
| :---- | :---- | :---- | :---- | :---- |
| Customer-initiated or self-guided | Customer, with AE/SA available as needed | Simple | Customer starts through the website or product trial flow and validates capabilities independently | Trial scope, eligibility, product guidance, support path, and outcome capture where the opportunity is active |
| SA-assisted trial | AE \+ SA | Simple or Extended | Customer receives scoped technical guidance, enablement, and cadence | Qualification, use cases, success criteria, owner, schedule, and result |
| Partner-led | Partner, with GitLab account team oversight | Simple or Extended | Partner leads implementation or evaluation with GitLab supporting product and escalation needs | Named partner/customer/GitLab owners, scope, handoffs, success criteria, and commercial next step |
| Professional Services trial | PS \+ AE \+ SA | Extended by default | Customer evaluates through a services-led implementation or workshop | Statement of work or defined service boundary, delivery plan, success criteria, acceptance, and transition plan |
| Pilot | Customer \+ GitLab cross-functional team | Extended | Customer validates in a representative environment with a limited user or project population | Project discipline, named roles, metrics, governance, risk management, formal readout, and rollout recommendation |

### 3.1 Customer-initiated or self-guided trials

A customer can start an eligible GitLab trial directly, without an SA:

* Ultimate self-serve trial — from the website or an in-product upgrade prompt, for GitLab.com or self-managed.
* DAP (Duo Agent Platform) self-serve trial for prospects — a free SaaS trial capped at 100 users for 30 days, or a free self-managed trial (GitLab 18.9+) with no user cap; both include DAP evaluation credits automatically, so a prospect does not file a Fulfillment credit request. Existing paying customers use the SA-assisted DAP trial in Section 6 instead, since their credits are a one-time allocation against an active subscription.
* Monthly Commitment self-service purchase — since February 3, 2026, an eligible Premium/Ultimate SaaS or self-managed-cloud-license customer can buy DAP Monthly Commitment credits directly in the Customer Portal without a sales-assisted order. Self-managed offline, Dedicated, reseller, and multi-year subscriptions still require a sales-assisted purchase.

The account team should not automatically convert every self-guided trial into a POV. Convert it to an SA-assisted POV when one or more of the following is true:

* The customer has a named business outcome and decision date.
* The opportunity is late-stage or strategically important.
* The customer needs architecture, deployment, security, compliance, migration, or integration guidance.
* The evaluation includes usage-based or credit-governed capabilities.
* Multiple teams, environments, or decision-makers must coordinate.

For trials that stay self-guided, give the customer a product playbook, prerequisites, a smoke test, and a support route — do not commit dedicated SA time without qualification.

### 3.2 SA-assisted trials

An SA-assisted trial is the default model when the customer needs technical guidance but does not require a full transformation program. The SA and AE agree on the execution mode before the trial starts.

#### Enterprise and Commercial / Lite SA-assisted trials

Default to Extended when the customer is enterprise or strategic and the evaluation includes multiple stakeholders, multiple products, Self-Managed or Dedicated deployment, security/compliance requirements, complex integrations, or a material commercial decision.

GitLab frames this as **Use Case Validation** — proving business value against a defined outcome, most often using the **3 Goals in 30 Days ("3-in-30")** framework: 1 to 3 measurable technical goals tied to business outcomes, proven in 30 days with structured weekly checkpoints.

Default to Simple for commercial and lower-complexity opportunities when the customer can move quickly with limited SA touch. The Lite path is not an unqualified enterprise-guided trial.

**Mandatory before kickoff**

| Requirement | Enterprise SA-assisted | Commercial / Lite SA-assisted |
| :---- | :---- | :---- |
| Opportunity and context | Opportunity, customer context recorded in SalesForce, decision date, stakeholders, and commercial path recorded | Opportunity, customer problem/capability, customer context, and decision date recorded |
| Roles and ownership | Named executive approver, technical champion, evaluators, AE, SA, and escalation contacts | Named customer owner, evaluators, AE, SA, and support/escalation contact |
| Goals and success | One to three business or technical goals with baseline, target, metric, and evidence plan | One to three focused goals or technical checks with a clear success check for each |
| Scope | In-scope and out-of-scope use cases, workflows, participants, and evidence defined | In-scope use cases or smoke tests and completion criteria defined |
| Environment and prerequisites | Deployment model, version, licenses/seats, repositories/projects, integrations, access, and all technical prerequisites validated or scheduled | Deployment and access prerequisites validated; supported configuration and sample data/project identified |
| Risks | Technical, security, network, legal, adoption, timing, and resource risks documented with owners | Known blockers, support path, and material risks documented |
| Schedule | Mutual schedule with kickoff, cadence, midpoint check, final readout, and decision date | Target start/end dates, kickoff, light cadence, and outcome check scheduled |
| Customer agreement | Customer acknowledges the scope, responsibilities, plan, and decision criteria | Customer acknowledges the scope, responsibilities, and next step |
| System of record | POV record created, linked to the opportunity, and ready for ongoing updates | POV record or opportunity notes created and ready for closeout |

Use Extended instead when the Lite trial has more than one material risk, requires multiple teams, needs custom architecture, involves usage-sensitive products, or is likely to become a pilot.

### 3.3 Partner-led trials

A partner can lead the technical evaluation directly with the customer, with the GitLab account team providing product expertise, escalation support, and commercial oversight. Name the partner owner, the customer owner, and the GitLab AE/SA of record before the trial starts; define handoff points where the partner stops and GitLab starts, and vice versa; and confirm success criteria and the commercial next step jointly, since a partner's own success criteria may not map automatically to GitLab's technical-win definition.

### 3.4 Professional Services trials

A Professional Services (PS) trial runs as a services-led implementation or workshop rather than a self-directed evaluation, and defaults to Extended. It requires a statement of work or a clearly defined service boundary, a delivery plan, success criteria agreed with the customer, a formal acceptance step, and a transition plan back to the account team (AE/SA/CSM) once the engagement closes.

### 3.5 Pilots

A pilot validates GitLab in a representative slice of the customer's real environment — a limited set of users, teams, or projects — rather than a demo environment, and defaults to Extended. It requires the same project discipline as a full Extended POV (named roles, metrics, governance, risk management) plus a formal readout and an explicit rollout recommendation for expanding beyond the pilot population.

## 4\. Standard trial lifecycle

| Stage | Objective | Required actions | Required output | Simple | Extended |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1\. Request | Start with a clear customer need | AE or customer submits request; identify product, opportunity, timeline, customer owner, and requested support | Intake/request and linked opportunity | Required | Required |
| 2\. Qualify | Confirm the evaluation is worth dedicated effort | Validate pain, impact, decision process, champion, decision date, technical fit, risks, and mode | Go/no-go decision and execution mode | Required | Required |
| 3\. Scope | Agree what will be proven | Select one to three goals, use cases, metrics, participants, in/out of scope, environment, and schedule | Scope and success-criteria table | Concise | Full |
| 4\. Prepare | Remove blockers before the clock starts | Complete access, licensing, version, network, data, runner, security, legal, and support checks; test a smoke path | Readiness checklist, playbook, and collaboration location | Minimum checks | Full preflight and dry run |
| 5\. Kick off | Align both teams on how the evaluation will run | Confirm scope, roles, dates, communication, success criteria, and escalation path | Kickoff notes and agreed plan | Required | Required |
| 6\. Execute | Validate the selected use cases | Run the product workflows, track issues, capture evidence, and maintain cadence | Progress notes, issue log, evidence | Async or light cadence | Weekly or twice-weekly cadence |
| 7\. Measure | Determine whether the goals were met | Compare evidence to baseline and target; conduct midpoint check for Extended and DAP | Metric/evidence update and midpoint decision | Outcome check | Midpoint review and surveys |
| 8\. Feedback | Capture customer and product feedback while there is still time to act | Get survey feedback; identify use cases requiring bug fixes, enhancements, Product Management action, or Customer Support action; create and track issues | Feedback record, issue links, and updated POV report/evaluation record | Outcome feedback | Midpoint and ongoing feedback review |
| 9\. Read out | Make the technical decision | Present results and feedback to decision-makers; state technical win, loss, or inconclusive | Final readout and recommendation | Concise readout | Formal readout |
| 10\. Record and transition | Convert learning into action | Update POV record, opportunity, result, next step, close timing, feedback, issues, and handoff to Sales, CS, PS, Support, Product, or Engineering | System-of-record update and transition plan | Required | Required |

### 4.1 Feedback and issue-management requirements

Feedback is an explicit lifecycle gate, not an activity reserved for the final readout. Collect survey feedback at the midpoint and end of the trial, and capture feedback during the weekly cadence. Ask which use cases are working, which require bug fixes or enhancements, and which issues need Product Management, Engineering, or Customer Support follow-up.

For every new customer request or material issue:

* Create an issue that conforms to the applicable customer request template, including the customer context, use case, expected behavior, actual behavior, business or technical impact, evidence, priority, and customer-facing comments.
* Record the issue link and current status in the POV report you are maintaining either in the POV evaluation plan or customer collaboration project.
* Record the issue and associated feedback in the evaluation document or collaboration project.
* Link the issue to the relevant use case and success criterion so the impact on the technical result is visible.
* Carry open issues, owners, and next actions into the final readout and transition plan.
* Make sure to update your [General Notes](#general-notes) in the POV Object.

### 4.2 Minimum system-of-record fields

The [POV record](#tracking-a-pov-in-salesforce) should include

* the linked opportunity,
* subscription when applicable,
* POV type,
* execution mode,
* product/motion,
* start and end dates,
* status,
* result,
* SA/AE owners,
* customer champion,
* success criteria,
* collaboration link,
* trial or credit request link,
* and next step.

For usage-based trials, link the subscription identifier and credit request so usage and trial status can be inspected together.

### 4.3 Day in the Life of a POV

This section presents the POV lifecycle from the perspective of the people doing the work. It is an operating view for AEs, SAs, and SA Managers: who acts, what good looks like, and what must be true before the POV moves to the next stage.

The role-based rhythm below is designed for a 30-day evaluation, but the responsibilities apply to Simple, Extended, Enterprise, Commercial/Lite, partner-led, PS-led, pilot, and DAP motions. Use the [DAP AE Checklist](https://docs.google.com/presentation/d/1Xw49Kdz8xihfoMQ5Mlq-h5ig0IM0jrOFtElhT_IlRdc) and [POV Evaluation Plan Checklist](https://docs.google.com/document/d/1XzttRqG8r7fQmQv4ZRbe6vv6hO_8VWQLC7CgDnZQNp8) for detailed templates and timing examples.

#### Role-by-stage operating view

| Stage | AE / Rep | SA | SA Manager | Stage exit / best practice |
| :---- | :---- | :---- | :---- | :---- |
| **1\. Request** | Confirm the customer has asked to evaluate a defined capability or outcome. Confirm the opportunity, customer owner, decision date, and requested support. For DAP, submit the DAP trial/credit request issue once the request has enough customer and opportunity context. | Create the Salesforce POV Object as soon as the customer indicates interest in moving forward. Associate it to the correct opportunity, enter the planned future Start Date and End Date, select the POV Type, and add the initial product, customer problem, and plan link. | Acknowledge the request, assess SA capacity and complexity, and identify the approval path. Do not approve a vague request or allow the team to promise a start date before qualification and readiness are complete. | POV Object exists in `New`; opportunity and owners are clear; future dates are entered; request is linked to the initial plan or evaluation record. |
| **2\. Qualify** | Establish business impact, champion, executive buyer, decision path, commercial timing, and next commercial step. Confirm this is not merely a generic demo or renewal activity. | Validate technical fit, platform (SaaS, Self-Managed, or Dedicated), deployment model, use-case fit, risks, prerequisites, and whether the evaluation is Simple or Extended in the POV Plan. | Confirm the evaluation is worth dedicated SA effort, determine the appropriate level of governance, and identify resource, security, legal, credit, or partner/PS exceptions. | Go/no-go and execution approach are agreed; the customer has a credible reason to evaluate and a decision path. |
| **3\. Scope** | Align the customer on participants, decision-makers, decision date, commercial next step, and what the customer must provide. Confirm the customer will acknowledge the plan. | Create or tailor the POV Scope Plan. Define one to three goals, measurable success criteria, use cases, users, environment, in/out of scope, risks, roles, timeline, and evidence. Do not send a generic template without customer-specific content. | Review the plan for completeness, customer commitment, technical feasibility, resource demand, and risk. Identify gaps before approval. | Customer-specific POV Plan exists; goals, use cases, owners, users, success criteria, risks, and decision date are documented. |
| **4\. Prepare** | Create or coordinate the customer-facing POV process slides. Present the goals, use cases, roles, timeline, prerequisites, success criteria, responsibilities, and decision plan to the customer. Obtain customer agreement. Schedule kickoff, configuration time, weekly cadences, midpoint survey, final survey, and readout. | Create the Evaluation Plan, Customer Collaboration Project, Issue List, and POV Report tab. Select the use-case playbook, write configuration/install instructions, schedule the smoke test and dry run, test the use cases in a control/demo environment, and prepare the kickoff deck. For DAP, confirm use cases, users, credits, readiness, and the DAP configuration plan. | Review the POV Object, customer-approved POV Plan/slides, readiness, schedule, use cases, and risks. Approve the POV before kickoff. For DAP, review and approve the AE-submitted request issue; after approval, provision credits if authorized or route provisioning through the approved owner. | SA Manager approval is recorded; customer has acknowledged the plan; configuration day, smoke test, kickoff, cadence, and readout are scheduled; collaboration and reporting locations exist. |
| **5\. Kick off** | Lead commercial alignment and introductions. Ensure the customer owner, technical champion, evaluators, decision-makers, and executive buyer understand the plan and cadence. Confirm communication channels and weekly executive reporting. | Run the kickoff. Review goals, success criteria, scope, roles, schedule, issue process, and escalation path. Set the day to configure the environment, complete access checks, run the smoke test, and confirm the customer can execute a representative workflow. | Confirm approval and readiness gates are satisfied. Approve exceptions only when documented. Ensure the SA does not move the POV to active execution without the agreed plan and prerequisites. | Move the Salesforce POV Object from `New` to `In Progress` at kickoff. The environment, access, smoke path, and first execution step are ready. |
| **6\. Execute** | Maintain executive and commercial alignment. Send the weekly email or Slack report to the executive buyer, remove account blockers, maintain the opportunity, and keep the commercial decision date current. | Guide the customer through the use cases. Conduct the agreed weekly or twice-weekly cadence, record progress and issues, update the POV Report, maintain the Issue List, capture evidence, and update Salesforce General Notes with the weekly forecast summary. | Inspect progress, usage, blockers, customer engagement, and SA capacity. Coach the team, approve exceptions, and intervene when the evaluation is drifting or the customer is not executing. | Use cases are actively progressing; evidence and issues are recorded; the account team and customer know the next actions and owners. |
| **7\. Measure** | Confirm the evaluation remains connected to the customer's business decision. Validate that the executive buyer is seeing progress and that the commercial next step remains current in the Opportunity. | Compare evidence to baseline and target. Track use-case completion, technical metrics, usage, adoption, and readiness for the final decision. Conduct the midpoint check and survey at approximately Day 15\. | Review whether the evidence is sufficient, whether the POV is on track for a technical result, and whether additional support or an approved change in scope is needed. | Evidence is sufficient to discuss progress against success criteria; midpoint feedback and risks are visible. |
| **8\. Feedback** | Obtain customer and executive-buyer feedback. Ask what is working, what is blocked, and what must be addressed for a decision. Escalate product, support, commercial, or executive asks. | Conduct midpoint and final surveys, plus ongoing feedback collection. Create or contribute to issues using the customer request template. Record bugs, enhancements, Product Management requests, Engineering actions, and Customer Support requests in the POV Report, Evaluation Plan, collaboration project, and issue records. | Ensure feedback is actionable, issues have owners and paths, and material gaps are reflected in the forecast and final decision. Decide whether to continue, stall, extend, or close based on evidence. | Feedback is captured while there is still time to act; every material issue is linked to a use case or success criterion and has an owner. |
| **9\. Read out** | Present business value, customer impact, commercial recommendation, and next step to the executive buyer and decision-makers. Make the ask explicit: proceed, expand, remediate, or stop. | Deliver the technical readout. Show success criteria, evidence, use-case results, product gaps, issues, customer feedback, and recommendation: Successful, Unsuccessful, or Inconclusive where applicable. | Confirm the technical and commercial recommendation is supported by evidence. Ensure the final readout and customer decision are reflected in the forecast and Salesforce record. | Final readout occurs with decision-makers; result and next step are agreed or explicitly unresolved. |
| **10\. Record and transition** | Update the Opportunity SA Next Steps field with `<action, owner, and due date>`. Lead procurement, expansion, rollout, close-lost, or transition activity. | Update the POV Object, General Notes, Result, closeout reason, POV Report, Evaluation Plan, collaboration project, issue links, and handoff records. Close the object as Successful or Unsuccessful, or mark it Stalled if it is paused without a final decision. | Inspect Salesforce hygiene, outcome quality, conversion, unresolved issues, and lessons learned. Confirm stalled and unsuccessful reasons are specific and that any follow-on work has an owner. | Salesforce, the Opportunity, the Evaluation Plan, the POV Report, the collaboration project, and issue records tell the same story. |

#### Stage 1: Request — the first day in the life of a POV

The request stage establishes whether the evaluation is real, owned, and worth planning. The account team should not treat a customer request as approval to begin execution.

**AE / Rep actions**

* Confirm the customer's reason for evaluating, desired outcome, decision date, customer owner, and requested GitLab support.
* Confirm the opportunity and commercial path. Identify the executive buyer, technical champion, and decision-makers as early as possible.
* For a DAP POV, submit the DAP trial or credit request issue with the customer, opportunity, subscription, user count, requested credits, use cases, timeline, and evaluation-plan link once the request is sufficiently scoped.
* Set expectations that the evaluation begins after the plan, readiness, and approvals are complete—not when the request is first received.

**SA actions**

* Create the Salesforce POV Object immediately when the customer indicates interest in moving forward.
* Link the object to the correct Account and Stage 3 — Technical Evaluation Opportunity.
* Enter the planned future Start Date and End Date, POV Name, POV Type, Products Being Evaluated, owners, and initial Success Criteria or POV Plan link.
* Create the initial evaluation workspace or identify where the POV Plan will be developed.
* Keep the object in `New` until the evaluation has been approved and kicked off.

**SA Manager actions**

* Confirm that the request has an accountable SA, a credible opportunity, and a likely execution path.
* Identify whether the request needs Simple or Extended discipline, but keep that designation in the POV Plan and evaluation documentation rather than treating it as a Salesforce field.
* Flag capacity, legal, security, platform, DAP credit, partner, PS, or support dependencies early.
* Establish what must be true before approval and kickoff.

**Request-stage output**

* Salesforce POV Object in `New` with future dates.
* Correct Account, Opportunity, owner, SA, customer, POV Type, and product/motion.
* Initial request or plan link.
* Named next action, owner, and due date in the Opportunity SA Next Steps field.

#### The 30-day POV operating rhythm

| Timing | AE / Rep | SA | SA Manager |
| :---- | :---- | :---- | :---- |
| **Week 0 / T-14 to T-2** | Confirm business case, customer participants, decision-makers, and commercial path; coordinate POV process slides and customer acknowledgement; submit DAP request issue when applicable. | Scope goals and use cases; create the POV Plan, Evaluation Plan, collaboration project, Issue List, POV Report, configuration plan, and smoke test; schedule kickoff, cadences, surveys, and readout. | Review the POV Object and plan; approve the POV and any DAP credit request; provision DAP credits after approval when authorized. |
| **Day 0** | Lead kickoff alignment and confirm executive communication. | Run kickoff, configure the environment, validate access, complete the smoke test, and start the first use case. | Confirm the evaluation is ready and status is moved to `In Progress`. |
| **Weeks 1–2** | Send weekly executive-buyer email or Slack report; remove commercial blockers; keep Opportunity SA Next Steps current. | Run use cases, conduct weekly/twice-weekly cadence, update POV Report, record issues, and update General Notes. | Inspect progress, customer engagement, blockers, and resource load. |
| **Day 15 / Week 2** | Confirm the customer's business and executive feedback. | Conduct midpoint survey/checkpoint, compare evidence to targets, and adjust the plan only with agreement. | Decide whether the evaluation remains on track or needs intervention, scope correction, or escalation. |
| **Weeks 3–4** | Prepare the executive buyer for the final decision and commercial next step. | Complete use cases, gather final evidence, resolve or disposition issues, conduct final survey, and prepare the readout. | Review evidence, outcome quality, and closeout readiness. |
| **Day 30 / Week 4** | Present the business recommendation and lead the commercial next step. | Deliver technical readout; record feedback, result, issues, and transition actions. | Confirm Salesforce, forecast, POV Report, and Opportunity hygiene; approve closeout or documented stall disposition. |

#### DAP-specific callouts

DAP adds a usage and credit-control path to the normal POV lifecycle:

1. **AE / Rep submits the DAP request issue.** Include the opportunity, subscription, customer-specific evaluation plan, user count, use cases, requested credits, dates, deployment model, and any retrial or extension context.
2. **SA validates the technical plan.** Confirm the customer's use cases, users, platform, version, access, configuration, runner/network readiness, smoke test, evidence, and timeline.
3. **SA Manager reviews and approves.** Confirm the Salesforce POV Object, non-renewal opportunity, customer-specific plan, credible decision path, user count, readiness plan, schedule, customer-facing slides, and measurement plan.
4. **SA Manager or authorized provisioning owner provisions credits after approval.** Provision only within the approved credit ceiling and record the provisioning result in the POV records.
5. **The account team does not start the DAP clock until the customer can execute.** Configuration, smoke test, kickoff, cadence, surveys, executive reporting, issue tracking, and final readout must be planned.
6. **The AE/Rep reports progress weekly to the executive buyer.** The SA supplies technical status, use-case progress, issues, feedback, and evidence.

#### Where each type of information belongs

| Information | System of record / working location | Purpose |
| :---- | :---- | :---- |
| POV summary, status, dates, owners, type, result, General Notes | Salesforce POV Object | Technical forecast, management inspection, and outcome hygiene |
| Opportunity SA Next Steps | Salesforce Opportunity | `<action, owner, and due date>` for the next commercial or account-team action |
| Summary weekly status | General Notes in the POV Object in Salesforce | Summary by Week of Status (Red, Green, Yellow), Customer Sentiment, Blocker or Issue, that SA Managers can report on, during weekly POV cadences and Technical Forecasts |
| Detailed weekly status and POV Running Report | POV Report tab or section in the POV Evaluation Plan or in your Collaboration Project | Full execution history, progress, customer sentiment, issues, and evidence |
| Detailed tasks, issues, and work tracking | POV Evaluation Plan or Customer Collaboration Project / Issue List | Joint customer/GitLab execution and issue ownership |
| Success criteria and final results | POV Plan / Evaluation Plan | What was agreed, what was proven, and what remains unresolved |
| Product bugs, enhancements, PM, Engineering, or Support requests | Customer request issue with links back to the POV Report in the POV Evaluation Plan or Customer Collaboration Project and use case | Cross-functional action and traceability |
| DAP credit request and provisioning evidence | DAP request issue plus Salesforce POV Object and Evaluation Plan | Approval, credit governance, usage, and audit trail |

The best practice is to keep Salesforce concise enough for forecast inspection, while maintaining a complete POV Running Report in the Evaluation Plan. The SA Manager should be able to understand the current state from General Notes and then consult the POV Report when the forecast requires more detail.

## 5\. Trial evaluation checklist

The checklist is product-neutral. Product-specific pre-checklists add detail; they do not remove the common requirements.

### 5.1 Unified trial evaluation checklist

The checklist is product-neutral. Product-specific pre-checklists add detail; they do not remove the common requirements. Every row below must be addressed; the Enterprise / Extended and Commercial / Lite columns define the minimum evidence for each mode.

| Checklist area | Common requirement | Enterprise / Extended | Commercial / Lite |
| :---- | :---- | :---- | :---- |
| Qualification | Customer problem, impact, decision date, champion, decision-makers, competitive context, and reason GitLab is being evaluated | Mandatory discovery, decision process, champion, decision-maker, impact, and risk review | Mandatory problem, owner, decision date, and opportunity context |
| Scope | Goals, use cases, in-scope and out-of-scope items, target environment, and expected evidence | Scope document plus full evaluation plan or collaboration project | Concise scope and playbook/checklist |
| People | Customer owner, evaluators, approvers, GitLab AE, SA, partner/PS owner if relevant, and support/escalation contacts | Full participant and role map, including approver and support contacts | Customer owner, evaluators, AE, and SA |
| Goals and success | Baseline, target, metric owner, evidence source, and result definition | One to three goals with baseline, target, metric, and evidence plan | One to three focused goals or technical checks |
| Use cases | Named workflows that can produce evidence | Named use cases, workflow steps, owners, prerequisites, and status tracking | Named use cases or smoke tests with completion criteria |
| Environment | GitLab deployment model, version, edition, namespaces/projects, repositories, IDEs, languages, runners, integrations, network, and data requirements | Full deployment, architecture, security, network, integration, and data readiness | Minimum deployment/access readiness and supported configuration |
| Access | Licenses/seats, roles, permissions, service accounts, groups, projects, and required admin availability | All access and admin prerequisites validated or scheduled with owners | Minimum roles, permissions, licenses, and admin availability confirmed |
| Readiness | Prerequisites complete, smoke test successful, representative projects/data available, and customer resources scheduled | Full preflight and dry run; no evaluation clock until blockers are cleared | Minimum checks and a successful smoke path before kickoff |
| Execution | Kickoff, cadence, issue tracking, communications, evidence capture, and decision checkpoints scheduled | Kickoff, weekly/twice-weekly cadence, midpoint, final readout, and decision date | Kickoff and agreed async or light cadence |
| Risk and governance | Known technical, security, network, legal, adoption, and timing risks with owners and escalation path | Formal risks log, escalation plan, and legal/security review where needed | Known blockers and support path |
| Measurement and feedback | Usage/adoption, customer feedback, technical result, and commercial transition evidence | Baseline/target evidence, midpoint review, final report, and survey where applicable | Outcome check and customer feedback |
| System of record | POV record, opportunity, collaboration link, trial/credit request, result, and next step | POV record complete and maintained throughout | POV record or opportunity notes complete at close |
| Approval and transition | Buyer/approver, target next step, procurement timing, expansion or rollout path, and ownership after trial | SA manager or designated approver for material resource, license, credit, or risk exceptions | SA/AE approval for scope and capacity; manager escalation when exceptions exist |

### 5.2 Other Preparation Tasks

1. For self-managed evaluations, confirm the customer architecture is ready;
2. for SaaS evaluations, confirm the customer's network can reach GitLab.com;
3. create the customer success collaboration project;
4. for the largest strategic opportunities, notify GitLab Support of POV dates and customer details in the relevant Slack channel;
5. for SaaS trials that need CI/CD, request trial-runner activation.

## 6\. POV products and motions

The same lifecycle applies across solution areas. Use the category playbook, success-criteria library, and smoke tests for the chosen motion.

### 6.1 Platform qualification and execution nuances

Every motion must be qualified against the platform where the customer will evaluate it. Platform choice changes the prerequisites, ownership, timeline, support model, security discussion, and evidence required; it does not create a separate POV lifecycle.

| Platform | Qualification questions | Execution nuances |
| :---- | :---- | :---- |
| SaaS | Is GitLab.com permitted for the customer's data, users, integrations, and compliance requirements? Can the customer provide the group/project owners, representative repositories, users, and any required external integrations? | Fastest path. Focus on namespace/group configuration, project access, user onboarding, SaaS runners or customer runners, data usage expectations, and usage dashboards. Use a controlled pilot group/project rather than enabling the whole organization by default. |
| Self-Managed | What GitLab version, license, cloud licensing mode, network egress, runners, integrations, admin capacity, and upgrade path are available? Are there security, residency, air-gap, or self-hosted model requirements? | Add installation/configuration time to the plan. Validate version, licensing sync, network paths, runners, instance/group settings, service accounts, and support ownership before the clock starts. Self-hosted or offline AI requires a separate architecture and readiness plan. |
| Dedicated | What Dedicated environment, region, upgrade schedule, administrative boundary, network path, and customer-controlled integrations apply? Who can configure the environment and how long will approvals take? | Treat environment readiness, provisioning, change windows, and access approvals as first-class dependencies. Confirm feature availability and version timing, coordinate with the Dedicated owner, and schedule a technical dry run before customer kickoff. |

For all three platforms, the SA must record the platform, target environment, version or release constraint, access owner, prerequisites, known risks, smoke test, and evidence source in the POV plan.

| Motion | Typical POV question | Example evidence |
| :---- | :---- | :---- |
| Core DevOps / DevSecOps | Can GitLab improve delivery flow, collaboration, and operational visibility? | Pipeline execution, deployment frequency, lead time, traceability, tool consolidation, or migration result |
| Security and Compliance | Can GitLab reduce risk and improve security/compliance workflow? | Findings caught pre-production, remediation time, policy enforcement, audit evidence, or tool consolidation |
| Duo Agent Platform | Can customers safely adopt AI agents and flows for measurable developer and security outcomes? | Use-case completion, adoption, time saved, MR/pipeline/security evidence, credit consumption, surveys, and rollout recommendation |
| Flex capabilities | Can usage-aware AI capabilities be adopted with an agreed value and consumption model? | Use-case value, usage pattern, guardrails, budget band, and adoption plan |
| Duo Hosted Runners | Can hosted execution remove infrastructure friction and improve flow throughput? | Queue time, flow completion, execution reliability, setup effort, and cost/operating model |
| Secrets Manager | Can GitLab centralize and govern secrets in the customer workflow? | Secret lifecycle, access controls, rotation, audit evidence, and reduced exposure risk |
| Orbit and future motions | Can the capability solve a defined workflow or governance outcome? | Category-specific workflow evidence, adoption, risk controls, and commercial next step |

### 6.2 How to Handle POVs by Product

Do not create a separate POV lifecycle per product — build category-specific enablement assets instead: qualification prompts, success-criteria examples, prerequisites, configuration checklists, smoke tests, use-case playbooks, evidence templates, and known gotchas. The four success-criteria libraries already built (DAP, Security/Compliance, Agile Planning, CI/CD) are the model to extend to Flex, Duo Hosted Runners, Secrets Manager, and Orbit as those motions mature.

### 6.3 DAP Self Hosted Models

**Custom/self-hosted models:** any POV involving a self-hosted or custom AI model must be tracked in a confidential issue in the Custom Models project (mandatory), because the Custom Models team has limited concurrent capacity. Engage that team during qualification to validate feasibility, confirm support availability, and agree success criteria before committing to a timeline.

## 7\. Tracking in Salesforce (System of Record) {#tracking-a-pov-in-salesforce}

The Salesforce **POV Object is the single system of record for every POV and trial**. It is the management summary for the opportunity, while the POV Plan, evaluation document, customer collaboration project, and issue records contain the detailed execution evidence.

Every Self-Managed, Cloud, Dedicated, and usage-based trial with SA involvement requires:

* A Salesforce POV Object entry.
* SA Manager sign-off after review of the POV Plan and readiness.
* A clear association to the relevant opportunity.
* Ongoing status, progress, result, and next-step hygiene.

Create the POV Object once the customer has indicated interest in moving forward and the evaluation is associated with the relevant opportunity at **Stage 3 — Technical Evaluation**. Do not wait until the evaluation is complete to create the object, and do not create duplicate POV Objects for the same evaluation.

> **DAP note:** DAP request, credit, readiness, and execution requirements are maintained in the [Duo Agent Platform POV and Trials Handbook](/handbook/solutions-architects/playbooks/pov/ai.md). This section defines the Salesforce hygiene required for DAP and all other SA-involved POVs.

### 7.1 When a POV is requested: create the object immediately

When the customer requests a POV, agrees to a technical evaluation, or the account team commits to an SA-assisted trial:

1. Create the Salesforce POV Object immediately.
2. Associate it to the correct Account and Stage 3 opportunity.
3. Enter the **planned future Start Date** and planned End Date.Do not backdate the start date to the request date or create a historical object after execution has started.
4. Select the POV Type. Record Simple/Light or Extended/Heavy in the POV Plan and supporting evaluation documentation; it is not a Salesforce POV Object field.
5. Add the initial customer problem, proposed use cases, product/motion, and intended decision date.
6. Link the draft or working POV Plan, evaluation document, or collaboration project when available.
7. Keep Status as `New` while the evaluation is being qualified, planned, and reviewed.

A future Start Date signals the expected kickoff; it is not permission to begin execution. The evaluation clock starts only after the team is ready, the customer has agreed to the plan, and the required approval has been completed.

### 7.2 Salesforce POV Object fields

Complete the required fields at request, then add or update the supporting fields as the plan matures.

| Field | When required | Guidance |
| :---- | :---- | :---- |
| POV Owner / SAE | At request | Name the accountable SA/SAE. Do not use a team alias. |
| Customer Success Manager | At request when applicable | Add the CSM who owns the post-sale or transition relationship. |
| Solutions Architect | At request | Name the SA executing or technically accountable for the POV. |
| POV Name | At request | Use a searchable convention such as `<Account> — <Product/Motion> — <POV>`; avoid generic names. |
| Account | At request | Associate the object to the correct customer account. |
| Opportunity | At request | Link the Stage 3 — Technical Evaluation opportunity that will track the technical and commercial outcome. |
| Start Date | At request | Enter the planned future kickoff/start date. Update only when the agreed plan changes. |
| End Date | At request | Enter the planned evaluation end/readout date. Extend only with a documented reason and updated plan. |
| POV Type | At request | Identify the motion: customer-initiated, SA-assisted, partner-led, PS trial, or pilot. |
| Subscription | When applicable | Add the active subscription, especially for usage-based, DAP, or credit-governed evaluations. |
| Products Being Evaluated | At request or scope | List the actual products/capabilities in scope; do not use a generic 'GitLab' label. |
| Success Criteria | Before manager approval | Link the customer-specific POV Plan or evaluation document. The plan must contain measurable goals, use cases, evidence, and decision criteria. |
| POV Milestone in Collaboration Project | Before kickoff | Link the customer collaboration project or issue. If no project exists, link the evaluation plan until the project is created. |
| SA Manager Leader Approved | Before kickoff | Obtain SA Manager approval after the manager reviews the POV Plan, readiness, opportunity, and execution mode. |
| General Notes | Weekly and at milestones | Maintain the forecast-level weekly summary using Week \#, Status, Progress, Customer Sentiment, Main Blocker / Issue, and Decision / Readout. Keep the latest week at the top. |
| Status | Throughout | Use `New`, `In Progress`, `Stalled`, or `Closed` according to the status guidance below. |
| Result | At close | Select `Successful` or `Unsuccessful` only when the POV Object is being closed. |
| Closeout notes / reason | At close or when stalled | Record evidence, customer decision, unresolved gaps, and a specific unsuccessful or stalled reason. |

The separate **SA-validated technical evaluation start/end date fields are deprecated**. Consolidate POV tracking into the Salesforce POV Object.

### 7.3 SA Manager approval workflow

The AE/Rep or SA creates the POV Object first; the SA Manager approves the evaluation after reviewing the object, POV Plan, and opportunity context.

Before approval, the SA Manager should confirm:

* The POV Object is linked to the correct opportunity and Account.
* The opportunity is a credible technical evaluation and is not a renewal-only motion.
* The planned future Start Date and End Date are realistic.
* The POV Type, product/motion, and platform are clear. Record the execution mode in the POV Plan, not in the Salesforce POV Object.
* The POV Plan is customer-specific, not a copied template.
* Goals, use cases, success criteria, participants, users, responsibilities, and decision date are defined.
* The customer-facing plan has been presented or is scheduled for customer agreement.
* Technical readiness, configuration, smoke test, access, and support prerequisites are complete or have dated owners.
* The collaboration project, evaluation document, and issue-tracking location are linked.
* Capacity, risk, credits, and any required cross-functional approvals are understood.

After approval, set **SA Manager Leader Approved** to Yes and record any conditions or exceptions in General Notes. Do not start the POV or provision trial resources while approval is pending.

### 7.4 Marking a POV In Progress

Move the POV Object from `New` to **`In Progress` at kickoff**, when the customer and GitLab have begun the agreed evaluation activities.

Before changing the status:

* Confirm the customer has agreed to the scope, schedule, roles, and success criteria.
* Confirm the planned Start Date, End Date, and decision/readout date.
* Confirm the SA Manager approval is recorded.
* Confirm the required platform, access, configuration, smoke test, and support prerequisites are ready or actively executing against a dated plan.
* Confirm the POV Plan, collaboration project, and issue-tracking location are linked.

Do not mark a POV In Progress merely because an object was created, a discovery call occurred, or a generic demo was delivered. `In Progress` means the evaluation is actively being executed against an agreed plan.

### 7.5 Updating General Notes with POV progress {#general-notes}

General Notes are the concise Salesforce management summary used by the SA Manager in the POV technical forecast. They are not a replacement for the SA Next Steps, detailed POV Report, Evaluation Plan, collaboration project, issue board, or meeting notes.

Use the SA Next Steps field on the opportunity to record the next steps for the entire opportunity, regardless of POV activity. SA Next Steps should record `<action, owner, and due date>`. This is maintained on the Opportunity, not the POV Object.

Update General Notes at least weekly and at every material milestone. Use **Week \#**, not a date, as the heading. A standard 30-day evaluation uses `Week 1`, `Week 2`, `Week 3`, and `Week 4`, with the latest week at the top and `Week 4` as the final evaluation week.

Record one main blocker or issue in General Notes for your manager. Record all details, all the issues you create, and all customer feedback in the detailed POV Report tab you maintain in your Evaluation Plan or collaboration project.

Recommended format:

```text
Week 4
Status: Green / Yellow / Red
Progress: <what was completed against the success criteria>
Customer Sentiment: <positive / mixed / at risk, with evidence>
Main Blocker / Issue: <primary blocker or issue affecting progress, owner, and escalation>
Decision / Readout: <current decision, readout date, or next commercial/technical step>

Week 3
Status: Green / Yellow / Red
Progress: <prior-week progress>
Customer Sentiment: <positive / mixed / at risk, with evidence>
Main Blocker / Issue: <primary blocker or issue affecting progress, owner, and escalation>
Decision / Readout: <prior-week decision or next step>

Week 2
Status: Green / Yellow / Red
Progress: <prior-week progress>
Customer Sentiment: <positive / mixed / at risk, with evidence>
Main Blocker / Issue: <primary blocker or issue affecting progress, owner, and escalation>
Decision / Readout: <prior-week decision or next step>

Week 1
Status: Green / Yellow / Red
Progress: <initial progress against the success criteria>
Customer Sentiment: <positive / mixed / at risk, with evidence>
Main Blocker / Issue: <primary blocker or issue affecting progress, owner, and escalation>
Decision / Readout: <initial next step>
```

A good General Notes update should answer:

* What changed this week against the agreed use cases and success criteria?
* What is the current status: Green, Yellow, or Red?
* What is the customer sentiment and level of engagement?
* What is the main blocker or issue, who owns it, and what is the escalation path?
* What is the current decision, readout date, or next commercial/technical step?

The **POV Report tab in the Evaluation document** is the detailed execution record. Put the full status narrative, weekly progress, customer feedback, and every issue the SA or account team created or contributed to in the POV Report. Link each issue and relevant evidence from the report to the use case or success criterion.

The SA Manager should use General Notes for the technical forecast. When more detail is needed, the SA Manager should consult the POV Report tab in the Evaluation Plan. A good practice is to maintain a **POV Running Report** throughout the evaluation so the final readout and Salesforce closeout are based on a complete execution history.

Do not paste detailed issue histories, meeting transcripts, or long status narratives into General Notes. Summarize the management signal there and maintain the source detail in the POV Report, Evaluation Plan, collaboration project, or issue record.

### 7.6 Closing the POV Object

Close the POV Object when the evaluation has reached its agreed end/readout, the customer has made a decision, or the account team has determined that the evaluation will not resume.

Before closing:

1. Complete the final technical review against every success criterion.
2. Capture customer and executive-buyer feedback.
3. Record open bugs, enhancements, Product Management actions, Engineering actions, and Customer Support actions.
4. Deliver or schedule the final readout and document the commercial or rollout next step.
5. Update General Notes with the final evidence and decision.
6. Set Status to `Closed`.
7. Set Result to either `Successful` or `Unsuccessful`.
8. Add a concise closeout note with the reason, evidence, unresolved gaps, and next owner/action.
9. Update the linked opportunity, collaboration project, evaluation plan, and trial/credit record.

#### Successful

Use `Successful` when the customer and GitLab have sufficient evidence that the agreed technical success criteria were met or the customer explicitly accepted the outcome and is moving to the agreed commercial, rollout, or implementation next step.

The closeout notes should include:

* The use cases and success criteria validated.
* Evidence or metrics supporting the result.
* Customer confirmation or readout outcome.
* Commercial, rollout, procurement, or transition next step.
* Any remaining issues that do not prevent the stated result.

#### Unsuccessful

Use `Unsuccessful` when the POV did not meet the agreed success criteria, the customer selected another path, the product or architecture was not a fit, the customer could not execute, or the evaluation ended without a credible path forward.

The unsuccessful reason must be specific and evidence-based. Examples include:

* Technical success criteria not met.
* Product gap, bug, or required enhancement prevented success.
* Deployment, security, network, data, or configuration constraint prevented execution.
* Customer did not provide the required users, time, access, data, or decision participation.
* Competitive or architectural decision favored another solution.
* Timing, budget, procurement, or organizational priority changed.
* Customer disengaged or made no decision after the agreed follow-up path.

Do not use "Unsuccessful" without a reason. If the evaluation is still active but blocked, use `Stalled` instead.

### 7.7 Marking a POV Stalled

Use **`Stalled`** when the POV is not actively progressing because of a material blocker, customer pause, missing prerequisite, resourcing issue, or decision delay—but the team has not yet made a final closeout decision.

When marking a POV Stalled:

* Change Status from `New` or `In Progress` to `Stalled`.
* Add the stalled reason in General Notes and closeout notes.
* Name the owner responsible for resolving the blocker.
* Record the next action and a specific review or restart date.
* Link the blocking issue, customer communication, or decision record.
* Stop presenting the POV as actively executing until the customer and GitLab agree to restart.

When the blocker is resolved, update the plan and move the POV back to `In Progress` at the restart/kickoff checkpoint. If the POV will not resume, close it as `Unsuccessful` with a clear "stalled/no decision" or other evidence-based reason.

### 7.8 Status and hygiene rules

| Status | Use when | Required Salesforce action |
| :---- | :---- | :---- |
| New | POV requested, object created, qualification or preparation underway | Future dates, required fields, plan links, and approval path recorded |
| In Progress | Kickoff occurred and the evaluation is actively executing | General Notes updated weekly; progress, issues, and next steps linked |
| Stalled | Evaluation paused or blocked without a final decision | Reason, owner, next review date, and blocker link recorded |
| Closed | Evaluation completed or will not resume | Result set to Successful or Unsuccessful; closeout evidence and next step recorded |

Avoid these hygiene failures:

* Creating the POV Object after the trial has already started.
* Leaving Start Date or End Date blank or using dates that do not match the customer plan.
* Creating duplicate objects for the same POV.
* Leaving Status as `New` after kickoff.
* Leaving a blocked evaluation as `In Progress`.
* Closing without selecting Successful or Unsuccessful and documenting why.
* Pasting detailed meeting notes into General Notes without linking the source record.
* Leaving the POV Object, opportunity, evaluation plan, collaboration project, and issue records out of sync.
