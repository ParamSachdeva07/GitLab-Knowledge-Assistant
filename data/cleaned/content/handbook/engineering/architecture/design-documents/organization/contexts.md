---
title: "Request Context"
description: "Names the three request contexts GitLab has always had — Organization, User, and Nil — as a single model, and how isolation determines which one applies."
owning-stage: "~devops::tenant scale"
group: Organizations
toc_hide: true
---

## What is a context?

A context is a data boundary. It sets what data an execution path can
reach. A path can also have an **anchor** — the entity it names, such
as an Organization or a User. An anchor is not itself a context; see
"Organizations anchor a path," below, for the distinction.

This document describes how the GitLab product resolves context today,
and how Organizations extend that model.

## The three contexts

GitLab has three contexts:

1. **Organization context.** The execution path is bound to one isolated
   Organization.
1. **User context.** The execution path is bound to one User. It reaches
   every Organization that User can reach.
1. **Nil context.** The execution path is bound to nothing. It has no
   Organization and no User.

## The context matrix

Two facts decide the context:

1. Is an Isolated Organization present?
2. Is a User present?

| | No User | User present |
|---|---|---|
| **No organization** | Nil context | User context |
| **Non-isolated organization** | Nil context | User context |
| **Isolated organization** | Organization context | Organization context |

The "No organization" row and the "Non-isolated organization" row are
identical. Isolation is the only fact that changes the answer.

## Examples

Routes are the clearest examples. Some also carry an anchor — the
entity the path names:

| Example route | Context | Anchor |
|---|---|---|
| `/dashboard/...` | User context | None |
| `/explore` | Nil context | None |
| `/o/acme/...`, Acme isolated | Organization context | Acme (Organization) |
| `/o/acme/...`, Acme not isolated, user signed in | User context | Acme (Organization) |
| `/o/acme/...`, Acme not isolated, signed out | Nil context | Acme (Organization) |

The same route, `/o/acme/...`, can carry two different contexts, but
the same anchor. Isolation decides which context applies, not the URL.
See "Organizations anchor a path," below, for why.

Every process resolves to one of these three contexts, not just routes.
The same three apply to background jobs, scheduled tasks, GraphQL
queries, and ActionCable connections.

## One service, more than one context

A service can accept more than one context. It does not need a separate
code path per context. For example, a to-do list service takes a context
as input. Given User context, it returns to-do items from every
Organization. Given Organization context, it returns to-do items from
one Organization.

## Organizations anchor a path. Isolation makes it a boundary

A URL path can be about something without that something being the
request's context. An **anchor** names which entity a path is about —
for example, an Organization, or a User. An anchor does not, by itself,
set a data boundary. Only a context does that.

An anchor is a property of a path, not of every execution path. A
background job or a scheduled task has a context, the same as a route
does, but it has no path to anchor it.

Organizations add a new fact: a URL path can now name an Organization.
On its own, this does not reach the "Isolated organization" row. A path
naming a non-isolated Organization still resolves to User context or
Nil context. This is why the "No organization" and "Non-isolated
organization" rows in the context matrix are identical, and why
`/o/acme/...` can carry two different contexts.

Isolation is the fact that reaches the third row. An isolated
Organization keeps all of its data inside its own boundary. No data
crosses that boundary, in or out. Only then does Organization context
exist for that Organization. Only then do its anchor and its context
become the same thing.

The table above makes the distinction concrete. Neither
`/dashboard/...` nor `/explore` names an entity in the URL, so neither
has an anchor. Only `/o/acme/...` does, which is exactly why its
context can diverge from what it names.

## Isolation removes an Organization from User and Nil context

Isolation is one rule about the Organization boundary: no data crosses
it. It is not a separate rule for User context, and another separate
rule for Nil context. Two facts follow from the one rule:

1. An isolated Organization's Users no longer belong to User context.
   Their identity now belongs to one Organization only.
1. An isolated Organization has no data outside its own boundary. Nil
   context has nothing left to find there.

## Related decisions

- [ADR 016: `organization_id` and Organization-scoped query filtering](decisions/016_user_context.md) decides how this model is encoded today.
