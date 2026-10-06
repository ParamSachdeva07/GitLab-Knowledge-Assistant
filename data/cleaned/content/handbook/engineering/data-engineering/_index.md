---
title: "Data Engineering and Monetization"
description: "Building the unified data foundation, both operational and analytical, that scales GitLab across every deployment model and unlocks intelligent monetization."
---

## Mission

We build the unified data foundation, both operational and analytical, that scales GitLab across every deployment model and unlocks intelligent monetization. By connecting fragmented systems into a seamless, low-touch ecosystem and ensuring zero data issues during migrations and upgrades, we enable customers to adopt new features faster while transforming raw data into leading indicators across customer journeys that accelerate growth & competitive advantage.

## Vision

We envision GitLab to define Developer-Led Economy: A global shift where software developers, empowered by agents and data-driven platforms, are the core drivers of innovation, growth, and competitive advantage—similar to how oil defined industrial power in the 20th century.

## Organization Structure

```mermaid
flowchart LR
    DEAM[Data Engineering and Monetization]
    click DEAM "/handbook/engineering/data-engineering/"

    DEAM --> AN[Analytics]
    click AN "/handbook/engineering/data-engineering/analytics"
    DEAM --> MON[Monetization]
    DEAM --> DE[Database Excellence]
    click DE "/handbook/engineering/data-engineering/database-excellence/"

    AN --> AI[Analytics Instrumentation]
    click AI "/handbook/engineering/data-engineering/analytics/analytics-instrumentation"
    AN --> Optimize
    click Optimize "/handbook/engineering/data-engineering/analytics/optimize"
    AN --> PI[Platform Insights]
    click PI "/handbook/engineering/data-engineering/analytics/platform-insights"

    MON --> Growth
    click Growth "/handbook/engineering/development/growth"
    MON --> MONS[Monetization Section]
    click MONS "/handbook/engineering/development/monetization"
    MON --> Fulfillment
    click Fulfillment "/handbook/engineering/development/fulfillment"

    MONS --> PUR[Purchase]
    MONS --> SUBL[Subscription Lifecycle]
    MONS --> BE[Billing Engine]
    MONS --> MP[Monetization Platform]
    MONS --> OMI[Observability, Monitoring, and Integrations]
    MONS --> COMP[Compliance]

    Fulfillment --> ENT[Entitlements]
    Fulfillment --> SEATM[Seat Management]
    Fulfillment --> UV[Usage Visibility]
    Fulfillment --> CM[Cost Management]

    Growth --> Acquisition
    click Acquisition "/handbook/engineering/development/growth"
    Growth --> Activation
    click Activation "/handbook/engineering/development/growth"
    Growth --> Engagement
    click Engagement "/handbook/engineering/development/growth"

    DE --> DBF[Database Frameworks]
    click DBF "/handbook/engineering/data-engineering/database-excellence/database-frameworks"
    DE --> DBO[Database Operations]
    click DBO "/handbook/engineering/data-engineering/database-excellence/database-operations"
    DE --> SMDX[Self-Managed Database Experience]
    click SMDX "/handbook/engineering/data-engineering/database-excellence/self-managed-database-experience"
```

## How we work

- [Pre-mortems for launches](/handbook/engineering/data-engineering/pre-mortems/): an optional, forty-five-minute practice for surfacing launch-specific risks before the ship date. The launch DRI decides whether to run one.
