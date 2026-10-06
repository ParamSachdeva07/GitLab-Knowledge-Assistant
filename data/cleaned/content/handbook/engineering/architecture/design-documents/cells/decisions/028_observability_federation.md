---
title: 'Cells ADR 028: Observability Federation'
description: "Expose each Cell's Prometheus endpoint over a secured public ingress and automate Grafana data source registration via Instrumentor."
owning-stage: "~devops::tenant services"
group: cells-infrastructure
creation-date: "2026-07-06"
authors: ["@romongbale"]
approvers: ["@jarv", "@daveyleach", "@a_richter", "@knottos", "@nduff"]
status: proposed
toc_hide: true
---

## Summary

Each Cell exposes its in-cluster Prometheus endpoint through Tenant Ingress Gateway
(Gateway API, `gateway.networking.k8s.io`) resources that terminate TLS for
machine-to-machine traffic between tenants in AWS and global Grafana in GCP.
Access is gated by a CIDR allowlist and restricted to the read-only Prometheus
query paths. Global Grafana queries the endpoint directly as a data source, and
data source provisioning is automated by Instrumentor via the Grafana HTTP API
using service-account API keys. mTLS can be enabled per-Cell without
architectural changes.

Tracked
in [tenant-services work item #454](https://gitlab.com/gitlab-com/gl-infra/tenant-scale/tenant-services/team/-/work_items/454).
Reference

## Context

This ADR addresses the open questions raised in
[Observability 2.0 for Cells](../infrastructure/observability_2_0.md). The
federated pull model introduces several design challenges:

- Global Grafana (`dashboards.gitlab.net`) needs to query per-Cell Prometheus
  endpoints in AWS.
- Onboarding a Cell's Prometheus endpoint as a Grafana data source must be
  automated as part of the tenant lifecycle.
- The network path between GCP Grafana and AWS Prometheus traverses the
  public internet and must be secured.

This ADR resolves the following questions:

- How do we handle a Cell being unreachable during a global query?
- How is authentication/authorization handled between the global Grafana
  instance and each Cell's observability stack?
- Do we need a global alerting layer, or do alerts remain Cell-local?
- How are new Cells automatically registered as data sources in global
  Grafana?

This federated pull design is the current approach. As the Cell fleet scales,
the expected evolution is to selectively remote write a curated set of
high-value metrics into a centralized store; see
[Why Federated Pull Instead of Centralized Remote Write](../infrastructure/observability_2_0.md#why-federated-pull-instead-of-centralized-remote-write).

## Decision

### 1. Network: Envoy Gateway with TLS, CIDR restriction, and path filtering

Each Cell's Prometheus endpoint is exposed via Envoy Gateway (Gateway API,
`gateway.networking.k8s.io`) resources with:

- **TLS termination** at the Gateway (cert-manager-managed certificate,
  renewed via ACME HTTP-01 on a dedicated HTTP listener), securing
  machine-to-machine traffic between the Cell in AWS and Grafana in GCP.
- **Path filtering**: the `HTTPRoute` only exposes the read-only Prometheus
  query surface required by Grafana: `/api/v1/query`, `/api/v1/query_range`,
  and `/api/v1/query_exemplars`. Admin, write, and config endpoints are
  intentionally not routed and remain blocked: `/api/v1/admin/*`,
  `/api/v1/write`, `/-/reload`, `/-/quit`, `/federate`,
  `/api/v1/status/config`, `/api/v1/status/flags`.
- **CIDR allowlist** via an Envoy Gateway `SecurityPolicy` restricting inbound
  access to known Grafana egress IPs. The policy is always created and
  **fails closed**: an empty observability allowlist yields a deny-all policy
  rather than an unguarded route. This matters because the Cloudflare WAF is
  bypassed for this host.
- **mTLS disabled by default**, enabled per-Cell via the Instrumentor tenant
  model (`prometheus_central_grafana_mtls_enabled`) without re-architecting
  the Gateway. When enabled, an Envoy Gateway `ClientTrafficPolicy` requires a
  client certificate signed by the per-tenant CA (cert-manager-issued,
  `prometheus-mtls-ca-tls`); the CIDR allowlist alone is no longer sufficient.
  The policy targets only the HTTPS query listeners (`prometheus-web-<i>`)
  by `sectionName`: the ACME HTTP listener is excluded so HTTP-01 certificate
  renewal (which presents no client cert) keeps working, and because
  `mergeGateways` is enabled, a Gateway-wide (`sectionName`-less) policy would
  wrongly force mTLS onto every listener on the tenant cluster's merged
  gateway, breaking all other workload traffic on the Cell, not just the
  Grafana-facing Prometheus paths.

### 2. Authentication

Authentication happens on two distinct planes:

**Instrumentor to Grafana (data source registration):** Instrumentor calls the
Grafana HTTP API using a **bearer-token API key** issued by a Grafana service
account scoped to data-source administration. The key is:

- Stored in Vault and injected into Instrumentor at provisioning time.
- Rotated as part of the standard Instrumentor secret-rotation lifecycle.
- Passed as the `Authorization: Bearer <token>` header on Grafana API calls
  to create and delete data sources.

**Grafana to Cell Prometheus (query path):** Grafana's access to each tenant's
Envoy Gateway is gated at the network layer, not by the API key:

- **TLS** terminated at the Gateway authenticates the server to Grafana.
- The `SecurityPolicy` **CIDR allowlist restricts inbound access to the
  Grafana load balancer egress IPs only**.
- When mTLS is enabled, Grafana additionally presents a client certificate
  signed by the per-tenant CA (stored in Vault), authenticating the caller.

### 3. Automation: Instrumentor provisions Grafana data sources

Instrumentor manages the Grafana data source lifecycle as part of the tenant
configure and deprovision flows:

- **On provision/configure:** call the Grafana HTTP API to create a Prometheus
  data source pointing at `https://<tenant_managed_domain>/prometheus` (or
  equivalent ingress hostname), authenticated with the service-account API key.
  Data source name: `cell-<tenant_id>-<region>` (for example,
  `cell-icellapp-us-east-1`).
- **On deprovision:** call the Grafana HTTP API to delete the data source.
- The Grafana API endpoint and service-account credentials are injected into
  Instrumentor via the Jsonnet-generated environment (same pattern as
  `TENANT_PROMETHEUS_DB_DISK_SIZE` and other environment variables).

### 4. Allowed IP List Automation

The global observability stack (Grafana for dashboards and Mimir for
long-term metric storage) is deployed via config-mgmt, which has write access
to Vault. config-mgmt automatically updates the allowed-IP list in Vault based
on Grafana's egress IPs. Instrumentor consumes this list to build the ingress
rules for each tenant's Prometheus endpoint.

## Security Considerations

| Concern                                  | Mitigation                                                               |
|------------------------------------------|--------------------------------------------------------------------------|
| Unauthenticated access to Prometheus     | CIDR allowlist (Grafana LB egress IPs only) + TLS              |
| Exposure of admin/write/config endpoints | Path filtering: only the read-only query surface is routed               |
| Empty allowlist leaving the route open   | `SecurityPolicy` always created; fails closed to deny-all                |
| Cloudflare WAF bypassed for this host    | Gateway-level CIDR allowlist and path filtering as compensating controls |
| Credential exposure                      | Keys stored in Vault; never in source or env files                       |
| Insufficient auth for sensitive Cells    | mTLS opt-in per tenant model (`ClientTrafficPolicy`, per-tenant CA)      |
| Data in transit                          | TLS enforced for Grafana-to-Gateway traffic; plaintext public transport not permitted |
| Grafana service account over-privilege   | Scoped to data-source admin only                                         |

## Consequences

- Instrumentor gains two new Grafana API calls (create/delete data source)
  in the configure and deprovision playbooks.
- A Vault secret path convention for Grafana API keys must be defined and
  documented.
- The Envoy Prometheus Gateway resources (`HTTPRoute`, `SecurityPolicy`, and
  optional `ClientTrafficPolicy`) are managed by Instrumentor per Cell, with
  the CIDR list sourced from the tenant model or a well-known Grafana egress
  IP list.
- The Grafana egress IP allowlist is owned by the Observability (O11y) team, who are the source of truth for its
  contents. It is expected to be static and change infrequently. If the allowlist changes in config-mgmt, config-mgmt
  should update the corresponding Vault secret automatically so Instrumentor and the Grafana-facing Gateway
  configuration can consume the latest IPs without manual intervention.
- mTLS enablement requires a follow-up runbook and Instrumentor support for
  injecting client certs into the Grafana data source config.
- Per-tenant aggregate network egress must be instrumented so the query-time
  egress of federated pull can be compared directly against continuous remote
  write, validating the accepted-uncertainty trade-off before committing to
  either model long term.

## Follow-up

- [ ] Instrumentor: Grafana data source create/delete via API (configure and
  deprovision)
- [ ] Instrumentor: CIDR-restricted, path-filtered TLS Prometheus exposure via
  Envoy Gateway per Cell (in progress:
  [instrumentor!8025](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/instrumentor/-/merge_requests/8025))
- [ ] Define Vault secret path convention for Grafana API keys
- [ ] config-mgmt: automatically sync Grafana egress IP allowlist changes to
  Vault
- [ ] mTLS enablement runbook for Cells requiring stronger auth
- [ ] Instrument per-tenant aggregate network egress to enable direct cost
  comparison between federated pull (query-time egress) and centralized remote
  write (ingest-time egress) (tracking item TBD)
