---
title: "UX Quality Metrics Framework"
description: "A framework defining what to measure and how to measure to assess the UX quality of concepts, designs and in-app experiences."
---

Last updated: 2026-01-22

Find your current stage, identify which metrics matter most for your decision, then select the appropriate research method.

## 1. What is UX Quality?

UX quality is the degree to which a product solves a real user problem, fits naturally into their workflow, and lets them complete their goals efficiently and confidently — while remaining easy to learn, easy to find, consistent, and satisfying to use over time.

## 2. Why Have a UX Quality Framework?

A shared UX quality framework creates a common language between Research, Product Design, and Product Management to assess and improve product quality throughout development. This framework helps teams make informed decisions with clear, measurable quality signals at each stage, and:

- **Unify metrics** that track against the "definition of good" and desired user and product outcomes
- **Track improvement** over time with consistent metrics
- **Balance speed and quality** by knowing which metrics matter most at each stage

## 3. What's in This Document

This guide covers:

- **Understanding metric types** (Behavioral vs. Attitudinal, and when to use each)
- **The three-stage framework** with specific metrics and research methods for each:
  - Concepts stage: Validate ideas before investing in design
  - Designs stage: Test usability before investing in development
  - Live stage: Monitor satisfaction and performance after launch
- **Practical guidance** for integrating quality measurement into your workflow

## 4. Understanding Metric Types

UX quality can be measured through two complementary lenses:

### Behavioral vs. Attitudinal Metrics

| **Type** | **Definition** | **When Available** | **Examples** |
|----------|----------------|-------------------|--------------|
| **Behavioral** | What users actually **do** -- observable actions and outcomes | Designs stage onward (requires testable prototype or live product) | Task completion rate, time on task, error rates, first-click accuracy, feature adoption |
| **Attitudinal** | What users **think** and **feel** -- perceptions and opinions | All stages (can measure on concepts, designs, or live products) | Satisfaction, perceived efficiency, value-fit, ease of use, desirability |

**Why both matter:** Behavioral metrics show what's actually happening, while attitudinal metrics explain why it's happening and help in predicting future behavior. For example, users might complete a task (behavioral success), but find it frustrating (attitudinal failure), signaling they'll avoid using it in the future.

**Stage availability:**

- **Concepts stage:** Attitudinal only (nothing exists to interact with yet)
- **Designs stage:** Both attitudinal and behavioral (can test with prototypes)
- **Live stage:** Both attitudinal and behavioral (full product in use)

### Objective vs. Subjective Data Sources

Within these metric types, you'll collect both objective and subjective data:

- **Objective data:** Measured independently of user opinion (e.g., system logs showing task completion, analytics showing time on task, technical performance metrics)
- **Subjective data:** Based on user perception (e.g., satisfaction ratings, perceived efficiency, reported ease of use)

Some metrics can be measured both ways. For example:

- **Value-fit** can be subjective ("Do users *say* this solves a meaningful problem?") or objective ("Does this concept map to a documented Job-to-be-Done in our research?")
- **Efficiency** can be subjective ("Do users *perceive* this as faster?") or objective ("Did task completion time actually decrease?")

Both sources are valuable. Subjective data helps you understand user experience and predict behavior; objective data validates whether your solution delivers on its promise.

## 5. The Framework: Three Stages of Product Development

### Stage 1: Concepts

Validate whether to build this before investing in detailed design. Test rough ideas, sketches, or descriptions---not polished designs.

#### UX Quality Metrics (All Attitudinal)

