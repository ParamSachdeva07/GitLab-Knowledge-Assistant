---
title: "Prompts are Process"
description: "Why every AI agent is a process, and every process needs an owner."
---

## The problem this page exists to solve

We are at a point where anyone in the org can build something useful with AI. A clever prompt gets saved in a note. The same prompt becomes a skill in whichever platform you use. The skill gets wrapped into an agent. The agent gets shared with a colleague. The colleague asks: "Can we roll this out to the whole team? The whole function? The whole company?"

That request sounds simple. It isn't. And the reason it isn't is the entire point of this page.

This page is deliberately tool-agnostic. Whether you are talking about a prompt pasted from a personal doc each time, a skill built in Glean, a skill built in Claude, or a fully autonomous agent stitched together from several of the above, the same logic applies. The reasoning is about the *instructions*, not where they happen to live.

If you have been asked to approve any of these for wider rollout, or you are the one asking, please read this before the conversation goes any further.

## Start with what a prompt actually is

A prompt is a set of instructions for an AI to follow. The AI then does work a human would otherwise have done.

So step back: what do we call a set of instructions for a human to follow, repeatedly, to produce a consistent outcome?

**Process.**

A prompt copy-pasted from a personal doc is process. A skill in any platform is process. A plugin that wraps a skill is process. An agent that strings several together is process. Everything we are building in this space is process, expressed in natural language instead of a handbook page or a Confluence doc.

Once you see that, everything else follows.

## Process cannot be siloed and improvised

If a prompt is process, then we should treat it the way a mature organisation treats any other process:

- **Shared, not siloed.** Every person in a role should be operating from the same instructions. We don't write one customer onboarding playbook per CSM. We shouldn't write one prompt per CSM either.
- **Versioned, not improvised.** Process should evolve through iteration towards a desired state, not through every individual quietly tweaking their own copy. We need to see the changes, discuss them, agree, and roll them out.
- **Owned, not orphaned.** Someone has to be accountable for the process being correct, up to date, and aligned with how we want people to work.

A great prompt living in one person's notes app, or a great skill living in their private workspace in whichever AI platform, is not a win for the company. It is shadow process: the prompt equivalent of someone keeping the "real" sales playbook in a personal Google Doc.

## A collection of process is strategy

Now zoom out. What do you get when you combine every process a function uses to do its job?

You get how that function operates. You get its strategy expressed at the operational level.

Strategy is determined by the leader of the function. The VP of Marketing decides Marketing's strategy. The CIO decides how the IT and ETA org operates. The CEO decides company strategy.

If our processes (our prompts, skills, plugins) define how a function operates, then they are an instrument of that leader's strategy.

Which gives us a useful test: **if a leader cannot change the way their function operates by changing a process, they have lost control of their strategy.**

## What happens when prompts are siloed

Imagine a VP of Sales who wants to shift the sales motion. New qualification approach, new discovery framing, new discovery questions.

In an unowned-prompt world: every AE has their own "call prep" prompt. Some are out of date. Some embed the old qualification framework. Some are excellent and some are awful. The VP says "shift the motion" and nothing happens, because there is no single thing to change.

In an owned-process world: there is a canonical Sales call prep skill. The VP, working with the Sales ATO, agrees the new behaviour. The ATO updates the skill, opens a branch, gets review, merges. Every AE using the skill picks up the new behaviour automatically the next time they run it.

That second world is the one we are building towards. The first world is the one we keep accidentally creating when we launch agents without an owner.

## Three places ownership can sit

Ownership of a process doesn't have to look the same in every case. There are three legitimate homes it can have, and the right one depends on the shape of the process itself:

- **Function-scoped.** The process serves a single function's work (Marketing, Sales, CX, etc.). Owner: the function exec, with an AI Transformation Owner (ATO) maintaining the canonical version.
- **Repo-scoped.** The process relates directly to using or modifying a specific repo. Owner: the repo's maintainers / CODEOWNERS, with git doing most of the heavy lifting.
- **Company-wide.** The process is horizontal and benefits the whole company. Owner: the right central function (People, Ops, Comms, ETA, etc.), with ETA as interim home where the natural owner isn't yet obvious.

The next three sections unpack each.

## Function-scoped: enter the ATO

The AI Transformation Owner (ATO) is the person, embedded in a function, who owns that function's AI-expressed process.

The ATO is the bridge between:

- The exec who owns the strategy, and
- The people doing the work using AI.

Concretely, the ATO:

- Maintains the canonical skills, prompts, and agents used by the function.
- Translates strategy changes from the exec into process changes in the skills.
- Reviews proposals from individuals who have built something useful and want it adopted more widely.
- Keeps the function's AI footprint aligned with how the leader wants the function to operate.

