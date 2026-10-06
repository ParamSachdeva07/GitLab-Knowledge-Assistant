---
title: "Theseus ADR 001: Protobuf as the Preferred Schema Language"
owning-stage: ""
description: "Decision to adopt Protobuf as Theseus's preferred schema language for declarative manifests, configuration schemas, and APIs — while accepting alternatives that meet the same interface properties."
toc_hide: true
---

<!-- Design Documents often contain forward-looking statements -->
<!-- vale gitlab.FutureTense = NO -->

## Status

**Proposed.**

## Context

Theseus is built around the idea that the platform–component boundary
is a *contractual interface*
between Application Development teams and Platform Engineering
([Section 2.3](../#23-what-is-an-interface)).
For an interface to do this job, it must be:

- strongly typed and schema-defined,
- machine-readable
  (so validation, language bindings, JSON Schema, and documentation
  can be generated rather than hand-written),
- semver-versioned with compatibility guarantees,
- co-located with its validation rules and reference documentation.

Multiple schema technologies can be used to satisfy these operational properties:

- **Protobuf** (Google) —
  strongly typed,
  code-generation-first,
  established Go and Ruby toolchains,
  mature versioning conventions,
  inline validation via [protovalidate](https://protovalidate.com).
- **JSON Schema** —
  strongly typed,
  language-agnostic,
  broad ecosystem support,
  suited to runtime-configurable systems where the *shape of the data*
  (rather than generated client code) is what matters most.
  Used today by the [Tenant Model Schema](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/tenant-model-schema/)
  in GitLab Dedicated.
- **OpenAPI / Swagger** —
  appropriate for HTTP APIs but not for non-API contracts.
- **Avro / Thrift** —
  used in data-pipeline contexts;
  less aligned with GitLab's existing Go/Ruby ecosystem.

By deciding on a default technology for defining schema,
we can improve the platform, and tooling, share expertise
and focus on building value for our customers.

## Decision

**Protobuf is Theseus's preferred schema language for schema-defined contracts** —
declarative manifests, configuration schemas, and protocol-level APIs.

The reference path is:

1. Schemas are authored as `.proto` files.
1. Validation rules are expressed inline
   via [protovalidate](https://protovalidate.com) annotations,
   following the [LabKit Configuration design doc](/handbook/engineering/architecture/design-documents/labkit_configuration/)
   (implementation in [labkit!345](https://gitlab.com/gitlab-org/labkit/-/merge_requests/345);
   design discussion at [`gitlab-org/gitlab#591894`](https://gitlab.com/gitlab-org/gitlab/-/work_items/591894)),
   so schema and validation cannot diverge.
1. LabKit's typed configuration surface
   ([Principle 6 in Section 3.2](../#32-platform-as-a-product-commitments))
   is the canonical Theseus-side consumer of these schemas.
1. Where a contract crosses an HTTP boundary,
   OpenAPI is generated from the proto definitions
   rather than authored separately.

**Protobuf syntax version.**
Theseus-aligned schemas target [**Protobuf Edition 2023**](https://protobuf.dev/editions/overview/),
the forward-looking successor to `proto3`.
The wire format is unchanged from `proto3` and remains fully backward compatible,
but Edition 2023 gives us per-feature opt-in.

**Platform-supported tooling.**
[`buf`](https://buf.build/) is the highly encouraged toolchain
for proto linting, breaking-change detection, and module management.
Support is delivered as reusable CI jobs
in [`common-ci-tasks`](https://gitlab.com/gitlab-com/gl-infra/common-ci-tasks) —
see [MR !1444](https://gitlab.com/gitlab-com/gl-infra/common-ci-tasks/-/merge_requests/1444) —
so component teams pick up `buf`-based validation, lint, and breaking-change checks
by including the relevant CI Component,
rather than wiring the toolchain into each project.

**Reference documentation generation.**
`common-ci-tasks` will also ship documentation-generation tooling
(e.g. [`protoc-gen-doc`](https://github.com/pseudomuto/protoc-gen-doc))
that emits reference documentation for `.proto` schemas
in the [Theseus Diátaxis format](../#5211-organization-of-documentation),
so that schema reference material is generated from the schema itself
and lands in the same Modular Component docs surface
as the rest of a component's documentation.

**Other schema technologies are acceptable** —
but only where they demonstrably meet the interface properties
in [Section 2.3](../#23-what-is-an-interface)
(strongly typed, machine-readable, versioned, validation co-located).

The **Tenant Model Schema** in GitLab Dedicated
is the documented exemplar of an acceptable alternative:

- It is a versioned JSON Schema, not Protobuf.
- Switchboard owns and stores tenant model state
  and lets Switchboard users
  (customers and Environment Automation engineers)
  edit or stage patches against it.
- Instrumentor consumes the validated tenant model
  and turns it into infrastructure
  (Terraform, Ansible, Helm, Kubernetes).
- Versioning is operationally meaningful:
  the `$schema` is not freely editable in Switchboard;
  it is selected from the Instrumentor version via a mapping file.
  A newer schema cannot be used against an older Instrumentor branch.

## Consequences

### Positive

1. **Single default reduces ecosystem fragmentation.**
   Component teams default to `.proto`,
   so platform tooling, code generators, and docs
   target one schema family rather than three.
1. **Validation cannot drift from schema.**
   `protovalidate` annotations live on the proto definition itself,
   so a schema change that breaks a validation rule
   is caught at code-generation time, not in production.
1. **Generated bindings.**
   Go and Ruby clients, JSON Schema, OpenAPI, and reference documentation
   are all generated artifacts, not hand-maintained.
1. **Aligns with LabKit's typed configuration contract.**
   LabKit already standardises on `.proto`-schema configuration;
   choosing Protobuf as the platform default
   closes the loop between component configuration and platform contract.

### Negative

1. **Protobuf has a learning curve.**
   Teams unfamiliar with `.proto` files, `buf`, or code-generation toolchains
   need to learn the tooling.
1. **Choice creates a defensible-deviation burden.**
   Any team picking JSON Schema, OpenAPI-first, or another technology
   has to justify the choice against Protobuf.
1. **Tooling investment is locked to one ecosystem.**
   Improvements in code generation, validation, and documentation tooling
   are made on the Protobuf path first;
   alternative paths can lag.

## Alternatives Considered

### Alternative: JSON Schema as the default

#### Approach

Pick JSON Schema as the Theseus-wide default.
The Tenant Model Schema already uses it;
the schema language is widely understood, language-agnostic,
and especially natural for human-edited configuration.

#### Why Not Chosen

1. **Code generation is weaker.**
   Protobuf's code-generation toolchains
   produce typed Go and Ruby bindings out of the box;
   JSON Schema's binding generators are less mature
   and more fragmented across languages.
1. **Validation co-location is weaker.**
   JSON Schema's validation vocabulary is expressive,
   but extension keywords are not standardised across implementations
   the way `protovalidate` is in the Protobuf ecosystem.
1. **LabKit already standardises on Protobuf.**
   Choosing JSON Schema as the default
   would force LabKit to support two first-class schema technologies
   for typed configuration.
1. **JSON Schema is still acceptable where it fits.**
   The decision does not exclude JSON Schema;
   it makes Protobuf the default
   and JSON Schema (and others) the justified exception.
   The Tenant Model Schema is unaffected.

### Alternative: No platform-wide default — each contract picks its own technology

#### Approach

Treat schema language as a local decision.
Component teams pick the technology that fits their use case;
the platform does not endorse one.

#### Why Not Chosen

1. **Fragmentation.**
   Without a default, the ecosystem accumulates
   `.proto`, `.json`, OpenAPI, and ad-hoc YAML schemas,
   multiplying the tooling each platform tool must support.
1. **Generated artifacts become harder to standardise.**
   Tools that consume schemas —
   validation, docs, generated clients —
   need a normalised input to produce consistent output across components.
1. **Defaults are how platforms move fast.**
   [Section 2.3](../#23-what-is-an-interface)
   and the "defaults over decisions" principle
   ([Section 2.3 principle list](../#23-what-is-an-interface))
   explicitly favour platform-wide defaults.
   A no-default stance would contradict that.

### Alternative: OpenAPI-first

#### Approach

Author contracts as OpenAPI specifications,
generating Protobuf, JSON Schema, and other artifacts from them.

#### Why Not Chosen

1. **OpenAPI is HTTP-API-shaped.**
   It works well for REST-style APIs,
   but is awkward for declarative manifests like `FairwayManifest`
   or configuration schemas like the Tenant Model
   that are not HTTP-bound.
1. **OpenAPI is still a generated artifact in the Protobuf path.**
   Where a contract crosses an HTTP boundary,
   OpenAPI is produced *from* the proto definitions.
   Making it the source would invert the dependency.

## References

- [Section 2.3 — What is an interface?](../#23-what-is-an-interface) —
  the source for the interface-property criteria this ADR depends on.
- [Section 2.3.2 — Preferred technology: Protobuf](../#232-preferred-technology-protobuf) —
  the position statement this ADR formalises.
- [Section 3.2 — Platform-as-a-product commitments](../#32-platform-as-a-product-commitments) —
  Principle 6 (typed configuration via LabKit).
- [Section 5.2.1.1 — Organization of Documentation](../#5211-organization-of-documentation) —
  the Theseus Diátaxis convention that generated schema reference docs land in.
- [LabKit Configuration design doc](/handbook/engineering/architecture/design-documents/labkit_configuration/) —
  the canonical implementation of typed configuration in Theseus.
- [`gitlab-org/gitlab#591894`](https://gitlab.com/gitlab-org/gitlab/-/work_items/591894) —
  design discussion for the standardised LabKit configuration management module.
- [labkit!345](https://gitlab.com/gitlab-org/labkit/-/merge_requests/345) —
  the in-flight implementation of LabKit's `v2/config` module.
- [protovalidate](https://protovalidate.com) —
  the inline-validation library this ADR depends on.
- [`buf`](https://buf.build/) —
  the encouraged Protobuf toolchain.
- [`common-ci-tasks` MR !1444](https://gitlab.com/gitlab-com/gl-infra/common-ci-tasks/-/merge_requests/1444) —
  `buf` support landing in `common-ci-tasks`.
- [`protoc-gen-doc`](https://github.com/pseudomuto/protoc-gen-doc) —
  the candidate reference-docs renderer for `.proto` schemas.
- [John Ousterhout, *A Philosophy of Software Design*](https://web.stanford.edu/~ouster/cgi-bin/aposd.php) —
  the interface-design principles Theseus aligns with.
