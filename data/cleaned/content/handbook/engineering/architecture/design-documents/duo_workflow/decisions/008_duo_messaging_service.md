---
title: "Duo Agent Platform ADR 008: Duo Messaging Service"
status: proposed
creation-date: "2026-04-17"
authors: [ "@thomas-schmidt" ]
coach: [ ]
approvers: [ ]
owning-stage: "~devops::ai_powered"
participating-stages: []
toc_hide: true
---

## Context

We want users to interact with Duo from various surfaces — external messaging
services (Slack, Microsoft Teams, WhatsApp, Telegram) as well as GitLab-native
surfaces like issue and merge request comments. A user @mentions Duo, gives it
a task, and Duo works on it asynchronously and posts back the result.

While the primary motivation is external messaging platforms, the same adapter
pattern naturally extends to GitLab note-based interactions (e.g., @mentioning
a Duo service account on an MR or issue). Comments on a merge request are
conceptually a form of messaging, and the architecture treats them uniformly.

Two challenges are specific to these interactions:

1. CI pipelines require a project, but some surfaces (e.g., Slack) have no
   project context
2. Multiple surfaces need to be supported without duplicating orchestration
   logic

### Alternatives considered

Five approaches were investigated:

1. **CI job (Flows API)** — Trigger a CI pipeline via the existing Flows
   infrastructure. Battle-tested, ADR 004 compliant, no Workhorse or DWS
   changes. The only approach that provides a real execution environment —
   the agent can git clone, run tests, install tools, and do full development
   tasks. Downside: CI startup latency (~10s with empty project). Requires a
   project for the pipeline — solved by auto-creating a workspace project when
   no project context exists. When the surface already provides a
   project (e.g., a GitLab note on an MR), no workspace project is needed.

2. **WebSocket blocking** — Sidekiq worker opens a WebSocket to Workhorse,
   keeps it open for the full workflow duration. Simple, supports streaming.
   Downside: blocks a Sidekiq thread for up to 5 minutes per request, limiting
   throughput to ~50 concurrent workflows per Sidekiq process. No execution
   environment — the agent runs inside Workhorse with no filesystem, no git,
   no ability to run commands. Limits the agent to read-only API interactions
   with no path to development tasks.

3. **WebSocket fire-and-forget** — Sidekiq opens WebSocket, sends start
   request, disconnects immediately. **Blocked**: prototyping revealed Workhorse
   terminates the workflow when the client disconnects (sends `StopWorkflow` on
   clean close, tears down gRPC on abnormal close). Would require Workhorse
   changes to add a headless/detached mode. Same execution environment
   limitation as option 2.

4. **Direct gRPC** — Sidekiq opens a gRPC bidi stream directly to DWS.
   Lower latency, type-safe. **Violates ADR 004** (introduces a second path to
   DWS). Must reimplement HTTP action proxying in Ruby. No established pattern
   for gRPC bidi streaming from Sidekiq in the codebase. Same execution
   environment limitation — no filesystem or tooling available.

5. **Workhorse headless HTTP** — New Workhorse endpoint that accepts a
   workflow trigger via HTTP POST, manages the gRPC stream internally.
   **Requires cross-team Workhorse changes** (~50-100 lines of Go) and a
   modified runner lifecycle. Same execution environment limitation as
   options 2-4 — no path to development tasks without additional architecture.

## Decision

Use the **Flows API (CI job)** approach with an **adapter pattern** for
multi-surface support and a **per-namespace workspace project** as a fallback
for surfaces that lack project context.

### Architecture

