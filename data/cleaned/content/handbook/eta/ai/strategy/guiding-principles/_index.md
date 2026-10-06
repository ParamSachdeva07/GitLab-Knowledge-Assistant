---
title: "Guiding Principles"
description: "Five principles that guide every internal AI initiative at GitLab, and the North Star of what work looks like when they click."
---

## The vision: a preview of work transformed

Imagine starting your day not with inbox triage and meeting prep, but with a compiled briefing of what happened overnight. Your AI agents have processed incoming requests, flagged items needing your judgement, drafted responses awaiting approval, and surfaced cross-team developments affecting your work.

You're preparing for a customer call. Instead of spending an hour gathering context from Salesforce, Gainsight, ZenDesk, and Gong, you ask your briefing agent to pull together the key information. Within minutes, you have a clear view of the relationship, recent issues, usage trends, and recommended talking points, ready for your review and refinement.

A complex issue arises requiring judgement about competing priorities, or an issue with no clear "right" choice. Your agents have already assembled the relevant context, identified the stakeholders, and outlined the trade-offs. You focus on the decision itself, not the legwork of understanding the situation.

Think of it as having a high-performing team that can research, draft, analyse, coordinate, and execute the repeatable parts, while you stay accountable for strategy, judgement and direction. Team members become orchestrators: setting intent, approving plans, reviewing outputs, and continuously improving how work gets done.

The principles that follow are designed to get us there.

## The five principles

1. **Amplify human contribution, don't automate it away.** Use AI to extend what people can accomplish, not to remove them from the equation.
2. **Redesign workflows, don't retrofit AI onto existing processes.** Reimagine how work should flow with AI as a core capability, rather than accelerating broken processes.
3. **Empower builders, not just users.** Give team members the tools and permission to create AI solutions for their specific contexts, not just consume centrally deployed tools.
4. **Start small, build trust, scale what works.** Progress through proven value using a Crawl-Walk-Run approach, earning autonomy through demonstrated reliability.
5. **Govern for speed, not just safety.** Establish clear guardrails that enable rapid, confident action rather than creating bottlenecks.

## Principle 1: Amplify human contribution, don't automate it away

**The principle.** AI should handle execution-heavy tasks while team members stay accountable as the DRI, choosing what to delegate, what to retain, and what level of autonomy is appropriate. The metric shouldn't be time saved, it's impact amplified (i.e. business value metrics).

**Why this matters.** The most valuable work at GitLab requires human capabilities that AI cannot replicate: understanding nuanced customer needs, making strategic trade-offs, building relationships, navigating ambiguity, and applying ethical reasoning. When we position AI as a tool that sets out to remove humans from processes, we lose these capabilities. When we position AI as a tool that handles the grunt work so humans can focus on high-impact activities, we multiply what our people can achieve.

### What this looks like in practice

The balance shifts depending on the task:

- **Routine, repeatable success criteria.** AI operates autonomously (data enrichment, follow-ups, account engagement that would otherwise be impossible).
- **Requires context or piecing things together.** AI does the heavy lifting, humans review the outputs or step in when flagged.
- **Unfamiliar situations, relationships, strategic calls.** Humans lead, AI supports with research and preparation.

**The risk of getting this wrong.** Organisations that focus purely on efficiency and cost reduction through AI often discover they've optimised away the human contribution that made their work valuable. The goal isn't to see how much human involvement we can eliminate, it's to see how much more impact our people can have when freed from low-value tasks.

**Key question to ask.** "Does this AI implementation give our team members more capacity for high-impact work, or does it just remove them from the process?"

## Principle 2: Redesign workflows, don't retrofit AI onto existing processes

**The principle.** Before deploying AI tools, map current workflows and value streams, and ask: "If we were designing this process today with AI as a *core capability*, how would it look?" Often the answer involves eliminating entire steps rather than simply accelerating or automating them.

**Why this matters.** Most AI initiatives fail not because the technology doesn't work, but because organisations apply AI to existing processes without questioning *whether those processes should exist at all*. Automating a broken process just produces broken results *faster*. The organisations achieving significant returns fundamentally reimagine how work flows rather than simply overlaying AI on what already exists.

### What this looks like in practice

