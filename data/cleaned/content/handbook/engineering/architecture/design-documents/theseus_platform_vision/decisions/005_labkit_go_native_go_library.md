---
title: "Theseus ADR 005: LabKit Go remains a native Go library"
owning-stage: ""
description: "Decision that LabKit Go stays a pure native Go library rather than wrapping a non-Go core via FFI, dynamic linking, subprocess+IPC, or WASM."
toc_hide: true
---

<!-- Design Documents often contain forward-looking statements -->
<!-- vale gitlab.FutureTense = NO -->

## Status

**Proposed.**

## Context

LabKit Go has been implemented as a native Go library for roughly six years.
It is in production across the majority of GitLab's Go components,
its API surface is mature,
and the cost of changing the implementation language is not free.

The Developer Experience team owns LabKit across languages
(see the [LabKit North Star strategy](/handbook/engineering/architecture/design-documents/labkit_north_star_strategy/)),
and the team's expertise is concentrated in Go.
Maintenance, support, and architectural evolution of LabKit Go
land on engineers whose strongest tool is Go.

Theseus's reliance on LabKit raises the stakes of any change to how LabKit is built and shipped.

The downside for every non-native alternative
would impact the productivity of every GitLab engineer.

Periodic conversations float the idea of sharing implementation
with a non-Go core (typically Rust)
on the basis that a single core would deduplicate work across language bindings.
This ADR records why that path is not chosen for LabKit Go.

## Decision

**LabKit Go is implemented as a native Go library.**
The reference implementation is pure Go (`go.mod`, idiomatic Go packages),
with `cgo` reserved for unavoidable system bindings only.

A non-Go LabKit runtime consumed via FFI, dynamic linking, subprocess+IPC, or WASM
is explicitly **out of scope** for LabKit Go.

This decision is scoped to LabKit Go.
It does not constrain LabKit Ruby
or any future LabKit implementation for another language.
For these languages, there may well be a better case for
a single shared runtime component.

## Consequences

### Positive

1. **Maintained on the team's existing skill set.**
   LabKit Go evolves on the language the Developer Experience team already operates in,
   without a parallel investment in a second core ecosystem.
1. **No toolchain regressions for consumers.**
   `go build`, `go test`, `go mod`, `CGO_ENABLED=0`,
   and `go install` semantics keep working unmodified for every component that depends on LabKit.
1. **Single-file binaries remain possible.**
   Components depending on LabKit can still produce static, scratch-image-compatible Go binaries
   without shipping shared objects, plugin processes, or WASM runtimes alongside them.
1. **Predictable runtime behaviour.**
   No FFI stack-switch surprises, no subprocess lifecycle to manage,
   no per-invocation WASM cold-start cost.

### Negative

1. **LabKit-Go and LabKit-Ruby implementations evolve in parallel.**
   Behavioural parity across languages is a coordination problem,
   not something the compiler can enforce.
1. **Capabilities that genuinely require a non-Go implementation
   must be justified case-by-case.**
   For example, a FIPS-validated cryptographic primitive
   that is only available in a non-Go form
   would need its own narrow exception with explicit ownership,
   rather than dragging LabKit's whole core across the boundary.
1. **Cross-language deduplication is not a compile-time gain.**
   Sharing a single core across Go and Ruby via FFI is permanently off the table for LabKit Go;
   shared specifications, test suites, and conformance harnesses are the substitute.

## This is a two-way door decision

If we decide that this is important, we can, at a later stage, move to a single
binary.

## Alternatives Considered

Each possible alternative brings with it several downsides.