```mermaid
graph LR
    classDef surface fill:#dbeafe,stroke:#93c5fd,color:#1e3a5f
    classDef adapter fill:#d1fae5,stroke:#6ee7b7,color:#065f46
    classDef execution fill:#ede9fe,stroke:#c4b5fd,color:#3b0764
    classDef callback fill:#fef9c3,stroke:#fde047,color:#713f12

    Caller["💬 Caller<br/><i>PostProcessService · AppMentionedService · ...</i><br/><i>policy: auth, SA, flow, project, goal</i>"]
    Adapter["🔌 Delivery Adapter<br/><i>GitlabDuoNote · Slack · ...</i><br/><i>lifecycle: progress, results, errors</i>"]
    Base["⚙️ Base Adapter<br/><i>mechanism: identity, membership,<br/>enrichment, execution</i>"]
    CI["🏃 CI Runner<br/><i>ExecuteWorkflowService</i>"]
    CW["📬 CallbackWorker<br/><i>WorkflowStartedEvent · WorkflowFinishedEvent<br/>WorkloadFinishedEvent (backstop)</i>"]
    PW["📡 ProgressDeliveryWorker<br/><i>checkpoint streaming (live)</i>"]

    Caller -->|"resolved params"| Adapter
    Adapter -->|"trigger"| Base
    Base -->|"start pipeline"| CI
    CI -.->|"workflow started / finished,<br/>workload finished"| CW
    CI -.->|"checkpoint created"| PW
    CW -.->|"result / error / started"| Adapter
    PW -.->|"on_progress delta"| Adapter
    Adapter -.->|"post answer / status"| Caller

    class Caller surface
    class Adapter,Base adapter
    class CI execution
    class CW,PW callback
```

**Solid arrows** = synchronous calls &nbsp;&nbsp; **Dashed arrows** = async events

### Request flow

```mermaid
sequenceDiagram
    participant User
    participant Caller as Caller
    participant Adapter as Delivery Adapter
    participant Base as Base Adapter
    participant CI as CI Runner
    participant CW as CallbackWorker
    participant PW as ProgressDeliveryWorker

    User->>Caller: @duo do something
    Caller->>Caller: Resolve auth, SA, flow, project, goal
    Caller->>Caller: Build resolved params
    Caller->>Adapter: adapter.trigger(params)

    rect rgb(209, 250, 229)
        Note right of Adapter: Trigger phase (sync)
        Adapter->>Adapter: on_request_received (acknowledge user)
        Note right of Base: Composite identity link,<br/>SA project membership,<br/>callback enrichment
        Base->>CI: ExecuteWorkflowService.execute
        CI-->>Base: success + workflow
        Adapter->>User: on_flow_enqueued (👀 / progress note, workflow URL)
    end

    rect rgb(237, 233, 254)
        Note right of CI: Execution phase (async)
        CI->>CI: Agent works (tools, API, git)
        CI-->>CW: WorkflowStartedEvent (agent running)
        CW->>Adapter: on_flow_started (update ack message with session link)
        CI-->>PW: checkpoint created (per step)
        PW->>Adapter: on_progress(delta) (plan + monologue updates)
    end

    rect rgb(254, 249, 195)
        Note right of CW: Callback phase (async)
        CI-->>CW: WorkflowFinishedEvent (agent done, answer persisted)
        CW->>Adapter: deliver_result(message)
        Adapter->>User: Post answer
        Adapter-->>CW: truthy only if it reached the surface
        CW->>CW: Record delivered_at
        CW->>Adapter: on_flow_completed (✅)
        Note over CI,CW: Later, once CI finalization completes
        CI-->>CW: WorkloadFinishedEvent (backstop)
        CW->>CW: delivered_at present → no-op
    end
```

### Key design choices

**Caller owns policy, adapter owns delivery, base adapter owns mechanism.**
The architecture separates three concerns:

- **Callers** (e.g., `PostProcessService` for `@mention` triggers,
  `AppMentionedService` for Slack) own all policy decisions: authorization,
  service account selection, flow selection, version selection, project
  selection, and goal building. The caller resolves everything and builds a
  typed, resolved input before involving the adapter.
- **Delivery adapters** (e.g., `GitlabDuoNote`, `Slack`) own the user-facing
  lifecycle: acknowledging the request, showing progress, delivering results
  or errors, and persisting callback state for async restoration. Adapters are
  organized by **delivery channel**, not trigger source — a `GitlabDuoNote`
  adapter handles any flow that delivers via note threads, whether triggered
  by `@mention`, `@GitLabDuo`, or a future webhook.
