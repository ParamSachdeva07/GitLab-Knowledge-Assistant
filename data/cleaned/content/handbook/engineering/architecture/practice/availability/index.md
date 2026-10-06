---
title: "Availability"
---

Your system **will fail**. Availability is the practice of minimizing the impact when it does. This page provides:

- Best practices for building and operating reliable systems
- A framework for making tradeoffs during incidents

## The Pillars of Availability

When a system is under pressure, we focus on what to protect. These four pillars are interdependent — we tune them rather than sacrifice one for another.

| Pillar | Focus | Why it matters |
|---|---|---|
| **Data Integrity** | Protecting data | Availability is worthless if the data is corrupted. Even during failover, data must remain accurate and consistent. |
| **System Resiliency** | Stability & scale | The ability to absorb shocks — traffic spikes, hardware failure — without total collapse. Includes self-healing and load shedding. |
| **Experience Validation** | Customer experience | Not just "is the system up?" but "is the feature functional and performant?" |
| **Controlled Change** | Safety of evolution | Most outages are caused by change. Safe rollouts, feature flags, and fast rollbacks keep change from becoming a crisis. |

![Pillars of Availability](/images/engineering/architecture/practice/availability/pillars-of-availability.png)

### Measuring Severity

Three questions define the weight these pillars must carry during an incident:

- **Blast Radius (Scope):** Does this affect one user, or all users?
- **Persistence (Duration):** Is this failure Transient and self-healing, or persistent and requires manual intervention?
- **Breadth (Spread):** Does this impact one feature or the whole platform?

## Availability Best Practices

This section collects availability best practices, gathered over time through experience. They are guidelines, not rules, that we apply to build and operate reliable systems in a structured fashion.

<style>
.availability-practice {
  display: inline-block;
}
</style>

<details>
<summary>

### Failure is Inevitable{.availability-practice}

</summary>

Your system will fail. 100% availability is never the correct target.

#### Why

Every system has failure modes. Hardware degrades, software has bugs, networks partition, and cloud providers have outages. Many of these are outside your control. Accepting this reality and designing for it is the foundation of building available systems. Setting an availability target of 100% is never correct because it implies infinite cost and zero change, neither of which is achievable or desirable.

