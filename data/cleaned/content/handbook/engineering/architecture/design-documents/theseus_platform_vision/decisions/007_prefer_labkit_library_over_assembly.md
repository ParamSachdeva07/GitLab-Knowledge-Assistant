---
title: "Theseus ADR 007: Prefer LabKit library code over assembly-framework implementations"
owning-stage: ""
description: "Decision that cross-cutting service capabilities are delivered as LabKit library code in preference to the Lab Bench assembly framework, because library code reaches the whole portfolio."
toc_hide: true
---

<!-- Design Documents often contain forward-looking statements -->
<!-- vale gitlab.FutureTense = NO -->

## Status

**Proposed.**

## Context

The [Lab Bench: GitLab SOA Architecture](https://docs.google.com/document/d/11Zj918LuZeY3fPcU50ZPhzJtcqzvyXaO0SDamW7cDc8/)
proposal describes a wide set of capabilities a service needs:
structured logging, metrics, tracing, configuration, feature flags,
cryptography and mTLS, secrets, request-context propagation, datastore access,
caching, and health checks.

Many (although not all) of these concerns should be fulfilled through a library.
Several already exist in
[LabKit](/handbook/engineering/infrastructure-platforms/developer-experience/labkit/),
some for years; others are recent; some are not yet built.
This ADR focuses on where such a capability should live
when both options are open: as LabKit library code, or inside the Lab Bench assembly framework.

The Lab Bench proposal itself takes the same position —
its stated goal is to "provide a SOA library (as part of LabKit)" —
so this ADR is alignment, not contradiction.

## Decision

**Cross-cutting service capabilities are delivered as LabKit library code
in preference to being implemented inside the Lab Bench assembly framework.**

Capabilities should be compiled into the assembly framework only when they are
genuinely specific to assembly, and the team proposing it can clearly justify
why LabKit is the wrong place.

## Consequences

### Positive

1. **Global reach.**
   Functionality in LabKit is consumable by every component,
   including those that predate Lab Bench or never adopt it — Workhorse, GitLab Pages, Gitaly.
   For example, LabKit's protobuf typed configuration can be retrofitted onto Gitaly,
   but this would not be possible if the same functionality lived inside Lab Bench.
1. **Consistent with the platform's library commitment.**
   It reinforces [ADR 005](005_labkit_go_native_go_library.md):
   LabKit is the platform's standard-library surface, and capabilities accrue to it.

### Negative

1. **LabKit must keep pace.**
   Putting capabilities in LabKit makes the Developer Experience team's roadmap a dependency
   for teams that need them; the library has to be resourced to absorb that demand.
1. **Cross-language parity is a coordination cost.**
   A capability wanted in both Go and Ruby components must be implemented in each LabKit binding,
   rather than once inside a single-language assembly framework
   (see [ADR 005](005_labkit_go_native_go_library.md)).
1. **Some capabilities legitimately belong in the assembly.**
   For example, logic that only makes sense when several services share one process
   does belong in Lab Bench.

## Alternatives Considered

### Alternative: Implement capabilities in the Lab Bench assembly framework

#### Approach

Build logging, metrics, configuration, secrets, and the rest
directly into the assembly framework, where Lab Bench services consume them.

#### Why Not Chosen

The capability would then be available only to Lab Bench assemblies.
Existing and non-adopting components (Workhorse, GitLab Pages, Gitaly) could not use it,
and GitLab would maintain two homes for the same concern —
one in LabKit for the broad portfolio, one in Lab Bench for assemblies.

## References

- [Section 2.8 — Lab Bench and the wider Theseus initiative](../#28-lab-bench-and-the-wider-theseus-initiative) —
  the library-preference principle in narrative form.
- [Theseus ADR 005 — LabKit Go remains a native Go library](005_labkit_go_native_go_library.md) —
  LabKit as the platform's standard-library surface.
- [Theseus ADR 006 — Lab Bench assemblies are first-class platform components](006_lab_bench_assemblies_are_first_class.md) —
  the opacity decision this one complements on the question of capability placement.
- [Section 2.3 — What is an interface?](../#23-what-is-an-interface) —
  the "pull complexity downwards" discipline behind the preference.
