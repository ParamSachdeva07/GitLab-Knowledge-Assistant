---
title: "Extracting cross-cutting libraries into gems"
description: "How and why GitLab extracts cross-cutting, ActiveRecord-free platform libraries out of lib/ and ee/lib into Ruby gems under gems/."
status: proposed
creation-date: "2026-06-12"
authors: [ "@fabiopitino", "@ayufan" ]
coach: [ ]
approvers: [ ]
owning-stage: ""
toc_hide: true
---

This page is the single source of truth for extracting cross-cutting **platform**
(library) code out of `lib/` and `ee/lib` into Ruby gems under `gems/`. The
decision to do this is recorded in
[ADR-004: Extract cross-cutting libraries into gems](decisions/004_library_extraction/).

It covers only the extraction of generic, cross-cutting libraries. It does **not**
cover feature-domain extraction, transport/layer gems, or deployment modes —
those are separate concerns described elsewhere in the
[modular monolith design](_index.md).

## What is platform code?

Platform code is the third layer of the [hexagonal monolith](hexagonal_monolith/index.md),
alongside the [application domain](hexagonal_monolith/index.md#application-domain) and the
[application adapters](hexagonal_monolith/index.md#transport-layer). It is the set of
classes and modules that the domain and adapters depend on in order to run, but
which carry no business logic of their own.

These are genuine **cross-cutting concerns**: logging, error reporting, metrics,
rate limiters, parsers, and generic utilities such as `Banzai`. They are useful
to many domains precisely because they know nothing about any single domain.

The defining property of true platform code is that it **does not depend on
ActiveRecord models**. If a piece of code reaches into `Project`, `User`, a
service, or any AR model, it is almost certainly **domain code** — it belongs
with its domain, not in `gems/`. See [Be skeptical of "generic"](#be-skeptical-of-generic).

## The problem

The Rails `lib/gitlab/` directory has become a junk drawer. It holds roughly
3,100 files (~94,000 lines) that mix three very different categories of code:

1. **Generic / universal** — utilities, parsers, and data structures with no
   ActiveRecord dependencies. True platform code.
1. **GitLab-specific but isolated** — libraries that reference GitLab concepts
   but not application models. Also extractable.
1. **Tightly coupled** — code that depends on AR models, services, or the Rails
   runtime. This is domain code wearing a `lib/` disguise.

Category 1 definitely contains the extraction candidates. Category 2 will depend
on how we decide to group domain-specific libraries. Category 3 is not: it should
move to its [bounded context](bounded_contexts.md).

This mixing hides dependencies, blurs ownership, and lets generic-looking code
quietly couple itself to the application.

## Goals

1. **Enforced isolation** — a gem declares its dependencies explicitly. Hidden
   dependencies become visible errors instead of silent coupling.
1. **Clearer ownership** — each gem carries an explicit `feature_category:` and
   maps to a team boundary.
1. **Establish the pattern and tooling** — a repeatable extraction recipe and CI
   wiring that later decomposition work can reuse.
1. **Faster CI** — a real but limited benefit; see [the caveat below](#a-note-on-ci-speedups).

## Be skeptical of "generic"

Not everything that looks generic should be extracted. The strongest smell that
a "library" is really domain logic is needing to **inject AR data into it** to
make it work.

The tempting pattern is to keep the AR dependency out of the gem by having the
monolith feed it data through callbacks with tailored data structures:

```ruby
# The gem defines the shape of data it needs
Gitlab::Diff::FileInfo = Struct.new(:path, :content, :size, keyword_init: true)

# The monolith wires a lambda that maps an AR object to that shape
Gitlab::Diff.config.find_file = ->(id) {
  blob = Repository.find_blob(id)
  Gitlab::Diff::FileInfo.new(path: blob.path, content: blob.data, size: blob.size)
}
```

Treat this with caution. If you find yourself reaching for dependency injection
or callbacks to feed AR-derived data into a "generic library", that is usually a
sign the code is **not** generic at all — it is domain logic that should move to
its bounded context. Use callbacks sparingly and deliberately, not as the happy
path for every extraction.

## Namespacing

Extraction is an opportunity to give code the right namespace.

- **Platform / non-domain code** may keep the `Gitlab::` namespace. Note the
  ongoing debate that `Gitlab::` adds little value beyond collision-avoidance —
  it tells you nothing about what the code does.
- **Domain code pulled out of `lib/gitlab/`** should **not** keep `Gitlab::`. It
  should move to its explicit [bounded context](bounded_contexts.md) namespace
  per [`config/bounded_contexts.yml`](https://gitlab.com/gitlab-org/gitlab/-/blob/master/config/bounded_contexts.yml).

## Extraction pattern

All in-repo gems live in `gems/` and are referenced via `path:` in the Gemfile.

1. **Move files** — relocate `lib/gitlab/<name>/` (and any `ee/lib/gitlab/<name>/`)
   into `gems/gitlab-<name>/`. Keep the namespace for platform code; re-namespace
   domain code (see [Namespacing](#namespacing)).

1. **Keep it AR-free** — a library gem must not reference AR models. If it
   needs application data, that is a [signal to reconsider](#be-skeptical-of-generic)
   whether the code is really a library at all.

1. **Wire into the Gemfile**

   ```ruby
   gem 'gitlab-<name>', path: 'gems/gitlab-<name>',
     require: false, feature_category: :<category>
   ```

1. **EE extensions** — EE code lives in an `ee/` folder inside the gem directory.
   The gem's entry point conditionally loads the `ee/` tree in EE context.

   ```text
   gems/gitlab-<name>/
     lib/
       gitlab/<name>/...
     ee/
       gitlab/<name>/...     # EE overrides
     spec/
   ```

1. **Per-gem CI** — each gem gets a `gems/<name>/.gitlab-ci.yml` and an entry in
   `.gitlab/ci/gitlab-gems.gitlab-ci.yml`, so it runs its own isolated test suite.

## Candidates

The candidates below are illustrative tiers, ordered by how cleanly they
separate from the monolith. Only Tier 1 and the AR-free parts of Tier 2 are true
library candidates; tightly-coupled code belongs with its domain.

### Tier 1 — Low coupling, high value

| Library | Current location | Notes |
|---------|------------------|-------|
| `ci/parsers` + `ci/reports` | `lib/gitlab/ci/parsers/`, `lib/gitlab/ci/reports/` | Parsing/report data structures |
| `regex` | `lib/gitlab/regex/` | Pure Ruby |
| `slug` | `lib/gitlab/slug/` | Pure utility |
| `json` | `lib/gitlab/json/` | Wrapper around Oj/JSON |
| `sanitizers` | `lib/gitlab/sanitizers/` | HTML/text sanitization |
| `diff` | `lib/gitlab/diff/` | Diff parsing and formatting |
| `template_parser` | `lib/gitlab/template_parser/` | Template parsing logic |
| `word_diff` | `lib/gitlab/word_diff/` | Word-level diff |

### Tier 2 — Moderate coupling, clear seams

These contain a separable generic core plus AR-coupled glue. Extract only the
generic core; the AR-coupled part stays with its domain.

| Library | Current location | What stays behind |
|---------|------------------|-------------------|
| `pagination` | `lib/gitlab/pagination/` | Keyset pagination is generic; AR scopes stay |
| `search` | `lib/gitlab/search/` | Query building is separable from AR scopes |
| `changelog` | `lib/gitlab/changelog/` | Templating is generic; commit/repository access stays |

### Tier 3 — Coupled to AR but still possible

This code depends on AR models, the Rails runtime, or cuts across all domains.
It is **not** a library. It either stays in the monolith or moves to its bounded
context.

| Library | Reason |
|---------|--------|
| `auth` | Touches Devise, OmniAuth, session, and every model |
| `background_migration` | Inherits from AR, references schema directly |
| `event_store` | Publishes/subscribes across all domains |
| `sidekiq_middleware` | Depends on the Rails middleware stack |

## Sequencing and circular dependencies

Extracting code into a gem is an **atomic refactor**: in a single step the code
must declare all its dependencies and be fully isolated. That strictness is
exactly what makes gems good at enforcing explicit dependencies — but it is
painful for large or complex code that can only be isolated gradually.

Two pieces of guidance follow from this.

**Start from the bottom.** Begin with the lowest-level code that has no
dependencies and walk upward. This avoids creating circular dependencies between
half-extracted gems.

**Start fine, not coarse.** Extract small, focused gems one at a time.
The cleanly-separable [Tier 1](#tier-1--low-coupling-high-value) libraries already
have good seams, so each one is a small atomic refactor that is easy to land,
test, and revert. This proves the extraction pattern and CI wiring sooner.

### Optional: Packwerk-assisted gradual isolation

For code that cannot be isolated in a single atomic move,
[Packwerk](https://github.com/Shopify/packwerk) (static analysis) can **assist**
the gradual path. It lets you draw a package boundary in place and surface
dependency and privacy violations without moving any files or changing runtime
behavior. Once enough isolation is achieved, the eventual gem extraction is much
simpler.

The explicit dependency and privacy graph Packwerk produces is also valuable for
**AI-agentic refactoring**: it gives an agent a precise, machine-readable map of
what a piece of code depends on and what depends on it, so the agent can reason
about the blast radius of an extraction instead of inferring it from implicit
coupling. This makes Packwerk a useful aid for agent-driven extraction work.

Packwerk is an **optional, complementary** tool for the gradual path, not the
main approach — and the handbook treats it as a
[proof-of-concept / proposal](proof_of_concepts.md#use-packwerk-to-enforce-module-boundaries),
not a committed approach. The primary path remains direct, atomic gem extraction
starting from the lowest-level code.

## A note on CI speedups

Isolating code into a gem lets CI test it only when it — or something it depends
on — actually changes, instead of re-running it as part of the monolith's suite
on every change. This is precisely why isolating **stable** code pays off:
`lib/gitlab/` libraries are largely stable and rarely changed, so once they are
behind a gem boundary their suites rarely need to run at all. Stable, low-churn
code is the best candidate for this kind of CI saving, not the worst.

The benefit is real but not unbounded. In a tightly coupled system gems remain
interconnected — many domains depend on CI, and CI depends on many gems — so when
a heavily-depended-on gem does change, its pipeline still cascades across every
dependent. The win comes from isolating low-churn code so it rarely triggers that
cascade, not from eliminating the cascade itself.

## Open questions

- **Explicit per-gem dependencies, or a shared platform gem?** Should every domain
  gem or module declare all of its dependencies explicitly (for example in its
  gemspec), or should it depend on a single "platform" gem — [LabKit](https://gitlab.com/gitlab-org/labkit-ruby)
  or similar — that provides the basic tooling a domain needs to run (logging,
  error reporting, observability, strong-memoize, and so on)? Explicit
  dependencies make coupling fully visible and keep each gem minimal; a shared
  platform gem reduces boilerplate and gives every domain a consistent baseline,
  at the cost of a coarse, widely-depended-on dependency.
- **How are EE extensions handled?** Each gem carries its EE code in an `ee/`
  folder, but it is unresolved how EE-only *dependencies* are declared. If a gem
  needs a dependency only used by its `ee/` tree, is it declared unconditionally
  in the gem's gemspec, or conditionally — and does that imply a split `Gemfile`
  and `Gemfile.ee`? This likely depends on how we package GitLab FOSS versus EE.
