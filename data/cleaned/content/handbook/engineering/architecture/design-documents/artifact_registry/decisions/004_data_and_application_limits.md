---
title: "Artifact Registry ADR 004: Data and Application Limits"
owning-stage: "~devops::package"
description: "Limits for storage, artifact size, API rate, concurrency, and entity counts in the Artifact Registry"
toc_hide: true
---

## Context

The Artifact Registry must define explicit limits to ensure system stability, prevent abuse, and enable predictable resource consumption. These limits are distinct from data retention policies (see [ADR-010](010_data_retention.md)), which govern how long data is kept. Limits here govern how much data and how many operations are allowed at any point in time.

Without defined limits, a small number of tenants can consume disproportionate resources, degrading service quality for all customers. CI/CD workloads create highly spiky traffic (see [ADR-003](003_system_requirements.md)), making burst control especially important.

This ADR distinguishes between three types of constraints:

- **Limits** protect the stability and security of the application. They are enforced per request or per time window and are not tied to billing. Examples: maximum artifact upload size, API rate limits, entity count caps.
- **Quotas** are aggregate consumption constraints tied to a billing cycle or plan. They govern how much of a resource a namespace may consume overall. Example: storage quota per namespace.
- **Policies** represent business logic decoupled from application code that controls access to the Artifact Registry. Policies are evaluated before limits and quotas.
  - _Example:_ deny access from IPs not on the organization's IP allowlist
  - _Example:_ deny access for blocked or banned users

This ADR covers **limits** (artifact size, API rate, entity counts) and **quotas** (storage).

The Artifact Registry targets GitLab.com scale: thousands of API requests per second steady-state, tens of petabytes of total stored data, and millions of artifacts per large organization (see [ADR-003](003_system_requirements.md)). Limits must be high enough to support legitimate enterprise workloads and low enough to prevent any single namespace from destabilizing the service.

Where applicable, limits align with or extend those already established in the Package Registry and Container Registry to provide a consistent experience across GitLab registries.

## Decision

**The Artifact Registry enforces quotas and limits at the namespace level, the Artifact Registry's tenancy and partition boundary, across four dimensions: storage (quota), artifact size (limit), API rate (limit), and entity counts (limit). Plan-tier defaults for rate limits and storage quota are inherited from the billing anchor (the organization), but every limit is enforced and measured per namespace. An organization that owns multiple namespaces is billed for the sum of its namespaces' usage; there is no cross-namespace deduplication or pooling.**

Artifact size limits and entity count limits use the same defaults across all installation types. Rate limits are plan-dependent on GitLab.com — each plan tier defines its own default rate limits, and individual namespaces can receive custom overrides for legitimate heavy usage. On Self-Managed, administrators can adjust all limits at the instance level.

### Storage Quota

The storage quota is enforced at the namespace level. Storage is measured as the deduplicated total of all unique blobs within a namespace; deduplication is scoped per namespace, consistent with [ADR-002](002_storage_deduplication_scope.md). There is no deduplication across namespaces: an organization that owns multiple namespaces consumes and is billed for the sum of each namespace's storage, with the organization remaining the billing anchor ([ADR-001](001_organizations_as_anchor_point.md)).

| Quota | Default | Notes |
| ----- | ------- | ----- |
| Max storage per namespace | Plan-dependent (SKU-based) | The Artifact Registry is a new premium SKU (see [overview](../_index.md)); storage quota is defined by the purchased add-on |
| Max storage per repository | No hard limit by default | Optional warning threshold configurable at the namespace level; when exceeded, the namespace owner is notified but uploads are not blocked |

A warning threshold (for example, 80% of quota) can be configured per namespace. When usage exceeds this threshold, the namespace owner is notified, but uploads are not blocked until the quota is fully reached.

Before accepting a new upload session, the system checks whether the namespace is at or over its storage quota. If the namespace still has headroom, the upload is accepted and usage counters are updated after successful completion. If the namespace is already at or over quota, the upload session is rejected.

Because usage counters are updated after each successful upload, concurrent upload sessions may each pass the quota check independently and collectively exceed the quota by a small margin. This is acceptable — strict enforcement would require serializing all uploads, which conflicts with the concurrency targets in [ADR-003](003_system_requirements.md). The overshoot is bounded by the number of concurrent uploads and corrected on the next quota check.

### Artifact Size Limits

Artifact size limits vary by artifact type. The default values below apply to all installation types. On Self-Managed, administrators can override these defaults at the instance level.

| Artifact type | Max artifact size | Notes |
| ------------- | ----------------- | ----- |
| Maven | 5 GB | Consistent with existing Package Registry limit |
| npm | 5 GB | Consistent with existing Package Registry limit |
| Container images | 50 GB | Maximum size per blob. |

Additionally, for container images, the following limits apply:

| Limit | Default | Notes |
| ----- | ------- | ----- |
| Max manifest payload | 250 KB | Applies to Docker and OCI manifests. |
| Max manifest reference count | 200 | Maximum number of blobs or manifests a manifest may reference |

