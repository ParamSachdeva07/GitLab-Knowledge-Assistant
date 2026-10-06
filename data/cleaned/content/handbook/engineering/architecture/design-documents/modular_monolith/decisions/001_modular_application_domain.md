---
title: "Modular Monolith ADR 001: Modularize the application domain"
creation-date: "2024-05-07"
authors: [ "@fabiopitino" ]
toc_hide: true
---

## Context

Before we modularize a codebase we first needed to define how we are going to divide it.

## Decision

We start by focusing on the application domain (backend business logic) leaving the
application adapters (Web controllers and views, REST/GraphQL endpoints) outside the
scope of the modularization initially.

The reasons for this are:

1. Code in application adapters may not always align with a specific
   domain. For example: a project settings endpoint or a merge request page contains
   references to many domains.
1. There was a need to run separate Rails nodes for the SaaS architecture using different
   profiles in order to save on memory.
   For example: on SaaS we wanted to be able to spin up more Sidekiq nodes without the need
   to load the whole Rails application. The assumption is that for running Sidekiq we don't
   need ActionCable, REST endpoints, GraphQL mutations or Rails views.
   We only need the application domain and infrastructure code.
   This could still be true even with the introduction of [Cells](https://docs.gitlab.com/ee/architecture/blueprints/cells/index.html) but
   we need to re-evaluate this assumption.
1. Keep the scope and effort smaller. Tackling only domain code is easier to understand than
   the complexity of how to breakdown the application adapters and all their edge cases.

The decision to scope out application adapters is not final and we decided to defer
it to later.

Finally, the infrastructure code containing technical concerns (typically the `lib/`) will
be part of a common "platform" layer that every domain module will depend on in order to function.

The "platform" layer can be broken down into independent libraries extracted as gems.

## Consequences

We focus on modularizing business logic, defining rules and guidelines for engineers.
We can apply the same set of patterns across modules.

## Alternatives

We looked into including application adapters to the modularization effort but noticed that
modularizing adapters is more delicate as we need to preserve user-facing dependencies like routes.