| **Metric** | **Type** | **Definition** | **Why it matters** | **Example script** |
|------------|----------|----------------|-------------------|-------------------|
| **Value-fit 🔴** | Attitudinal | Does this solve a meaningful problem for users? | If users don't see value, they won't adopt it regardless of design quality. | **Subjective:** "On a scale of 1-5, how well does this concept solve a meaningful problem for you?" (1=Not at all, 5=Extremely well)<br><br>**Objective:** Does this concept map to a documented Job-to-be-Done or pain point from prior research? |
| **Workflow-fit 🔴** | Attitudinal | Can users see how this fits into their current process? | Reveals integration challenges early---users won't adopt if they can't envision using it daily. | "On a scale of 1-5, how easily can you see this fitting into your current workflow?" (1=Can't see it fitting at all, 5=Fits perfectly) |
| **Understandability 🔴** | Attitudinal | Do users grasp what this concept does? | Depends on concept maturity. Confusion about basic value means concept needs refinement. | "On a scale of 1-5, how clearly do you understand what this concept does?" (1=Very unclear, 5=Very clear)<br><br>Follow-up: "In your own words, what does this concept do?" |

🔴 = Must measure for all concepts

#### Research Methods

Test concepts as soon as you have a rough description or sketch. Coordinate with UX Research to run the appropriate method for your needs. Re-test after major pivots.

- [Rapid Validations](/handbook/upstream-studios/experience-research/rapid-validations/) for quick turn around on 1-2 ideas - 2 weeks turnaround time
- Concept interviews for deep dives - 3-4 weeks
- Desirability studies, e.g. Kano for assessing 3-5 ideas - 2-3 weeks

#### Proceed to Designs When Both Conditions Are Met

- All metrics are ≥ 4.0/5.0
- **All critical user concerns** from qualitative feedback have mitigation plans

**Note:** These thresholds are proposed starting points. Validate against other data sources if available and adjust based on what correlates with successful launches.

### Stage 2: Designs

Validate how to build this before investing in development. Test with higher-fidelity mockups or prototypes that users can interact with.

#### UX Quality Metrics (Attitudinal + Behavioral)

| **Metric** | **Type** | **Definition** | **Why it matters** | **Example script** |
|------------|----------|----------------|-------------------|-------------------|
| **Task completion rate 🔴** | Behavioral | Can users successfully complete key tasks in the prototype? | <90% task success = critical issues causing user frustration post-launch.<br><br>Ref [1](https://maze.co/collections/reporting-analysis/measure-usability-metrics/), [2](https://www.awa-digital.com/blog/usability-testing-metrics/), [3](https://medium.com/@claus.nisslmueller/task-success-rate-in-ux-how-to-use-the-simplest-metric-in-a-serious-way-34177fede27f). | Observe during usability test: "Please [complete specific task]." Record: Success / Failure<br><br>Calculate: (# successful completions / # attempts) × 100 |
| **Perceived efficiency 🔴** | Attitudinal | Will this save users time compared to their current approach? | Early signal of workflow improvement. Same construct measured again post-launch. | "On a scale of 1-5, how much time would this save you compared to what you currently do to [achieve this goal]?" (1=Would take longer, 3=About the same, 5=Much faster) |
| **Overall satisfaction** | Attitudinal | What's the general user sentiment toward this design? | Leading indicator of post-launch satisfaction. Catches issues metrics alone might miss. | "On a scale of 1-5, how satisfied are you with this design overall?" (1=Very dissatisfied, 5=Very satisfied)<br><br>Follow-up: "Why did you give that rating?" |

🔴 = Must measure for all designs

#### Research Methods

Test designs once you have a clickable prototype. Coordinate with UX Research to run the appropriate method for your needs. Re-test after significant design changes. Plan 1-2 rounds of iteration based on findings.

- [Rapid Validations](/handbook/upstream-studios/experience-research/rapid-validations/) for quick turn around on 1-2 designs - 2 weeks turnaround time
- Moderated usability testing for deeper dives - 3-4 weeks
- [Unmoderated usability testing](/handbook/upstream-studios/experience-research/unmoderated-testing/) for self-explanatory designs - 1-2 weeks (can self-serve with tools)
- [Heuristic evaluation](/handbook/product/ux/heuristics/) / [UX Scorecards](/handbook/product/ux/ux-scorecards/) for speed and when lack of access to users - varies (can be done by PD/Research)

#### Proceed to Development When Both Conditions Are Met

- All metrics are ≥ 4.0/5.0
- **All critical user concerns** from qualitative feedback have mitigation plans

Note: [Industry benchmark](https://www.nngroup.com/articles/success-rate-the-simplest-usability-metric/) is set at 77% for first attempts on new interfaces; 90%+ is excellent.

**Note:** If you don't instrument for analytics now, you can't measure behavioral metrics post-launch. Work with Product Management and Engineering to identify which events to track. See [Tracking Critical Experiences](/handbook/product/ux/tracking-critical-experiences/) for instrumentation guidance.

### Stage 3: Live / Post-Launch

Validate that you built the right thing well and monitor quality over time. Real users are now using your product in production.

#### UX Quality Metrics (Attitudinal + Behavioral)

Metric tiers for B2B systems:

- Core attitudinal metrics (measure for any features and the overall experience): e.g. User Satisfaction Score, Perceived efficiency, Navigation & discoverability, Learnability
  - They are particularly useful to measure UX quality when the task results are non-deterministic, e.g. AI generated content which can look good to some but not others.
- Contextual (measure based on experience type): e.g. Funnel adoption vs. abandonment, Error rate, Task completion rate, Feature adoption rate

##### Core attitudinal metrics

| **Metric** | **Definition** | **Why it matters** | **Example script** | **Definition of good** |
|------------|----------------|-------------------|-------------------|----------------------|
| User Satisfaction Score 🔴 | How satisfied are users with the product overall? | Satisfaction ties directly to retention | "How satisfied are you with [product/feature]?" (1=Very dissatisfied, 2=Dissatisfied, 3=Neutral, 4=Satisfied, 5=Very satisfied) | Excellent: ≥ 90% positive scores<br><br>Good: ≥ 80%<br><br>Needs improvement: <70% |
| Perceived efficiency 🔴 | Does the product save users time in their real workflow? | Critical for B2B productivity tools. Same construct as Designs stage, now measured post-launch. | "How much time does [feature] save you compared to how you currently achieve [this outcome/goal]?" (1=Takes longer, 3=About the same, 5=Much faster)<br><br>"GitLab enables me to work efficiently" (1=Strongly Disagree; 2=Disagree; 3=Neither agree nor disagree; 4=Agree; 5=Strongly Agree) | Excellent: ≥ 4<br><br>Good: ≥ 3.5<br><br>Needs improvement: < 3 |
| Navigation & discoverability 🔴 | Can users find features when they need them? | If users can't find features, they can't use them - directly impacts adoption. | Subjective: "How easy is it to find [what] in [where]?" (1=Very difficult, 5=Very easy)<br><br>Behavioral: Feature usage analytics, search behavior, help doc usage (see [Tracking Critical Experiences](/handbook/product/ux/tracking-critical-experiences/)) | Excellent: ≥ 4<br><br>Good: ≥ 3.5<br><br>Needs improvement: < 3 |
| Learnability 🔴 | How quickly can new users become productive? | Faster onboarding = faster value = better retention. | Subjective: "How easy was it to learn to use [product/feature]?" (1=Very difficult, 5=Very easy)<br><br>Behavioral: Time to first value, feature adoption curve (see [Tracking Critical Experiences](/handbook/product/ux/tracking-critical-experiences/)) | Excellent: ≥ 4<br><br>Good: ≥ 3.5<br><br>Needs improvement: < 3 |
| Perceived Usefulness | How do users evaluate the match between their needs and what the product delivers? | Users won't adopt the product if it doesn't solve their problems. | "GitLab's capabilities meet my requirements." (1=Strongly Disagree; 2=Disagree; 3=Neither agree nor disagree; 4=Agree; 5=Strongly Agree) | Excellent: ≥ 4<br><br>Good: ≥ 3.5<br><br>Needs improvement: < 3 |
| General Usability / Ease of Use | How easily users can use the product to accomplish their goals? | An easy-to-use product supports user adoption and ongoing engagement. | "GitLab is easy to use." (1=Strongly Disagree; 2=Disagree; 3=Neither agree nor disagree; 4=Agree; 5=Strongly Agree) | Excellent: ≥ 4<br><br>Good: ≥ 3.5<br><br>Needs improvement: < 3 |
| Cognitive Load | How mentally demanding it is to use the product? | High complexity and visual overwhelm frustrate users and prevent them from working efficiently. | "GitLab is unnecessarily complex." (Perceived Complexity) / "The GitLab interface is visually overwhelming." (Visual Overwhelm) | Excellent: ≥ 4<br>Good: ≥ 3.5<br>Needs improvement: < 3 |
| Dependability | Can users rely on the product to work consistently? | A product that is unavailable, slow, error-prone, or unresponsive disrupts workflows and damages user trust. | Subjective : "GitLab is available when I need to use it." (System Availability) / "GitLab runs without significant wait times." (System Performance) / "GitLab works without errors." (System Reliability)/ "GitLab's interface elements respond as intended when I click on them." (Interface Reliability)<br><br>(1=Strongly Disagree; 2=Disagree; 3=Neither agree nor disagree; 4=Agree; 5=Strongly Agree) | Excellent: ≥ 4<br>Good: ≥ 3.5<br>Needs improvement: < 3 |
| System Integration | How well different elements work together as a unified whole (both within GitLab and between GitLab and other tools)? | Poor integration between product components and external tools disrupts user workflows and causes friction. | Subjective : "Different parts of GitLab work together smoothly." (Internal Integration) / "GitLab works seamlessly with other tools." (External Integration)<br><br>(1=Strongly Disagree; 2=Disagree; 3=Neither agree nor disagree; 4=Agree; 5=Strongly Agree) | Excellent: ≥ 4<br>Good: ≥ 3.5<br>Needs improvement: < 3 |
| Accessibility | Can all users, despite any accessibility needs, use the product effectively? | Accessibility barriers prevent users with accessibility needs from using the product effectively, limiting adoption and market reach. | Subjective : I do not encounter accessibility issues in GitLab (related to vision, hearing, physical, speech, or cognitive needs). (1=Strongly Disagree; 2=Disagree; 3=Neither agree nor disagree; 4=Agree; 5=Strongly Agree) | Excellent: ≥ 4<br><br>Good: ≥ 3.5<br><br>Needs improvement: < 3 |
| Visual Appeal | How visually attractive do users find the product interface? | A visually appealing interface creates a positive user experience and contributes to product perception. | "The GitLab interface is visually appealing." (1=Strongly Disagree; 2=Disagree; 3=Neither agree nor disagree; 4=Agree; 5=Strongly Agree) | Excellent: ≥ 4<br><br>Good: ≥ 3.5<br><br>Needs improvement: < 3 |
| Consistency | Is the design consistent across different parts of the product? | Inconsistency disrupts user workflows and creates friction by making the product harder to predict and use. | "There is too much inconsistency in GitLab." (1=Strongly Disagree; 2=Disagree; 3=Neither agree nor disagree; 4=Agree; 5=Strongly Agree) | Excellent: ≥ 4<br><br>Good: ≥ 3.5<br><br>Needs improvement: < 3 |

*For more inspiration on metrics for AI, see [this handbook page](/handbook/upstream-studios/experience-research/research-in-the-ai-space/)*

🔴 = Must measure for all features

Priority for B2B systems:

1. User Satisfaction Score (most important as it predicts retention)
2. Perceived efficiency (critical for B2B productivity tools)
3. Navigation & discoverability (if users can't find features, they can't use them)
4. Learnability (faster onboarding = faster value = better retention)
5. All others: Measure based on feature type and strategic priorities

##### Research methods for core attitudinal metrics

Coordinate with UX Research to run the appropriate method for your needs.

- [USAT+ Survey](/handbook/product/ux/performance-indicators/usat-plus/) for overall product perception - quarterly turnover time (managed by UX Research)
- Follow-up interviews - 2-3 weeks (for example: you can contact users who opted in via USAT+)
- [Longitudinal studies](/handbook/upstream-studios/experience-research/longitudinal-studies/) - 4-12 weeks

##### Contextual metrics

| **Metric** | **Type** | **Definition** | **Why it matters** | **Definition of good** |
|------------|----------|----------------|-------------------|----------------------|
| Task completion rate | Behavioral | Percentage of users who successfully complete a task without unrecoverable errors | Core usability indicator - shows whether users can accomplish their goals | Excellent: ≥ 95% completion rate<br><br>Good: ≥ 90%<br>Acceptable: ≥ 85%<br><br>Needs improvement: < 85% |
| Error rate | Behavioral | Percentage of user interactions that result in errors (system errors, validation errors, failed actions).<br><br>Note they can encounter errors while still succeed in the task | High error rates frustrate users and signal UX or technical issues | Excellent: ≤ 0.5% of all interactions result in errors<br><br>Good: ≤ 1%<br><br>Acceptable: ≤ 2%<br><br>Needs improvement: > 2% |
| Error recovery rate | Behavioral | Percentage of users who encounter an error but successfully recover and complete their task | Shows resilience of the UX - good error handling prevents task abandonment | Excellent: ≥ 90% of users who hit errors recover<br><br>Good: ≥ 80%<br><br>Acceptable: ≥ 70%<br><br>Needs improvement: < 70% |
| Funnel adoption vs. Funnel abandonment | Behavioral | Percentage of users who complete a multi-step flow vs. drop off at each stage | Identifies friction points in critical workflows; high abandonment = revenue/value loss | Excellent: ≥ 80% complete full funnel<br><br>Good: ≥ 70%<br><br>Acceptable: ≥ 60%<br><br>Needs improvement: < 60%<br><br>(Note: Benchmarks vary by funnel complexity) |
| Feature adoption rate | Behavioral | Percentage of eligible users who use a feature at least once within a defined timeframe (typically 30-90 days post-launch) | Measures whether users discover and try new features; low adoption = wasted investment | Context dependent - benchmark against historical data and set feature-specific goals based on target audience, feature type, and business priority |
| Feature engagement depth | Behavioral | Frequency of feature use by active users (e.g., daily, weekly, monthly active users) | Shows feature stickiness and value; high depth = feature is integral to workflows | Context dependent - benchmark against historical data and set feature-specific goals based on intended use frequency |
| Feature engagement width | Behavioral | Average number of distinct features used per user within a timeframe | Indicates product stickiness and comprehensive value delivery; higher width = better retention | Context dependent - benchmark against historical data. Note: Higher width generally correlates with retention but varies by product complexity |
| UX bugs | Behavioral | Unexpected and unintended behavior that is detrimental to the user experience. | [UX bugs](/handbook/product-development/how-we-work/issue-triage/#ux-bugs) indicate the quality of the feature. | See [issue severity](/handbook/product-development/how-we-work/issue-triage/#severity) for details. |

**Notes**

- Select the metrics that are best applicable to your experiences.
- Calibrate all thresholds to your product's baseline data
- Longer/more complex funnels naturally have higher abandonment
- Adoption and engagement metrics are context dependent---set feature-specific goals

##### Research methods for contextual metrics

Though user research can be arranged to capture contextual metrics, the best approach would be in-app analytics, which you can work with Data/Engineering teams on. See [Tracking Critical Experiences](/handbook/product/ux/tracking-critical-experiences/) for details.

## 5. Putting It Into Practice

### Common Pitfalls to Avoid

❌ "We'll test it after we build it" → Test concepts and designs early. It's 10x cheaper to fix a concept than a shipped feature.

❌ "We don't have time for research" → Rapids takes 2 weeks. Fixing issues post-launch takes months and damages user trust.

❌ "Our analytics will tell us everything" → Analytics show what users do, but not why. You need both behavioral and attitudinal data.

❌ "We'll instrument analytics later" → If you don't plan instrumentation during development, you can't measure quality post-launch.

❌ "One perfect score means we're done" → UX quality requires monitoring over time. User needs and competitive context evolve.

### Trade-offs and Conflicts

What if metrics conflict? (e.g., high task completion but low satisfaction)

- Prioritize based on stage and strategic goals
- Investigate qualitative data to understand why metrics diverge
- For B2B systems, task completion usually takes priority (users need to get work done), but sustained low satisfaction and perceived efficiency may signal future churn

What if we can't meet all thresholds?

- Distinguish between must-have and should-have metrics
- Consider partial rollout or beta to gather more data
- Document known issues and plan improvements for next iteration

What if we're running out of time?

- Don't skip Concepts stage---it's your cheapest insurance against building the wrong thing
- Consider reducing scope to test core flows only in Designs stage
- Never skip instrumentation---you'll need it to validate post-launch

### Questions or feedback on this framework?

[Link to feedback issue](https://gitlab.com/gitlab-org/ux-research/-/issues/3728)