If your function does not yet have an ATO, that is a gap. Building agents into a vacuum and then asking for company-wide rollout will keep hitting this wall until that gap is closed.

## Repo-scoped skills

There is a second valid home for a skill: inside a specific repo, versioned with the rest of that repo's content.

This is the pattern Claude Code uses. A `.claude/skills/` folder ships with the codebase. Anyone who clones the repo gets the skills. The skills evolve through the same pull request process as the code itself. There's no central marketplace involvement, but the skill is still:

- **Owned**, by the repo's maintainers / CODEOWNERS.
- **Versioned**, literally via git.
- **Shared, not siloed**, since every contributor to the repo gets the same skill.

This pattern is explicitly encouraged. When a skill is genuinely repo-specific, repo-scoping is the cleanest possible expression of every principle on this page: ownership is literally CODEOWNERS, versioning is literally git, reviewability is literally merge requests, rollout is literally `git pull`. The metaphor we use throughout the rest of this document is the actual mechanism in this case.

The same pattern applies to non-code repos at GitLab, but only where the skill relates directly to using or modifying that specific repo. A skill that helps contributors to the handbook repo apply the GitLab voice and style belongs there. A skill that helps with a specific ops runbook repo belongs there. The bar is *tight coupling to that repo's purpose*, not "we happen to keep things in git."

### The key test

A skill belongs in a repo when it relates directly to using or modifying *that specific repo*. The following are signals that a skill is wearing repo clothing but actually belongs elsewhere:

- It would be useful to people who never touch this repo.
- It encodes a process that should apply consistently across multiple repos.
- The team using it is split across several codebases or assets.

If any of those are true, the skill is generic or reusable, and it belongs in a function-scoped or company-wide home instead.

## Company-wide processes

Some processes don't belong to any one function or repo. Things like: standardising how we write internal updates, summarising a meeting consistently, preventing duplicate work across teams, decoding internal acronyms. No single exec's strategy is shifted by these on their own, but every team benefits when they exist and are consistent.

The principle doesn't change: ownership is still required. What changes is *where* that ownership sits. For a company-wide process, the right home is the most appropriate central function. People for ways-of-working norms. Ops or Comms for internal communication standards. ETA for AI patterns themselves. And so on. If it's genuinely unclear, ETA will act as interim home until the natural owner emerges.

A few things about company-wide processes that matter:

- **Don't wait for the perfect owner.** Commit and iterate is the right approach here. Get the first version out, gather feedback broadly, refine. The cost of slow iteration is higher than the cost of an imperfect first cut.
- **The builder is not blocked from contributing.** Someone in CX who has built a brilliant version of an anti-rework process should absolutely make the first commit. They just don't own the canonical version going forward, and they shouldn't be the only person able to tweak it once it's out there.
- **Broad feedback substitutes for a single exec's sign-off.** A function-specific process is vetted by the function's exec. A company-wide process is vetted by being shared widely, gathering input, and iterating fast under a central owner.

The "no obvious function owner" answer is not "default to the builder." It is "find the right central home, let the builder make the first commit, then move fast from there."

## This is not a constraint on individual creativity

The ATO model does not stop people experimenting. It does not stop a CSM, an AE, a marketer from building a personal prompt that helps them do their job. That is exactly the kind of grassroots experimentation we want.

What it stops is the leap from "this is useful for me" to "this should run across the function or the company" without going through the conversation about ownership and alignment.

