---
title: "Tracking Critical Experiences"
description: "Critical Experiences are the make-or-break experiences, which we track in GitLab to monitor the quality of our design work in action."
---

### What

This is a comprehensive step-by-step guide on how to identify Critical Experiences in your GitLab product area and establish the process and tools needed to monitor and track such experiences through analytics and visualization.
This guide is built on industry-leading Critical User Journeys framework from Google, established GitLab UX Quality Metrics practices, and GitLab-specific implementation requirements.

### Why

Tracking actual UX Quality through Critical Experiences enables data-driven decision making at GitLab by:

- Bridging the gap between business metrics and pre-release UX Research validation
- Measuring both user perceptions and actual performance of critical workflows
- Focusing team efforts on the user journeys and features that matter most to business outcomes
- Providing objective data to guide product improvements and resource allocation

## Understanding the Framework: Definitions and Relationships

### Concepts Hierarchy

```text
User Experience (Complete product experience)
└── Critical Experiences (Make-or-break moments)
    ├── Critical User Journeys (Linear, sequential workflows)
    └── Critical Features (Key capabilities, non-linear exploration)
```

### User Experience vs. Critical Experience

- User Experience encompasses the complete experience users have when interacting with our product - every touchpoint, interaction, and outcome across their entire relationship with GitLab.
- Critical Experiences are the subset of user experiences that are "make-or-break" for both user success and business outcomes. These are the moments where success or failure dramatically impacts whether users achieve their goals and whether your business objectives are met.

### Two Types of Critical Experiences

Critical experiences can be measured in two fundamentally different ways, depending on how users derive value.