- **Before AI.** A team member gathers data from five systems, pulls it together into a report, sends it for review, incorporates feedback, and distributes the final version.
- **Retrofitted AI.** AI helps draft the report faster, but the same five-system data gathering, review cycles, and distribution steps remain.
- **Redesigned workflow.** Two of the systems identified can be removed, AI continuously monitors the three remaining systems and surfaces relevant changes proactively; reports are generated on-demand from live data; review happens only when AI flags anomalies or when humans request it.
- **Previously impossible.** AI identifies patterns across thousands of customer calls, surfacing trends no individual or team could spot. Work that simply couldn't be done before at this scale.

### The decomposition approach

For any workflow under consideration:

- Map (with Flow Engineering) every step in the current process.
- For each step, ask: should this step exist at all? Can it be eliminated entirely?
- For remaining steps: should a human do this, should AI do this, or should they collaborate?
- Design the new workflow from scratch, not as a modification of the old one.

**Key question to ask.** "Are we making a bad process faster, or are we creating a fundamentally better way of achieving the outcome?"

## Principle 3: Empower builders, not just users

**The principle.** Create infrastructure and incentives for team members to build and share AI-powered workflows, not just consume centrally deployed tools. The goal is an internal ecosystem of proven AI solutions.

**Consume before build.** The flip side of empowering builders is the discipline to consume before building: reach for what already exists across the company first, and build new only when nothing fits. That is what turns a pile of individual builds into a shared ecosystem.

**Why this matters.** Central IT teams cannot possibly understand the nuances of every role and workflow across GitLab. The people closest to the work understand their pain points, their edge cases, and what "good" looks like in their context. When we empower them to build AI solutions (and share those solutions with others facing similar challenges) we multiply our innovation capacity dramatically.

### What this looks like in practice

- Team members can create custom AI workflows for their specific functions without waiting for central deployment.
- Successful solutions are documented and shared in a way that others can discover and adapt them.
- "Superusers" emerge organically and are recognised for enabling others.
- The AI Engineering team provides platforms, guardrails, and support, not gatekeeping.

### The builder spectrum

Not everyone needs to build from scratch. Empowerment exists on a spectrum:

- **Consumers.** Use AI tools as provided, follow documented workflows.
- **Configurers.** Adapt existing AI solutions to their specific context.
- **Builders.** Create new AI workflows using provided platforms and tools.
- **Contributors.** Share their solutions back to the organisation for others to use.

**Measuring success.** Track not just how many people use AI tools, but how many people create and share AI solutions. The ratio of builders to pure consumers indicates whether we're achieving genuine empowerment.

### A word of caution

Self-service tooling and citizen development have been promised for decades in BI, RPA, and traditional automation. It's rarely delivered at scale. We should be clear-eyed about this.

