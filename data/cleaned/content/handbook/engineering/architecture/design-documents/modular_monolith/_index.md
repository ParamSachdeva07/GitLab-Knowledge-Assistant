---
title: "Rails Monolith Decomposition"
status: proposed
creation-date: "2023-05-22"
authors: [ "@grzesiek", "@fabiopitino", "@ayufan" ]
coach: [ ]
approvers: [ ]
owning-stage: ""
participating-stages: []
toc_hide: true
---

{{< engineering/design-document-header >}}

## Summary

The main [GitLab Rails](https://gitlab.com/gitlab-org/gitlab)
project has been implemented as a large monolithic application, using
[Ruby on Rails](https://rubyonrails.org/) framework. It has over 2.2 million
lines of Ruby code and hundreds of engineers contributing to it every day.

The application has been growing in complexity for more than a decade. The
monolithic architecture has served us well during this time, making it possible
to keep high development velocity and great engineering productivity.

Even though we strive for having [an approachable open-core architecture](https://about.gitlab.com/blog/2022/07/14/open-core-is-worse-than-plugins/)
we need to strengthen the boundaries between domains to retain velocity and
increase development predictability.

The same is true of the frontend. The web UI is a large, tightly coupled
JavaScript and Vue codebase built and shipped as a single Webpack bundle. It
shares the monolith's fate: everything is compiled, deployed, and released
together, and there is no way to evolve or ship one area of the UI
independently of the rest. Decomposition therefore has two complementary
tracks — a **backend** track that modularizes the Rails application, and a
**frontend** track that modularizes the build pipeline and UI. Both share the
same goals and principles described below.

### Why now: the agentic imperative

The way software gets built is shifting. Agentic AI changes what is possible
when agents pick up work as soon as an issue is filed, operate independently
within a well-defined area of the codebase, and validate their own work before
opening an MR. To unlock this, a module needs clear boundaries, explicit
contracts, and no tribal knowledge baked into how it is built and run.

The monolith was built for human developers who carry years of context in their
heads. Agents have no such context: they cannot safely change one area without
reasoning about the whole, because dependencies are implicit and the knowledge
needed to work safely does not all live in the repository.
Modular boundaries make an area of the codebase small enough for an agent —
and a human — to reason about in isolation.

This reframes modularization. It is no longer only about engineering velocity
and cognitive load; it is the structural prerequisite for agentic development at
scale. A module with clear contracts, self-contained context, and high test
coverage is one where agents can work autonomously, where fixes reach customers
sooner, and where teams move at their own pace without being dragged down by
monolith coupling.

### What we are building toward

We want to evolve toward
[a modular monolith design](https://en.wikipedia.org/wiki/Modular_programming),
while still using a [monolithic architecture](https://en.wikipedia.org/wiki/Monolithic_application)
with satellite services, and — for the modules where it pays off — toward
independently deployable units that integrate with the monolith, on GitLab.com,
on Dedicated, and on self-managed instances against a single contract.

This should allow us to increase engineering efficiency, reduce the cognitive
load, make the codebase legible to AI agents, and eventually decouple internal
components to the extent that allows us to deploy and run them separately when
the return on that investment is clear.

On the frontend, this means independently buildable and deployable UI modules
that integrate through a shared shell application and an explicit module
contract — the visual counterpart to the backend's bounded contexts and public
interfaces.

## Motivation

Working with a large and tightly coupled monolithic application is challenging:

Engineering:

- Onboarding engineers takes time. It takes a while before engineers feel
  productive due to the size of the context and the amount of coupling.
- We need to use `CODEOWNERS` file feature for several domains but
  [these rules are complex](https://gitlab.com/gitlab-org/gitlab/-/blob/409228f064a950af8ff2cecdd138fc9da41c8e63/.gitlab/CODEOWNERS#L1396-1457).
- It is difficult for engineers to build a mental map of the application due to its size.
  Even apparently isolated changes can have [far-reaching repercussions](../../../devops/#reducing-the-impact-of-far-reaching-work)
  on other parts of the monolith.
- Attrition/retention of engineering talent. It is fatiguing and demoralizing for
  engineers to constantly deal with the obstacles to productivity.

Architecture:

- There is little structure inside the monolith. We have attempted to enforce
  the creation [of some modules](https://gitlab.com/gitlab-org/gitlab/-/issues/212156)
  but have no company-wide strategy on what the functional parts of the
  monolith should be, and how code should be organized.
- There is no isolation between existing modules. Ruby does not provide
  out-of-the-box tools to effectively enforce boundaries. Everything lives
  under the same memory space.
- We rarely build abstractions that can boost our efficiency.
- Boundaries are silent on the database. Even apparently isolated domains
  share tables, hold cross-boundary foreign keys, and keep ORM associations
  that span the line. Data coupling is what actually blocks extraction.
- Moving stable parts of the application into separate services is impossible
  due to high coupling.
- We are unable to deploy changes to specific domains separately and isolate
  failures that are happening inside them.

Agentic AI:

- Agents have no implicit context. They cannot safely change one area without
  reasoning about the whole, because dependencies are implicit and the blast
  radius of a change is unclear.
- The knowledge needed to work in a domain — its boundaries, contracts,
  invariants, and runbooks — does not all live in the repository.
- Without clear boundaries and self-contained context, an agent cannot pick up
  an issue, make the change, validate it, and open an MR without a human
  supplying tribal knowledge.

Customer value:

- Self-managed and Dedicated customers do not see a fix until they upgrade,
  sometimes months later. We cannot roll out a targeted fix to a single
  capability without shipping an entire monolith release.
- A fault in one domain can degrade the whole application, and we cannot scale
  a hot domain independently of the rest. Independent modules can be scaled and
  isolated separately, improving reliability and fault tolerance.

Productivity:

- High median-time-to-production for complex changes.
- It can be overwhelming for the wider-community members to contribute.
- Reducing testing times requires diligent and persistent efforts.

## Goals

- Increase development velocity and predictability through separation of concerns.
- Improve code quality by reducing coupling and introducing useful abstractions.
- Make modules agent-ready: clear boundaries, explicit contracts, and all the
  context an agent needs to work autonomously committed in the repo.
- Make dependencies explicit and enforced. A dependency that is not declared
  does not exist; coupling cannot be re-created through the back door.
- Modularize broadly, extract selectively. Most code is modularized in place
  within the monolith; a module is extracted into a separately deployed service
  only when the ROI is clear.
- Build the abstractions that make extraction cheap when it is justified —
  data ownership, independent operability, and independent deployment — so a
  fix can reach customers without a full monolith release.

## Backend decomposition

The backend track modularizes the [GitLab Rails](https://gitlab.com/gitlab-org/gitlab)
application into bounded contexts with explicit, enforced boundaries, building
toward independently operable and — where the ROI is clear — independently
deployable domains.

### How do we get there?

While we do recognize that modularization is a significant technical endeavor,
we believe that the main challenge is organizational, rather than technical.
We not only need to design separation in a way that modules are decoupled in a
pragmatic way but we need to align modularization with the way in which we want to
work at GitLab.

There are many aspects and details required to make modularization of our
monolith successful. We will work on the aspects listed below, refine them, and
add more important details as we move forward towards the goal:

1. [Deliver modularization proof-of-concepts that will deliver key insights](proof_of_concepts.md).
1. Align modularization plans to the product structure by [defining bounded contexts](bounded_contexts.md).
1. [Extract cross-cutting libraries into gems](library_extraction.md), pulling
   platform code out of `lib/`/`ee/lib`. The value is the extraction pattern,
   tooling, and enforced isolation — not CI time saved.
1. [Decompose the transport layer into adapters](transport_layer.md), isolating the
   Web, REST, GraphQL, and Sidekiq transports so each depends only on the domain
   layer. This enables runtime profiles such as API-only or Sidekiq-only nodes.
1. [Isolate the domain layer](domain_layer.md) so each domain owns its data and is reached only through its public API.
1. Start a training program for team members on how to work with decoupled domains (TODO)
1. Build tools that will make it easier to build decoupled domains through inversion of control (TODO)
1. [Introduce hexagonal architecture within the monolith](hexagonal_monolith/index.md)
1. Introduce clean architecture with one-way-dependencies and host application (TODO)
1. Build abstractions that will make it possible to run and deploy domains separately (TODO)

### Decisions

1. [ADR-001: Modularize application domain](decisions/001_modular_application_domain/)? Start with modularizing
   the application domain and infrastructure code.
1. [ADR-002: Define bounded context around feature categories](decisions/002_bounded_contexts_definition/) as a SSoT in the code.
1. [ADR-003: Assign stewards to all modules and libraries](decisions/003_stewardship/).
1. [ADR-004: Extract cross-cutting libraries into gems](decisions/004_library_extraction/).

### Glossary

- `modules` are Ruby modules and can be used to nest code hierarchically.
- `namespaces` are unique hierarchies of Ruby constants. For example, `Ci::` but also `Ci::JobArtifacts::` or `Ci::Pipeline::Chain::`.
- `packages` are Packwerk packages to group together related functionalities. These packages can be big or small depending on the design and architecture. Inside a package all constants (classes and modules) have the same namespace. For example:
  - In a package `ci`, all the classes would be nested under `Ci::` namespace. There can be also nested namespaces like `Ci::PipelineProcessing::`.
  - In a package `ci-pipeline_creation` all classes are nested under `Ci::PipelineCreation`, like `Ci::PipelineCreation::Chain::Command`.
  - In a package `ci` a class named `MergeRequests::UpdateHeadPipelineService` would not be allowed because it would not match the package's namespace.
  - This can be enforced easily with [Packwerk's based RuboCop Cops](https://github.com/rubyatscale/rubocop-packs/blob/main/lib/rubocop/cop/packs/root_namespace_is_pack_name.rb).
- `bounded context` is a top-level Packwerk package that represents a macro aspect of the domain. For example: `Ci::`, `MergeRequests::`, `Packages::`, etc.
  - A bounded context is represented by a single Ruby module/namespace. For example, `Ci::` and not `Ci::JobArtifacts::`.
  - A bounded context can be made of 1 or multiple Packwerk packages. Nested packages would be recommended if the domain is quite complex and we want to enforce privacy among all the implementation details. For example: `Ci::PipelineProcessing::` and `Ci::PipelineCreation::` could be separate packages of the same bounded context and expose their public API while keeping implementation details private.
  - A new bounded context like `RemoteDevelopment::` can be represented a single package while large and complex bounded contexts like `Ci::` would need to be organized into smaller/nested packages.

## Frontend decomposition

The goal is a modular frontend where independently buildable UI modules
integrate through a shared shell application and an explicit module contract,
mirroring the bounded contexts and public interfaces of the backend.

The frontend workstreams are:

1. **Modernize the build pipeline** to enable independent frontend module deployment.
1. **Migrate from Webpack 4 to Webpack 5 / Vite** and complete the Vue 3 migration this unblocks.
1. **Define a module contract** that manages authorization, user context, and feature flags across module boundaries.
1. **Build the supporting infrastructure**: a shell application, a module registry, and a Context provider API.
1. **Create a "Frontend LabKit"** to standardize shared libraries and ensure a consistent user experience across modules.

See [Frontend decomposition](frontend/_index.md) for the detailed design.

## References

[List of references](references.md)
