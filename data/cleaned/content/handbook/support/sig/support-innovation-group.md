---
title: Support Innovation Group (SIG) Workflow and Approval Process
description: This page describes the Support Innovation Group (SIG) workflow and approval process for submitting, reviewing, and approving ideas.
---

## Overview

Ideas are submitted as an RFC (Request for Comments) under STM (Support Team Meta) work items using the RFC template and may propose a completely new tool or process, or improvements to an existing one. MRs are included in this scope if they contain updates to the process.

This inforamtion is accompanied by three process diagrams:

- Diagram 1 : High level overview: A simplified end-to-end view of the full process. Start here.
- Diagram 2 : Phase 1 detail: The full approval flow from STM submission through to sign-off.
- Diagram 3 : Phase 2 detail: The implementation planning flow from team feedback through to delivery.

Every idea passes through an initial SIG review, an investment assessment, and a scope-driven approval path before moving to implementation planning. The approval path depends on scope: global or substantially-changing ideas require global senior leader sign-off; regional ideas require regional leaders approval with global leaders notified.

### Roles and Responsibilities

![Roles and Responsibilities diagram](/images/support/assets/roles.png)

## The Process

**Step 1: Submit the idea**

The team member raises an STM (Request for Comment)  work item to submit their idea. The work item should include a clear description of the problem being solved, the proposed solution (new tool, new process, or improvement to an existing one), and the suggested scope of impact (regional or global).This will/ should also include a set timeline (so as the request is not left open for extended period of time) 

Guidance on how to frame the submission, including scope definitions, is provided in the existing RFC template.

Note: 

- The STM fields are sufficient to begin the process. The form may be iterated over time as the process matures.

- Not every SIG Request will require an RFC (example: adding a product category doesn't require an RFC. It's a straight SIG Intake).

**Step 2: SIG initial review**

The SIG reviews the submission against two criteria

- Strategic alignment: Does this idea support short- or long-term goals for Support? Ideas that do not align are closed out with written feedback to the submitter.
- Duplicate check: Has this, or something substantially similar, already been submitted or is in progress? If so, the submitter is informed and signposted to the existing item.
- Does this align with another request (and impacted by that request) 

*Note: Ideas closed at this stage are not eligible for resubmission unless goals or context change materially* 

**Step 3: Investment and priority assessment**

The SIG, in consultation with the technical/ops team where needed, assesses whether the idea is worth investing in. This covers two questions:

- Does the value justify the investment? Does the expected value, efficiency gain, quality improvement, or strategic benefit, justify the cost and effort? Ideas that do not clear this bar are closed out with written feedback to the submitter.
- If yes, what is the priority? Where does this idea sit relative to existing work in flight? The output is a priority rating (high, medium, or low) which determines how quickly it moves forward.

*Note: A low priority rating does not close the idea, it is logged and revisited. Only a decision not to invest results in closure. The SIG aims to complete investment assessments on an async weekly cadence*

**Step 4: Scope determination**

The submitter indicates the suggested scope including whether it is Regional or Global on the submission form. The SIG reviews this as part of the process and may adjust the scope designation, as may approve at later stages, if the likely impact differs from the submitter's assessment. The final scope determination drives the approval path:

**Step 5a: Regional approval path**

For regional-scope ideas, the following sequence applies

- Regional leaders: Reviews the idea and provides formal sign-off (or rejection with feedback). 
- Regional team call: The idea is shared for awareness. No sign-off required.
- Global senior leaders: Receive a notification for awareness. No sign-off required.

**Step 5b: Global / substantial change approval path**

For global-scope ideas or those substantially changing a region, the following sequence applies:

- SIG full vetting: The SIG conducts a detailed review of the proposal, covering impact, risks, resource needs, and implementation approach.
- Regional leaders calls: Regional leaders are briefed by regional SIG members (could be async), given the opportunity to raise concerns or provide input, and asked to confirm awareness.
- Global senior leaders: Provide formal sign-off. This is a required approval gate, the idea cannot proceed to implementation without it.

**Step 6: Team feedback and requirements gathering**

Once approved in principle, the support team is consulted via the STM work item to capture what they would like to see in the final implementation. When input has been gathered and agreed, the consolidated requirements are used to populate a SIG intake work item, marking the transition from idea to active work item.

**Step 7: RICE scoring and final prioritisation**

The SIG intake work item goes through a RICE scoring process (Reach, Impact, Confidence, Effort). This is the final prioritisation step and determines where the item sits in the delivery queue relative to all other active and pending work

**Step 8: Implementation path**

Following RICE scoring, the implementation path depends on whether Support Operations involvement is required. As Support Ops are represented within the SIG, this determination is made as part of the RICE scoring process, no separate escalation or decision is needed.

- Support Ops required: The item is prioritised against the Support Operations team's existing workload. Scheduling and resourcing is agreed with that team before work begins.

- Support Ops not required: The original idea submitter will typically act as DRI and sees the work through to implementation. If the submitter is not best positioned to lead, they can work with their leaders to identify a more suitable person before work begins.

### Rejected or Closed Ideas

Ideas may be closed at any stage in the process , initial review, investment assessment, or approval. In all cases:

- The submitter receives written feedback explaining the reason for closure.
- Closed ideas are not eligible for resubmission unless there is a material change in goals, context, or circumstances.
- There is no formal appeal path. Submitters who believe a decision was incorrect should raise this with their regional leaders.

### Quick Reference: Approval Matrix

![Quick Reference Approval Matrix](/images/support/assets/approvalmatrix.png)

### Process Diagrams

![SIG Process Diagram 1: High level overview — a simplified end-to-end view of the full process](/images/support/assets/diagram1.png)

![SIG Process Diagram 2: Phase 1 detail — the full approval flow from STM submission through to sign-off](/images/support/assets/diagram2.png)

![SIG Process Diagram 3: Phase 2 detail — the implementation planning flow from team feedback through to delivery](/images/support/assets/diagram3.png)