- **The shared base adapter** handles security-critical mechanism no caller or
  adapter should do individually: composite identity linking, SA project
  membership, callback context enrichment, resource translation, and workflow
  execution via `ExecuteWorkflowService`.

This means different callers can have fundamentally different auth models
(e.g., Slack uses workspace install + namespace mapping, GitLab note uses
`:trigger_ai_flow` policy, `@GitLabDuo` uses MR-level abilities) while
reusing the same delivery adapter when the channel is the same.

**Flow reference and version are caller-controlled.** Each caller specifies
which flow to trigger (e.g., `developer/v1`) and optionally pins a version.
Callers can use the standard resolution path for flow versioning or override
the version independently. This allows the same infrastructure to support
multiple agent flows with different version strategies.

**`project:` is caller-controlled — workspace project is a fallback.** When a
caller has a project (e.g., a GitLab note on an MR provides `note.project`),
that project is used directly. The `duo-workspace` auto-created project only
comes into play for callers without project context (e.g., Slack's
`AppMentionedService`).

**`duo-workspace` auto-created project (for project-less surfaces).** A
private, empty project per top-level namespace provides CI pipeline context
when no project is available. The workspace project is created at the **root
namespace** of the user's `duo_default_namespace` — for example, if the user's
default namespace is `gitlab-org/editor-extensions`, the workspace project is
created at `gitlab-org/duo-workspace`. This keeps one workspace project per
top-level group, avoiding proliferation of projects across nested namespaces.
The exact project name (`duo-workspace`) is not final and can be iterated on.

The workspace project is created when the admin enables the flow for the
namespace (using admin permissions), with a fallback find-or-create at trigger
time for robustness. Teams customize the workspace project (Docker image,
AGENTS.md, skills, CI variables, runner tags) using existing project features.
Follows the same pattern as Security Policy Projects.

**Composite identity uses existing auth-domain primitives.** Composite identity
linking delegates to the auth domain rather than introducing a parallel linker
module. The SA uses `composite_identity_enforced: true` — the same security
model used by Duo Developer and other agent platform flows. Effective
permissions are the intersection of the triggering user's and the service
account's access.

**Tiered resilience.** Lifecycle hooks are categorized by criticality:
user-facing acknowledgement must succeed or the trigger short-circuits;
best-effort hooks (progress updates, completion signals) are resilient to
failure; security-critical steps and workflow execution fail loudly.

**EventStore callback.** `CallbackWorker` is the sole subscriber for messaging
lifecycle events, and subscribes to three:

| Event | Hook | Role |
|---|---|---|
| `Ai::DuoWorkflows::WorkflowStartedEvent` | `on_flow_started` | Agent transitioned to `:running` |
| `Ai::DuoWorkflows::WorkflowFinishedEvent` | `deliver_result` | **Primary result delivery** — fires the moment the agent finishes |
| `Ci::Workloads::WorkloadFinishedEvent` | `deliver_result` / `on_flow_failed` | Backstop for a lost success delivery; primary path for failures (drop/stop) |

It checks for `messaging_callback_context` on the workflow record (JSONB column)
and delivers results through the adapter. No GraphQL, no polling. The base adapter
enriches the adapter-provided callback context with orchestration metadata
(adapter key, service account ID, flow reference, version) before persisting
it, so the async path can resolve the adapter and service account without
re-resolving them. Example:

```json
{
  "adapter": "slack",
  "team_id": "T0123ABC",
  "channel_id": "C0123ABC",
  "thread_ts": "1234567890.123456",
  "status_ts": "1234567890.654321",
  "session_url": "https://gitlab.com/-/duo_workflows/123",
  "progress_cursor": 42,
  "delivered_at": "2026-08-05T10:38:05Z",
  "service_account_id": 12345,
  "flow_reference": "developer/v1"
}
```

**`progress_cursor`** is written by `ProgressDeliveryWorker` after each
successful delivery and read on the next tick to compute the delta. This
ensures each delivery only processes new checkpoints and is idempotent on
retry.

