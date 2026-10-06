---
title: "LabKit ADR 001: HTTP routing approach for Go services"
toc_hide: true
---

## Context

As part of LabKit v2 development, we evaluated whether to adopt
[go-chi/chi](https://github.com/go-chi/chi) as the standard HTTP router for
all Go services at GitLab, and whether LabKit should expose a `Router`
interface that abstracts the underlying framework.

The discussion ([team-tasks#4311](https://gitlab.com/gitlab-org/quality/quality-engineering/team-tasks/-/issues/4311))
was an open discussion where senior technical leaders and Go service maintainers
could raise concerns, suggest alternatives, or approve the direction.

An investigation with benchmarks was conducted in
[team-tasks#4294](https://gitlab.com/gitlab-org/quality/quality-engineering/team-tasks/-/issues/4294).

## Decision

1. LabKit does not own the routing layer. LabKit v2 provides
   observability middleware (tracing, access logging, correlation IDs, health
   probes) that works with any `net/http`-compatible handler. Services bring
   their own router.

1. No Router interface in LabKit. The original `v2/httpserver.Router`
   interface is removed. Abstracting a router behind a LabKit API adds
   maintenance cost without clear gain. Per
   [Hyrum's Law](https://www.hyrumslaw.com/), consumers will inevitably
   depend on the concrete implementation, making the abstraction difficult to
   honor in practice.

1. Go 1.22+ standard library `ServeMux` is sufficient for most services. Modern
   `ServeMux` supports method-based routing (`GET /path`) and path
   parameters (`/items/{id}`), covering the needs of services with simple
   routing requirements.

1. Chi is recommended when advanced routing is needed. For services
   requiring route grouping, scoped middleware, or sub-router mounting,
   `go-chi/chi` is the recommended choice. It depends only on the standard
   library, uses `http.Handler` throughout, and is already in use at GitLab
   (Container Registry migration, Zoekt indexer).

1. LabKit middleware must compose with any standard library-compatible router.
   Middleware signatures use `func(http.Handler) http.Handler`. This works
   with standard library `ServeMux`, chi, or any other `http.Handler`-compatible
   router.

1. Lab Bench owns higher-level HTTP abstractions. If a structured service
   chassis requires a routing abstraction (for capability analysis,
   convention enforcement, or the three-layer service model), that
   abstraction belongs in Lab Bench, not LabKit.

## Consequences

- Services adopting LabKit v2 are not locked into a specific router. They
  choose the router that fits their complexity level.
- LabKit's API surface is smaller and more stable. Middleware is the
  extension point, not routing.
- Cross-cutting concerns (rate limiting, circuit breakers, auth) are
  delivered as middleware that composes with any router, rather than being
  tied to a specific routing framework.
- Services that already use chi (Container Registry, Zoekt) or standard library
  (Workhorse, Runner) do not need to change their routing to adopt LabKit v2
  middleware.
- If a future need arises for a routing abstraction, it can be introduced
  in Lab Bench with full knowledge of the service chassis requirements,
  rather than prematurely in LabKit.

## Alternatives

1. Adopt chi as the default router in LabKit and expose a `Router`
   interface. This was the original proposal in
   [team-tasks#4283](https://gitlab.com/gitlab-org/quality/quality-engineering/team-tasks/-/issues/4283).
   Rejected because the abstraction adds maintenance cost without clear
   benefit, and Hyrum's Law makes swapping implementations impractical.

1. Mandate chi for all services. Rejected because many services have
   simple routing needs fully served by the standard library, and mandating a dependency
   for services that do not need it conflicts with the
   "minimal API surface" principle.

1. Do nothing. Rejected because the lack of shared middleware leads to
   fragmented observability setups across services, as documented in the
   DX survey results referenced in the
   [LabKit North Star Strategy](../_index.md).

## References

- [Discussion issue: team-tasks#4311](https://gitlab.com/gitlab-org/quality/quality-engineering/team-tasks/-/issues/4311)
- [Router investigation: team-tasks#4294](https://gitlab.com/gitlab-org/quality/quality-engineering/team-tasks/-/issues/4294)
- [Lab Bench proposal](https://docs.google.com/document/d/11Zj918LuZeY3fPcU50ZPhzJtcqzvyXaO0SDamW7cDc8/)
- [LabKit North Star Strategy](../_index.md)
