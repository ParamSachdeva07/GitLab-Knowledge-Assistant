---
title: "Isolating the domain layer"
status: proposed
creation-date: "2026-06-12"
authors: [ "@fabiopitino", "@ayufan" ]
coach: [ ]
approvers: [ ]
owning-stage: ""
toc_hide: true
---

This page is the single source of truth for isolating the **application domain** —
the business logic at the core of the [hexagonal monolith](hexagonal_monolith/index.md) —
into bounded, independently-owned modules.

It covers domain code only. Extracting cross-cutting **platform** code is covered in
[Extracting cross-cutting libraries into gems](library_extraction.md); extracting the
**transport layer** (Web, REST, GraphQL, Sidekiq) is covered in
[Decomposing the transport layer into adapters](transport_layer.md). How domains are
identified and named is covered in [Defining bounded contexts](bounded_contexts.md).

Domain isolation is the hardest part of modularization. The platform and transport
layers have relatively clean seams; the domain is where the coupling actually lives.

## What domain isolation means

A domain is isolated when:

- **Nothing crosses its boundary except through its public API.** Other domains call
  a documented, intentional interface — they never reach into internals, AR models,
  or private services.
- **It exclusively owns its data.** The domain owns its database tables and the
  ActiveRecord models that map them. No other domain queries those tables or holds
  references to those models.

