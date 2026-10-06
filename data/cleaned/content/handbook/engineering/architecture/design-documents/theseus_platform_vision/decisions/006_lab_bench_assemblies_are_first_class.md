---
title: "Theseus ADR 006: Lab Bench assemblies are first-class platform components"
owning-stage: ""
description: "Decision that Theseus provisioning treats a Lab Bench assembly identically to any other OCI container, which makes components built on Lab Bench first-class platform participants."
toc_hide: true
---

<!-- Design Documents often contain forward-looking statements -->
<!-- vale gitlab.FutureTense = NO -->

## Status

**Proposed.**

## Context

The [Lab Bench: GitLab SOA Architecture](https://docs.google.com/document/d/11Zj918LuZeY3fPcU50ZPhzJtcqzvyXaO0SDamW7cDc8/)
proposal is part of the wider Theseus initiative.
It is a service-chassis and assembly framework that bakes multiple
[LabKit](/handbook/engineering/infrastructure-platforms/developer-experience/labkit/)-based services
into a single binary and runs them together as one container.

This vision document does not depend on Lab Bench:
the immediate focus is onboarding Artifact Registry on the components Platform Engineering delivers.

However, as per the Lab Bench proposal's own decision, the entrypoint is a single process per assembly.
This is compatible with the OCI entrypoint that Theseus Platform deployments expect.
An assembly is just an ordinary container: the standard OCI image and entrypoint contract
that any Kubernetes component satisfies, and the platform treats it as such.

The ownership of the Lab Bench assembly is proposed to sit with the
Sec Infrastructure team.

## Decision

**Theseus provisioning treats a Lab Bench assembly identically to any other application,
and components built on Lab Bench are first-class Theseus Platform components.**

From the perspective of Fairway and the Platform Bindings,
an assembly is just a container that starts like any other:
the platform schedules it, satisfies its declared infrastructure needs,
and observes it exactly as it would any other component.
Theseus does not model what runs inside the container.

## Consequences

### Positive

1. **Lab Bench evolves independently.**
   Its internal architecture is behind the container boundary,
   so it can change without platform coordination,
   and the platform needs no knowledge of it.
1. **No special-casing in provisioning.**
   Fairway and the Platform Bindings need no "Lab Bench mode";
   an assembly is provisioned with the same path as any other OCI component.
1. **Teams can adopt Lab Bench without leaving the platform.**
   Adoption is a team choice that does not forfeit first-class status,
   which removes the incentive to treat Lab Bench and Theseus as rivals.

### Negative

1. **Overlapping responsibilities sit inside the container.**
   Lab Bench's own inbound and outbound layers (ingress, mTLS, load-shedding,
   connection management) can overlap platform-provided capabilities
   (service-mesh mTLS, ingress, observability).
   Reconciling them is the adopting team's responsibility and an open design tension.
1. **The platform cannot observe intra-assembly structure.**
   Per-service signals inside an assembly are not visible to platform provisioning;
   they depend on the assembly emitting them through the standard (LabKit) interfaces.
1. **Library-vs-assembly placement still needs governance.**
   Opacity makes assemblies first-class but does not decide *where* a capability belongs;
   that is the subject of [ADR 007](007_prefer_labkit_library_over_assembly.md).

## Alternatives Considered

### Alternative: Have Theseus model the assembly's internals

#### Approach

Give provisioning awareness of the services packed inside an assembly
so it can route, scale, or observe them individually.

#### Why Not Chosen

It breaks the Container interface's information hiding,
couples the platform to Lab Bench's internal design,
and would force every other component into a similar level of internal disclosure.
The point of the contract is that the platform does not reach inside the container.

## References

- [Section 2.8 — Lab Bench and the wider Theseus initiative](../#28-lab-bench-and-the-wider-theseus-initiative) —
  the narrative positioning this ADR records.
- [Theseus ADR 007 — Prefer LabKit library code over assembly-framework implementations](007_prefer_labkit_library_over_assembly.md) —
  where shared capabilities should live.
- [Section 2.5 — Theseus vs the Component Ownership Model](../#25-theseus-vs-the-component-ownership-model) —
  the user-space / kernel-land framing in which Lab Bench is user-space.
