---
title: "Theseus ADR 003: Enterprise Platform Binding services must survive Cell outages"
owning-stage: ""
description: "Decision that services running on the Enterprise Platform Binding cannot synchronously depend on the GitLab Application or any Modular Component running in Cells, so that a Cell-level outage does not propagate to Enterprise-deployed services."
toc_hide: true
---

<!-- Design Documents often contain forward-looking statements -->
<!-- vale gitlab.FutureTense = NO -->

## Status

**Proposed.**

## Context

The [Enterprise Platform Binding](../#43-the-enterprise-platform-binding) hosts GitLab-Inc-operated services
that are not tied to a single Cell or Dedicated instance —
`customers.gitlab.com`,
license generation,
billing aggregation,
and other services that span the whole fleet.

These services operate *above* the tenant:
many Cells depend on them at once.

Cell failures happen, and recent history shows the upper bound is not minutes:

- In March 2026,
  drone strikes damaged three AWS data centres in the Gulf
  ([reporting](https://theconversation.com/why-iran-targeted-amazon-data-centers-and-what-that-does-and-doesnt-change-about-warfare-278642));
  AWS advised migration out of `me-central-1` and waived a month of charges.
- A follow-on strike four weeks later kept the region degraded.

The same shape of outage is reachable through power events,
network partitions,
regulatory action,
and sustained natural disasters.
The blast radius for an Enterprise service that hard-depends on a Cell is the *Cell's* blast radius.
"Operating above the tenant" is only true if the service stays available when a tenant doesn't.

## Decision

**Enterprise-binding services must have no synchronous dependency on the GitLab Application,
or on any other Modular Component running in Cells.**

Calling the GitLab API on the hot path,
or relying on Tier 3 application authorisation for a request-time decision,
disqualifies a service from the Enterprise binding.

The test product teams apply
([Section 4.3.1](../#431-isolation-boundaries)):

> *If the service goes down or becomes degraded when one Cell goes down,
> it isn't an Enterprise service.*

Services that fail the test go through the Cells, Dedicated, or Self-Managed binding —
the binding whose tenancy model already aligns with the failure domain the service is coupled to.

## Consequences

### Positive

1. **Cell outages don't propagate.**
   Billing and licensing continue working when any single Cell is unavailable,
   regardless of how long the outage lasts.
1. **The test is mechanical.**
   "Pick a Cell, take it offline for a week; does this service stay up?"
   The team building the service can apply the rule themselves.
1. **The binding's tenancy model is honest.**
   Enterprise services genuinely operate above tenants;
   the binding's design isn't quietly contradicted by service-level coupling.

### Negative

1. **Services that need real-time GitLab state can't use Enterprise.**
   Anything that has to read live application data at request time
   belongs on a tenant-aligned binding.
1. **More design work up front.**
   Async patterns — eventual consistency, periodic sync, change-data-capture, caches —
   replace the simpler "call the GitLab API" path.
1. **The boundary has to be re-litigated when scopes shift.**
   A service that started without GitLab dependencies might grow them.
   The constraint forces an explicit decision (rewrite, move binding, or refuse the dependency)
   rather than letting the coupling accrete.

## Alternatives Considered

### Alternative: Allow synchronous GitLab API calls, mitigate with retries and circuit breakers

#### Approach

Permit synchronous calls into Cells from Enterprise services
on the grounds that retries and circuit breakers handle short outages.

#### Why Not Chosen

The threat model is a multi-day regional outage, not a transient blip.
A circuit breaker that has been open for three days
means the feature has been unavailable for three days.

## References

- [Section 4.3 — The Enterprise Platform Binding](../#43-the-enterprise-platform-binding) —
  the binding this constraint protects.
- [Section 4.3.1 — Isolation Boundaries](../#431-isolation-boundaries) —
  the Cell-as-isolation-boundary primitive this builds on.
- [March 2026 AWS Gulf data-centre strikes](https://theconversation.com/why-iran-targeted-amazon-data-centers-and-what-that-does-and-doesnt-change-about-warfare-278642) —
  the concrete incident that informs the multi-day-outage threat model.