Upload sessions are subject to an inactivity timeout. If no data is received within the timeout window, the session is terminated and partially uploaded data is discarded. This mitigates slow-rate denial-of-service attacks (such as Slowloris) and prevents idle sessions from holding resources indefinitely.

### Rate Limits

Rate limits protect the API from abuse and prevent any single user or namespace from exhausting shared infrastructure. Rate limit violations return HTTP 429 (Too Many Requests) with a `Retry-After` header.

On Self-Managed, administrators can override rate limit defaults at the instance level.

On GitLab.com, rate limits are initially deployed in logging/warning mode and only enforced after traffic distributions are analyzed (see [rollout strategy](#implementation-notes)). This phased rollout is a one-time process to establish sensible defaults. On Self-Managed, administrators can configure and enforce rate limits directly.

#### IP-Based Limits

IP-based rate limits provide the outermost defense layer against abuse and are the first limits introduced during rollout (see [rollout strategy](#implementation-notes)). They reuse the [GCRA-based middleware from the Container Registry](https://gitlab.com/gitlab-org/container-registry/-/issues/1225). Initial default values will be determined during the Observe phase based on production traffic analysis.

#### Per-User Limits

Per-user rate limits are plan-dependent: users within an organization inherit defaults from the organization's plan tier. Default values per plan will be determined during the Observe phase of the [rollout strategy](#implementation-notes) based on per-user traffic distributions. The existing [Package Registry rate limits](https://docs.gitlab.com/administration/settings/package_registry_rate_limits/) serve as a baseline reference.

#### Per-Namespace Limits

Per-namespace rate limits are plan-dependent: each plan tier (Premium, Ultimate) defines its own default rate limit, inherited from the namespace's billing anchor. Individual namespaces can have their own rate limits set as a first-class property of the configuration, not managed on an exception basis, to accommodate legitimate heavy usage without raising defaults for all namespaces on the same plan. Default values per plan will be determined during the Observe phase of the [rollout strategy](#implementation-notes) based on per-namespace traffic distributions.

This tiered approach avoids the problem of a single global default: setting one value high enough for heavy legitimate users effectively disables rate limiting for everyone else. Plan-based defaults with per-namespace overrides allow the platform to protect against abuse at lower tiers while supporting high-volume customers at higher tiers.

Namespace-level limits are the primary protection mechanism for the platform. Per-user limits provide a secondary layer to prevent a single user from consuming the full namespace quota.

#### Concurrent Upload Sessions

Concurrent upload session limits cap the number of in-flight uploads per user and per namespace. This prevents a single actor from monopolizing upload infrastructure. Like rate limits, concurrent upload session limits are plan-dependent. Default values per plan will be determined during the Observe phase of the [rollout strategy](#implementation-notes).

### Entity Count Limits

Entity count limits cap specific operational parameters that affect API behavior, proxy chain complexity, and policy evaluation cost. Repository count is capped per namespace per artifact type to prevent runaway creation from automation bugs.

| Entity | Limit | Notes |
| ------ | ----- | ----- |
| Repositories per namespace per artifact type | 1,000 | Configurable at the instance level |
| Tags per artifact / package version | 1,000 | Prevents abuse and accidental misuse |
| Versions per package | 25,000 | Prevents abuse and accidental misuse |
| Upstream sources per virtual repository | 20 | Limits proxy chain complexity |
| Lifecycle policy rules per repository | 50 | Limits policy evaluation complexity |

Limits on upstream sources and lifecycle policy rules are enforced synchronously at write time. Attempts to exceed these limits return HTTP 422 (Unprocessable Entity).

## Consequences

### Positive

1. **System stability**: Explicit limits prevent runaway workloads from destabilizing shared infrastructure
2. **Predictable performance**: Bounded policy evaluation and proxy chain complexity ensure metadata queries remain performant at scale
3. **Clear customer expectations**: Documented limits allow customers to plan their usage and capacity
4. **Fair multi-tenancy**: Namespace-scoped rate limits, storage quotas, and entity caps distribute resources across tenants
5. **Enforceable SLAs**: Defined limits are a prerequisite for setting meaningful SLOs on API response times

### Negative

1. **Customer friction**: Legitimate high-volume workloads may hit default limits and require manual quota increases
2. **Operational overhead**: Quota management adds ongoing work monitoring usage and processing limit increase requests
3. **Eventually consistent storage accounting**: Usage counters are updated asynchronously; a brief window after a large upload may show stale usage
4. **Limit tuning required**: Default values are initial estimates and will need adjustment based on observed production traffic patterns

## Alternatives Considered

### Alternative 1: No Explicit Limits (Trust Fair Use)

Rely on monitoring and reactive intervention rather than proactive limits.

#### Positive

- No customer friction from hitting limits
- No limit-tuning overhead

#### Negative

- A single misbehaving tenant can degrade service for all customers
- Reactive intervention is slower than automatic enforcement
- No clear basis for customer communication during incidents

**Why rejected:** At GitLab.com scale, proactive limits are necessary for reliable multi-tenancy. The container registry's lack of per-organization limits contributed to [operational complexity](https://gitlab.com/gitlab-org/container-registry/-/issues/1242).

### Alternative 2: Instance-Level Limits Only

Apply limits globally at the instance level rather than per namespace.

#### Positive

- Simpler to implement and reason about

#### Negative

- Does not prevent a single large namespace from consuming the full instance capacity
- Cannot attribute resource usage to specific namespaces for billing and capacity planning

**Why rejected:** Per-namespace limits are required for fair multi-tenancy on GitLab.com. The organization remains the anchor and billing point ([ADR-001](001_organizations_as_anchor_point.md)), aggregating the usage of its namespaces.

### Alternative 3: Limit at CDN/Load Balancer Only

Enforce all rate limits at the CDN or load balancer layer (Cloudflare) rather than in the application.

#### Positive

- Offloads rate-limit computation from the application
- Lower latency for rejection of throttled requests

#### Negative

- CDN-layer limits apply to GitLab.com only; Self-Managed installations would have no equivalent protection
- Cannot enforce per-namespace limits without complex CDN configuration

**Why rejected:** Application-layer rate limiting provides consistent enforcement across all GitLab installation types. CDN-layer limits can complement application limits for IP-based throttling but cannot replace them.

## Implementation Notes

The Artifact Registry is a standalone service. **Open question:** Where limit and quota configuration is stored and managed (e.g., in the Rails monolith and retrieved by the registry via the API, or managed directly within the registry) is yet to be decided.

1. Storage quota: async check at upload session start using a Redis counter updated after each upload and GC cycle
2. Artifact size: enforced during upload by counting bytes as they are read from the request body (not by trusting the `Content-Length` header, which clients can omit or misreport). When the byte count exceeds the limit the read is aborted and the request is rejected. This is the same approach used by Workhorse for upload size enforcement
3. Rate limits: Redis counters using GCRA algorithm; HTTP 429 with `Retry-After` on violation. The rate limiting implementation should reuse the GCRA-based middleware and Redis counter patterns established in the [Container Registry](https://gitlab.com/gitlab-org/container-registry/-/issues/1225), adapting the configuration schema for Artifact Registry-specific operations
4. Entity counts (upstream sources, lifecycle policy rules): database query before insert; HTTP 422 on violation

On GitLab.com, infrastructure-level rate limits via Runway provide an additional defense layer for IP-based throttling. These complement but do not replace application-level limits, which are required for per-namespace and per-user enforcement across all installation types.

All limit violations include a machine-readable error code (for example, `artifact_registry/quota_exceeded`) and a human-readable message identifying the exceeded limit.

**Rollout strategy:** Rate limits and per-namespace quotas are introduced in three phases:

1. **Observe** — All limits (IP-based, per-namespace, and per-user) are configured but only emit metrics and log warnings (no blocking). IP-based limits reuse the existing GCRA middleware from the Container Registry. This phase runs for at least one milestone to collect traffic distributions across all dimensions.
1. **Warn** — Requests that would exceed per-namespace or per-user limits return warning headers (e.g., `X-RateLimit-Remaining`) but are still served. Namespaces approaching limits are notified.
1. **Enforce** — Per-namespace and per-user limits are actively enforced with HTTP 429 responses. Default values are adjusted based on data collected in phases 1 and 2.

## References

- [Rate Limiting Architecture Blueprint](/handbook/engineering/architecture/design-documents/rate_limiting/) - Defines the distinction between limits, quotas, and policies
- [ADR-001: Organizations as Anchor Point](001_organizations_as_anchor_point.md) - Organization as the primary resource boundary
- [ADR-002: Storage Deduplication Scope](002_storage_deduplication_scope.md) - How deduplicated storage is measured
- [ADR-003: System Requirements](003_system_requirements.md) - Scale targets and infrastructure components used for enforcement
- [Package Registry Rate Limits](https://docs.gitlab.com/administration/settings/package_registry_rate_limits/) - Existing rate limit defaults used as baseline
- [Container Registry Rate Limiting Spec](https://gitlab.com/gitlab-org/container-registry/-/blob/main/docs/spec/gitlab/rate-limiting.md) - GCRA-based rate limiting approach
- [Container Registry Rate Limiting Implementation](https://gitlab.com/gitlab-org/container-registry/-/issues/1225) - GCRA-based rate limiting middleware and configuration, reusable for Artifact Registry
- [GitLab Plan Limits API](https://docs.gitlab.com/api/plan_limits/) - Existing per-type artifact size limits
- [Managing Limits](/handbook/engineering/infrastructure-platforms/rate-limiting/managing-limits/) - Process for introducing and changing rate limits
<!-- - [ADR-010: Data Retention](010_data_retention.md) - Retention policies (distinct from limits) -->
