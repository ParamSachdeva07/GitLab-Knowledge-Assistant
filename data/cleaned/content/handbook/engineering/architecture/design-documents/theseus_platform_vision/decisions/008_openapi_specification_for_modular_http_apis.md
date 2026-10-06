---
title: "Theseus ADR 008: Modular HTTP APIs ship an OpenAPI specification that meets a platform quality bar"
owning-stage: ""
description: "Decision that every modular feature exposing a GitLab-designed HTTP JSON API ships an OpenAPI 3.1 document meeting an API Platform quality bar, with the production method left to the team and Lab Bench scaffolding and enforcing the bar."
toc_hide: true
---

<!-- Design Documents often contain forward-looking statements -->
<!-- vale gitlab.FutureTense = NO -->

## Status

**Draft.**

## Context

### Goals

This ADR gives modular features one shared way to describe their HTTP APIs:

1. **Guardrails.** Every modular HTTP API has a specification that is linted, complete against its declared routes and checked for breaking changes before it reaches consumers.
1. **Consistency.** API consumers and platform tooling get the same kind of contract from every modular feature, whatever its runtime, instead of a different approach per team.
1. **Less toil.** Lab Bench scaffolds the specification and CI enforces the bar, so a team building a new modular feature starts from a working specification rather than designing its own API process.

### Background

