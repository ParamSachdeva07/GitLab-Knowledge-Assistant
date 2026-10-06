---
title: "Modular Monolith ADR 003: Module stewardship"
creation-date: "2024-05-08"
authors: [ "@fabiopitino" ]
toc_hide: true
---

## Context

How do we assign stewardship to domain and platform layer? We have a large amount of shared code
that does not have explicit stewards who can provide a vision and direction on that part of code.

## Decision

We use the term **stewards** instead of **owners** to be more in line with GitLab principle of
**everyone can contribute**. Stewards are care takers of the code. They know how a specific
functionality is designed and why. They know the architectural characteristics and constraints.
However, they welcome changes and guide contributors towards success.

A module, whether is from a domain bounded context or platform layer, must have at least 1 group of stewards.
This group can be a team name (or GitLab group handle). Optionally, the list of stewards can include
single IC entries.

We have not yet decided on the code-structure mechanism for modules (e.g. Packwerk packages
or gems). Until that decision is made, we indicate stewardship using the existing `CODEOWNERS`
file, assigning the module's directory to one or more groups (and optionally individual ICs):

```text
/ci/ @gitlab-org/maintainers/pipeline-execution @gitlab-org/maintainers/pipeline-authoring @grzesiek @ayufan
```

If we later adopt a code-structure mechanism that carries metadata (such as a Packwerk
`package.yml` or a gemspec), stewardship can move into that metadata and the relevant
`CODEOWNERS` sections can be generated from it.

Gems extracted from the platform layer (e.g. `Gitlab::Redis`) should also have stewards assigned.

## Consequences

Stewardship defined in code can be very powerful:

- Review Roulette or Suggested Reviews features use `CODEOWNERS` to route reviews to stewards.
- Engineers can easily identify stewards and have design conversations early.

## Alternatives

Instead of using `CODEOWNERS`, we could rely on each team to informally know what bounded contexts
they are responsible for, without recording stewardship anywhere. For the "shared code" in the
platform modules we would expect maintainers to fill the role of stewards.

- Pros: we give trainee maintainers a clear development path and goals. Today it feels unclear what they must
  learn in order to become successful maintainers.
- Cons: The amount of "shared" code is very large and still hard to understand who knows best about
  a particular functionality. Without an explicit record, stewardship stays tribal knowledge — invisible
  to new contributors and to agents — which is exactly what modularization aims to remove.
