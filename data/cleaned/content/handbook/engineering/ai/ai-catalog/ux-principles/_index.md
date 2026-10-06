---
title: AI Catalog — Design Principles & Vision
description: "Design principles and vision for the AI Catalog, defining what the catalog is, what it is not, and the principles that guide every design and engineering decision."
---

## Purpose

This document defines what the AI Catalog is, what it is not, and the principles that should guide every design and engineering decision made within it. It is intended as a reference point for anyone contributing to the catalog to align on intent before making tradeoffs.

---

## What the Catalog is

The AI Catalog is the central place where users discover, evaluate, configure, and enable AI-powered objects on GitLab. It is the layer that connects the builders who create these objects with the users and teams who want to put them to work.

The catalog serves four distinct jobs:

| Job | What it means |
|---|---|
| Discover | Users can find what exists across the differing catalog item types, without already knowing what to look for |
| Evaluate | Users can assess whether an item is right for their use case before enabling it by using trust signals, usage data, and available configuration options |
| Configure | Users with the right permissions can configure item scope and settings within the projects where items run |
| Enable | Users can activate items, making them available to run on their projects |

### What lives in the catalog

The catalog contains three object types. Each has its own detail page and its own role in how agents and flows are built and run:

1. Agents - autonomous AI entities with a defined role, tools, and a system prompt. They can be chatted with or added to flows, and they produce focused outputs.
1. Flows - orchestrators that coordinate multiple agents, passing context between them. They execute when triggered and can interact with other GitLab features.
1. MCPs (Model Context Protocol servers) - external services an agent can read from or write to. They extend what an agent can reach.

---

## What the Catalog is not

### Not a settings panel

The catalog is not a general administrative settings area. It is where users discover, evaluate, enable, and manage AI-powered items. Administrative settings for GitLab instances and groups live elsewhere.

### Not a documentation hub

The catalog shows enough information to make an enable decision. It links to documentation where relevant, but it does not replace or replicate docs. Detailed reference material lives elsewhere.

### Not a monitoring dashboard

Usage metrics and run data appear in the catalog to support evaluation - not as a primary observability tool. Users who need deep operational visibility should go to Sessions or dedicated observability tools.

---

## Design Principles

These principles apply to every design and engineering decision made within the catalog. If a proposed change conflicts with a principle, the conflict should be discussed and resolved as a team.

### 1. Discoverability is a primary concern

- The catalog must be reachable and legible before a user has decided to look for it - discovery is a distinct design problem from evaluation, not a subset of it
- The catalog must have relevant, high-quality items before promoting them proactively - promoting without quality reads as spam, not discovery
- Empty or sparse catalog views should prioritize helping users understand what exists and how to contribute, not artificially fill space
- Success here is measured by whether users who could benefit from an existing item actually find and use it - not just by whether search works for users who already know what they want

### 2. Evaluation before enablement

The catalog exists to help users make a good enable decision, not to make enabling as fast as possible. Every page should answer 'should I use this?' before it answers 'how do I use this?'

- The first question a user has is 'what does this do?' - helping users understand an item's purpose and behavior comes before any trust signal
- Trust signals (who built it, what it accesses, how it performs) must be visible before the enable action
- Configuration details are secondary to evaluation signals - they support the decision, they don't lead it
- The enable action should feel deliberate, not incidental

### 3. Transparency over polish

Users trust what they can inspect. The catalog should make it easy to see what an item does, what it can access, and what happens when it runs - without requiring elevated permissions or navigating away.

- System prompts, tool lists, and data access scope should be visible by default on detail pages
- Usage and performance data (runs, success rate, scopes enabled) should be visible as primary signals
- Users may expect to see certain data. If we hide that data, we must explain why.
- Where AI Catalog items consume metered resources such as credits or compute, consumption should be visible

### 4. Terminology carries weight

Every label, section header, and descriptor in the AI Catalog is an opportunity to calibrate or confuse users, since they are often already familiar with terminology from other platforms. The AI Catalog is often their first contact with DAP's conceptual model, so we must be thoughtful with our terminology. For canonical definitions of DAP terms, refer to the [DAP Glossary](https://docs.gitlab.com/development/ai_features/glossary/).

- Labels should be accompanied by short descriptors wherever the term could be misread
- 'Flow', 'Agent', 'Trigger', 'MCP', and 'Skill' should never appear as bare labels without context nearby
- The terms 'workflow' and 'user flow' should not be used within the AI Catalog context - they will be confused with GitLab Flows
- 'Flow' should only ever refer to GitLab's Flow object - any other use of the word should be avoided

### 5. Scope is always explicit

The AI Catalog is exposed in three areas of GitLab: the Explore area, and in the Groups and Projects users are a member of. AI Catalog features should be explicit about the scope the user is impacting, such as when enabling an item in a project.

- Sometimes there are technical and security requirements that make usability more challenging for users. These constraints should be communicated from a user's perspective as close to the interaction site as possible

### 6. Signal density over decoration

The catalog audience is builders. The page should be dense with useful signal and sparse with everything else.

- Status indicators should be ambient - present when needed, invisible when not (e.g. a 'last run: 2 mins ago' badge when an agent is active, hidden when it has never run)
- Empty states should be informative - '0 sessions' is useful because it confirms the section exists and tracking is working; omitting the section entirely implies nothing is being tracked

### 7. Shared accountability is a design concern

The catalog should expose the full provenance chain so accountability is legible to all parties.

- Who built it, who manages it, where it is enabled, and what it can access should all be visible
- Enablement should make the scope of responsibility clear - enabling at group level has different implications than enabling at project level
- Audit and access information should be accessible to the relevant role, not just the builder

### 8. Building and maintaining agents is a team activity, not a solo one

The catalog's 'configure' job assumes items are maintained over time by more than one person. This has been implicit in the catalog's design so far and should be made explicit.

- Ownership and edit permissions should support multiple named collaborators per agent or flow, not a single owner
- Version history and change attribution should be visible to all collaborators, not just the original builder
- The catalog should make it clear who else can edit or maintain an item.
