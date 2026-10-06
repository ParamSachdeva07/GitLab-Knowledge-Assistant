---
title: "User journeys"
description: "User journeys help GitLab teams understand and optimize the complete experience of customers as they discover, adopt, and integrate our DevSecOps platform to drive both user success and business value."
---

User journey mapping at GitLab provides a strategic framework for teams to understand the complete journey of customers and GitLab users as they discover, evaluate, adopt, and integrate our DevSecOps platform. By systematically mapping these experiences:

- We identify friction points, opportunities for education, and moments that matter most to users.
- We create seamless pathways that increase first orders, accelerate successful onboarding, and strengthen long-term retention across our customer base.

## Key terminology

- **User journey:** A user journey is the complete sequence of experiences, interactions, and touchpoints that a user has with GitLab over time to accomplish specific goals or outcomes. It encompasses the user's progression through various stages and touchpoints relevant to their goals across different stages of the software development lifecycle. The specific details captured (such as emotions, pain points, or granular steps) will vary based on the elevation level of the journey map being created.

- **Golden journey:** A golden journey is the most valuable and strategically important user path through GitLab's platform that maximizes both user success and business value. It represents the ideal, high-frequency route that users take to achieve core outcomes while driving key business metrics such as activation, retention, expansion, and monetization. Golden journeys typically span multiple stages of the software development lifecycle and serve as the foundation for product strategy and cross-functional alignment.

- **Journey map:** A journey map is a visual representation and documentation of a user journey that captures the user's workflow, stages, and key opportunities across different touchpoints. The specific details captured (such as emotions, pain points, or sub-steps) will vary based on the elevation level of the journey map. It serves as a shared artifact for cross-functional teams to understand, analyze, and improve the user experience.

## Journey map elevations

Journey map elevation refers to the different levels of detail and scope at which user journeys can be mapped and analyzed, each serving different strategic and tactical purposes within the organization.

Journey map elevation levels connect and inform each other, with micro-level insights about specific interactions feeding into mid-level understanding of complete workflows, and mid-level findings informing macro-level strategic decisions.

