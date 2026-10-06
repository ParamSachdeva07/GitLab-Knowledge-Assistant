---
title: "Pre-mortems for launches"
description: "An optional, forty-five-minute practice for surfacing launch-specific risks before the ship date. A practice teams may use, not a step teams must follow; the launch DRI decides whether to run one."
date: 2026-09-16
---

## Overview

We are good at learning from failures after they happen. Our [incident reviews](/handbook/engineering/infrastructure-platforms/incident-review/) are strong: blameless, written down, with corrective actions tracked as issues with owners. The problem is that those failures are often noticed by customers, and at times before we notice them ourselves.

From an operations perspective, the first half of the software development lifecycle gets much less attention. What we have not had is an intentional, focused window in which the people who know the system say out loud what they are privately worried about, before the ship date, with social permission to be pessimistic. In most project failures, someone on the team almost always knew. The goal is to make it safe and quick to surface that risk proactively.

A pre-mortem is forty-five minutes to collect that.

Beyond surfacing unspoken risk, pre-mortems help with one of the harder leadership problems: scaling decision-making and decision quality across an organization. They give team members a forum to recognize a diverse set of failure modes and to learn from scars others have seen without living through them. Run often enough, the exercise builds the muscle to shift the handling of failure scenarios left, early in the development lifecycle.

Teams in [Data Engineering and Monetization](/handbook/engineering/data-engineering/) use this practice, and any team at GitLab is welcome to. This page describes a practice teams may use, not a step teams must follow. The DRI for a launch decides whether to run one.

## What a pre-mortem is, and what it isn't

The whole idea is one inversion. Instead of asking a team "what could go wrong?", phrase it as a failure that has already happened: *it is eight weeks after launch, this failed, everyone in this room already knows it failed. Write down why.*

The certainty that we have failed is what does the work. "What could go wrong" invites people to defend the plan. "It already failed, explain it" removes the hesitation. You are not being pessimistic; you are answering the question you were asked.

A pre-mortem is:

