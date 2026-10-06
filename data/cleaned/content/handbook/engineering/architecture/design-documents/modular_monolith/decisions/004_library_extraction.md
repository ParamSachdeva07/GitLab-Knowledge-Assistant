---
title: "Backend decomposition ADR 004: Extract cross-cutting libraries into gems"
creation-date: "2026-06-12"
authors: [ "@fabiopitino", "@ayufan" ]
toc_hide: true
---

## Context

[ADR-001](001_modular_application_domain/) established that the "platform" layer —
the technical, cross-cutting code that today largely lives in `lib/` and
`ee/lib` — can be broken down into independent libraries extracted as gems. This
ADR commits to how we do that.

`lib/gitlab/` has become a junk drawer mixing three kinds of code: genuinely
generic utilities, GitLab-specific but isolated libraries, and code that is
tightly coupled to ActiveRecord models and the Rails runtime. The last category
is domain code, not platform code.

The detailed extraction pattern, candidate tiers, and sequencing guidance live
in the [Extracting cross-cutting libraries into gems](../library_extraction.md)
page, which is the single source of truth for this topic.

## Decision

We extract cross-cutting **platform** libraries out of `lib/`/`ee/lib` into Ruby
gems under `gems/`, referenced via `path:` in the Gemfile, with the following
commitments:

- **Libraries must be ActiveRecord-free.** Only true cross-cutting concerns
  (logging, error reporting, metrics, rate limiters, parsers, generic utilities
  like `Banzai`) become gems. Needing to inject AR data into a "library" is a
  signal that it is not generic.
- **Domain code will follow the bounded context strategy.** AR-coupled code pulled
  out of `lib/gitlab/` moves to its
  [bounded context](../bounded_contexts.md) namespace per
  `config/bounded_contexts.yml` — it does not keep the `Gitlab::` prefix.
  Platform code may keep `Gitlab::`.
- **Gem extraction is an atomic refactor**, optionally Packwerk-assisted for
  code that can only be isolated gradually. Packwerk is a complementary tool,
  not the main path.
- **Start fine, from the bottom.** Begin from the lowest-level dependency-free
  code and extract small, focused gems one at a time. That proves the extraction
  pattern and CI wiring sooner.

## Consequences

- Dependencies that were implicit become explicit and enforced at the gem
  boundary; hidden coupling surfaces as errors.
- Each gem carries an explicit `feature_category:` and a clearer owner, and runs
  its own isolated CI suite.
- The CI speedup is modest in practice — `lib/gitlab/` libraries are stable and
  gems remain interconnected — so the primary value is establishing the pattern,
  tooling, and isolation rather than CI time saved.
- The exercise forces a useful classification: code that resists AR-free
  extraction is revealed as domain code and routed to its bounded context.

## Alternatives

- **Leave platform code in `lib/`** and rely only on static analysis to enforce
  boundaries. Rejected as the primary path: keeping everything in `lib/` does not
  improve the design — interfaces stay blurred and coupling unconstrained — and
  it does not let us run fewer CI tests, since the code stays part of the
  monolith's suite. A gem gives code an explicit, isolated dependency declaration
  and its own CI suite that `lib/` cannot.