### Reply delivery: workflow finish, not pipeline finalization

**The reply is delivered when the agent finishes, not when the CI pipeline winds
down.** Delivery originally had only one signal available at the end of a run —
`WorkloadFinishedEvent`, derived from `Ci::PipelineFinishedEvent` — so the answer
sat fully persisted in `checkpoints.latest` while CI job finalization ran. That
added a **significant delay to every reply**, varying per run with whatever that
pipeline's teardown happened to cost, and entirely outside Rails and DWS.
`Ai::DuoWorkflows::WorkflowFinishedEvent` closes that gap: published from
`after_transition on: :finish`, scoped to the successful `running → finished`
transition (not `drop`/`stop`) and to workflows carrying a
`messaging_callback_context`, so non-messaging CI workflows emit nothing.

**Ordering prerequisite (DWS).** Delivering at `:finish` is only safe because DWS
defers its FINISH transition until the terminal checkpoint has been persisted to
Rails. LangGraph's `aput_writes` previously triggered FINISH *before* the
message-bearing `aput` landed, so a listener could read a stale
`checkpoints.latest` and report no response — a race the pipeline-gated design
hid by firing long after the checkpoint had flushed. Future consumers of this
event inherit the guarantee and should not re-add a delay to compensate for it.

**The workload event remains the backstop**, being still the last event of a run.
A `delivered_at` timestamp in `messaging_callback_context` makes success delivery
idempotent across both events: delivery is skipped when it is already set, so the
reply is never posted twice and a Sidekiq retry of either event is harmless. It is
written *after* a confirmed delivery rather than claimed before one — claiming
first would let a crash mid-delivery permanently suppress the reply, the exact
failure this design prevents. The `no_response` case is marked before the attempt,
because a message missing at `:finish` stays missing and the backstop would
otherwise post a second error.