- **Not a risk register.** No likelihood-times-impact scoring.
- **Not a design review.** There is limited value if the outcome of the meeting is "we should have built this differently".
- **Not a post-mortem with the tense changed.** A post-mortem explains one thing that happened. A pre-mortem generates many things that could.
- **Not a replacement** for [feature flags](https://docs.gitlab.com/development/feature_flags/), readiness reviews such as [PREP](/handbook/engineering/infrastructure-platforms/production/prep/), [error budgets](/handbook/engineering/error-budgets/), or tests.

## When to run one

An easy mental model is two questions. If either answer is yes, forty-five minutes is probably worth it.

1. **If this goes wrong, can we undo it in minutes?** If not, it is a candidate.
1. **If this goes wrong, who tells us?** If the honest answer is a customer in a Slack channel with an executive in it, rather than an automated alert, it is a candidate.

Concretely, at GitLab, that tends to mean:

- A schema change with a backfill measured in hours at GitLab.com scale.
- Anything touching replication, storage, or the write path. The [Orbit](/handbook/engineering/architecture/design-documents/orbit/) and [Data Insights Platform](/handbook/engineering/architecture/design-documents/data_insights_platform/) rollout is the clearest recent example: logical replication, [WAL accumulation risk](/handbook/engineering/architecture/design-documents/siphon/#runtime-risks), and a [shared messaging dependency](/handbook/engineering/architecture/design-documents/orbit/decisions/01-delivery/#negative) where one outage or misconfiguration affects every consumer.
- Anything crossing the GitLab.com, GitLab Self-Managed, and GitLab Dedicated boundary, where the environments differ and newer engineers may have blind spots. Dedicated tenants have maintenance windows and customer-specific configuration; GitLab.com does not.
- Anything in the authentication or permissions path.
- First production use of a new dependency, datastore, or vendor.
- Anything with a fixed external date. A hard date removes our ability to act on what we learn late, which is exactly why we want to learn it early.
- A Beta-to-GA transition where the support and on-call model is not settled. "Who gets paged, and can they do anything at 03:00?" is the most common real gap, and no readiness checklist reliably asks it.

**Timing.** Ideally after the design is settled and before the code is finished: roughly sixty to seventy percent through the build, or two to three weeks before rollout starts. Earlier than that, we are speculating about a design that will still change. Later, the only honest answer to every finding is "we ship anyway". The DRI makes the judgement call.

## When not to run one

This section matters more than the one above it. The fastest way to kill a good practice is to apply it everywhere.

- **The change is behind a flag with a real ramp and a tested kill switch.** The flag is the pre-mortem. Don't add a meeting to something you can turn off in thirty seconds. If the kill switch has never been exercised, that is a different problem, and the fix is to exercise it, not to hold a meeting about it.
- **Routine work.** Bug fixes, dependency bumps, docs, UI changes, the twentieth iteration of a mature feature. The checklist is the right tool and it is much cheaper.
- **One person can already write the list.** Then write the list. A pre-mortem is for surfacing what is distributed across several people's heads. It is not a mechanism for making one engineer's known concerns feel official.

## How to run one

Use the [template](#template) below. The shape is fixed on purpose.

1. **Async writing, twenty-four hours ahead.** The facilitator shares the document with a scenario written as a fact that has already happened. Each participant writes their own answers in their own section, without reading anyone else's first. Ten minutes of focused, silent writing by everyone, on failure modes and failure reasons, is the core value of the exercise.
1. **A thirty-minute call.** Read-out, one item each, round the room, no debate (15 minutes). Cluster into themes and, per theme, ask what is the cheapest thing we can do this week that tells us whether this is real (10 minutes). The DRI picks at most three (5 minutes).
1. **Output pasted into the launch epic.** At most three actions, each with an owner, a date, and an issue. Everything else becomes a "known and accepted" line: *we know X could happen; we are not acting on it because Y; if it happens, we find out via Z.*

## Measuring it

You cannot prove a pre-mortem prevented an incident. Any metric we could propose would be gameable, and every gameable metric here pushes teams to run more of them, which is the opposite of the goal. The one signal worth looking at, informally, once a quarter: when we do have an incident, was the cause on somebody's pre-mortem list? If it repeatedly was, we have an action problem rather than a foresight problem, and that is a more interesting conversation to have. If it consistently wasn't, the pre-mortems are not finding the right things and we should change how we run them or drop the practice. Being willing to drop it is the price of asking people to start.

## Frequently asked questions

**"Why not have Claude do it?"** Partly, you should. The [the-fool](https://github.com/jeffallan/claude-skills/blob/main/skills/the-fool/SKILL.md) skill (community-maintained, not an official GitLab or Anthropic tool) in pre-mortem mode produces a plausible failure list from a design document in ninety seconds, and that is a good seed for the async writing step: hand it out with the prompt and let people react to it and add. What it cannot produce is the thing that makes this work: that the engineer who owns the retry path has been quietly assuming somebody else owns it, or that Support has already seen this shape of failure at two customers. That is not in the design document. Use Claude to widen the list. Don't use it to skip the silent writing.

**"We already do readiness reviews and change management."** Different failure modes. A readiness review such as [PREP](/handbook/engineering/infrastructure-platforms/production/prep/), or [change management](/handbook/engineering/infrastructure-platforms/change-management/), asks whether you did the things we already know to do. A pre-mortem asks what is specific to this one launch that nobody's checklist knows about.

**"Our design docs already have a risks section."** They do, and it is useful. Siphon's runtime risks were written down long before any of this. But a risks section is written by the person most invested in the launch succeeding, likely alone, at design time. The pre-mortem's value is that several people write separately, at a point where the design is real, and the aggregate surfaces the interactions no single author was positioned to see.

**"What if the list is all obvious?"** Then you finish in twenty minutes with written agreement on the risks, which is a good outcome. The failure mode isn't an obvious list. It's a list nobody in the room surfaced or reflected on before.

**"Who owns this? Where does it live?"** The DRI for a launch decides whether to run one. There is no pre-mortem programme, no quarterly report, and no tracking issue. If it needs a programme to survive, it shouldn't survive. This page describes a practice teams may use, not a step teams must follow.

## Template

Copy this into a document and share it twenty-four hours ahead. If you find yourself adding sections to it, that is the drift this page is worried about.

```markdown
## Pre-mortem: [launch name]

Session: [date] · DRI: [name] · Facilitator: [name]

**Scenario.** It is [launch date plus six to eight weeks]. [One specific bad outcome,
written as a fact that has already happened. Name a date, a number, and who noticed.]

**Before the call (async, 24 hours).** Write your own answers in your own section.
Do not read anyone else's first.

- Why did it fail?
- What did we find out too late, and how did we find out?
- What did we assume that turned out not to be true?

Be specific. "It didn't scale" is not an answer.
"The backfill held a lock for nine minutes at 14:00 UTC and web timed out" is.

**On the call (30 minutes).**

1. Read-out, one item each, round the room, no debate. (15 min)
2. Cluster into themes. Per theme: what is the cheapest thing we can do this week
   that tells us whether this is real? (10 min)
3. DRI picks at most three. (5 min)

**Output (paste into the launch epic).**

Actions, maximum three:

| Action | Owner | By | Issue |
|--------|-------|----|-------|
|        |       |    |       |
|        |       |    |       |
|        |       |    |       |

Known and accepted, one line each:

We know [X] could happen. We are not acting on it because [Y]. If it happens, we find out via [Z].
```