If you have built something brilliant, the right next step is to find the ATO (or, if there isn't one yet, the exec who owns that area of work) and propose it. The output of that conversation is either:

1. We adopt your work as the basis of the function's canonical skill, with the ATO taking ownership going forward, or
2. We don't adopt it now, because it conflicts with how the leader wants the function to operate, or because there are higher-priority changes in flight.

Both outcomes are legitimate. Both are better than rolling out an unowned agent and discovering six months later that it has quietly trained a hundred people to do something the leader never agreed to.

## Our posture: guided creation

Put all of that together and it describes a deliberate stance, worth naming so we stay consistent about it. Our posture is guided creation. Anyone can build, anyone can experiment, and we want them to. What is gated, on purpose, is the step from personal use to canonical, shared process: that goes through an owner and a review, in whichever of the three scopes fits.

That is a choice, and not the only one we could have made. We could have locked it down, where a central team builds and everyone else only consumes. We could have gone fully open, where anything one person builds publishes to everyone by default. Guided creation sits between the two deliberately. It keeps the grassroots energy that makes any of this work, while making sure nothing quietly becomes "how the function operates" without someone accountable agreeing to it.

The posture tightens where the stakes call for it. A process touching sensitive data, regulated work, or customer-facing commitments warrants heavier review before promotion, and occasionally admin-only creation. It can loosen too, once a function is mature and its review habits are trusted. The default, though, is guided creation, and it is the stance the rest of this page assumes.

For how this posture maps to the admin settings in Claude and Glean, see [Governance posture: platform mapping](./platform-mapping/).

## Human judgement is preserved

Owning process is not the same as removing judgement. The output of a skill is a starting point, not a final answer.

A call prep brief generated from a canonical skill is still tweaked by the AE before the call. A customer summary is still reviewed by the CSM before being shared. A draft email is still edited before being sent.

The process gives us a consistent foundation. The human supplies the context and judgement on top.

This is the right division of labour: the AI does the repeatable bit consistently, the human does the bit that requires taste and judgement well. This is the practical expression of our first guiding principle, [Amplify human contribution, don't automate it away](../guiding-principles/#principle-1-amplify-human-contribution-dont-automate-it-away).

## So what does this mean if you want to share what you've built?

This applies to anything that encapsulates reusable process: a prompt you paste from a note, a skill in any AI platform, a plugin, a fully wired agent. The moment you want it to operate beyond yourself or a small pilot group, work through these questions:

1. **Whose process does this encode?** If the answer is "mine," it is not ready for wider rollout. It needs to become someone's canonical process first.
2. **What's the right scope?** Three options:
   - **Repo-scoped** if it relates directly to using or modifying a specific repo. Owner: the repo's maintainers / CODEOWNERS.
   - **Function-scoped** if it serves a single function's work. Owner: the function exec, with an ATO maintaining the canonical version.
   - **Company-wide** if it applies horizontally across the company. Owner: the right central home (People, Ops, Comms, ETA, etc.). ETA can help work this out.
3. **Is the owner identified and ready?** Repo maintainer, function exec + ATO, or central owner. If yes, that's your first conversation. If no, the conversation is with whoever's accountable about who that should be.
4. **Is the process versioned and reviewable?** For repo-scoped this is automatic, it's git. For function-scoped and company-wide, it needs to live somewhere it can be reviewed, branched, merged, and rolled out, not in a personal notes app or a private workspace.
5. **Does the owner actually want this to be how their domain operates?** If you cannot answer this, you are not yet ready to share more widely.

If you can answer all five, you have a real proposal. If you cannot, you have a prototype, and the next step is conversation rather than rollout.

## How to propose something for adoption

The short version, whether what you've built is a prompt, a skill, a plugin, or a full agent:

1. Identify the scope: repo, function, or company-wide.
2. Identify the owner: repo maintainer / CODEOWNERS, function exec + ATO, or central home.
3. Bring them the prototype, the use case, and the proposed adoption path.
4. Let the owner take responsibility for the canonical version going forward.

If you are unsure who the right owner is, the ETA team can help you find them.

## FAQ

**"But there isn't an agent doing this today. Surely something is better than nothing?"**

Maybe. But "something" still has to be aligned with how the leader wants the function to operate, otherwise we are encoding accidental strategy. The fix is usually fast: a short conversation with the right exec, an ATO taking ownership, and then we can move quickly. The fix is rarely "just turn it on."

**"This feels like bureaucracy on top of a fast-moving space."**

It is the opposite. Without ownership, every change to how we work happens through a hundred uncoordinated individual prompt edits. With ownership, a single change at the source updates every user instantly. The owned model is faster, not slower, once it exists.

**"I built this on my own time, why does someone else now own it?"**

The personal version is still yours. What changes is the canonical, function-wide version, which has to be owned by the function. In practice, the original builder is very often the right person to keep contributing, and ATO ownership is about accountability and review, not authorship.

**"Where does the ATO sit?"**

Embedded in the function, not in the ETA team. The ATO is part of Marketing, or Sales, or CX, or wherever the work is being done. ETA supports them with the tooling, the patterns, and the platform.

**"Doesn't this just apply to skills in a central marketplace? What about skills that live in a repo?"**

Repo-scoped skills are explicitly encouraged when the skill is genuinely tied to that repo's usage or modification. The repo maintainers are the owner, git is the versioning mechanism, merge requests are the review mechanism. The principle on this page is about ownership, not about a single canonical marketplace. See the Repo-scoped skills section above for the test that determines whether a skill actually belongs in a repo or only looks like it does.

## Summary in one paragraph

A prompt is process. A collection of process is strategy. Strategy needs an owner. Therefore every prompt, skill, plugin, or agent that is going to operate beyond an individual needs an owner. That ownership can sit in three places: with a function's exec and ATO when the process serves that function's work; with a repo's maintainers / CODEOWNERS when the process is tightly scoped to that specific repo; or with the right central home when the process is horizontal across the company (with ETA as interim home where the natural owner isn't yet obvious, and commit-and-iterate as the right pace). Until that ownership exists somewhere appropriate, what you've built is not ready for wider rollout. This is not a bottleneck, it is the thing that makes the system change-able when the strategy itself changes.