Journey maps can be accessed in this [centralized location in Figma](https://www.figma.com/files/972612628770206748/team/1517620701713485782).

### Macro level

- Purpose: Strategic alignment and ecosystem understanding
- Timeframe: Covers months to years capturing the full customer lifecycle from initial awareness through long-term use/advocacy
- Scope:
  - Focus on high-level phases, major milestones, and business outcomes
  - Show cross-service and cross-channel experiences
  - Identify ecosystem-wide improvement opportunities
- Artifacts: [Figma template](https://www.figma.com/board/CAw05ogtEWiRrhW48Uqt22/Journey-Mapping-Templates?node-id=1-156)

### Mid level

- Purpose: Cross-functional alignment and end-to-end experience optimization
- Timeframe: Covers days to weeks for a specific user goal or service experience
- Scope:
  - Focus on specific user scenario from start to finish
  - Include detailed pain points and emotional journey
  - Show specific touchpoints and channels
  - Identify tactical improvement opportunities
- Artifacts: [Figma template](https://www.figma.com/board/CAw05ogtEWiRrhW48Uqt22/Journey-Mapping-Templates?node-id=1-104)

### Micro level

- Purpose: Interaction optimization and usability improvement
- Timeframe: Covers minutes to hours for specific task completion
- Scope:
  - Focus on granular user flows and micro-interactions
  - Include detailed interface elements and user actions
  - Show moment-by-moment emotions and friction points
  - Identify specific UI/UX improvements and metrics
- Artifacts: [Figma template](https://www.figma.com/board/CAw05ogtEWiRrhW48Uqt22/Journey-Mapping-Templates?node-id=0-1)

## Best practices

The most effective and informative journey mapping goes beyond assumptions to create user experience maps grounded in real data. It balances research depth with practical needs to generate actionable insights.

### Getting started

1. Begin by creating an issue using the [User journey issue template](https://gitlab.com/gitlab-org/gitlab/-/issues/new?description_template=User%20Journey).
    1. Determine who will participate in defining the user journey. You may work async or sync with this team to complete your user journey.
    1. Identify the fundamentals of your journey such as the job performer, [JTBD](/handbook/product/ux/jobs-to-be-done/), and customer segment.
    1. Compile research questions, collect existing data, and determine if additional research is needed.
    1. Map the journey using the [Figjam templates](https://www.figma.com/board/CAw05ogtEWiRrhW48Uqt22/Journey-Mapping-Templates?t=EpYC7EjZOkOQkeUu-6) provided. Review the [journey mapping essentials](#journey-mapping-essentials) section below for steps on how to use the journey map templates.
    1. Create [actionable insight issues](https://gitlab.com/gitlab-org/gitlab/-/issues/new?description_template=Actionable%20Insight%20-%20Product%20change) for the opportunities identified. Review the [action planning and funnel optimization](#action-planning-and-funnel-optimization) section below for best practices.
    1. Share your journey in the [#GitLab-user-journeys (internal)](https://gitlab.enterprise.slack.com/archives/C0927BQATJA) slack channel.

### Journey mapping essentials

1. **Add journey metadata.** Set the stage for the journey by copying necessary content from the user journey issue into the metadata section.
1. **Create the step-by-step workflow.** Document each step users take to accomplish their selected scenario, keeping steps simple (verb + noun) and arranged chronologically from the user's perspective. Prompt for missing steps, alternative paths, and error scenarios to ensure completeness.
1. **Group steps into stages.** Group workflow steps into natural stages with clear, action-oriented names that represent what users are trying to accomplish in each phase.
    - Map user journey stages to funnels that drive first orders (acquisition → trial → purchase), accelerate customer value (onboarding → activation → feature adoption), and enable customer-focused innovation (feedback collection → feature usage → expansion)
1. **Add additional context.** Fill in the remaining table sections, including who's involved, handoffs, insights, and opportunities. These sections differ depending on the journey map elevation level you chose.
1. **Link related journeys.** As applicable, add nested journeys to macro and mid maps and parent journeys to mid and micro maps. Nested journeys provide a deeper dive into a particular step of your journey while a parent journey maps one elevation higher. To add a journey preview in Figjam, copy the Figjam link and paste into your Figjam file.
1. **For micro journeys, add screenshots.** Micro journeys are granular user flows with steps that may be represented by a single screenshot. Include these screenshots for context in your journey map.
1. **For micro and mid journeys, plot the emotional journey.** Map how users feel throughout the journey using emojis to create an emotional curve, then review where the most significant emotional drops occur and how they correlate with pain points. Emotional journeys are omitted from macro maps because the steps are often too high level to capture one emotion at this elevation.
1. **Validate your map.** Review your map with your team stakeholders for further feedback. Cross-check insights across different data sources and test your assumptions with additional research if needed.

### Action planning and funnel optimization

- Ensure each insight translates into an actionable business opportunity. Create an actionable insights issue for each opportunity.
- Prioritize journey improvements based on their direct impact on first-order conversion, time-to-value, and product-market fit signals.
- Collect data from instrumentation or other metrics to show impact, and document improvements.
- Monitor how journey enhancements affect conversion to first orders, reduce time-to-value, and increase adoption of new features
- Assess journey optimization contributions to key business objectives, and share success stories demonstrating ROI through improved first-order conversion, faster customer success, and validated innovation direction

## Research Methodologies

If new research needs to be conducted, select the best approach from below to gather needed data.

### Quantitative methods

**Analytics and behavioral data**

- Track user flows and conversion rates
- Identify drop-off points and completion rates
- Analyze user segments and their different behaviors
- Measure time spent on tasks and interactions

*When to use*: To understand what users are doing and identify patterns at scale

**Surveys**

- Use validated scales like USAT+, CSAT or other metrics
- Ask about specific journey stages and experiences
- Gather feedback from large user samples
- Track satisfaction and sentiment over time

*When to use*: To quantify user satisfaction and validate findings across larger groups, particularly good for high risk/low confidence decisions which affect a large number of users

### Qualitative methods

**User interviews**

- Conduct structured conversations about user experiences
- Ask about motivations, frustrations, and goals
- Explore the "why" behind user behaviors
- Gather detailed stories and context

*When to use*: To understand user motivations and get detailed insights about experiences

**Observation and usability testing**

- Watch users complete tasks in their natural environment
- Identify where users struggle or get confused
- Observe actual behavior vs. what users say they do
- Document contextual factors that influence experience

*When to use*: To see actual user behavior and identify usability issues

**Diary studies**

- Have users document their experiences over time
- Capture experiences that happen across multiple sessions
- Understand how context affects user behavior
- Gather insights about long-term usage patterns

*When to use*: For journeys that span multiple days or weeks, or when you can't observe users directly
