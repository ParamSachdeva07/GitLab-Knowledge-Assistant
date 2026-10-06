---
title: "AI-Native Hiring Working Group"
description: "The AI-Native Hiring Working Group aims to redesign GitLab's technical interview process for engineering roles to evaluate the skills that matter most in an AI-assisted development environment."
status: active
---

## Overview

| Attribute | Details |
|-----------|---------|
| **Status** | Proposed |
| **Start Date** | 2026-04-04 |
| **Target End Date** | 2026-05-15 |
| **Facilitator** | Shekhar Patnaik |
| **Executive Sponsor** | Siva Padisetty  |
| **Slack Channel** | `#wg_ai-native-hiring` |
| **Meeting Cadence** | Weekly, 25 minutes (async recording available) |

---

## Charter

### Problem Statement

Our current technical interview process centres on a merge request review exercise: candidates identify issues in a code sample, comment on best-practice violations, and implement fixes. AI coding assistants can now surface 90–99% of common code issues and generate explanations and fixes on demand. This means our current process primarily measures skills that AI has commoditised, reducing our ability to differentiate between candidates who possess strong engineering judgment and those who can operate an AI tool to produce a passable review.

### Goal

Design, pilot, and recommend an updated technical interview process for engineering roles that evaluates the skills most critical in an AI-assisted development environment — specifically: design judgment, clear communication of intent, iterative problem-solving, code comprehension, validation discipline, and awareness of AI limitations — while preserving GitLab's emphasis on asynchronous collaboration and MR-based communication.

### Scope

This working group will focus on the **technical interview stages** for Software Engineer roles across all levels. It will not redesign behavioural interviews, hiring manager screens, or offer processes, though recommendations may note implications for those stages. The initial pilot will target Ruby backend roles, with a phased rollout to Go, TypeScript, Python, and Frontend engineering.

### Guiding Principles

These principles reflect feedback received during the initial proposal discussion and should guide all design decisions:

1. **Realistic scope, not artificial time pressure.** Interviews are inherently stressful. The process should be ambitious but should not use time pressure as a deliberate evaluation tool. We want to see how candidates think, not how they perform under manufactured stress.
2. **Preserve the async MR signal.** Asynchronous written communication via merge requests is central to how GitLab operates. Any new process must retain a component that evaluates a candidate's ability to communicate clearly and constructively in an MR context.
3. **Standardised tooling for fairness.** All candidates should have equal access to AI tooling during the interview. We will provide temporary Duo access rather than relying on candidates' personal setups, ensuring we evaluate skill rather than existing tool investment.
4. **Discussion over dictation.** Candidates should not be forced to write production code under observation as the primary signal. Where code is produced (likely with AI assistance), the emphasis should be on the candidate's ability to evaluate, discuss, and reason about that code — not on the raw output itself.
5. **AI as amplifier, not crutch.** The process should reveal candidates who use AI as a force multiplier for their own judgment, and flag candidates who delegate judgment entirely to the tool.

---

## Exit Criteria

The working group will disband when all of the following are satisfied:

- [ ] A revised interview rubric is published that maps evaluation criteria to AI-era engineering skills.
- [ ] Interview guides for both proposed interview parts (greenfield design and codebase navigation) are complete, reviewed, and published.
- [ ] An async MR-based assessment component has been designed and integrated into the proposed process.
- [ ] A playbook for provisioning temporary Duo access to candidates is documented and validated with the Duo team.
- [ ] At least 3 pilot interviews have been conducted using the new process.
- [ ] A retrospective on the pilots has been completed, with quantitative and qualitative feedback from interviewers and candidates.
- [ ] A final written recommendation (approve, iterate, or reject the new process) has been published and reviewed by the executive sponsor.
- [ ] If approved, a rollout plan with timeline and ownership has been merged into the handbook.

---

## Proposed Interview Structure

*Note: This is the starting proposal. The working group's job is to refine, pilot, and validate this — not to rubber-stamp it.*

### Component 1: Async MR Assessment (Pre-Interview)

Candidates receive a prepared merge request and are asked to review it asynchronously, leaving comments and suggesting improvements. This preserves the current process's strongest signal — written communication in an MR context — while acknowledging that AI tools will be used.

**Evaluates:** Reading and understanding code, async communication quality, MR collaboration skills.

### Component 2: Design & Iterative Implementation (Synchronous, ~1 hour)

Candidates are given a greenfield problem with enough complexity to support multiple valid architectural approaches. They use Duo to design, implement, and iterate on a solution while thinking aloud. The interviewer observes their design reasoning, how they direct the AI, and how they evaluate AI output.

**Evaluates:** Design judgment, expressing intent clearly, iterating toward a solution, knowing AI boundaries.

### Component 3: Codebase Navigation (Synchronous, ~1 hour)

Candidates are given access to an existing codebase and asked to implement a specific feature. They use Duo to explore the codebase, locate relevant code, plan their approach, and produce a merge-ready change. Interviewers assess how effectively candidates orient themselves in unfamiliar code and leverage AI for exploration.

**Evaluates:** Reading and understanding code, expressing intent clearly, iterating toward a solution, validating and testing.

---

## Roles & Responsibilities

| Role | Person | Responsibility |
|------|--------|----------------|
| **Executive Sponsor** | Siva Padisetty | Removes blockers, provides strategic alignment, approves final recommendation |
| **Facilitator** | Shekhar Patnaik | Runs meetings, tracks exit criteria, maintains handbook page |
| **Talent Acquisition Lead** | Jack Connors | Ensures process aligns with candidate experience goals, coordinates pilot logistics |
| **Engineering Reps** | Terri, Max, Doug | Creates and pilots new technical interview process |

---

## Members

| Name | Function | Role |
|------|----------|------|
| Shekhar Patnaik | Engineering | Facilitator |
| Siva Padisetty | Engineering Leadership | Executive Sponsor |
| Jack Connors| Talent Acquisition | Member |
| Matt Angell | Talent Acquisition | Member |
| Doug Stull | Engineering/Technical Interviewer | Member |
| Terri Chu | Engineering/Technical Interviewer | Member |
| Chaoyue Zhao | Engineering/Technical Interviewer | Member |
| Max Woolf | Engineering/Technical Interviewer | Member |

*To join this working group, please communicate with your manager and the facilitator, then open an MR to add yourself to the member list above.*
