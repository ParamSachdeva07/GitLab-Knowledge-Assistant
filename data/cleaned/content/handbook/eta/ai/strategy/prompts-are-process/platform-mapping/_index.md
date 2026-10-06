---
title: "Governance posture: platform mapping"
description: "How our guided-creation posture maps to the admin settings in Claude and Glean, and where each platform can and cannot enforce function-scoping."
---

This is the companion to [Prompts are Process](../), which sets out the policy: personal use is free, and promotion to a canonical, shared version goes through an owner and a review. That page is deliberately tool-agnostic. This one is the wiring diagram: it maps our posture to the admin settings across our Claude surfaces (Chat, Cowork and Code) and Glean. The split is about tool-agnostic versus tool-specific, not about anything being hidden.

Enterprise AI (ETA) owns this configuration. Platform and tooling choices are the Hub's decision right, not the function's.

## The posture in one line

Guided creation: anyone can build and experiment; promotion to a canonical, shared version is owned and reviewed through one of the [three scopes](../#three-places-ownership-can-sit) (function-scoped, repo-scoped, company-wide).

## Mapping the posture to platform settings

| Posture intent | Claude (Chat, Cowork, Code) | Glean |
|---|---|---|
| People can build their own skills/agents | User-created skills enabled | "Can create agents" (Default Member permission, default **On**) |
| People can share peer-to-peer | Skill sharing enabled | "Can share agents with individual teammates" (default **On**) |
| Publishing to everyone is gated, not automatic | Share-with-organisation off; promotion to org goes through the owner and review | "Can publish agents" (default **Off**) and "Can share agents with the entire company" (default **Off**) |
| Distribution of approved work to a team | Packaged and scoped to the relevant group (e.g. a team plugin) | Share the agent with a Department or identity-provider group (Google/Entra); promote it by marking it Verified / company-branded in the Agent Library; scope Library categories by Department |
| Heavier control for sensitive cases | Tighten that surface towards admin-curated (user creation off) | Tighten the Default Member permissions; control reach with the per-agent access tiers (Viewer / Editor / Owner) and the underlying document permissions |

Glean's controls live in the Admin Console under **Users → Default Member permissions** (the create/share/publish toggles) and under **Agents** (the Library, verification and group-sharing). Claude's org-level toggles live in its org/admin settings and apply across the Claude surfaces.

Three things worth drawing out:

1. **Glean ships guided creation as its default.** Out of the box, default members can create agents and share them with individual teammates, but cannot publish or share with the whole company. That is exactly our posture, with no reconfiguration needed. The work is in governing promotion, not in locking creation down.
1. **Approved publishers are people, not a new admin club.** In Glean, company-wide reach is gated to users with publish rights plus the Agent Moderator and Department Agent Moderator roles, who verify and brand agents as official. The **Department Agent Moderator** is the closest platform analogue to the ATO: they can see, edit, verify and govern agents created by members of their department, and nobody else's. Agent Moderator and Admin are the Hub. So the "who approves" question maps onto the same people as the rest of the model: ATO for a function, Hub for company-wide.
1. **Claude Code is the exception that proves the model.** Its skills live in the repo (`.claude/skills/`), versioned in git and reviewed by merge request. That is repo-scoped ownership enforced by the tooling itself, with no org toggle involved. When a process is genuinely tied to a repo, this is the cleanest home.
1. **The [AI marketplace](https://gitlab.com/gitlab-com/marketplace) resources are company-wide.** Each resource should be self-contained and include everything needed to use it, rather than pointing users to external or access-restricted resources.

## Where the platform can enforce scope, and where it can't

The create / publish / share-to-company *policy* is org-wide in both tools: you set the default member permissions once, for everyone. You cannot, through those toggles alone, say "Marketing may publish but Sales may not" (Glean's per-department moderator roles are the lever for that kind of difference, not the default-permission toggles).

The real difference shows up when you try to keep a *specific* shared asset inside one function:

- **Claude cannot do this today.** Connectors are org-wide on or off and cannot be scoped per team, and skill-sharing is org-level. So keeping a function's skill inside that function is an **ownership control, not a technical one**: it is held by the ATO and the function exec deciding what becomes canonical, and by where the canonical version is stored and reviewed.
- **Glean can.** A given agent can be shared with a Department or an identity-provider group, the Agent Library can be scoped by Department, and a Department Agent Moderator governs per-function. So in Glean, function-scoping has genuine platform support behind it.

Either way the principle leads and the platform follows: ownership decides what becomes canonical, and the platform varies in how much it helps enforce the boundary. The practical caution: do not assume Claude keeps a function's skills inside that function. It doesn't, and there what holds the line is the owner. Glean gives you more to work with, but the owner still decides what gets promoted.

## How the three scopes land in practice

1. **Repo-scoped** is the one scope where enforcement *is* technical, and cleanly so. Ownership is CODEOWNERS, versioning is git, review is the merge request, distribution is `git pull`. This is the Claude Code pattern above, and it remains the tidiest expression of the posture.
1. **Function-scoped** is enforced by ownership in Claude and supported by department/group scoping in Glean. The ATO is the approver, mirrored in Glean by the Department Agent Moderator role.
1. **Company-wide** is where org-publishing rights actually get used, by the approved publishers (central functions, with ETA as interim home), under commit-and-iterate. The Hub is the approver, mirrored in Glean by the Agent Moderator and Admin roles.

## Open items to confirm

1. Confirm in our own Glean tenant that the Default Member permissions still sit at the guided-creation defaults (create on, share-with-teammate on, publish off, share-with-company off), and decide who we appoint as Department Agent Moderators as each spoke goes live.
1. Decide whether we want a documented "tighten" profile for sensitive or regulated surfaces, or handle it case by case.
1. Decide whether group-scoped packaging in Claude is worth using now, or only once we have more than one or two live spokes.

## Sources

Glean documentation, as of March–April 2026: [Managing agent library](https://docs.glean.com/administration/managing-agents/managing-agent-library), [Managing agent access](https://docs.glean.com/administration/managing-agents/agent-access), [Sharing agents with identity provider groups](https://docs.glean.com/administration/managing-agents/agent-group-sharing).