```mermaid
flowchart LR
  uniffi["uniffi-rs"]:::tool
  cbindgen["cbindgen + cgo"]:::tool
  staticlib["staticlib (.a)"]:::tool
  cdylib["cdylib (.so/.dylib)"]:::tool
  purego["purego + cdylib"]:::tool
  r2g_cgo["rust2go (cgo mode)"]:::tool
  r2g_ipc["rust2go (IPC mode)"]:::tool
  wazero["wasm32-wasi + wazero"]:::tool
  wasmtime["wasmtime-go"]:::tool
  goplugin["go-plugin (HashiCorp)"]:::tool
  grpc["gRPC / stdio subprocess"]:::tool

  static_mech(["Static library\ncgo links .a"]):::mech
  dynamic_mech(["Dynamic library\ncgo + .so/.dylib"]):::mech
  runtime_mech(["Runtime FFI\ndlopen, no cgo"]):::mech
  wasm_mech(["WASM module\nembedded, pure Go host"]):::mech
  subprocess_mech(["Subprocess + IPC\nseparate binary"]):::mech

  dev_complex["Developer complexity\nUsers need a C toolchain\n(gcc/clang/MinGW) installed.\nCGO_ENABLED=0 builds break.\nPer-platform .a artifacts\nmust be prebuilt and shipped."]:::term
  compile_speed["Compile speed\ncgo invokes system linker (no fast Go internal linker).\n+1–3s per cgo package, cold.\nSlows go test, gopls, lint across the whole module."]:::term
  per_call["Per-call overhead\nFFI/IPC boundary cost per invocation.\nWASM: 100s of ns. Subprocess + serde: microseconds.\nKills chatty APIs; forces batching."]:::term
  loss_binary["Loss of single binary\nShip .so/.dylib/.dll or a\nsecond executable alongside the Go binary.\nLD_LIBRARY_PATH or PATH must be set.\nBreaks scratch/distroless deploys."]:::term
  startup["Startup time\nWASM compile/instantiate cost\nper process. wazero AOT helps\nbut adds tens to hundreds of ms\non cold start. Bad for CLIs\nand short-lived processes."]:::term
  experimental["Experimental\npurego skips cgo's goroutine\nstack switch. Rust runs on a small movable stack — large\nstack use, callbacks, threads, or async will corrupt state."]:::term
  ops_complex["Operational complexity\nTwo binaries to version,\nrelease, and monitor. Crash\nhandling, restarts, IPC\nschema evolution, and orphan\nprocess cleanup all on you."]:::term

  uniffi --> static_mech
  cbindgen --> static_mech
  staticlib --> static_mech
  r2g_cgo --> static_mech

  cdylib --> dynamic_mech
  purego --> runtime_mech

  wazero --> wasm_mech
  wasmtime --> wasm_mech

  r2g_ipc --> subprocess_mech
  goplugin --> subprocess_mech
  grpc --> subprocess_mech

  static_mech --> dev_complex
  static_mech --> compile_speed

  dynamic_mech --> dev_complex
  dynamic_mech --> loss_binary

  runtime_mech --> experimental
  runtime_mech --> loss_binary

  wasm_mech --> per_call
  wasm_mech --> startup

  subprocess_mech --> ops_complex
  subprocess_mech --> loss_binary
  subprocess_mech --> per_call

  classDef tool fill:#EEEDFE,stroke:#534AB7,color:#26215C,stroke-width:0.5px;
  classDef mech fill:#E1F5EE,stroke:#0F6E56,color:#04342C,stroke-width:0.5px;
  classDef term fill:#A32D2D,stroke:#791F1F,color:#ffffff,stroke-width:0.5px;
```

## References

- [Section 3.2 — Platform-as-a-product commitments](../#32-platform-as-a-product-commitments) —
  Principle 6, which treats LabKit as the platform's standard-library commitment.
- [Theseus ADR 001 — Protobuf as the Preferred Schema Language](001_protobuf_as_preferred_schema_language.md) —
  the typed-configuration surface that depends on LabKit Go.
- [LabKit North Star strategy](/handbook/engineering/architecture/design-documents/labkit_north_star_strategy/) —
  governance model and per-language ownership.
- [LabKit repository](https://gitlab.com/gitlab-org/labkit) —
  the canonical implementation.
- [`purego`](https://github.com/ebitengine/purego),
  [`wazero`](https://wazero.io/),
  [`go-plugin`](https://github.com/hashicorp/go-plugin),
  [`uniffi-rs`](https://github.com/mozilla/uniffi-rs) —
  the binding technologies surveyed above.
