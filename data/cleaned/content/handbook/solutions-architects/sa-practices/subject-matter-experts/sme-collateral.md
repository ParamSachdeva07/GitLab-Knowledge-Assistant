---
title: SME Collateral and Resources

description: Maintaining Collateral for each SME Area

---

## SME Content and Collateral (TBD)

\*NOTE: Currently the CSM SMEs have collated resources and materials for each SME Area. They are maintained in Highspot at [CS SME Hub of content](https://gitlab.highspot.com/items/667095b95cc9b08c87d40b68?lfrm=srp.0).

This is [description of the CS SME program](https://gitlab.com/gitlab-com/customer-success/subject-matter-experts/cs-subject-matter-experts/-/tree/main) taking the lead on the gathering of collateral for each SME Area

To effectively organize and scale SME knowledge, we can implement the following structure:

1. Discovery Questions
   - Develop a comprehensive list of discovery questions for each SME area
   - Categorize questions by topic, complexity, and customer segment
   - Regularly update and refine questions based on customer interactions

2. Frequently Asked Questions (FAQs)
   - Compile FAQs for each SME domain
   - Provide clear, concise answers with relevant examples
   - Include links to additional resources or documentation

3. Standard Demos
   - Create a library of standardized demos for common use cases
   - Ensure demos are easily customizable for specific customer needs
   - Maintain version control and update demos regularly

4. Knowledge Base
   - Develop a centralized repository for SME knowledge
   - Organize content by topic, product area, and difficulty level
   - Include best practices, troubleshooting guides, and case studies

5. Learning Paths
   - Design structured learning paths for each SME area
   - Include recommended resources, training materials, and hands-on exercises
   - Define milestones and assessments to track progress

6. Collaboration Tools
   - Implement tools for SMEs to share knowledge and collaborate
   - Set up regular knowledge-sharing sessions and workshops
   - Encourage cross-functional collaboration between SMEs and other teams

7. Mentorship Program
   - Establish a mentorship program pairing experienced SMEs with aspiring experts
   - Define clear goals and expectations for mentors and mentees
   - Track progress and provide feedback on mentorship relationships

8. Continuous Improvement
   - Implement a feedback loop to gather insights from SAs and customers
   - Regularly review and update SME content based on feedback and industry trends
   - Measure the effectiveness of SME resources and adjust strategies accordingly

By implementing this structure, we can effectively scale SME knowledge, provide clear paths for skill development, and ensure consistent, high-quality support for customers across all SME areas.

The CS org has already started on content gathering, and creation  of content.  They have been meeting in Pods to accomplish this.

Here is the HighSpot page for the [CS SME Hub of content](https://gitlab.highspot.com/items/667095b95cc9b08c87d40b68?lfrm=srp.0).  Here is the [CS SME Charter](https://gitlab.com/gitlab-com/customer-success/subject-matter-experts/cs-subject-matter-experts) that talks about solving the problem of version controlled enablement content.

How can SAs help:  We need to also have a process to scale the SME knowledge beyond the SMEs, for example: creating discovery questions, creating frequently asked questions by customers per and creating or using some standard demos..

How can Enablement Help: We can approach enablement to structure the content so that if someone wants to become a SME there is a path. This is a long term outcome.

The  [Technical Skills Exchange initiative](/handbook/solutions-architects/sa-practices/subject-matter-experts/sme-cadences/#sme-tech-skills) can be utilized to that effect

### AI / Duo Agent Platform (DAP) — SA Visibility Dashboards

These dashboards provide SAs with visibility into customer Duo and DAP usage, adoption, and engagement. Use them for customer health checks, POV tracking, success plans, and QBR preparation.

#### Usage Billing Analytics

{{% alert title="Draft dashboard" color="info" %}}This workbook is under active development by the Product Data Insights team. Views and metrics may change. See [gitlab-data/product-analytics#3227](https://gitlab.com/gitlab-data/product-analytics/-/issues/3227) for status.{{% /alert %}}

Workbook: [Usage Billing Analytics](https://10az.online.tableau.com/#/site/gitlab/workbooks/3888582/views)

| Dashboard | Purpose | Link |
|-----------|---------|------|
| Duo KPI Dashboard | Key performance indicators for Duo adoption | [Duo KPI Dashboard](https://10az.online.tableau.com/#/site/gitlab/views/UsageBillingAnalytics_17685202519710/DuoKPIDashboard?:iid=2) |
| Consumption Deep Dive Metrics | Detailed credit consumption breakdown | [Consumption Deep Dive Metrics](https://10az.online.tableau.com/#/site/gitlab/views/UsageBillingAnalytics_17685202519710/ConsumptionDeepDiveMetrics?:iid=3) |
| Customer Report Dashboard | Per-customer consumption reporting | [Customer Report Dashboard](https://10az.online.tableau.com/#/site/gitlab/views/UsageBillingAnalytics_17685202519710/CustomerReportDashboard?:iid=4) |

#### DAP Usage & Engagement

| Dashboard | Purpose | Link |
|-----------|---------|------|
| Duo Daily Usage | Daily DAP usage trends | [Duo Daily Usage](https://10az.online.tableau.com/#/site/gitlab/views/DAPUsage/DuoDailyUsage?:iid=1) |
| Agent Success Metrics | Agent task completion rates, success/failure breakdown | [Agent Success Metrics](https://10az.online.tableau.com/#/site/gitlab/views/AgentUsageEngagement/AgentSuccessMetrics?:iid=2) |
| Agent Engagement Trends | Usage trends, adoption curves, engagement patterns | [Agent Engagement Trends](https://10az.online.tableau.com/#/site/gitlab/views/AgentUsageEngagement/AgentEngagementTrends?:iid=1) |

#### DAP Monetization Metrics

Workbook: [DAP Monetization Metrics](https://10az.online.tableau.com/#/site/gitlab/workbooks/3489989/views)

| Dashboard | Purpose | Link |
|-----------|---------|------|
| DAP Monetization Insights | Credit consumption per agent type, cost trends | [DAP Monetization Insights](https://10az.online.tableau.com/#/site/gitlab/views/DuoAgentPlatformMonetizationMetrics/DuoAgentPlatformMonetizationInsights?:iid=2) |
| Full Report Dashboard | Comprehensive DAP monetization report | [Full Report Dashboard](https://10az.online.tableau.com/#/site/gitlab/views/DuoAgentPlatformMonetizationMetrics/FullReportDashboard?:iid=2) |
| Token Consumption Metrics | Token-level consumption analysis | [Token Consumption Metrics](https://10az.online.tableau.com/#/site/gitlab/views/DuoAgentPlatformMonetizationMetrics/TokenConsumptionMetrics?:iid=1) |

#### AI Gateway Reporting

| Dashboard | Purpose | Link |
|-----------|---------|------|
| AI Gateway Overview | AI Gateway request volume, latency, error rates | [AI Gateway Overview](https://10az.online.tableau.com/#/site/gitlab/views/AIGatewayReporting/Overview?:iid=1) |

#### Duo Subscription Utilization

Workbook: [Duo Subscription Utilization](https://10az.online.tableau.com/#/site/gitlab/workbooks/2484649/views)

| Dashboard | Purpose | Link |
|-----------|---------|------|
| Duo Subscription Utilization | Seat usage, activation rates, subscription health | [Duo Subscription Utilization](https://10az.online.tableau.com/#/site/gitlab/views/DuoProSubscriptionUtilization/DuoSubscriptionUtilization?:iid=2) |
| Tier Enabled Duo Core Utilization | Duo Core feature utilization by tier | [Tier Enabled Duo Core Utilization](https://10az.online.tableau.com/#/site/gitlab/views/DuoProSubscriptionUtilization/TierEnabledDuoCoreUtilization?:iid=3) |
| Duo Subscription Account Report | Per-account subscription report | [Duo Subscription Account Report](https://10az.online.tableau.com/#/site/gitlab/views/DuoProSubscriptionUtilization/DuoProSubscriptionUtilizationReport?:iid=1) |

#### Duo Feedback

| Dashboard | Purpose | Link |
|-----------|---------|------|
| Duo Feedback Dashboard | User feedback, satisfaction signals, feature requests | [Duo Feedback Dashboard](https://10az.online.tableau.com/#/site/gitlab/views/DuoFeedbackDashboard/DuoFeedbackDashboard?:iid=1) |

#### Product Roadmap Reference

- [DAP Product Roadmap Q1 FY27](https://gitlab.com/groups/gitlab-operating-model/-/work_items/41) — Company Priority 3: AI Modernization Journey. Key results: pooled credits NARR, 400K agentic chat LLM requests, 250K custom agent requests, 200K external agent requests, governance implementation.
- **DAP Trial Playbook:** See the [DAP Customer Trial process](/handbook/solutions-architects/playbooks/pov/ai/#dap-customer-trial) for the full 8-step evaluation workflow.

### StackOverflow (TBD)

Make sure that whoever is designated as an SME is listed as such in Stack Overflow. This will ensure that questions tagged with those relevant topics get routed to the right folks.

It should be part of the regular rigor that SMEs review questions in Slack (specifically #cs-questions) and Stack Overflow to ensure the answers are upvoted and relevant as new changes/features get released.

We can also use Stack Overflow for FAQs and Articles related to those particular areas.