**The difference.** Previous waves often empowered people to automate existing processes, which meant automating mess. This principle only works when paired with the others, particularly Principle 2 (redesign workflows, don't retrofit) and Principle 4 (earn autonomy through proven value).

The AI Engineering team's role isn't to step back entirely. It's to provide platforms with guardrails, curate what works, and deprecate what doesn't. Not everyone will become a builder, and *that's fine*. The goal is an environment where good solutions can emerge from anywhere, not a mandate that *everyone must build*.

**Key question to ask.** "Are we creating an environment where the best AI solutions can emerge from anywhere in the organisation?"

## Principle 4: Start small, build trust, scale what works

**The principle.** Progress AI capabilities through a Crawl-Walk-Run approach, where autonomy is earned through demonstrated reliability. Invest heavily in the human side (enablement, culture change, feedback loops) because technology alone *doesn't drive adoption*.

**Why this matters.** The limiting factor for AI impact is rarely the technology itself. It's whether people trust it, understand how to use it, and have confidence in its output. Trust is built incrementally: by starting with AI as a suggestion engine, proving value, then gradually increasing autonomy as reliability is demonstrated. Jumping straight to full automation, or worse, deploying tools without investing in adoption, consistently underperforms.

### The Crawl-Walk-Run framework

**Crawl: AI suggests, humans decide and act.**

- AI provides recommendations, drafts, or analysis.
- Humans review every output and make all decisions.
- Focus is on learning what AI does well and where it falls short.
- Success metric: are the suggestions useful? Are humans saving time?

**Walk: AI automates, humans validate and trigger.**

- AI executes routine tasks but waits for human approval.
- As confidence grows, approval can shift from one-by-one to batches (e.g. reviewing a sample, then approving 100 actions at once).
- Humans spot-check outputs and approve before actions take effect.
- Confidence builds through consistent, reliable performance.
- Success metric: what percentage of AI outputs are approved without modification?

**Run: AI acts autonomously, humans handle exceptions.**

- AI executes independently within defined guardrails.
- Humans are notified of actions taken and intervene only when needed.
- Reserved for workflows where AI has proven reliable and errors are low-risk or reversible.
- Success metric: are outcomes improving? Are humans freed for higher-impact work?

### Earning the right to progress

Movement from Crawl to Walk to Run should be based on evidence, not hope:

- **Track accuracy.** What percentage of AI suggestions are accepted? What percentage of automated actions succeed?
- **Measure trust.** Are users comfortable with the current level of autonomy? What would make them confident in the next level?
- **Define thresholds.** What accuracy rate or success rate justifies increased autonomy? Make this explicit.
- **Build in reversibility.** Ensure you can step back to a lower level of autonomy if problems emerge.

### Investment in people, not just tools

Most people won't adopt new AI tools from watching training videos or reading documentation. They adopt when:

- They see peers succeeding with the tools.
- They have a safe space to experiment and fail.
- The tools solve an immediate, felt pain point.
- They receive support at the moment they get stuck.

Identify and support [Champions](../hub-and-spoke/#the-three-roles) who help their peers adopt new workflows. Build feedback loops so the AI Engineering team understands what's working and what isn't.

**Key question to ask.** "Have we earned the right to increase autonomy, and are we investing enough in helping people succeed?"

## Principle 5: Govern for speed, not just safety

**The principle.** Establish clear principles for AI use that enable rather than constrain. Define which decisions require human approval, which AI can make autonomously, and which fall in between. Treat governance as a living document requiring regular reassessment.

**Why this matters.** Without clear guardrails, teams either move too slowly (seeking approval for everything) or too recklessly (ignoring risks in pursuit of speed). Well-designed governance actually accelerates deployment by providing clarity about what's acceptable, reducing decision "analysis paralysis" and back-and-forth.

### Permission tiers for AI actions

- **Autonomous.** AI acts independently on routine, low-risk, easily reversible matters.
- **Propose-and-wait.** AI drafts actions and awaits human approval before execution.
- **Escalate immediately.** AI flags situations requiring immediate human attention.

### Clear boundaries

- What data can AI access? What data is off-limits?
- What decisions can AI make? What decisions require human approval?
- What outputs can AI publish directly? What requires human review?
- How do we handle errors? Who is accountable?

**The governance anti-pattern.** Governance that requires committee approval for every AI use case creates bottlenecks that kill momentum and frustrate teams. Instead, establish clear principles that teams can apply themselves, with escalation paths for genuinely novel situations.

**Living documentation.** AI capabilities evolve rapidly. Governance established in January may be outdated by June. Build in regular review cycles and make it easy for teams to flag when governance doesn't match reality.

**Key question to ask.** "Does our governance give teams clarity and confidence to move fast, or does it create uncertainty and delay?"

## North Star: what work looks like when these principles click

In this world, most knowledge work starts the same way: you state the outcome you're driving, and your team of AI agents spins up the work needed to get you there.

You have a high-performing staff team that can research, draft, analyse, coordinate, and execute the repeatable parts, while you stay accountable for judgement and direction.

### How work feels

**Less busywork, more real work.** Team members spend far less time gathering context, updating systems, producing first drafts, chasing approvals, or reconciling conflicting information. The cognitive load of being a "human router" disappears.

**You manage outcomes, not tasks.** Work is framed as: "Here's the goal, the constraints, and what good looks like." Agents propose plans, run the steps, and return options with evidence. You decide, approve, and course-correct.

**Your attention goes where humans add value.** Team members focus on strategy, trade-offs, relationships, creativity, ethical judgement, and navigating ambiguity. The mechanical parts of work happen in the background.

**Decision-making speeds up without getting sloppy.** Agents bring you the best available picture, with sources and confidence levels, and you decide. Fewer "alignment meetings" because context is already packaged. Fewer delays waiting for information to be assembled.

### What "managing AI agents" actually means day-to-day

Team members become orchestrators:

- Setting intent and success criteria for what needs to happen.
- Approving plans and delegating execution to specialised agents.
- Reviewing outputs with the right level of scrutiny (light touch for low-risk, careful examination for high-stakes).
- Asking better questions when things don't look right.
- Continuously improving workflows: removing unnecessary steps, not just automating mess.
- Coaching and providing feedback to improve agent performance over time.

It feels closer to leading a highly capable team than using a tool.

### A day in the life

**Morning.** You arrive to a compiled briefing of what happened overnight. Agents have processed incoming requests, flagged items needing your judgement, drafted responses awaiting approval, and surfaced cross-team developments affecting your work. Your morning is transformed from a reactive catch-up to proactive decision-making.

**Midday.** You're preparing for a customer call. Instead of spending an hour gathering context from Salesforce, Gainsight, ZenDesk, and Gong, you ask your briefing agent to pull together the key information. Within minutes, you have a clear view of the relationship, recent issues, usage trends, and recommended talking points, ready for your review and refinement.

**Afternoon.** A complex issue arises that requires judgement about competing priorities. Your agents have already assembled the relevant context, identified the stakeholders, and outlined the trade-offs. You focus on the decision itself, not the legwork of understanding the situation.

**End of day.** You set intentions for overnight work. Research to be conducted, drafts to be prepared, monitoring to be done. When you return tomorrow, the groundwork is already laid.

### Benefits to GitLab

**Compounding productivity.** When someone creates a better way of working with AI, it doesn't just help them, it can be shared and reused everywhere. Improvements compound rather than staying siloed.

**Scalable consistency.** Great ways of working spread fast through shared agents and workflows, without turning into bureaucracy or process bloat.

**Faster adaptation.** New initiatives ramp quicker because agents can assemble context, identify risks, and propose execution plans on demand. The "getting up to speed" phase shrinks dramatically.

**Better risk posture.** Governance is embedded in the system through permission tiers, data boundaries, and audit trails. Speed doesn't come at the expense of control.

### Benefits to team members

**More meaningful work.** Less time spent being a human router, data gatherer, or format converter. More time solving real problems, building relationships, and applying expertise.

**Lower cognitive load.** You're not juggling ten systems and hundreds of micro-decisions. The mental overhead of "keeping track of everything" is handled by agents designed for exactly that purpose.

**Higher leverage and growth.** Team members level up into judgement, leadership, systems thinking, and craft, the capabilities that stay valuable and become more important as AI handles routine execution.

**More autonomy.** With strong guardrails in place, people can move faster without waiting for permission at every step. Clear boundaries create freedom, not constraint.

### The transformation is closer than it appears

The components of this vision exist today. Morning briefings, AI agents handling execution within guardrails, humans focusing on judgement, these aren't science fiction. What remains is the intentional work of implementation: decomposing workflows, building enabling infrastructure, changing culture, and measuring what matters.

GitLab's opportunity is to build this future transparently and iteratively, in a way that reinforces our values of collaboration, results, efficiency, and iteration. We don't need to wait for perfect technology. We start with clear principles, learn through experimentation, and build the muscle memory for human-AI collaboration that will define how work happens in the years ahead.

## Conclusion

These five principles provide a foundation for internal AI initiatives that avoid the failure patterns plaguing most enterprise AI efforts:

1. **Amplify human contribution** rather than automate it away.
2. **Redesign workflows** rather than retrofit AI onto existing processes.
3. **Empower builders** rather than just deploy tools for users.
4. **Start small, build trust, scale what works** through a Crawl-Walk-Run progression.
5. **Govern for speed** as well as safety.

The North Star isn't about replacing team members with AI. It's about giving every team member the leverage of a high-performing support team, allowing them to focus on the work that only humans can do while AI handles the execution-heavy tasks that consume so much of today's working hours.

The organisations moving fastest aren't waiting for perfect technology. They're starting with clear principles, learning through experimentation, and building the capabilities that will define competitive advantage in the years ahead. That's the opportunity in front of us.

## Related

- [Hub & Spoke & Hub](../hub-and-spoke/): the operating model that turns these principles into delivery.
- [Operating Rhythm](../hub-and-spoke/operating-rhythm/): the cadence, channels, and decision rights that support delivery.
- [Prompts are Process](../prompts-are-process/): why every AI agent needs an owner, and the three places ownership can sit.
