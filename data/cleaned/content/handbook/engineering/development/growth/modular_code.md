---
title: Modular Code Guiding Principle
description: "Why and how Growth Engineers write modular code by default, optimizing for AI-native collaboration and long-term maintainability"
---

## Why modularity is our default

Growth Engineers write modular code **by default**. This is a guiding principle for how we
work, not an optional refactoring activity we get to "if there is time."

When delivery pressure is high, it is tempting to reach for whatever is fastest in the
moment: tightly coupled code that is quick to add to today but expensive to change, test, and
reason about later. We are deliberately moving away from that. Modularity is how we keep
moving fast _without_ accruing the debt that eventually slows everyone down.

### Scope and relationship to other documentation

This page is intentionally a **thin, Growth-scoped expectations layer**. It states what we
expect of Growth Engineers and delegates the _how_ to GitLab's canonical sources (linked
under [Guides and further reading](#guides-and-further-reading)) rather than restating that
guidance here. The aim is to keep one place that says "this is the expectation in Growth,"
not to create a competing source of truth.

We are starting in Growth on purpose. These expectations apply to how we operate as fullstack
engineers who iterate quickly, and scoping it here lets us model the behavior before proposing
broader adoption. If it proves useful, the natural next step is to promote the durable parts
into the company-wide engineering documentation.

### AI-native collaboration (lead reason)

We are building toward a future where engineers collaborate with AI agents across the full
development lifecycle. AI can only suggest correct, safe changes when the code exposes
**clear, well-bounded interfaces**:

1. Small modules with explicit inputs and outputs give AI the context it needs to reason about
   a change without loading the entire system into its working memory.
1. Clear seams mean an AI-suggested change is localized and reviewable, rather than rippling
   unpredictably across the codebase.
1. Well-named, single-responsibility units make intent legible to both humans and agents.

In short: **modular interfaces are a prerequisite for AI to help us correctly.** Tightly
coupled code is as hard for an agent to safely modify as it is for a new engineer.

### Maintainability (the durable reason)

The same properties that make code AI-friendly are the ones that have always made code good:

1. **Change isolation** — a change in one module does not force changes across unrelated areas.
1. **Testability** — small units with clear boundaries are straightforward to test directly.
1. **Readability and onboarding** — new engineers (and our future selves) can understand one
   piece without understanding everything.
1. **Clear ownership** — bounded modules map cleanly to responsibility and review.

AI-friendliness and maintainability are not in tension. They are the same discipline, and
investing in it pays off regardless of how the tooling evolves.

## What is expected of Growth Engineers

You do not need to be a software architect to apply this. The expectation is that you make
the modular choice your **default reflex**, and that you can articulate _why_ in reviews and
refinement. Concretely:

1. **Prefer small, single-responsibility units.** When a method, class, or component starts
   doing several things, split it.
1. **Make boundaries explicit.** Depend on clear interfaces, not on the internals of other
   modules. Pass what you need rather than reaching across the system.
1. **Plug new work into well-defined seams.** New features and changes should connect through
   clear extension points so they can be added, changed, or removed without untangling
   unrelated code.
1. **Leave it more modular than you found it.** When you touch a tangled area, make a small,
   in-scope improvement to the seam you are working in (boy scout rule), rather than adding to
   the tangle for speed.
1. **Be able to explain the seam.** In an MR or refinement, you should be able to say what the
   module's responsibility is, what its interface is, and why the boundary sits where it does.

## This is a learned skill — that is okay

Writing modular code well is a skill that builds over time, and it can feel slower at first
than just adding to existing code. That trade-off is expected and acceptable. We would rather
invest in the skill now than pay compounding interest on tangled code later. If you are unsure
where a boundary should go, raise it early — in refinement, in `#sd_growth_engineering`, or with a
[Engineering DRI](engineering_dri) — and treat it as a design conversation, not a blocker.

## How this shows up in our workflow

This is a judgment-based principle, not something a linter can fully check. It is reinforced
through how we already work, and it is owned by the whole engineering team — not policed by any
one reviewer.

1. **Refinement.** Knowing where the seams are is an output of refinement. This does _not_ mean
   splitting every change into more issues. It means the engineer understands the boundaries
   well enough to make a judgement about how many merge requests a change warrants and how to
   slice it.
1. **Code review.** Our [code review](/handbook/engineering/workflow/code-review/) is the main
   place this principle is reinforced. Reviewers are expected to raise coupling and boundary
   concerns, and engineers should be able to explain the seam — what a module's responsibility
   is, what its interface is, and why the boundary sits where it does.
1. **Tooling.** Where formal boundaries already exist — for example
   [bounded contexts](https://docs.gitlab.com/development/software_design/#bounded-contexts) on
   the backend and frontend encapsulation work — CI enforces them. Everything else is human
   judgement applied in review.

### Prefer vertical over horizontal changes

Knowing where the seams are lets you slice a change **vertically** — a thin slice that goes
end-to-end through the layers it touches and delivers value — rather than **horizontally**,
where you do all the database work, then all the backend work, then all the frontend work as
separate changes. Vertical slicing both _requires_ and _reinforces_ clean seams: you can only
cut a thin end-to-end slice when the boundaries between layers are explicit.

This matters more for Growth because our teams are staffed with
[Fullstack Engineers](/handbook/engineering/development/growth/#how-we-work). One
engineer typically owns the whole slice, from the database through to the UI, so we are
uniquely positioned to ship a coherent vertical slice in a single merge request where the
reviewer can see the full picture. Splitting the same change horizontally forces an artificial
handoff across layers the same person is writing, makes review harder (each layer lacks the
context of the others), and adds the risk of merging code without seeing the whole change. For
a small fullstack team, vertical slices are the lower-overhead, faster-feedback default.

This is a judgement call, not a rule. Sometimes the right answer is a single vertical merge
request; sometimes it is a few. Horizontal slicing is still the better choice when layers are
genuinely independent. See
[Tradeoffs between horizontal and vertical slicing](/handbook/engineering/workflow/iteration/#tradeoffs-between-horizontal-and-vertical-slicing)
and our [Iteration value](/handbook/values/#iteration) for more.

## Guides and further reading

This principle is grounded in GitLab's existing engineering standards. Use these as your
practical reference for _how_ to draw boundaries:

1. [Software design guides](https://docs.gitlab.com/development/software_design/) — GitLab's
   canonical guidance on bounded contexts, deep modules, and loose coupling / high cohesion.
1. [GitLab Modular Monolith design document](/handbook/engineering/architecture/design-documents/modular_monolith/)
   — the company-wide architecture direction this principle ladders up to.
1. Backend (Ruby): [Reusing abstractions](https://docs.gitlab.com/development/reusing_abstractions/)
   and the [Ruby style guide](https://docs.gitlab.com/development/backend/ruby_style_guide/).
1. Frontend (JavaScript/Vue): [Frontend design patterns](https://docs.gitlab.com/development/fe_guide/design_patterns/)
   and the [JavaScript style guide](https://docs.gitlab.com/development/fe_guide/style/javascript/).
1. External: [A Philosophy of Software Design](https://web.stanford.edu/~ouster/cgi-bin/aposd.php)
   (Ousterhout) on deep modules and minimizing complexity — the basis for much of the guidance above.

## Related

1. [Technical Exploration ("Spike") Guidelines](technical_spikes) — where modular design
   options are often explored before implementation.
1. [Milestone Planning, Refinement and Estimation](initiative_refinement_estimation) — where
   the cost of building the right seams should be reflected in estimates.
1. [Engineering DRI for Large-Scale Initiatives](engineering_dri) — for coordinating modular
   boundaries across larger, multi-issue efforts.
