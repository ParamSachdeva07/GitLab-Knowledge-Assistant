---
title: "SPA Teams Guiding Principles"
description: "Guiding principles for Security Platforms and Architecture team members covering decision-making, ownership, communication, support, and continuous improvement"
---

Last Updated: May 5, 2026

## SPA Teams Guiding Principles

These principles exist because the team must operate as leaders, not followers waiting for direction. Every principle below is designed to reduce dependency on any single person and increase the speed and quality of the team's decisions.

### How We Decide

- **Say "I intend to..." instead of asking permission.** If you see a rotation gap, a broken process, or a better approach, state your intent and act. Do not wait for a 1:1 to ask "is it okay if I...?" The expected format is: *"I intend to [action] because [reason]. I'll proceed unless I hear otherwise by [time]."* This is what GitLab means by being a [Manager of One](/handbook/leadership/#managers-of-one).
- **Decisions belong where the information lives.** The person closest to the problem makes the call. If you are the one reading the MR, triaging the issue, or talking to the engineer, you have the authority to decide. Escalate only when the decision is irreversible, cross-team, or carries significant risk. See GitLab's [Making Decisions](/handbook/leadership/making-decisions/) page for the boundaries of your authority.
- **When in doubt, act and inform. Don't wait and ask.** A wrong decision made quickly and corrected is better than no decision waiting for approval. You acted in good faith with the information available, the team **and** leadership has your back.

### How We Own Our Work

- **If it has your name on it, you own the outcome end to end.** Being a DRI means you drive the work to completion, unblock yourself, follow up with stakeholders, and close it out. You do not wait for someone else to remind you. If something is blocked, you surface the blocker with a proposed path forward. See GitLab's [Effective Delegation](/handbook/leadership/effective-delegation/) guidance.
- **Operational hygiene is not optional and does not need reminders.** Labels, status updates, milestone close-outs, and dashboard formatting are part of the work, not separate tasks. Treat them the same way you treat reviewing code: it's not done until it's done right.
- **Own your rotation fully (AppSec team only).** When you are on [triage](https://triage-dashboard-2c1ad6.gitlab.io/), you are the team's front door. Review the full [triage dashboard](https://triage-dashboard-2c1ad6.gitlab.io/) (AppSec side), not just what catches your eye. If the queue is growing, raise it and propose a plan. Do not wait for someone to notice. The [triage rotation runbook](/handbook/security/product-security/security-platforms-architecture/application-security/runbooks/triage-rotation/) and [rotation schedule](https://gitlab.com/gitlab-com/gl-security/product-security/appsec/tooling/rotation-management/-/blob/main/rotations.md) are your companions.
- **Hand off with context, not just a link.** When passing work, switching DRIs, or going on PTO, provide the what (current state), the why (context and decisions made), and the next (what the receiver should do first). A clean handoff is a sign of respect for your teammates' time.

### How We Communicate

- **Broadcast what you know, don't hoard it.** If you find a useful resource, solve a tricky problem, or learn something from another team, share it with the team directly. Do not assume someone else will relay it. Every team member is an information source, not just a consumer.
- **Think out loud in our team channels.** When you are working through a problem, post your thoughts in the team channel. This makes your reasoning visible, invites input early, and prevents surprises. The goal is not to ask for help. It's to make your thought process available so others can build on it. This is how we [build trust](/handbook/leadership/building-trust/) in a remote team.
- **Replace status questions with status updates.** Do not wait for someone to ask "where are we on X?" Post proactive updates when something meaningful changes: progress, blockers, scope changes, or completion. The team and leadership should never have to chase you for information.
- **When you raise a problem, bring a proposal.** "This isn't working" is an observation. "This isn't working, and I think we should try X because Y" is leadership. Always pair problems with at least one proposed direction.

### How We Support Each Other

- **Step in without being asked.** If a teammate is on rotation and the queue is heavy, or someone is ramping up on unfamiliar work, offer help directly. Do not wait for your manager to assign support. The team succeeds together.
- **Mentor by sharing control, not answers.** When helping a newer team member, resist the urge to take over. Instead, walk them through your reasoning and let them execute. Our goal is to multiply capability, not concentrate it. See GitLab's [Coaching](/handbook/leadership/coaching/) page for more on this approach.
- **Disagree openly, commit fully.** If you see a different approach, say so, directly and respectfully. Once the team or the DRI decides, commit to making it work. Passive disagreement (going along but not engaging) hurts the team more than open debate. See GitLab's [Guidance on Feedback](/handbook/people-group/guidance-on-feedback/) for how we approach this company-wide.

### How We Improve

- **Treat every process as a draft.** If something feels inefficient, broken, or unnecessary, propose a change. Our processes serve us, not the other way around. The bar for proposing improvements is low; the bar for ignoring friction should be high.
- **Automate the repeatable, protect the thinking.** Our time is best spent on judgment calls: threat model reviews, security testing, architectural reviews. Everything else (triage routing, status formatting, label hygiene and even threat model creations) should be automated or templated. If you find yourself doing the same manual task for the third time, open an issue. See AppSec's [automation monitoring page](/handbook/security/product-security/security-platforms-architecture/application-security/application-security-automation-monitoring/) for what's already in place.
- **Run short experiments, share what you learned.** Trying a new prompt, a different review approach, or a tooling change? Time-box it, try it, and share results with the team. We learn faster when experiments are visible and small.

### The One Rule Above All

- **You are a leader on this team, not a task executor.** Your job is not to complete assignments. It is to apply your expertise, judgment, and initiative to make our products more secure. Act like the expert you are. Be a [Manager of One](/handbook/leadership/#managers-of-one).
