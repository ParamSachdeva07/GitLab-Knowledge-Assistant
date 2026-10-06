---
title: "Frontend Decomposition"
status: proposed
creation-date: "2026-06-12"
authors: ["@ntepluhina", "@xanf", "@slashmanov"]
coach: []
approvers: []
owning-stage: ""
toc_hide: true
---

## Summary

The GitLab frontend is built and shipped as multiple Webpack bundles built simultaneously. This track
modularizes the frontend so that UI modules can be developed, built, tested, and
deployed independently, integrating through a shared shell application and an
explicit module contract — the frontend counterpart to the backend
[bounded contexts](../bounded_contexts.md).

This document shares the
[motivation](../_index.md#motivation),
[agentic imperative](../_index.md#why-now-the-agentic-imperative), and
[goals](../_index.md#goals) of the overall decomposition effort.

## Motivation

GitLab frontend has a set of issues that prevent faster development iterations and better user experience.

### Problems

- **Tight coupling to Rails.** GitLab is a multi-page application where Rails owns routing, page composition, and the template render tree. Integration and E2E tests must run against a full Rails application because there is no standalone frontend to test against. On top of this, ~440 files read `el.dataset` and 77 files read `window.gon` to hydrate Vue apps, with feature flags injected entirely via `window.gon.features` and no API alternative. This coupling slows down feedback loops: every frontend change must be validated through a full-stack pipeline.
- **Frontend masks backend performance problems.** The current Rails app is slow (400-500ms for initial HTML), and frontend architecture is designed around this constraint rather than addressing it. Pages either render partial content server-side so users see "something" before the client app loads, or render entirely on the client. In both cases, expensive data fetching is pushed to the frontend, adding latency on top of the already-slow server response. Secondary page elements compound this: sidebar and Duo Chat ship on every authenticated page, and their rendering cost creates a performance ceiling regardless of how optimized the primary content is. Rapid Diffs, for example, consumes only ~30% of page render time; the rest is secondary elements. A page that should load in 300ms loads in seconds.
- **No CSS architecture.** 36,000 lines of SCSS across 223 files have no isolation, co-location, or ownership. There are no guidelines on how to write proper CSS. Styles live far from the HTML they affect and heavily rely on cascade. Changing any SCSS file forces running all integration tests because the blast radius is unknown. Tailwind is put on top of legacy CSS, increasing complexity and maintenance.
- **No architectural layers.** Frontend code is scattered across `app/assets/javascripts/` with no structural conventions. Anything can import from anything. Specs live separately from the files they test, styles live separately from templates. Practices and patterns are not shared; each new app invents its own structure based on whichever existing app the author happened to look at. Code self-reproduces: bad patterns propagate just as easily as good ones. This also hurts agentic development because agents average across inconsistent approaches and cannot judge which pattern fits a given problem.
- **CI cost and duration.** Frontend predictive test selection exists but is largely ineffective. Most frontend MRs fall back to running the full E2E suite. RSpec system specs have no coverage-based mapping for frontend changes, only static file pattern matching. Fixture generation (8 parallel RSpec jobs) ignores predictive selection entirely.
- **Cross-app coordination.** Inter-app communication relies on three ad-hoc patterns (mitt-based EventHubs, DOM CustomEvents, sharing state via Pinia/Apollo Client cache/Vue reactive variables) with no formal contracts.
- **Bundle size risk for external services.** No module federation or runtime module sharing exists. Each external service (such as frontend island) would ship duplicate copies of Vue, GitLab UI, and Apollo, and we should disallow addition of such services in the monolith.

## Goals

1. **Explicit contracts.** If a relationship between two pieces of code is not traceable by tooling, it does not exist for the purpose of testing, building, or loading. This applies to JS, CSS, data from Rails, and inter-app communication.
2. **Clear guidance for data providers.** Use initial server data only for critical rendering path and to avoid request waterfalls, in any other case prefer calling an API.
3. **CSS ownership.** There should be a very minimal amount of global CSS. CSS must be isolated and co-located with the HTML it affects, making it part of the build graph for page entrypoints.
4. **CI that is both fast and trusted.** - Frontend-only changes should run smallest subset of tests possible to verify possible regressions.

## Workstreams (WIP)

### 1. Modernize the build pipeline

TODO: Enable independent frontend module deployment. Describe the target build
topology, per-module builds, and the deployment model.

### 2. Migrate Webpack 4 → Webpack 5 / Vite and complete Vue 3

TODO: Lay out the migration path from Webpack 4 to Webpack 5 / Vite and the Vue 3
migration this unblocks, including sequencing and risks.

### 3. Define the module contract

TODO: Define how modules manage authorization, user context, and feature flags
across boundaries. This is the frontend equivalent of a package's public
interface.

### 4. Build the supporting infrastructure

TODO: Specify the shell application, the module registry, and the Context
provider API, and how modules register with and integrate through them.

### 5. Frontend LabKit

TODO: Standardize shared libraries and tooling to ensure a consistent user
experience across modules.

## Proof of concepts

Related frontend PoCs already captured in
[Modular Monolith: PoCs](../proof_of_concepts.md):

- [Frontend sorting hat](../proof_of_concepts.md#frontend-sorting-hat)
- [Frontend assets aggregation](../proof_of_concepts.md#frontend-assets-aggregation)

## References

[Vue 3 migration epic](https://gitlab.com/groups/gitlab-org/-/work_items/6252)