For the backstop to work, **`deliver_result` must return truthy only when the
message actually reached the surface**: adapters swallow their own transport
errors (`Slack::API` turns both API and HTTP failures into `{'ok' => false}`,
`Notes::CreateService` returns an *unsaved* note), so "no exception raised" does
not mean delivered. When it reports failure, `on_flow_completed` is held back so
the surface is not marked answered (e.g. Slack's ✅) with no answer on it.

### Checkpoint streaming

Checkpoint streaming is **implemented** via `ProgressDeliveryWorker` and the
`on_progress` adapter hook. This is not future work.

```mermaid
sequenceDiagram
    participant CI as CI Runner
    participant Rails as Rails
    participant PW as ProgressDeliveryWorker
    participant Adapter as Messaging Adapter
    participant Slack as Slack
    participant User as User

    CI->>Rails: Save checkpoint
    Rails-->>PW: Enqueue (debounced, 2s window)
    PW->>Adapter: on_progress(delta, callback_context)
    Note right of PW: delta.messages = cumulative snapshot<br/>delta.new_messages = appended since last tick
    Adapter->>Slack: Update message (plan block + monologue block)
    PW->>Rails: Persist progress_cursor
```

`ProgressDeliveryWorker` is debounced per workflow (2-second window,
`until_executed` dedup with `reschedule_once` on collision) so a burst of
checkpoints collapses into one delivery. Adapters opt in by returning `true`
from `self.supports_live_progress?`; adapters that don't opt in never schedule
a `ProgressDeliveryWorker`.

The `delta` object carries two views of the same point in time:

1. `delta.messages` — the full cumulative snapshot. Replace-style surfaces
   (e.g. Slack, which rewrites its whole message) render from this so they
   keep still-current state (e.g. the active todo list) even when this tick's
   change was an unrelated entry.
1. `delta.new_messages` — only entries appended since the last delivery.
   Append/stream surfaces use this.

### Path to human approval

Human approval extends the same architecture additively — new EventStore
subscriptions and a new `on_approval_requested` adapter hook — without core
changes. This is not yet implemented.

```mermaid
sequenceDiagram
    participant CI as CI Runner
    participant Rails as Rails
    participant CW as CheckpointCallbackWorker
    participant Adapter as Messaging Adapter
    participant Slack as Slack
    participant User as User

    Note over CI,Slack: When approval is required:
    CI->>Rails: Save checkpoint (approval_required)
    Rails-->>CW: CheckpointCreatedEvent
    CW->>Adapter: on_approval_requested(context, details)
    Adapter->>Slack: Interactive message (Approve / Reject)
    User->>Slack: Clicks "Approve"
    Slack->>Rails: Interaction payload
    Rails->>Rails: Write approval → resume workflow
```

Approval state is persisted on the workflow record and the flow can be stopped
and restarted.

### Adapter interface

The adapter's `trigger` method accepts fully resolved input from the caller
(user, service account, flow, version, project, goal). The adapter does not
resolve policy — it only delivers.

**Delivery (required):**

| Method | Purpose |
|---|---|
| `build_callback_context` | Build adapter-specific context for async delivery (e.g., note/discussion IDs, Slack channel/thread IDs) |
| `deliver_result(callback_context:, message:, workflow:)` | Post the final answer to the surface. **Must return truthy only when the message actually reached it** — this is the worker's only signal to re-attempt a lost delivery via the backstop |
| `deliver_error(callback_context:, error:)` | Post an error message to the surface |

**Lifecycle hooks (optional overrides):**

| Method | When | Notes |
|---|---|---|
| `on_request_received` | Sync, before `build_callback_context`. Must succeed or trigger aborts | Pre-trigger acknowledgement (e.g., add 👀 reaction, post progress message) |
| `on_flow_enqueued(callback_context:, workflow:)` | Sync, after CI submission succeeds | Signal work is queued (e.g., persist workflow URL, post started system note). Container not yet running |
| `on_flow_started(callback_context:, workflow:)` | Async, driven by `WorkflowStartedEvent` | Agent has transitioned to `:running`. Must be idempotent (at-least-once delivery) |
| `on_flow_completed(callback_context:, workflow:)` | Async, after a **successful** `deliver_result` | Signal work done (e.g., ✅ reaction). Skipped when delivery failed, so the surface is never marked answered without an answer |
| `on_flow_failed(callback_context:, error:, workflow:)` | Async or sync | Signal failure. `workflow: nil` = sync failure before workflow existed |
| `on_progress(delta:, callback_context:)` | Async, per checkpoint (debounced) | Live progress update. **Required** when `supports_live_progress?` returns `true` |
| `on_approval_requested` | Async (future) | Post approval prompt |

**Class-level interface:**

| Method | Purpose |
|---|---|
| `self.adapter_key` | Unique string key used for registry lookup and callback context persistence |
| `self.from_callback_context(ctx)` | Factory: reconstruct adapter from persisted callback context for async delivery |
| `self.supports_live_progress?` | Return `true` to opt into `ProgressDeliveryWorker` checkpoint streaming. Adapters that opt in **must** implement `on_progress` |

**Async restoration:** Each adapter declares a unique key for registry lookup
and implements a factory method to reconstruct itself from persisted callback
context. `AdapterRegistry` maps adapter keys to classes; `CallbackWorker` and
`ProgressDeliveryWorker` use it to resolve the correct adapter class at
delivery time.

The base class provides a template method that orchestrates: acknowledgement,
callback context building, composite identity linking, SA project membership,
callback context enrichment, and workflow execution. Callers resolve policy and
build the input; adapters implement delivery; the base class handles shared
mechanism.

**`trigger` vs `with_lifecycle_hooks`:** `Base#trigger` is the full entry
point — it links composite identity, ensures SA membership, then calls
`with_lifecycle_hooks`. `with_lifecycle_hooks` is the pure lifecycle
orchestrator for callers that handle execution themselves (e.g., `@GitLabDuo`
note flows that provision execution outside the adapter). Both paths share the
same `on_request_received → build_callback_context → yield → on_flow_enqueued`
sequence.

### Responsibility split

| Concern | Owner |
|---------|-------|
| Authorization | Caller (surface-specific policy) |
| Service account selection | Caller |
| Flow and version selection | Caller |
| Project selection | Caller |
| Goal building | Caller |
| Build resolved input for adapter | Caller |
| Pre-flight checks (e.g., Slack OAuth linking, license) | Caller (before adapter is involved) |
| Callback context (channel/thread IDs) | Delivery adapter |
| User-facing lifecycle (progress, results, errors) | Delivery adapter |
| Async restoration from callback context | Delivery adapter |
| Live progress opt-in (`supports_live_progress?`) | Delivery adapter |
| Composite identity linking | Base adapter (mechanism) |
| SA project membership | Base adapter (mechanism) |
| Callback context enrichment (adapter key, SA ID, flow ref) | Base adapter (mechanism) |
| Resource translation (Issue → `issue_id`, MR → `merge_request_id`) | Base adapter (mechanism) |
| Workflow execution (`ExecuteWorkflowService`) | Base adapter (mechanism) |
| Final result extraction from checkpoints | `CallbackWorker` |
| Delivery idempotency + backstop retry (`delivered_at`) | `CallbackWorker` |
| Reporting whether delivery actually landed | Delivery adapter (`deliver_result` return value) |
| Checkpoint streaming + cursor management | `ProgressDeliveryWorker` |

This three-layer split — caller, delivery adapter, base adapter — means adding
a new trigger source on an existing channel (e.g., `@GitLabDuo` on GitLab
notes) requires only new caller-side resolution code; the existing delivery
adapter is reused unchanged. Adding a new channel (e.g., Microsoft Teams)
requires a new delivery adapter but no changes to the base adapter or existing
callers.

### Startup time

| Step | Today (large project) | With duo-workspace |
|---|---|---|
| Git clone | Seconds–minutes | Near-instant (empty repo) |
| Docker image | Default, pulled each time | Custom via `agent-config.yml`, cached |
| `duo-cli` install | `npm install` each run (~15s) | Pre-baked into custom image |

Prototyping showed end-to-end response times under 10 seconds with an empty
workspace project. This is acceptable for async messaging. Teams optimize
further by customizing the workspace project (cached images, dedicated runners,
pre-installed tools).

## Pros

- Battle-tested CI/Flows infrastructure — no new execution runtime
- No Workhorse or DWS changes required
- ADR 004 compliant
- Every CI improvement benefits messaging for free
- Adapter pattern cleanly separates surface policy from shared mechanism
- Same architecture handles both external messaging and GitLab-native surfaces
- Workspace project is a natural customization surface (image, skills, secrets)
- Typed adapter contract catches missing fields early
- Checkpoint streaming is live and extends the same architecture additively
  (new EventStore subscriptions, new adapter hooks — no core changes)
- Reply latency is decoupled from CI pipeline finalization: replies ride the
  workflow `:finish` transition instead of waiting on pipeline teardown, while
  the workload event is retained as a delivery backstop

## Cons

- CI startup latency (~10s with empty project) is slower than a direct
  service call, though acceptable for async messaging
- Auto-creating projects and service accounts adds implicit resources to
  namespaces
- Adapter methods run in two contexts — sync (full state) and async (only
  callback context) — requires clear documentation for new adapter authors
- Result delivery now has two possible trigger events, so adapters must report
  delivery success honestly and tolerate at-least-once delivery; the
  `delivered_at` marker is written after success, leaving a narrow window in
  which a crash mid-delivery produces one duplicate reply
- Each new trigger source must implement its own resolution logic (auth, SA,
  flow, project) at the call site, though this is typically straightforward
  code rather than a new class

## Implementation

- [Issue](https://gitlab.com/gitlab-org/gitlab/-/work_items/590434)
- [Reply latency optimization](https://gitlab.com/gitlab-org/gitlab/-/work_items/605913)

### Feature flag

The entire flow is gated behind the
[`slack_duo_agent`](https://gitlab.com/gitlab-org/gitlab/-/work_items/592185)
feature flag (per-user), which already gates the `AppMentionedService`.
