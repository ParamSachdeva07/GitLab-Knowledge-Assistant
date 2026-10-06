---
title: "Non-Linear Productivity"
description: "Vision and long-term initiatives for removing the bottlenecks between generating code and delivering it to customers."
---

## Intro

This page documents the initiatives engineering is pursuing to increase productivity
using AI.

## Why "Non-Linear" Productivity

Generating code is becoming trivial. The difficult part is getting that code into
customers' hands in a production-ready manner: A/B tests, rollout plans, rollback
plans, and everything else that surrounds a change once it exists. Those steps,
not authoring, are where the bottleneck now sits, and today at GitLab that
includes the time it takes to review code.

A related premise is that syntax will matter less over time. Agents may write
code that looks unoptimized from a maintainability, readability, or modularity
perspective, but agents are also the ones reading, maintaining, and changing it.
Some of our reviews today still spend their effort on exactly those
characteristics.

This project is the engineering-practice counterpart to the argument Bill Staples
makes in [When code is abundant](https://about.gitlab.com/blog/when-code-is-abundant/):
code production is becoming abundant while good software is not, so the constraint
moves from producing code to *trusting* it. That post also names the economic unit
this project optimizes for - **cost per accepted change**, which includes
generation, environment setup, context, verification, review, remediation, and
governance. Collapsing only the generation term moves the queue rather than
shortening it.

If productivity is going to scale non-linearly, the constraint has
to move away from human throughput at each step of the delivery path.

## Long-Term Initiatives

### Shift review left

It is already the [author's and their agents' responsibility](https://docs.gitlab.com/development/code_review/#the-responsibility-of-the-merge-request-author)
to produce code that would be acceptable to others, humans and agents alike.
This initiative will help to make that process easier for authors by building
tooling to help generate higher quality code from the onset. When the first iteration
of a merge request is already good, reviewers spend less time going back and forth,
and authors spend less calendar time getting their change in.

The foundation for this is `/review` in GitLab Duo, which allows a change to be
reviewed and fixed locally before a merge request is even created. Early
iterations will not be perfect; the intent is to improve them continuously.

### Reduce the pipeline bottleneck

Once better code can be generated more quickly, it also needs to reach
production quickly. The goal is to use agents at every step of the pipeline to
automate work and remediate failures, for example:

1. Flaky merge pipelines, which can be handled automatically.
1. Merge requests sitting idle and waiting on something, where an agent can take
  action: reviewing, fixing, or finding another approver when the first one is
  unavailable.

This is the same shift described in *When code is abundant*: the pipeline stops
being a gate at the end of development and becomes the system that runs the
development loop itself - generate, build, test, validate, review, remediate,
repeat - close to the code, the context, and the controls.

### Architectural modularization

For there to be no human in the loop, the architecture has to make it safe to
roll out a change in minutes to a defined corpus of customers without affecting
any other customer. This is not only feature flags and not only cellularization,
but broader than both. It requires tooling investments as well as architectural
change, and it will not happen overnight.

Removing the human from the loop is a governance problem as much as an
architectural one. *When code is abundant* frames this as autonomy being governed
rather than granted: the agent can be creative, and the system decides where
creativity stops. Deterministic gates, isolation, verification, policy, and
evidence are what let autonomy expand safely.

## Expected Trade-Offs

In the near short term, this direction may mean spending *more* time reviewing code
rather than less. That is accepted as short-term pain while the agents, models,
and foundations improve toward operating without human intervention.

## Further Reading

- [When code is abundant](https://about.gitlab.com/blog/when-code-is-abundant/) -
  Bill Staples on why the constraint moves from producing code to trusting it, the
  three modes of agentic development, and the durable layer of context,
  verification, and governance an enterprise needs around agents.

## Measurement

The metrics we are measuring are:

1. The time from when an MR is marked Ready till it is Merged
1. The time from when an MR is marked Ready till it is Assigned
1. The time from when an MR is Assigned till it is Reviewed
1. The number of iterations of an MR
1. The size of the MR

Out of these, the most important is (1) - The time from Ready to Merged.

These metrics are faceted by:

1. The type of change (docs vs code vs config)
1. The Engineering Organization of the team member that submitted the MR

Exclusions from being measured:

1. Any community contributions
1. Any MRs in Draft state
1. Any time an MR spends in Draft state prior to being marked Ready