A well-designed domain module is also **deep** — it encapsulates a large amount of
internal logic, state, and data behind that small interface — and **cohesive**, acting as
the single source of truth for the feature it describes. It follows the
[guideline on naming namespaces](https://docs.gitlab.com/ee/development/software_design.html#use-namespaces-to-define-bounded-contexts)
and uses [ubiquitous language](https://docs.gitlab.com/ee/development/software_design.html#use-ubiquitous-language-instead-of-crud-terminology)
rather than CRUD terminology. How domains are identified and mapped to feature categories
is covered in [Defining bounded contexts](bounded_contexts.md).

Everything below is about the work required to get there.

## The hard part: cross-domain coupling

Our modular-monolith research surfaced the coupling that makes this difficult. In the
current codebase:

- **Policies depend on other policies** — for example `PipelinePolicy` delegates to
  `ProjectPolicy`.
- **Services depend on shared components** — publishing events, sending mail, system
  notes, auditing, and so on.
- **Domains depend on each other's AR models**, both explicitly (`Ci::Pipeline.find_by_id`)
  and implicitly through associations (`security_scan.pipeline`).
- **Circular dependencies** between domains are common.

This is why domain isolation cannot be a mechanical file move the way library and
transport extraction largely can. Most of the effort is *refactoring away the coupling*,
not relocating code.

## Owning the data

Exclusive data ownership is the core of isolation. Each domain owns its tables and the
AR models that map them, and is the only code allowed to query them.

Two enforcement problems follow:

**Cross-domain AR associations.** Today any domain can call `project.ci_pipelines` and
walk straight into CI's data. Isolation requires removing cross-domain associations and
going through the owning domain's public API instead — `Ci::Pipeline.all(project)` rather
than `project.ci_pipelines`. A prerequisite is
[Taming Omniscient Classes](https://docs.gitlab.com/development/software_design/#taming-omniscient-classes):
classes like `Project` and `User` accrete associations and methods from every domain and
must be slimmed down.

**Direct model references.** Even with associations gone, any code can reference
`Ci::Pipeline` directly. One option is to keep the AR model private to the domain — for
example `Ci::Internal::Pipeline` — so it cannot be referenced from outside, exposing
pipeline data only through the `Ci::*` public interface.

### Repository-pattern option

A more structured variant uses AR strictly as a persistence/repository layer, separate
from the domain object:

```ruby
# Persistence only — scopes and AR persistence, nothing else. Private to the domain.
Ci::Repository::Pipeline

# Domain object wrapping the record, exposing behaviour. The public type.
Ci::Pipeline   # #builds, #cancelable?, ...
```

The AR model is never used outside its domain object. This makes the domain trivially
stubbable in tests and removes the AR dependency from callers. The cost is significant:
it is a large, invasive refactor regardless of whether we ultimately extract gems.

## Cross-domain data and shared models

The thorniest question is what happens to shared entities like `Project` and `User`,
which nearly every domain touches.

**Strip shared models to identity objects.** If a cross-domain accessor returns the full
`Project` AR object, it drags in that object's entire surface and re-couples the domains.
Shared data should be reduced to a minimal identity object, not the full model.

**Domain-specific representations.** Rather than every domain consuming a shared
`Project`, a domain can wrap the data it needs behind its own facade:

```ruby
project = Ci::Internal::Project.new(project_id) # PORO or record local to the CI domain
project.variables       # internal to CI
project.public_builds?  # CI-specific project setting
project.pipelines       # pipelines queried via Ci::Project, not Project
```

This keeps `project.pipelines` inside the CI domain instead of on the global `Project`.
A related idea is per-domain owner objects — for example `Ci::JobOwner` wrapping a
`user_id` and delegating to `User` only for identity-specific concerns.

**Prefer direct dependencies over monolith callbacks.** Where a domain needs data from
another domain, prefer a direct, declared dependency on that domain's public interface
over wiring callbacks back into the monolith. Direct dependencies are trackable — we can
render a cross-domain dependency graph and use it in CI to run only the affected tests —
whereas callbacks hide the coupling.

**A stable client interface, swappable to gRPC later.** A domain can be treated as
external from the start: it exposes a Ruby client interface and keeps everything else
private. The backend behind that interface can later move to gRPC without changing
callers.

**Avoid chatty domains.** Once boundaries are enforced we will find components that are
too dependent on each other — Rails makes everything available all the time, so a single
business transaction reaches across many domains. Avoiding chatty cross-domain calls
(a real problem once domains become services) means denormalizing or duplicating data,
keeping local representations, and applying interface segregation — for example a slim
`Ci::Internal::User` that wraps a basic identity object instead of the full `User`.

> The shared "scaffolding" every domain needs — `Project`/`User` lookups, permission
> checks, and similar — might instead live in a coarse `gitlab-platform`/`gitlab-core`
> gem that every domain depends on, rather than being injected per-domain. That
> trade-off is tracked as an
> [open question on the library-extraction page](library_extraction.md#open-questions).

## What must be resolved before extraction

Domain isolation is mostly unanswered design work. Before extracting a domain — into a
gem **or** a package — we need reproducible guidelines, so the refactor is not left to
per-engineer or per-agent interpretation, for at least:

1. What happens to cross-domain **AR associations**.
1. What logic lives on the **AR model** versus the **domain object**.
1. What data is allowed to **cross a boundary**, and in what shape.
1. What to do when a caller receives a data object but needs a method on a **domain
   object** (for example `Ci::Pipeline#merge_request`) — without creating chatty domains
   or over-serializing responses (a current pain in REST).
1. Who **owns database migrations**, and where they live.
1. Whether `Project` is a **shared model** or becomes a `Projects` **domain**.
1. How **EE and JH** extensions are isolated alongside the domain — the same extension
   problem the library and transport layers face.
1. How **tests** decouple. Factories are global and heavily coupled. As domains decouple,
   each should expose a public interface for specs/factories, or callers should stub
   rather than build cross-domain records:

  ```ruby
  RSpec.describe Ci::Pipeline do
    let(:user)    { Gitlab::Platform::Specs.create_user }
    let(:project) { Gitlab::Platform::Specs.create_project }
  end
  ```

The glue code that bridges domains during the transition could be very large. We likely
need a proof of concept to learn what it actually contains before committing to a
strategy.

## Where domain code lives: `domains/` vs `gems/`

Domain code should live under a dedicated `domains/` directory, separate from the `gems/`
directory used for cross-cutting libraries. Both can use the gem format, but separating
them buys us:

- No flat sprawl of mixed-responsibility gems under a single `gems/`.
- A clear distinction between **domain code** and **generic code**.
- The ability to track and visualise **cross-domain** dependencies separately from
  dependencies on generic libraries — an architecture-level diagram of domain
  relationships.
- An enforceable rule: a library may depend on another library, but **never on a
  domain**. Static analysis can enforce this in CI.

Domains follow [`config/bounded_contexts.yml`](https://gitlab.com/gitlab-org/gitlab/-/blob/master/config/bounded_contexts.yml)
and use their bounded-context namespace directly (`Ci::`, `Packages::`) — not a `Gitlab::`
prefix.

Optionally, a large domain can be broken into nested, private sub-domain gems:

```ruby
# domains/ci/ci.gemspec  (the public domain gem)
spec.add_dependency "ci-pipelines"
spec.add_dependency "ci-runners"
spec.add_dependency "ci-catalog"
```

## How we get there: gems, Packwerk, or both

**This is not decided.** We have not agreed whether domain decomposition uses Ruby gems,
[Packwerk](https://github.com/Shopify/packwerk) packages, or a combination — because the
decoupling challenges above dominate the choice of mechanism.

The trade-off:

- **Gems** give hard isolation and explicit, declared dependencies. But a gem extraction
  is **atomic**: the code must be fully isolated in a single step. That is painful for
  large, complex, tightly-coupled domains that can only be untangled gradually.
- **Packwerk (optional).** Static analysis can assist gradual, guided isolation *in
  place* — drawing a package boundary without moving files, surfacing privacy and
  dependency violations, and letting a domain's owners work the violations down over
  time. With RBS type signatures it can even catch implicit dependencies such as
  `security_scan.pipeline` when `Ci::Pipeline` is not an allowlisted constant. Once a
  domain is sufficiently isolated this way, a later gem extraction is far simpler.

The two are not mutually exclusive: an extracted gem can carry its own Packwerk
configuration to keep enforcing what it may depend on. Packwerk is a **complementary,
optional** tool for the gradual path — not a committed approach, and not a replacement
for gems.

### An optional gradual path with Packwerk

If we take the gradual route, the steps below describe how it could work.
They are **one option**, not a decision:

1. **Namespace first.** Put all classes and modules for a
   [bounded context](bounded_contexts.md) under the same namespace. Without a rough
   understanding of the domains no plan is possible; consistent namespacing is the
   prerequisite.
1. **Prepare Rails for Packwerk** — a once-off step: make the autoloader work with
   Packwerk's directory layout (as in
   [this PoC](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/129254/diffs#note_1512982957)),
   run [Danger-Packwerk](https://github.com/rubyatscale/danger-packwerk) in CI, and
   optionally a pre-commit/pre-push check.
1. **Move files into a package** — create the package and move files in iteratively.
   Constants autoload whether under `app/` or `lib/` inside a package. Code is split
   between the package and the Rails tree during this phase, so move quickly.
1. **Enforce boundaries** — require packages to
   [declare dependencies explicitly](https://github.com/Shopify/packwerk/blob/main/USAGE.md#enforcing-dependency-boundary)
   and depend only on a package's
   [public interface](https://github.com/rubyatscale/packwerk-extensions#privacy-checker).
   Enforcing privacy *after* moving files reveals the real coupling between constants and
   domains as recorded violations (like RuboCop TODOs).
1. **Work off the recorded violations** — a long-term phase the domain's DRIs nurture:
   make over-coupled constants private, move a constant to a better-fitting package, or
   merge packages that are too coupled, using the dependency diagram to guide the design.

Once the tooling exists, emerging domains can be implemented as packages from the start
and get isolation and a clear interface immediately.

## Related

- [Defining bounded contexts](bounded_contexts.md) — how domains are identified and named.
- [Hexagonal Rails Monolith](hexagonal_monolith/index.md) — the three-layer model.