Theseus modular features are HTTP services in several runtimes. Lab Bench supports Rust and Go today and names Ruby and Python in its handler schema for later (decision [LB-D5](https://gitlab.com/gitlab-org/lab-bench/bench/-/blob/main/docs/decisions/LB-D5-assembly-runtime.md)). Ruby features inside the monolith are a separate case.

Two models for producing a specification already exist at GitLab, with no house model to choose between them. [Artifact Registry](https://gitlab.com/gitlab-org/ops/artifact-registry/-/tree/main/api/openapi), the first modular feature to ship, hand-authors OpenAPI 3.1 in `api/openapi/`, lints it with Redocly in CI and verifies handlers against it with `kin-openapi` in tests, per its [API style guide](https://gitlab.com/gitlab-org/ops/artifact-registry/-/blob/main/docs/dev/api-style.md). The monolith generates its [specification](https://gitlab.com/gitlab-org/gitlab/-/blob/master/doc/api/openapi/openapi_v3.yaml) from Grape endpoint definitions with the [`gitlab-grape-openapi`](https://gitlab.com/gitlab-org/ruby/gems/gitlab-grape-openapi) gem.

A generated specification is only as complete as the generator's view of the code. Anything the generator cannot introspect is absent from the document, and nothing reports the gap.

[ADR 001](001_protobuf_as_preferred_schema_language.md) says that where a contract crosses an HTTP boundary, OpenAPI is generated from the proto definitions. That path needs a proto definition of the HTTP contract. Lab Bench's `HTTPEndpoint` message in [`config/gitlab/bench/v1/inbound.proto`](https://gitlab.com/gitlab-org/lab-bench/bench/-/blob/main/config/gitlab/bench/v1/inbound.proto) carries only `methods`, `route` and `handler`, no request or response types, while `GRPCEndpoint` beside it is schema-complete. So for every Lab Bench HTTP endpoint today, there is no proto to derive from.

The choice matters beyond style. It decides whether contract testing is load-bearing or tautological, what a breaking-change check has to compare, and whether tooling investment compounds across runtimes or forks per language. Three downstream epics wait on it: [epic 429](https://gitlab.com/groups/gitlab-org/quality/-/work_items/429) (ship a spec with every modular feature), [epic 432](https://gitlab.com/groups/gitlab-org/quality/-/work_items/432) (block breaking API changes in CI), and [epic 434](https://gitlab.com/groups/gitlab-org/quality/-/work_items/434) (contract testing framework). The parent epic is [epic 465](https://gitlab.com/groups/gitlab-org/quality/-/work_items/465).

The API Platform team enumerated seven models along the axis of what stops code and specification drifting: code-first generated; spec-first verified by tests; spec-first enforced by generated server code; spec-first enforced by the Lab Bench chassis; proto-first through `HTTPEndpoint` schemas; proto-first through gRPC transcoding; and an outcome standard that mandates the artifact and a quality bar, but not the method. The full table is in [`gitlab-org/gitlab#624041`](https://gitlab.com/gitlab-org/gitlab/-/work_items/624041#note_3896261398).

## Decision

**Every modular feature that exposes a GitLab-designed HTTP JSON API ships an OpenAPI 3.1 specification that meets the API Platform quality bar; how the specification is produced is not mandated, beyond the route authority set out in point 5.**

1. **Scope.** Applies to GitLab-designed HTTP JSON APIs, external and internal. Internal endpoints are tagged and excluded from public documentation, rather than exempted from the specification. Protocol-defined surfaces (npm, Maven and OCI registry protocols, MCP JSON-RPC) are out of scope; they follow their own protocol specifications. Because Lab Bench still has to route protocol-defined surfaces, `HTTPEndpoint` gains a way to mark a route as protocol-defined (for example, a scope field), and the completeness check in point 3 skips marked routes.
1. **Location and version.** One OpenAPI 3.1 document per assembly, in `api/openapi/` in the component repository, matching Artifact Registry. The assembly is the deployable unit with its own listeners ([LB-D20](https://gitlab.com/gitlab-org/lab-bench/bench/-/blob/main/docs/decisions/LB-D20-scaffold-layout.md), [LB-D21](https://gitlab.com/gitlab-org/lab-bench/bench/-/blob/main/docs/decisions/LB-D21-template-split.md)), so one document per component would merge independently deployed surfaces into one file.
1. **Quality bar, owned by the API Platform team:** a standard GitLab lint ruleset; completeness with respect to the declared inbound HTTP routes, excluding protocol-defined routes; breaking-change detection between versions; registration in the [public API reference](https://gitlab.com/groups/gitlab-org/quality/-/work_items/428), unless the component opts out. The ruleset is the bar, and the tool that runs it is an implementation detail. Today that tool is Redocly, which Artifact Registry already uses.
1. **Method is the team's choice:** code-first generation (the monolith's Grape path, or a runtime-specific generator), spec-first hand authoring (Artifact Registry's path), or proto-derived, where a proto definition of the HTTP contract exists. Each must produce a document that passes the bar. For Lab Bench services, the method governs everything except the route set, which comes from `bench.yaml` (point 5).
1. **Lab Bench scaffolds and enforces the bar** (this is the part that needs Lab Bench agreement).
   - **Authority.** Where `bench.yaml` is present, it is authoritative for the route set, and the specification is authoritative for everything else: request and response schemas, descriptions and examples. Where `bench.yaml` is absent, the specification is authoritative for everything.
   - **Scaffold and build.** `bench build` follows the rule it already applies to handler skeletons ([Lab Bench MR 140](https://gitlab.com/gitlab-org/lab-bench/bench/-/merge_requests/140)): it creates a missing file but never writes inside an authored one. If the specification is absent, `bench build` seeds it from the declared routes (path, method, path parameters, basic grouping, placeholder request and response schemas). If it is present, `bench build` compares the two route sets, fails on any disagreement and prints the stanza to add.
   - **Lint.** The ruleset lint runs in merge request pipelines and release pipelines through a CI component that the API Platform team owns, and a release fails without a passing specification. It does not run inside the `bench` binary (see the Redocly consequence below).
   - **Existing services.** For a service that already has a specification but no `bench.yaml`, such as Artifact Registry, a one-time import may seed `bench.yaml` route stanzas from the specification with `handler: TODO`, for a human to review once. Ongoing two-way synchronisation is not supported: it would leave neither file authoritative, and the transformation loses information in both directions.
1. **Relationship to ADR 001.** This ADR does not reopen ADR 001. ADR 001's proto-derived OpenAPI remains preferred where an HTTP contract is defined in proto, such as a gRPC service with HTTP annotations. This ADR fills the gap that ADR 001's fourth step leaves when there is no proto to derive from, which is every Lab Bench HTTP endpoint today. If Lab Bench later gives `HTTPEndpoint` request and response schemas, proto-derived becomes one more acceptable method under the same bar.
1. **Positions of existing specifications.** Artifact Registry conforms once the standard ruleset replaces its local Redocly configuration and its protocol routes are marked as protocol-defined. The monolith's generated specification is outside this decision, but the same ruleset should apply to it over time.

## Consequences

### Positive

1. **Language and framework neutral.** No method is mandated, so no runtime waits on a GitLab-owned generator, and Rust, Go and later runtimes are on equal footing from day one.
1. **Every component has a specification from the first scaffold,** and a non-protocol route declared in `bench.yaml` cannot go missing from it without failing the build.
1. **Tooling investment compounds.** The ruleset, the diff tool and the reference renderer serve every method.
1. **Downstream epics gain a definite scope.** Breaking-change detection is a specification diff; contract testing is the verification floor for payload fidelity.
1. **Preserves team autonomy over workflow** while enforcing one contract for API consumers.

### Negative

1. **Payload fidelity is not guaranteed.** Request and response schemas are hand-authored under most methods, and nothing in this decision checks them against the handler. Contract testing ([epic 434](https://gitlab.com/groups/gitlab-org/quality/-/work_items/434)) becomes load-bearing rather than optional. The payload contract already exists in code: the generated Lab Bench entrypoint binds each route to its handler package's `Request` and `Response` types, and the chassis deserialises into them. Deriving specification schemas from those types is a possible later step.
1. **`bench.yaml` completeness becomes load-bearing.** A representative subset of routes, as in the current Artifact Registry example in the Lab Bench repository, would yield an incomplete specification.
1. **Route comparison needs translation.** Route syntax differs (`:id` in `bench.yaml`, `{id}` in OpenAPI), and `HTTPMethod` does not yet cover `HEAD` or `OPTIONS`, so those routes cannot be seeded or compared until the enum is extended ([tracked gaps](https://gitlab.com/gitlab-org/lab-bench/bench/-/tree/main/examples/artifact-registry?ref_type=heads#gaps-found)).
1. **Redocly is a Node tool,** and the `bench` CLI is Rust with no Node dependency, so the lint runs through a CI component rather than inside the CLI binary. `bench build` checks route agreement locally, but not the ruleset.
1. **`HTTPEndpoint` needs a protocol-defined marker** before the completeness check can run on services with protocol-defined surfaces, such as Artifact Registry.
1. **The cost lands on the Lab Bench team** while the benefit lands on API consumers and the API Platform team.
1. **The public reference carries two specification versions for a period:** 3.0 from the monolith and 3.1 from modular components. The renderer ([epic 433](https://gitlab.com/groups/gitlab-org/quality/-/work_items/433)) must accept both.

## Alternatives Considered

### Alternative: Mandate code-first generation

#### Approach

Every runtime adopts or builds a generator that emits OpenAPI from handler code, as the monolith does with `gitlab-grape-openapi`.

#### Why Not Chosen

1. GitLab owns exactly one generator, and it serves only Ruby applications that use Grape. Lab Bench fixes one HTTP framework per runtime (`axum` for Rust, LabKit httpserver for Go), and third-party generators exist for some of them, but each would need adapting to GitLab's conventions and the ruleset, and GitLab would own one integration per runtime. We could consider providing generators in the future, as we do today for Grape, but mandating them now would block every runtime on that work.
1. A generated specification is only as complete as the generator's view of the code, and omissions are not reported.
1. Contract testing becomes tautological, since a specification cannot disagree with the code it was derived from.

### Alternative: Mandate spec-first authoring with contract tests or generated server code

#### Approach

The hand-authored document is the source of truth. Drift is caught by per-language contract tests (Artifact Registry today) or prevented by generating server interfaces from the document (`oapi-codegen` in Go).

#### Why Not Chosen

1. Verification is per language, mature in Go, weaker in Rust, absent for Ruby.
1. It forbids the monolith's working generated path, forcing migrations with no consumer benefit.
1. The same quality bar can be met by this method voluntarily, so mandating it adds constraint without adding assurance.

### Alternative: Spec-first enforced by the Lab Bench chassis

#### Approach

Lab Bench reads the OpenAPI document to derive the route table, the "OpenAPI escape hatch" the Lab Bench maintainers floated in [Lab Bench issue 46](https://gitlab.com/gitlab-org/lab-bench/bench/-/issues/46#note_3695983088), and the inbound layer validates requests against the document at runtime, making the specification load-bearing with no service-side code generation.

#### Why Not Chosen

1. It is the strongest drift guarantee, but it inverts the relationship between `bench.yaml` and the specification, requires runtime validation in each chassis runtime, and asks more of Lab Bench than the decision above, while the inbound layer is still being built.
1. It remains the natural next step if payload drift proves costly, and nothing in this decision precludes it.

### Alternative: Proto-derived, through `HTTPEndpoint` schemas or gRPC transcoding

#### Approach

Either `HTTPEndpoint` grows request and response types and a buf plugin emits OpenAPI (tracked in [`gitlab-org/gitlab#624042`](https://gitlab.com/gitlab-org/gitlab/-/work_items/624042)), or HTTP JSON APIs are declared as gRPC services with `google.api.http` annotations, and the chassis transcodes.

#### Why Not Chosen

1. Language-neutral by construction and fully aligned with ADR 001, but unavailable today. `HTTPEndpoint` carries no schemas, `config/buf.yaml` is lint-only with no code generation configured, and the Lab Bench maintainers' stated direction runs the other way.
1. The declaration is only load-bearing if the inbound layer deserialises into it; otherwise it drifts like any hand-authored document.
1. Transcoding constrains REST idioms, fixes the error shape to `google.rpc.Status`, and cannot describe protocol-defined surfaces.
1. Kept open as an acceptable method under the bar, should the proto path materialise.

## References

- [ADR 001](001_protobuf_as_preferred_schema_language.md) — the proto-derived OpenAPI step this ADR refines for the no-proto case.
- [Section 2.3 — What is an interface?](../#23-what-is-an-interface) — the interface this decision governs the HTTP shape of.
- [Section 2.3.2 — Preferred technology: Protobuf](../#232-preferred-technology-protobuf) — the proto-first position this ADR sits alongside.
- [Epic 465](https://gitlab.com/groups/gitlab-org/quality/-/work_items/465) — the parent epic.
- [`gitlab-org/gitlab#624041`](https://gitlab.com/gitlab-org/gitlab/-/work_items/624041) — the option table and the decision discussion.
- [`gitlab-org/gitlab#624042`](https://gitlab.com/gitlab-org/gitlab/-/work_items/624042) — the `HTTPEndpoint` schema question.
- [`gitlab-org/gitlab#624045`](https://gitlab.com/gitlab-org/gitlab/-/work_items/624045) — conformance positions for existing specifications.
- [`gitlab-org/gitlab#624046`](https://gitlab.com/gitlab-org/gitlab/-/work_items/624046) — re-scoping the breaking-change and contract-testing epics.
- [Epic 429](https://gitlab.com/groups/gitlab-org/quality/-/work_items/429) — ship a specification with every modular feature.
- [Epic 432](https://gitlab.com/groups/gitlab-org/quality/-/work_items/432) — block breaking API changes in CI.
- [Epic 433](https://gitlab.com/groups/gitlab-org/quality/-/work_items/433) — the public API reference renderer.
- [Epic 434](https://gitlab.com/groups/gitlab-org/quality/-/work_items/434) — contract testing framework.
- [Epic 428](https://gitlab.com/groups/gitlab-org/quality/-/work_items/428) — registration in the public API reference.
- [Lab Bench `inbound.proto`](https://gitlab.com/gitlab-org/lab-bench/bench/-/blob/main/config/gitlab/bench/v1/inbound.proto) — the `HTTPEndpoint` and `GRPCEndpoint` messages this ADR compares.
- [Lab Bench issue 46](https://gitlab.com/gitlab-org/lab-bench/bench/-/issues/46) — route enumeration burden and the OpenAPI escape hatch.
- [Lab Bench MR 140](https://gitlab.com/gitlab-org/lab-bench/bench/-/merge_requests/140) — `bench build` scaffolds missing files and never writes inside authored ones.
- [Lab Bench decision LB-D5](https://gitlab.com/gitlab-org/lab-bench/bench/-/blob/main/docs/decisions/LB-D5-assembly-runtime.md) — supported runtimes.
- [Lab Bench decisions LB-D20](https://gitlab.com/gitlab-org/lab-bench/bench/-/blob/main/docs/decisions/LB-D20-scaffold-layout.md) and [LB-D21](https://gitlab.com/gitlab-org/lab-bench/bench/-/blob/main/docs/decisions/LB-D21-template-split.md) — assemblies as the deployable unit.
- [Artifact Registry API style guide](https://gitlab.com/gitlab-org/ops/artifact-registry/-/blob/main/docs/dev/api-style.md) — the spec-first path this ADR draws on.
- [Artifact Registry `api/openapi/`](https://gitlab.com/gitlab-org/ops/artifact-registry/-/tree/main/api/openapi) — the hand-authored specification directory.
- [Monolith OpenAPI document](https://gitlab.com/gitlab-org/gitlab/-/blob/master/doc/api/openapi/openapi_v3.yaml) — the monolith's generated specification.
- [`gitlab-grape-openapi` gem](https://gitlab.com/gitlab-org/ruby/gems/gitlab-grape-openapi) — the generator that produces it.
- [LabKit Configuration design doc](/handbook/engineering/architecture/design-documents/labkit_configuration/) — the protobuf-first configuration precedent.