See [SRE Book: Embracing Risk](https://sre.google/sre-book/embracing-risk/) for more detail.

#### How

Define an error budget for your service that reflects its criticality. Use that error budget to make informed decisions about the pace of change versus the cost of failure. Ensure your system has a published availability target so that both operators and users can make informed choices.

#### Examples

GitLab.com targets 99.95% availability, which allows for roughly 22 minutes of downtime per month. This budget creates space for deployments, maintenance, and the occasional unexpected failure without treating every minor disruption as a crisis. Services like Gitaly and the CI runners each have their own error budgets tracked on the [GitLab.com SaaS Availability dashboard](https://dashboards.gitlab.net).

</details>

<details>
<summary>

### Prioritize Interactive Traffic{.availability-practice}

</summary>

When systems are under pressure, protect the traffic that users are actively waiting on.

#### Why

Interactive traffic directly impacts the user experience in real time. A user waiting for a page to load or a Git push to complete feels the impact of degradation immediately. Background processing, webhooks, and asynchronous jobs can tolerate delays without the user noticing.

#### How

Implement quality-of-service mechanisms that distinguish between interactive and background traffic. When saturation occurs, shed background work first. Use separate resource pools where possible so that background processing cannot starve interactive requests.

#### Examples

On GitLab.com, Sidekiq jobs are categorized by urgency. During periods of high database load, lower-priority background jobs such as project exports or pipeline artifact expiry can be deferred while web requests and API calls to the Rails application continue to be served. Separate Sidekiq shard configurations allow us to throttle or pause non-critical queues to minimize the impact on impact user-facing experience.

</details>

<details>
<summary>

### Design for Graceful Failure{.availability-practice}

</summary>

When a component fails, the system should degrade, not collapse.

#### Why

Hard failures cascade. If one dependency going down takes your entire application with it, you have coupled your availability to the least reliable component in the chain. Graceful failure keeps the blast radius small and preserves the parts of the system that still work.

#### How

Consider what happens when each of your dependencies becomes unavailable. Design fallback paths: serve cached data, disable non-essential features, or return partial results. Make failure modes explicit in your architecture so they can be tested and reasoned about.

#### Examples

If the Elasticsearch cluster backing GitLab's Advanced Search becomes unavailable, search results can fall back to basic database-backed search rather than returning errors. Similarly, when an external object storage provider experiences latency, the application can degrade by showing placeholder content for attachments rather than timing out entire page loads.

</details>

<details>
<summary>

### Latency is Part of Failure{.availability-practice}

</summary>

A slow system is a broken system from the user's perspective.

#### Why

Users do not distinguish between a request that fails and a request that takes so long they give up. Excessive latency also creates back-pressure: connections pile up, worker pools saturate, and what started as slowness becomes a full outage. Latency is often the first symptom of an impending failure.

#### How

Set latency targets alongside availability targets. Monitor p50, p95, and p99 latencies and treat sustained latency increases as availability incidents. Use [Apdex scores](https://www.apdex.org/) to quantify user satisfaction with response times: Apdex provides a standardized way to measure whether requests are completing within acceptable thresholds, and a declining Apdex score is an early warning of availability degradation. Use timeouts and circuit breakers to prevent slow dependencies from consuming resources indefinitely.

#### Examples

On GitLab.com, a slow Postgres query that takes 30 seconds instead of 30 milliseconds does not just affect one user. It holds a database connection and a Puma worker thread for the duration, reducing capacity for all other requests.

In many cases, such as database queries in Sidekiq or Sidekiq jobs themselves, monitoring traditional percentile latencies (p50, p95, p99) is impractical because the cardinality of histogram buckets would be too expensive. Instead, we classify requests as acceptable, tolerated, or bad and turn that into an Apdex score, giving us a clear signal of user-facing latency health without the observability cost.

</details>

<details>
<summary>

### Design for Redundancy{.availability-practice}

</summary>

No single component should be a single point of failure.

#### Why

Hardware fails, software crashes, and entire availability zones go offline. If your system depends on a single instance of any component, that component's failure becomes your system's failure. Redundancy provides the ability to survive individual failures without user impact.

#### How

For stateless services, run multiple instances behind load balancers and distribute them across failure domains (zones or regions). For stateful systems, use replication with automatic failover. Ensure that redundant components are truly independent: they should not share underlying infrastructure that could fail simultaneously.

#### Examples

GitLab.com runs stateless application workloads across multiple GCP zones, so the loss of a single zone does not cause an outage. Postgres uses synchronous replication with automatic failover via Patroni. Redis Cluster provides redundancy for caching and session storage. However, Gitaly remains an area where we lack full redundancy: repository data is not yet replicated in a way that allows seamless failover, making Gitaly node failures a known availability risk that requires manual intervention.

</details>

<details>
<summary>

### Networking is Hard{.availability-practice}

</summary>

Network failures are among the most common and least predictable causes of outages.

#### Why

It is always DNS (okay, not always, but often). Or it is packet loss, or asymmetric routing, or a misconfigured firewall rule, or a certificate expiry. The network is the connective tissue of distributed systems and its failure modes are diverse and often subtle. The distance between network components introduces latency that cannot be eliminated by adding more hardware.

#### How

Assume the network is unreliable. Design for retries with backoff and jitter. Minimize the number of network hops in critical paths. Instrument inter-service latency at the application layer so you can detect when network conditions degrade. Keep network topologies as simple as possible.

#### Examples

GitLab.com routes most of our traffic through Cloudflare before it reaches our GCP infrastructure. A misconfiguration at any layer, whether it is a DNS record, a Cloudflare rule, or a GCP load balancer health check, can take down the entire site. Certificate renewals and DNS TTLs are monitored and automated to reduce the likelihood of human error in these critical paths.

</details>

<details>
<summary>

### Avoid One-Way-Door Failures{.availability-practice}

</summary>

Irreversible actions deserve the highest level of scrutiny.

#### Why

A failure you can roll back is an inconvenience. A failure you cannot roll back from is a crisis. Data deletion, schema migrations that drop columns, and configuration changes that cannot be undone are all one-way doors. These failures are disproportionately expensive to recover from and often result in data loss or extended outages.

#### How

Use soft deletes wherever possible. Add confirmation checks and delays before destructive operations. Ensure database migrations are reversible or have a tested rollback path. Treat any operation that permanently alters data with extreme caution.

#### Examples

For database migrations on GitLab.com, the standard practice is to avoid dropping columns in the same release they are removed from code, ensuring a rollback is always possible. For columns in tables with relatively few rows or minimal data, consider not dropping the data at all: the cost of a clean schema may not be worth the risk. Rails' `ignore_columns` allows you to abandon a column in code while deferring the actual drop to a major upgrade, or indefinitely. Destructive operations like project or group deletion should be carefully gated and validated. When a migration or data change cannot be reversed, it requires additional review and a clear rollback plan that accounts for the possibility of failure.

</details>

<details>
<summary>

### Shared Resources are Expensive{.availability-practice}

</summary>

Shared resources create coupling between otherwise independent systems.

#### Why

Shared resources are not all yours. Every shared database connection, CPU cycle, and network socket costs someone, either you or another team's service or your customers. When shared resources become saturated, every consumer is affected simultaneously. Understanding your resource consumption is the first step toward not being the cause of someone else's outage.

#### How

Measure and monitor your consumption of shared resources. Set limits and quotas so that one consumer cannot exhaust the pool. Where possible, isolate critical workloads onto dedicated resources. Be a good neighbor.

#### Examples

GitLab.com's primary Postgres database is a shared resource consumed by every feature in the application. A single poorly optimized query from one feature can saturate database connections and impact every other feature. This is why we enforce connection limits per service, use PgBouncer for connection pooling, and track per-feature database resource consumption to identify and address excessive usage.

</details>

<details>
<summary>

### Expect the Unexpected from Customers{.availability-practice}

</summary>

Customers will use your system in ways you did not anticipate.

#### Why

If you hand someone a foot gun, they will use it. Customers will create repositories with millions of files, pipelines with thousands of jobs, and API integrations that poll every second. None of this is malicious, it is simply the natural consequence of building flexible tools. If your system cannot handle unexpected usage patterns, it is your system's problem, not the customer's.

#### How

Assume that every input field, API endpoint, and user-configurable parameter will eventually receive extreme values. Implement rate limits, [keyset pagination](https://docs.gitlab.com/development/database/keyset_pagination/), and resource caps as part of the initial design, not as afterthoughts. Test with realistic and adversarial workloads.

#### Examples

On GitLab.com, a single customer's CI pipeline configuration once generated thousands of child pipelines causing significant Sidekiq queue saturation. The configuration was entirely valid according to the API; the system simply was not designed for that scale of pipeline fan-out. Adding pipeline limits and improving queue isolation were necessary to protect the platform.

</details>

<details>
<summary>

### Rate Limits are a Double-Edged Sword{.availability-practice}

</summary>

Rate limits protect the platform, but enabling them late creates pain for everyone.

#### Why

Rate limits are essential for protecting shared infrastructure from abuse and runaway workloads. However, introducing rate limits after customers have already built integrations and workflows that exceed those limits creates a poor experience: customers are suddenly blocked from doing what they have been doing for months or years. The later you enable rate limits, the more disruptive they become.

#### How

Enable rate limits early, at conservative thresholds, before customers develop dependencies on unlimited access. It is far easier to raise a limit than to introduce one. When rate limits must be added to existing functionality, communicate proactively and provide customers with tools to understand their usage before enforcement begins.

#### Examples

On GitLab.com, API endpoints that launched without rate limits have required careful, staged rollouts when limits were eventually added. Customers with legitimate high-volume integrations were impacted, requiring exceptions, communication, and engineering effort to mitigate. In contrast, newer features that ship with rate limits from day one rarely generate complaints because customers design their integrations within those constraints from the start.

</details>

<details>
<summary>

### Protect Against Abuse{.availability-practice}

</summary>

Abuse is a constant. Your system must be resilient to it.

#### Why

You have even less control over abusive traffic than you do over legitimate customer behavior. Attackers, scrapers, and cryptocurrency miners will find and exploit any unprotected surface. If your system does not have defenses in place, abuse will consume resources meant for legitimate users.

#### How

Implement rate limiting at multiple layers. Use web application firewalls and bot detection. Design abuse mitigation that can be activated quickly without requiring code deployments. Ensure that abuse of one feature does not degrade the availability of unrelated features.

#### Examples

GitLab.com uses Cloudflare for DDoS protection, alongside application-layer rate limiting. Internally, `Rack::Attack` provides per-user and per-IP rate limits on the Rails application. When a new abuse pattern emerges, such as the use of free-tier CI minutes for cryptocurrency mining, the response must be rapid: adjusting rate limits and blocking abusive accounts through operational tooling rather than waiting for a code release.

</details>

<details>
<summary>

### Chaos Engineering and Testing{.availability-practice}

</summary>

You cannot be confident in your system's availability unless you have tested its failure modes.

#### Why

Assumptions about how systems fail are frequently wrong. The only way to know how your system behaves when a dependency is unavailable, a node is lost, or traffic spikes is to test it. Testing in production-like environments reveals failure modes that unit tests and code review cannot.

#### How

Run game days that simulate realistic failure scenarios. Perform load testing in staging to understand saturation points. Conduct operational testing to verify that runbooks, alerting, and incident response processes work as expected. Make this a regular practice, not a one-time event.

#### Examples

The GitLab.com infrastructure team runs periodic game days where components such as Redis, Postgres replicas, or Gitaly nodes are intentionally degraded to observe system behavior and validate alerting. Load testing in staging with realistic traffic profiles has identified bottlenecks, such as connection pool exhaustion, that would have caused production outages if left undiscovered.

</details>

<details>
<summary>

### Rollouts are a Problem{.availability-practice}

</summary>

A large percentage of production incidents are caused by changes.

#### Why

Deployments, configuration changes, feature flag toggles, and infrastructure modifications are the most common triggers for incidents. This is not a reason to stop making changes; it is a reason to make changes carefully. Changes interact with saturation in unpredictable ways: removing one bottleneck often reveals the next.

#### How

Roll out changes incrementally. Use feature flags and canary deployments to limit blast radius. Monitor key metrics during and after every rollout. Ensure that every change can be quickly rolled back. Treat change management as an availability practice, not an administrative burden.

#### Examples

GitLab.com uses a progressive deployment pipeline that rolls changes through canary, staging, and then production in stages. Feature flags allow new functionality to be enabled for a small percentage of users before a full rollout. When a deployment causes an increase in error rates, the deployment pipeline can be halted and the change reverted within minutes.

</details>

<details>
<summary>

### Cattle, not Pets{.availability-practice}

</summary>

A well-known, reproducible deployment architecture prevents availability problems.

#### Why

When infrastructure is hand-crafted and unique, every failure is a novel event that requires bespoke investigation and repair. When infrastructure is reproducible and disposable, recovery is fast because you replace rather than repair. Pets create single points of failure; cattle create resilience.

#### How

Automate infrastructure provisioning. Use immutable deployments where possible. Ensure that any single node, container, or instance can be destroyed and recreated without impact. Avoid storing state on ephemeral compute resources.

#### Examples

GitLab.com runs its application workloads on Kubernetes, where pods are ephemeral and automatically replaced if they fail health checks. Infrastructure is provisioned through Terraform, ensuring that environments can be reproducibly created. This approach means that a failed node is not a crisis; it is a routine event handled automatically by the platform.

</details>

<details>
<summary>

### Prove Your System Works{.availability-practice}

</summary>

In order to know that your system is available, you need telemetry that proves it works end to end.

#### Why

You cannot improve what you cannot measure, and you cannot protect what you cannot see. Observability is not about knowing how your system breaks; it is about being able to prove that it works. Telemetry that mirrors the customer experience is the foundation of availability measurement and alerting.

#### How

Instrument your system to measure end-to-end success from the customer's perspective. Focus on signals that confirm the system is working, not just signals that fire when it is broken. From there, set up alerting based on symptoms rather than causes. Use SLIs and SLOs to define and track what "working" means for your service.

#### Examples

GitLab.com uses synthetic monitoring that performs real Git operations (clone, push, pull) and web interactions against the production environment to continuously prove that the core user experience is functional. Service-level indicators such as the Apdex score for web requests and the error ratio for API endpoints provide a customer-centric view of availability that drives alerting and incident response.

</details>