- [Critical User Journeys (CUJs)](https://medium.com/initialized-capital/what-to-do-if-your-product-isnt-growing-7eb9d158fc) are a subset of [user journeys](/handbook/product/ux/user-journeys/). They are linear, sequential workflows with clear start and end points where users follow a defined path to achieve a specific goal. They typically fall into [three categories](https://blog.uxtweak.com/critical-user-journey/): High-Traffic (optimizing core workflows), High-Dollar (improving revenue flows), or OEC/Overall Evaluation Criterion (aligning with primary success metrics). Compared to other user journeys, CUJs usually exhibit a few of the following characteristics:
  - High business impact if they fail
  - Significant user traffic or strategic importance
  - Directly tied to key product value propositions
  - Cross-functional in nature (often span multiple teams/features)
- Critical Features are key product capabilities that enable users to achieve value through non-linear interaction patterns rather than following a prescribed sequence. They can be tied to an embedded UI element, like the Search and Filter bar, or as complex as a Security Posture Dashboard, where users can explore multiple paths from investigating specific vulnerabilities to exporting the report.

|  | **Critical User Journeys** | **Critical Features** |
|---|---|---|
| **Characteristics** | • Linear progression: Users move through defined steps in sequence<br>• Clear success criteria: Specific end goal that defines completion<br>• Task-based: Made up of discrete, essential tasks | • Non-linear usage: Users interact in various ways to derive value<br>• Multiple valid paths: Different users achieve success through different actions<br>• Exploration-based: Value comes from capability access rather than completion |
| **Examples** | • Complete merge request workflow<br>• New user onboarding and first project creation<br>• CI/CD pipeline setup process | • Security dashboard<br>• Repository analytics<br>• Advanced search and filtering capabilities |
| **Best measured through** | • Funnel analysis, task completion rates | • Feature adoption rates, usage depth, engagement patterns |

### UX Quality Metrics vs Service Level Indicators vs Business Outcomes

Important Distinction: We track Critical Experiences by focusing on UX Quality Metrics, which are different from GitLab's established [User Experience SLI framework](/handbook/engineering/architecture/design-documents/user_experience_slis/), and the business outcomes. UX Quality Metrics are the user-facing indicators of whether our product is delivering value, while SLIs measure whether our technical systems can support that delivery.

|  | **Business Outcomes (Ours)** | **Business Outcomes (Customers)** | **UX Quality Metrics** | **GitLab's Covered Experience Service Level Indicators (SLIs)** |
|---|---|---|---|---|
| **Purpose** | Measure GitLab's commercial success | Measure customer value achievement | Measure user experience success and journey completion | Measure technical service performance and reliability |
| **Scope** | Company-level revenue and growth metrics | Customer-level value and outcome metrics | User-level metrics (task completion, satisfaction, journey success) | System-level metrics (response times, uptime, error rates) |
| **Audience** | Executive leadership, Sales, Marketing | Customer Success, Account Management | Product, UX, Design teams | Engineering, Infrastructure, Site Reliability teams |
| **Example** | "$120M Ultimate ARR", "40% Ultimate adoption" | "50% reduction in security vulnerabilities", "30% faster incident response" | "95% of users successfully complete merge request creation" | "Web service responds within 200ms for 99.9% of requests" |

## Step-by-Step Implementation Guide

This is a collaborative process involving UX and cross-functional teams. We've outlined recommended ownership for each step below.

### Step 1 - Identify Your Critical Experiences

Owner: UX, Support: Product

#### Use these three dimensions to evaluate potential Critical Experiences

|  |  |
|---|---|
| **Business Criticality**: Does success/failure of this experience dramatically affect business outcomes? | Scoring Framework (1-5 scale):<br>• 5 - Critical: Direct revenue impact, strategic product differentiator, affects core business metrics<br>• 4 - High: Strong connection to key business objectives, important for competitive position<br>• 3 - Medium: Moderate business connection, supports strategic goals<br>• 2 - Low: Indirect business impact, nice-to-have optimization<br>• 1 - Minimal: Little business impact, not strategically important |
| **User Impact**: How important is this experience to user success? | Scoring Framework (1-5 scale):<br>• 5 - Critical: Large user base, no alternative workflows, high consequence of failure<br>• 4 - High: Important user segment, limited alternatives, significant user frustration if broken<br>• 3 - Medium: Decent user volume, some alternative paths available<br>• 2 - Low: Smaller user segment, multiple alternative workflows exist<br>• 1 - Minimal: Very small user base, many alternatives available |
| **Measurability**: Can you effectively track and optimize this experience? | Scoring Framework (1-5 scale):<br>• 5 - Excellent: Clear start/end events, all interactions trackable, simple analytics implementation<br>• 4 - Good: Most interactions trackable, moderate complexity, some custom instrumentation needed<br>• 3 - Fair: Key interactions trackable, requires significant instrumentation work<br>• 2 - Poor: Limited tracking capability, complex implementation required<br>• 1 - Not Feasible: Cannot meaningfully track or measure this experience |

#### Proposed Process

Brainstorm possible critical experience candidates, and assign them into one of two categories:

- User Journeys: Experiences in which users follow a relatively predictable sequence of steps to achieve a goal, and failure at any step prevents goal achievement
  - Key product capabilities: Experiences where users derive value through feature adoption, and the success is about accessing and utilizing capabilities effectively.
  - Score Each Experience: Rate 1-5 on Business Criticality, User Impact, and Measurability
- Calculate Priority Score: Multiply the three scores (max score = 125)
- Select Top 3-5: Start with highest-scoring experiences (e.g. scoring 60+)
- Validate with Stakeholders: Confirm alignment with product strategy

Pro Tip: Limit yourself to 3-5 Critical Experiences maximum. Better to deeply understand a few critical experiences than to spread efforts too thin.

### Step 2 - Define Indicators for Instrumentation

Owner: Product, Support: UX

#### For Critical User Journeys

- Map the Complete Flow: Document every task users perform from start to finish, following GitLab’s [User Journey Mapping](/handbook/product/ux/user-journeys/) best practices
- Double-check the boundaries of each step: Make sure each step represents a clear task or interaction within the CUJ. If the task or interaction fails, the CUJ fails.
  - Example Breakdown: Critical Journey: "New user creates first merge request"
  - Tasks:
    - Complete repository setup (or access existing repo)
    - Create and switch to feature branch
    - Make code changes using Web IDE
    - Commit changes with meaningful message
    - Navigate to merge request creation
    - Fill out merge request details
    - Submit merge request successfully
- Identify Indicators for Journey Progress or Feature Adoption: For each task, define:
  - Start Event: When does the task begin?
  - Success Event: What indicates task completion?
  - Failure Events: What are the different failure modes?
  - Context Data: What additional information helps analysis?
- Check for the Need of Self-Reported Data: Discuss whether self-reported data Is needed. And if so, whether we need to capture them in-app. For example, to capture the outcome quality of Duo, we need to capture the user's feedback in-app with voting up or down.

#### For Critical Features

- Identify sub-features to measure:
  - Example Breakdown: Critical Feature: “Security Posture Dashboard”
  - Sub features:
    - Interactive chart
    - Nested vulnerability list
    - Export report
- Identify Success Indicators: For each feature and sub feature, define:
  - Feature Discovery Indicator: How users find and access this capability?
  - Adoption / Usage Depth Indicator: Actions showing extensive feature exploration.
  - Failure Events: What are the different failure modes?
  - Context Data: What additional information helps analysis?
- Check for the Need of Self-Reported Data: Discuss whether self-reported data Is needed. And if so, whether we need to capture them in-app.

### Step 3 - Set Up Instrumentation and Data Visualization

Owner: Product, Support: UX, Engineering, Product Data Insights

#### Phase 1 - Audit Existing Tracking

Owner: Product

- Check Current Instrumentation:
  - Review [the GitLab metrics dictionary](https://metrics.gitlab.com/?status=active) for existing events
  - Verify [Snowplow](https://chromewebstore.google.com/detail/snowplow-inspector/maplkdomeamdlngconidoefjpogkmljm?hl=en&pli=1) tracking coverage for your critical tasks ([demo](https://gitlab.zoom.us/rec/share/6YsjPVjWZDn3T-qziXEqFDJdqPP6B8_ILHPqzdmIXzWTRaGMzAa7z6D1A4A319fq.QWnJfu2TTxKbZ1EF))
  - Assess data quality and completeness
  - Identify gaps in current tracking
- Inventory Existing Dashboards:
  - Review current Tableau dashboards for related metrics in your product area (via [Atlan](http://gitlab.atlan.com))
  - Document what's already available vs. what's needed

#### Phase 2 - Implement Missing Tracking

Owner: Engineering

- Fill in the gaps:
  - Create instrumentation requirements for missing events
  - Follow GitLab's instrumentation guidelines
  - Implement event tracking for each critical task
- Coordinate with [Product Data Insights Team](/handbook/product/groups/product-analysis/):
  - Share your Critical Journey framework and task breakdown
  - Work with [the Product Analyst in your area](/handbook/product/groups/product-analysis/#team-members) on event and variable setup
  - Plan implementation timeline and testing approach
  - Set up review processes

#### Phase 3 - Set Up Self-Reported Metrics Collection If Needed

Owner: UX

- In-Product Feedback:
  - Decide when and how in-product feedback should be captured.
  - Design lightweight feedback UI for self-reported data
  - Coordinate with the UX Research Operations team to avoid over-surveying users if applicable.
- Standalone Research Studies:
  - Partner with UX Research team to design scheduled survey
  - Agree on research cadence (monthly/quarterly)
  - Define target user segments for feedback collection
  - Coordinate with the UX Research Operations team to avoid over-surveying users if applicable.
  - Set up longitudinal tracking for user experience trends

#### Phase 4 - Build UX Quality Dashboards

Owner: Product Data Insights

- Design, Build and Iterate the Dashboards:
  - Design dashboard mockups aligned with your UX quality metrics
  - Follow [the issue intake process](/handbook/product/groups/product-analysis/#issue-intake) to collaborate on the dashboard
  - Create drill-down capabilities for deeper analysis where needed
  - Establish access permissions for relevant stakeholders
  - Test dashboard functionality with real data
- Recommended Dashboard Requirements:
  - For Critical User Journeys:
    - Journey Overview: High-level success rates for each CUJ
    - Step Breakdown: Detailed metrics for each critical step within journeys
    - Funnel Analysis: Drop-off points and conversion rates between steps
  - For Critical Features:
    - Feature Adoption: Percentage of eligible users actively using each feature
    - Capability Utilization: How extensively users explore feature capabilities
    - Engagement Patterns: Usage frequency, session depth, and interaction sequences
  - For All Critical Experiences:
    - Trend Analysis: Performance over time with comparative periods
    - Segmentation: Performance by user type, experience level, feature flags, etc.
    - Alert Thresholds: Visual indicators for metric degradation and escalation triggers
    - Drill-down Capabilities: Detailed views for root cause analysis when issues arise
- Recommended Dashboard Design Principles:
  - Keep the most critical metrics prominent and easy to find
  - Use consistent color coding and visualization patterns
  - Include target benchmarks and acceptable ranges
  - Provide context for metric interpretation
  - Enable export functionality for reporting if possible

### Step 4 - Agree on Quality Targets and Monitoring Cadence

Owner: Product, Support: UX, Engineering, Product Data Insights

- Agree on realistic targets and escalation process:
  - Acknowledge targets are context sensitive, even for the same UX Quality Metrics.
  - Decide on your target by referring to the UX Quality Metrics page (coming up)
  - Create escalation procedures for different severity levels
  - Define clear ownership and response protocols
  - Test alert systems to ensure reliability
- Recommended Review Processes:
  - Weekly: Review dashboard for trends and anomalies
  - Monthly: Deep-dive analysis of journey performance
  - Quarterly: Strategic review of journey prioritization and targets

## Provide feedback on this guide

Is this guide working for your team in GitLab? Leave your comment in [the feedback issue](https://gitlab.com/gitlab-org/ux-research/-/issues/3642). We'd love to hear from you!
