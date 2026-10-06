---
title: Artificial Intelligence POV Scope and Acceptance
description: Artifical Intelligence POV Scope and Acceptance
---

Other AI Resources: [Lab](https://gitlab.com/gitlab-learn-labs/sample-projects/tanuki-racing) | *Demo* | *Guided Trial* | **POV** | *Education Services* | [Professional Services](https://about.gitlab.com/services/#advisory-services)

## AI POV best practices

We need to proactively identify languages, testing questions and teams with them. Below are the best practices to review before the start of the POV:

- Small team size
- Languages which has a lot of open source contributions like Java, Python
- Proactive testing scenario
- Time boxed hands on POV with active guidance throughout
- Conduct a pre survey before the POV and post survey after the POV to gauge the success
- Verify which IDEs and versions will be used for the POV
- Prior to the POV, host office hours to assist in installing the GitLab Duo plugin in IDEs
- Create a collaboration project to keep track of issues and resolutions during office hours
- Provide the team lead and users with the [Getting Started with GitLab Duo Enterprise document](https://docs.google.com/document/d/1aK8IJMiYCs-7isZ-Ek-FnolY29_WJdexG_x1tkcLGs4/edit?tab=t.0) (internal only - can be distributed to the team lead) for all AI evaluations
- Provide the GitLab University - [Duo Learning Track](https://university.gitlab.com/pages/ai#developers-quick) , and this document with [quick start links](https://docs.google.com/document/d/14j5H5IlySAhJ0EUpcrpJy3jwQxTdmw5c1uLKVlymEGI/edit?tab=t.0) to various Duo topics
- Kick-off the POV with a workshop for a headstart. The schedule could be the following, for a 2-hour session
  - 5 min - welcome participants
  - 5 min - introduction
  - 20 min discussion about Gen-AI for development, and pitch of GitLab Duo
  - 1h20 min workshop
  - 10 min conclusion and next steps
- Make it as easy as possible for participants to experiment with the features, using the following recommendations and adjusting to the context:
  - Onboarding process. Minimize the number of steps needed for a participant to opt into the POV.
    - Example process:
      - Survey to gather participants' name, role, GitLab account
      - Participant is enrolled in the POV instance, and given access to the right projects
      - Participant is invited to POV meetings
      - In the meeting invitation, participant finds instructions to access the POV instance, link to pre-POV survey, link to instructions to go through the workshops asynchronously, etc.
  - Make sure that the POV environment is made available to participants for the kick-off session, even if this session doesn't include a workshop.
    Some participants may want to start experimenting with the solution during the kick-off or right after.
  - Give simple and clear instructions to ask for help:
    - Where to create an issue and who to tag
    - Invitation to Office Hours
- Bias for guided, hands-on activities. See POV activities for inspiration
- When POV goals are to surface quantitative indicators of improvements brought by AI-powered features, it is tempting to adopt a comparative study approach for the workshops or hackathons described above.
- It consists of assigning the same task to two groups of developers. One group works "as usual," while the other is allowed to use AI-powered features. Optionally, a second assignment is given, and the two groups are switched around.
- A drawback of this approach is that working without AI-powered features isn't very fun. Considering how precious it is in enterprise settings to have time dedicated to this kind of initiative, spending it on "working as usual" may not be ideal.
- As an alternative, ask participants to log, for each task
  - Before: a time estimate if they were working as usual
  - After: the time it actually took, with the help of AI-powered features.
  - After: include qualitative feedback about the comfort of working, quality of software, etc.
- Familiarize yourself with [Duo Chat best practices](https://about.gitlab.com/blog/2024/04/02/10-best-practices-for-using-ai-powered-gitlab-duo-chat/) and [Duo Code Suggestions top tips](https://about.gitlab.com/blog/2024/06/11/top-tips-for-efficient-ai-powered-code-suggestions-with-gitlab-duo/). There are some great tips and tricks in this blog to assist with integrating Duo Chat and Code Suggestions into a customer's workflow. Check the documentation for more practical [GitLab Duo uses case](https://docs.gitlab.com/ee/user/gitlab_duo/use_cases.html).

## Pre-requisites

We need to make sure the customer has gone through the AI hands-on [workshop](/handbook/solutions-architects/tools-and-resources/workshop/) to have a great experience with AI POV. We also recommend building a [Customer Success Plan](/handbook/solutions-architects/processes/customer-success-plan/) and getting agreement from your customer before the POV start.

Ensure all [SA Rules of Engagement](/handbook/solutions-architects/rules-of-engagement/) prerequisites are met (Stage 2+, MEDDPPICC populated, Champion engaged). For general POV guidance including qualification criteria, SFDC tracking, and approval processes, see the [POV parent page](/handbook/solutions-architects/playbooks/pov/).

### Input to the POV

- Example Customer [template1](https://docs.google.com/presentation/d/1m1u65qa8oj0_hHTklnhWAjyHxR8euQ14/edit?usp=sharing&ouid=113388956697042742039&rtpof=true&sd=true)
- Example Customer [template2](https://drive.google.com/file/d/1vAOW0Kko24ASeN7XDMnkHMWfGc57R9cw/view)
- Streamline your POV by adopting [3 Goals in 30 Days](https://docs.google.com/presentation/d/1PIDwrVSywtz82OANmRpO3rhRPKzh64CoLWf1xqGsBEQ/edit#slide=id.g237d0ad8d2e_0_1287)

### Setting up the POV instance

Set-up the POV instance with your customer's POV lead or technical counterpart.

- Getting GitLab Duo trial Licenses
  - For existing GitLab customers, [follow the steps here to request Duo trail](https://docs.gitlab.com/ee/subscriptions/subscription-add-ons.html#start-gitlab-duo-pro-trial)
  - For prospects, request trial licenses [here](https://about.gitlab.com/solutions/gitlab-duo-pro/sales/?toggle=gitlab-duo-pro)
- Setup the patricipant environment, their IDE and do a trial run. Below are a few links and documents to help.
  - GitLab University - [Duo Learning Track](https://university.gitlab.com/pages/ai)
  - Getting Started Documents - [Getting Started with GitLab Duo Enterprise](https://docs.google.com/document/d/1aK8IJMiYCs-7isZ-Ek-FnolY29_WJdexG_x1tkcLGs4/edit?tab=t.0)
  - [Quick Start - Duo links](https://docs.google.com/document/d/14j5H5IlySAhJ0EUpcrpJy3jwQxTdmw5c1uLKVlymEGI/edit?tab=t.0)
- Import the public [AI POV Plan project template](https://gitlab.com/gitlab-com/account-management/templates/ai-pov-plan) at the root of the POV group, namespace, or instance.
  - It is intended to be used as a central point of entry for participants to make all useful information and resources easily discoverable for testers.
- Follow the checklist provided in the REAMDE.md to customize this project
- Configurations needed in the instance or group are better done by the customer's POV lead
  - This way they have ownership and understanding of the configuration
  - It is also on them to review the terms of experimental features to be turned on, and GitLab's [testing agreement](/handbook/legal/testing-agreement/)
- Test AI-powered features in various settings, before undertaking any POV activity. Troubleshoot or adjust POV activities accordingly.
  - within the customer's network or not
  - with a VPN enabled or not
  - with different IDEs including the Web IDE

## POV Activities

The following are different workshop formats to pick and combine in order to facilitate and lead the POV.
Examples of POV activity timelines:

- Customer A
  - Week 1: Kick-off and standard guided workshop
  - Week 2: Custom workshop on IDE integration setups and IDE features
  - Week 4: Standard guided workshop for a second set of users
- Customer B
  - Week 1: Kick-off and standard guided workshop
  - Week 3: Custom workshop on improving quality and generating documentation
  - Week 4: Coaching the POV leads to prepare an internal demo
  - Week 6: AI Hackathon, in three separate sessions, with a measurement of productivity improvement (see [Comparative Study](#comparative-study))

### Standard AI Workshop

The standard AI workshop leverages the [Tanuki Racing](https://gitlab.com/gitlab-learn-labs/sample-projects/tanuki-racing) project from [GitLab Learn Labs](https://gitlab.com/gitlab-learn-labs).

- Under [Courses / Workshops / AI](https://gitlab.com/gitlab-learn-labs/sample-projects/tanuki-racing/-/tree/main/Courses/Workshops/AI?ref_type=heads) are the workshop instructions

Depending on the availability of the SA in charge, this workshop is either delivered

- In a synchronous, instructor-lead session, for optimal engagement
- In a self-paced, asynchronous setting, for low-touch engagements, or for participants unable to attend the sync session
  - Instructions in the workshop project are intended to suit this case.
  - A recording of the session may also be made available.

### Custom AI Workshop

This approach consists of customizing the standard AI workshop to a customer's specific needs or context.

- Consider exploring specific workflows that matter to the customer.
- Make sure to thoroughly test the workflow before the workshop, and adjust prompts and instructions as needed
- Consider using a different project to support the workshop. Either an open source project, or a customer project could be used to focus on a specific framework or language
  - If a customer project is used, first validate whether or not it is allowed to be uploaded to the POV instance or namespace.

It requires more involvement, both from GitLab's side and from the customer side. Validate this with the POV lead before starting the initiative.
It is also likely to yield higher engagement and enthusiasm from the participants. And to give decision makers a more accurate understanding of the value they can expect, including quantitative indicators.

### AI-powered Hackathon

This approach goes one step further in terms of involvement, both for preparation, and for the workshops themselves. Workshops are usually 1.5-2.5 hours long, whereas hackathons typically last half a day to a full day.

Participants form teams, and use AI-powered features at will for a given period of time to deliver a prototype.

A hackathon project is prepared to give participants

- Instructions and links to useful resources
- A project boilerplate, helper functions, evaluation functions. Consider having multiple versions for multiple use cases or languages.
- A GitLab issue, issue template, to log time estimates and results. The project's readme may also be used for this purpose

The scope could be

- The same for all teams. Eg "Flight tracking app" or "Competitive quiz app"
- To be chosen within a set of assignments.
- Free: develop whatever you want in the allocated time. Give some example use cases.
- Consider public coding challenges, which are good candidates for hackathon assignments, as they usually give
  - instructions and boilerplates for teams to use.
  - clear success/failure or performance for each tasks, when there is a possibility to submit a solution and get instantaneous feedback.
  - time estimates or public leaderboards for each tasks, which can be useful to estimate the value of AI-powered features
- A caveat to public coding challenges is that they could sometimes be considered too far from the reality of enterprise work. To be discussed  ahead of time with POV leads.

Additional guidance:

- Be mindful that a hackathon setting could be intimidating or stressful to participants because of:
  - Time pressure
  - Working on unfamiliar tasks
  - Working outside of their usual tooling
  - Starting from scratch, which may not be frequent in enterprise settings
  - Feeling exposed to coworkers or managers judgment
  - Discovering new AI-powered features
- To mitigate this discomfort:
  - Set expectations: participants are not expected to complete all tasks, or deliver perfect software in such a short timeframe
  - Set rules of conduct for participants, about openness, kindness, communication
  - Prepare resources and tools in the hackathon project
- To make the most out of the allocated time for the hackathon, consider forming teams before the workshop.

### Comparative study

When POV goals are to surface quantitative indicators of improvements brought by AI-powered features, it is tempting to adopt a comparative study approach for the workshops or hackathons described above.
It consists of assigning the same task to two groups of developers. One group works "as usual", while the other is allowed to use AI-powered features. Optionnally, a second assignment is given, and the two groups are switched around.

- A drawback of this approach is that working without AI-powered features isn't very fun. Considering how precious it is in enterprise settings to have time dedicated to this kind of initiatives, spending it on "working as usual" may not be ideal.
- As an alternative, ask participants to log, for each task
  - Before: a time estimate if they were working as usual
  - After: the time it actually took, with the help of AI-powered features.
  - After: include qualitative feedback about comfort of working, quality of software, etc.

### Guided Workshop best practices

Before the workshop

- See setup of the POV instance
- Have a dry run, to surface and tackle any issues with the GitLab instance, or videoconference: screen share, breakout rooms, etc.

During the workshop

- Lead the workshop with a co-host from GitLab, who is familiar with the workshop.
  - The co-host can answer questions in the chat, and help some of the students troubleshoot without slowing everyone down.
  - Useful resources include our docs' troubleshooting section, Field FAQ, AI SME FAQ
- Use video conference chat messages to gather feedback with emojis, in order to engage the audience and follow students' progression along workshop steps
  - Ex: "What's your favorite IDE?" "What's the language or framework you use the most", "Workshop project created?", "Pipeline triggered?", "Vulnerability fixed?", etc.
- Keep some time at the end to gather feedback, and prepare next steps.
  - Questions like "What features do you wish to test further?" will hopefully keep students involved after the workshop.

After the workshop

- Ask the customer POV lead about the feedback they had internally
- Give feedback about the workshop, in the appropriate GitLab project or Slack channel

### DAP Customer Trial

{{% alert title="Credit-based trials are different" color="warning" %}}
DAP customer trials use **evaluation credits**, not seat-based licenses like Duo Pro/Enterprise POVs. Every credit represents real dollars GitLab is investing in the customer relationship. There is no "free" trial — be strategic, disciplined, and highly engaged to maximize ROI for both GitLab and the customer.
{{% /alert %}}

**Before starting any DAP trial, every SA must:**

1. Review this playbook in full
2. Conduct thorough [discovery](#dap-trial-discovery-questions) to identify high-value use cases
3. Complete the DAP Trial Evaluation Plan with the customer (required for credit approval)

DAP customer trials are only available to **existing customers** with an active subscription. Prospects cannot receive evaluation credits ([see tracking work item](https://gitlab.com/groups/gitlab-org/-/work_items/20168)) but can access a self-serve Ultimate trial with included credits.

#### Trial eligibility quick reference

Before requesting evaluation credits, verify the customer's eligibility path:

| Customer Type | Trial Path | Key Constraints |
|---|---|---|
| **Prospect / Free (SaaS)** | Self-serve Ultimate trial + 24 credits/user | 100 user cap, 30 days, no extensions |
| **Prospect / Free (Self-Managed)** | Self-serve Ultimate trial + 24 credits/user | Requires 18.9+, no user cap on Self-Managed |
| **Existing Paid (Premium/Ultimate)** | Evaluation credits through [Fulfillment request](https://gitlab.com/gitlab-org/fulfillment/meta/-/issues/new?description_template=trial_credit_requests&issue%5Btitle%5D=%5BA-XXXXXX%5D%20%5BSubscription%20Name%5D,%20%5BCustomer%20Name%5D,%20%5BTotal%20Credits%20Requested%5D,%20%5BDate%20Requested%20For%5D) | One-time only, must not be opted into on-demand billing, cloud licensing required |
| **Dedicated** | Same as existing paid | Must be on **18.8.4+** — wait until Feb 18 maintenance window before requesting trials |
| **Air-gapped / Offline License** | NOT eligible for credit trials | Seat-based DAP self-hosted through $0 Deal Desk order + leadership approval |
| **OSS / EDU / Startup** | NOT eligible | — |
| **Dedicated for Government** | NOT eligible | — |
| **GitLab Duo with Amazon Q** | NOT eligible | — |

{{% alert title="Dedicated customers: timing matters" color="warning" %}}
Dedicated instances receive updates on a delayed schedule. Ensure your Dedicated customer is on **18.8.4+** before allocating trial credits. The February 18 maintenance window is the earliest most Dedicated instances will receive the required patch. Confirm patch status before submitting a credit request.
{{% /alert %}}

{{% alert title="Credits are one-time only" color="warning" %}}
Evaluation credits can only be issued **once** per subscription — no extensions, no re-issuing. In specific circumstances, a second trial may be approved with CXO approval. Ensure the customer is fully prepared and has completed the [DAP Trial Evaluation Plan](#dap-trial-evaluation-plan) before requesting credits.
{{% /alert %}}

#### Key constraints

| Constraint | Limit | Rationale |
|------------|-------|-----------|
| Trial duration | 30 days | Enough to demonstrate value, short enough to maintain momentum |
| Maximum users | 100 | More than this is unmanageable and risks "unused credits" perception |
| Credits per user | 100 | Sufficient to demonstrate value without overcommitment |

#### Credit consumption reality check

There is no fixed "credits per task" — consumption varies by flow complexity, number of tool calls, and the LLM model used. Set this expectation with customers early.

This [Metric: LLM Call Efficiency Dashboard](https://10az.online.tableau.com/#/site/gitlab/views/DuoAgentPlatformMonetizationMetrics/DuoAgentPlatformMonetizationInsights?:iid=1) allows LLM calls per task to be seen by selecting Flow Type and then looking at Average, which will give you an approximation of GitLab Credit consumption if you take that LLM Call count and divide it by the [credit multipliers](https://docs.gitlab.com/subscriptions/gitlab_credits/#models).

These are medians — individual invocations can vary significantly based on prompt complexity, context size, and model used.

The above dashboard's Tokens per Flow Histogram allows you to dig into credit consumption averages based on token consumption per flow.

**Key billing behaviors:**

- **Failed requests do NOT consume credits** — whether in trials or normal usage
- **Billing latency: ~90 minutes** — there is up to a 90-minute delay between credit consumption and access cutoff. During this window, flows may complete even after credits are depleted
- If the customer has **not** accepted on-demand billing, they will **not** be charged for small overages during this latency period
- If the customer **has** accepted on-demand billing, they will be charged for any overage beyond included credits, including during the latency window
- GitLab is working to reduce this latency over time

**Credit consumption hierarchy** (consumed in this order):

1. **Included Credits** — per-user basis, refresh monthly (Premium: 12/user, Ultimate: 24/user)
2. **Monthly Commitment Pool** — shared org-wide, refresh monthly
3. **Monthly Credit Waivers** — free buffer, shared, refresh monthly (if applicable)
4. **On-Demand Credits** — pay-as-you-go at $1/credit

Direct customers to the [Prompt Library](https://about.gitlab.com/gitlab-duo/prompt-library/) for use case examples that help them get the most value from their credits.

#### 8-step trial process

1. Deliver an [AI Strategy Workshop](https://docs.google.com/presentation/d/11rZCDA7BZaiSA9tEvblpRdYSYZVRmdwiriVlsEdqd-A/edit?slide=id.g3b4cfe06b69_7_1642#slide=id.g3b4cfe06b69_7_1642) pre-trial (as needed). Use output (value stream bottlenecks, identified use cases, sizing, adoption plan) as input to the trial.
2. [Set clear expectations](https://docs.google.com/presentation/d/1VW2xdRVoW-KkIBRFLqIhMccARKVtSpvew7n_tJZvc9Y/edit?slide=id.g3c30e1fb620_0_114#slide=id.g3c30e1fb620_0_114) with the customer and draft an engagement plan incorporating the ingredients below. Send the [evaluation plan template](#dap-trial-evaluation-plan) along with your trial request.
3. Complete the [DAP Trial Evaluation Plan](#dap-trial-evaluation-plan) with your customer.
4. Work with your AE to [submit a fulfillment trial request](https://gitlab.com/gitlab-org/fulfillment/meta/-/issues/new?description_template=trial_credit_requests&issue%5Btitle%5D=%5BA-XXXXXX%5D%20%5BSubscription%20Name%5D,%20%5BCustomer%20Name%5D,%20%5BTotal%20Credits%20Requested%5D,%20%5BDate%20Requested%20For%5D). If an AI Strategy Workshop was conducted, include it with your request.
5. Lead [four 60-minute weekly working sessions](https://docs.google.com/presentation/d/1VW2xdRVoW-KkIBRFLqIhMccARKVtSpvew7n_tJZvc9Y/edit?slide=id.g3bccdb4fbbe_0_0#slide=id.g3bccdb4fbbe_0_0) with all trial participants. Dedicate high-energy time to evangelize, train, and support the customer throughout the 30-day trial.
6. Conduct cadenced status checks outside the working sessions to maintain urgency (as needed). Provide hands-on support through a dedicated Slack channel.
7. Send the [DAP Trial Survey](#dap-trial-survey) at the midpoint and conclusion of the trial.
8. Submit the [DAP Evaluation Form](https://docs.google.com/forms/d/e/1FAIpQLSfbJeY_dDVsFz2F8cmww3VlHtzVWEymIueXEDQcY3qabaxEDg/viewform) at the conclusion. Assist the customer in sizing and securing budget for company-wide adoption.

#### Trial credit approval thresholds

Rely on the [Fulfilmment Issue Request Process's table](https://gitlab.com/gitlab-org/fulfillment/meta/-/issues/new?description_template=trial_credit_requests) for Trial Credit approval requirements.

**Request process:**

1. Validate subscription details (cloud licensing, not opted into on-demand billing)
2. Create an issue under the [Fulfillment epic](https://gitlab.com/gitlab-org/fulfillment/meta/-/issues/new?description_template=trial_credit_requests&issue%5Btitle%5D=%5BA-XXXXXX%5D%20%5BSubscription%20Name%5D,%20%5BCustomer%20Name%5D,%20%5BTotal%20Credits%20Requested%5D,%20%5BDate%20Requested%20For%5D)
3. Post the issue link to `#trial-credits-requests` in Slack — this channel automatically tags the appropriate approvers
4. **SLA: 1 business day** after approval, the Fulfillment team processes the request

Any account team member can submit the request, but **SAs should always be engaged** in trial planning.

{{% alert title="On-demand billing: the #1 field pain point" color="warning" %}}
**Understand this before any billing conversation with customers.**

- Customers with a Monthly Commitment **must still accept on-demand billing terms** as part of the purchase flow
- Consumption Controls will be shared in the [DAP Governance - Q1 epic](https://gitlab.com/groups/gitlab-operating-model/-/work_items/744)
- If a customer accepted on-demand billing to self-start a trial and wants to undo it, you can communicate that GitLab is working on a solution

**What to tell customers:** Monthly commitment pricing provides significant cost savings (up to 30% vs on-demand at $1/credit). On-demand billing is a safety net ensuring uninterrupted service — it only activates after included credits, committed credits, and any waiver credits are exhausted. Usage caps are on the roadmap (targeting 18.11) to provide additional spend controls.
{{% /alert %}}

**Your mission** is to help the customer:

1. Understand DAP and the use cases that translate to real value
2. Model costs and budget for DAP adoption enterprise-wide
3. Make a purchase decision within 30 days of ending the trial

#### Ingredients for success

- **Start small** — Identify the most likely-to-succeed teams to engage first. If you try to conduct a trial across too many users, the customer is unlikely to build strong momentum. Educate and plan which proven DAP use cases will benefit them most.
- **Define success criteria** — Know how the customer will judge success before beginning the trial. Use the [Business Value Consulting](/handbook/solutions-architects/sa-practices/business-value-consulting/) methodology and [Command of the Message metrics](/handbook/sales/command-of-the-message/metrics/) to quantify expected value.
- **Draft an engagement plan** — Map resources on both sides for the full 30 days. Ensure you have the time and resources to be in front of the customer evangelizing, training, answering questions, and responding to issues every week. The customer must commit to devoting resources and incorporating DAP into their daily work.
- **Establish baselines first** — Consider a [Value Stream Discovery workshop](/handbook/solutions-architects/sa-practices/value-stream-discovery/) pre-trial to capture current-state metrics (cycle time, MTTR, review time). These baselines are essential for measuring trial success and building the business case for adoption.

#### DAP Trial Evaluation Plan

{#dap-trial-evaluation-plan}

Share this template with the customer to align on scope, teams, use cases, and success metrics before requesting evaluation credits.

##### Focused Teams

Limit trials to a maximum of 100 engineers to ensure sufficient training and support. Participating teams need active support in training, experimenting, and adopting DAP as part of their daily routines. Conduct one 60-minute training session each week for all active participants (attendance required). Open a Slack channel for questions and provide rapid response throughout the 30-day period. With up to 100 engineers' active usage, you will have sufficient data to help the customer plan and budget for usage across their entire organization.

Work with the customer to identify and document the participating feature/project teams.

##### Valuable Use Cases

From beta testing and customer engagements, the following use cases have demonstrated considerable time savings and productivity benefits:

- **Contextual Agentic Chat** — Developer productivity
- **Agentic Code Review** — Reduce MR review time
- **Issue, Code, and MR Analysis and Summary** — Developer productivity
- **Security Agent: Vulnerability Explanation/Resolution** — Lower security and compliance risk
- **Fixing Broken Pipelines** — Reduced time to resolution
- **Speeding Up Developer Onboarding** — Time to first MR

These are a few of the [hundreds of possible use cases](https://about.gitlab.com/gitlab-duo/prompt-library/) available with DAP. Work with the customer to identify which use cases are most valuable for their organization.

##### Success Metrics

Define what success looks like from both a quantitative and qualitative perspective. Use the [Verifiable Outcomes framework](/handbook/customer-experience/csm/success-plans/) (SMART: baseline metrics, success criteria, business impact, timeline) and the [Business Value Consulting](/handbook/solutions-architects/sa-practices/business-value-consulting/) methodology to quantify DAP value.

**Per-stakeholder success criteria:**

For each key stakeholder, document what they need to see for the trial to be considered successful:

| Stakeholder | What They Need to See | How They'll Measure It | Deal-Breaker If Not Met? |
|---|---|---|---|
| Champion | *Developer enthusiasm, visible productivity gains* | *Survey scores, anecdotal feedback* | *Yes/No* |
| Economic Buyer | *ROI justification, cost model for rollout* | *Credits consumed vs. value delivered* | *Yes/No* |
| Technical Lead | *Code quality maintained, integration works* | *MR quality, pipeline metrics* | *Yes/No* |
| End Users (Developers) | *Genuine time savings, not disruptive* | *Self-reported time savings* | *Yes/No* |

For guidance on identifying these stakeholders, see [MEDDPPICC](/handbook/sales/meddppicc/) (Economic Buyer, Champion) and [Strategic Solution Selling](/handbook/solutions-architects/playbooks/strategic-solution-selling/).

**Quantitative metrics template:**

| Metric | Current Baseline | Target | Measurement Method | Timeline |
|---|---|---|---|---|
| *MR cycle time* | *5 days* | *3 days* | *GitLab Value Stream Analytics* | *Week 2-4* |
| *Time to first MR (new hires)* | *3 weeks* | *1 week* | *MR creation date* | *During trial* |
| *Security vulnerability MTTR* | *14 days* | *7 days* | *Issue close time* | *Week 2-4* |

**Stop criteria** — agree upfront on what would cause the customer to end the evaluation early (for example, data privacy concern, unacceptable latency, no measurable improvement by week 2). Documenting these prevents ambiguous outcomes.

**Evidence for leadership** — identify what the Economic Buyer needs to present internally: ROI calculation, performance metrics before/after, user testimonials, competitive comparison, security validation. Build this evidence throughout the trial, not just at the end.

#### Key resources

| Resource | Description | Link |
|----------|-------------|------|
| AI Strategy Workshop deck | Pre-trial workshop slides | [Google Slides](https://docs.google.com/presentation/d/11rZCDA7BZaiSA9tEvblpRdYSYZVRmdwiriVlsEdqd-A/edit?slide=id.g3b4cfe06b69_7_1642#slide=id.g3b4cfe06b69_7_1642) |
| Setting Expectations deck | Customer-facing trial overview | [Google Slides](https://docs.google.com/presentation/d/1VW2xdRVoW-KkIBRFLqIhMccARKVtSpvew7n_tJZvc9Y/edit?slide=id.g3c30e1fb620_0_114#slide=id.g3c30e1fb620_0_114) |
| Working Sessions deck | Weekly session materials | [Google Slides](https://docs.google.com/presentation/d/1VW2xdRVoW-KkIBRFLqIhMccARKVtSpvew7n_tJZvc9Y/edit?slide=id.g3bccdb4fbbe_0_0#slide=id.g3bccdb4fbbe_0_0) |
| Fulfillment Request template | Credit request issue template | [GitLab Issue Template](https://gitlab.com/gitlab-org/fulfillment/meta/-/issues/new?description_template=trial_credit_requests&issue%5Btitle%5D=%5BA-XXXXXX%5D%20%5BSubscription%20Name%5D,%20%5BCustomer%20Name%5D,%20%5BTotal%20Credits%20Requested%5D,%20%5BDate%20Requested%20For%5D) |
| Customer Checklist | Customer-facing trial checklist | [Google Doc](https://docs.google.com/document/d/1T1VSBj4c205ot1AXFxX1uKnsGotjlZPiA-oYxUbwCqs/edit?tab=t.0) |
| Fulfillment Playbook | Internal fulfillment process doc | [Google Doc](https://docs.google.com/document/d/1Jk8uve7OdlslwR1yG19IC5Ch7H1DsUENkTs78SEBdYg/edit?tab=t.0#heading=h.1htgeb1lsl53) |
| DAP Evaluation Form | Post-trial evaluation submission | [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSfbJeY_dDVsFz2F8cmww3VlHtzVWEymIueXEDQcY3qabaxEDg/viewform) |
| Prompt Library | Use case examples and prompts | [about.gitlab.com](https://about.gitlab.com/gitlab-duo/prompt-library/) |
| SA Initiatives tracking issue | Program tracking and questions | [Issue #693](https://gitlab.com/gitlab-com/customer-success/solutions-architecture-leaders/sa-initiatives/-/issues/693) |
| Usage Billing demo video | 5-min staging walkthrough of credit consumption | [Google Drive](https://drive.google.com/file/d/1xU_Pdh3TOWy_fZG_TkULSwJ_mtY02v6p/view?usp=drive_link) |
| DAP Pricing Message House | Customer-facing pricing messaging | [Highspot](https://gitlab.highspot.com/) |
| Value Stream Discovery | Pre-POV baseline metrics workshop | [Handbook](/handbook/solutions-architects/sa-practices/value-stream-discovery/) |
| Business Value Consulting | ROI, TCO, cost of inaction frameworks | [Handbook](/handbook/solutions-architects/sa-practices/business-value-consulting/) |
| Success Services (Duo Onboarding) | Post-trial Duo Enterprise Onboarding accelerator | [Handbook](/handbook/customer-experience/success-services/) |
| Customer Terrain Mapping | Structured discovery sessions by topic area | [Handbook](/handbook/customer-experience/customer-terrain-mapping/) |

#### Self-service purchase eligibility

Since **February 3, 2026**, eligible customers can purchase Monthly Commitment credits directly through the [Customer Portal](https://customers.gitlab.com) without Sales assistance.

| Subscription Type | Can Self-Purchase | Notes |
|---|---|---|
| Premium (SaaS) | Yes | — |
| Ultimate (SaaS) | Yes | — |
| Premium (Self-Managed, Cloud License) | Yes | — |
| Ultimate (Self-Managed, Cloud License) | Yes | — |
| Self-Managed (Offline License) | **No** | Requires Sales-assisted order |
| Dedicated | **No** | Requires Sales-assisted order |
| Reseller subscriptions | **No** | Requires Sales-assisted order |
| Multi-year subscriptions | **No** | Requires Sales-assisted order |

**Key constraints:**

- Customers **cannot reduce** their Monthly Commitment mid-term
- Credits are reflected immediately after purchase
- Monthly Commitment has a **minimum 12-month term** with monthly credit refresh
- Customers who need to purchase without a credit card must work with Sales
- Self-service purchases are commissionable (Incremental ARR)

#### Duo Core transition (March 19, 2026)

{{% alert title="Code Suggestions billing change — March 19" color="info" %}}
On **March 19, 2026** (GitLab 18.10 release), Duo Core transitions fully to agentic capabilities. After this date, Code Suggestions will consume credits from the general credit pool (at a rate of approximately 50 suggestions per credit). Customers currently relying on "free" Code Suggestions through Duo Core should plan for this transition. 30-day advance customer communications are planned.
{{% /alert %}}

**Timeline:**

- **Before March 19 (through 18.9):** Classic Duo Chat and Code Suggestions remain available as a fallback for Premium/Ultimate customers with included credits
- **March 19 (18.10):** All AI features operate through the agentic credit system
- Customers without a Monthly Commitment will exhaust their included credits (Premium: 12/user/month, Ultimate: 24/user/month) and lose access to AI features unless they accept on-demand billing or purchase a commitment
- **Preferred customer path:** Transition to DAP with a Monthly Commitment to ensure uninterrupted access and volume pricing

### Results

#### DAP Trial Survey

{#dap-trial-survey}

{{% alert title="Survey platform under evaluation" color="info" %}}
The survey delivery platform is being finalized — details coming soon. In the meantime, use the questions below as your survey framework.
{{% /alert %}}

Send the following survey to all trial participants at the **midpoint** and at the **conclusion** of the trial to collect quantitative and qualitative feedback:

1. How likely are you to recommend Duo Agent Platform to other teams in your company? (Scale of 1–10)
2. How much time did Duo Agent Platform save you each week?
3. Which use cases are most valuable to you?
4. What are the next features or enhancements GitLab should add?

Each question should allow for verbatim comments in addition to structured responses.

### Tracking

#### Dashboard visibility and sharing rules

{{% alert title="Internal dashboards must never be shared with customers" color="warning" %}}
The Tableau dashboards listed below (AI Gateway Reporting, Agent Success Metrics, DAP Monetization, etc.) are **internal only** and count metrics differently than customer-facing dashboards. Never share Tableau links or screenshots with customers.
{{% /alert %}}

**Customer-facing dashboard options:**

| Dashboard | Audience | Access |
|---|---|---|
| [GitLab Duo and SDLC Trends](https://docs.gitlab.com/user/analytics/duo_and_sdlc_trends/) (in-product) | Admins, Group Owners | Owner/Admin permissions |
| [GraphQL API](https://docs.gitlab.com/api/graphql/) | Technical users | API access |
| Customer Portal ([customers.gitlab.com](https://customers.gitlab.com)) | Billing/Subscription Managers | Portal access |

**Important setup — dashboard is OFF by default (GDPR/privacy):**

- **SaaS:** Top-level group > Settings > General > Permissions and group features > check "Display user data" under GitLab Credits dashboard
- **Self-Managed:** Admin > Settings > General > Visibility and access controls > check "Display user data" under GitLab Credits dashboard
- Dashboard data latency: typically 1 hour, max 3 hours
- Enable the dashboard **before** any trial or customer demo so data is ready to present

**Usage alert notifications:**

- Email alerts sent at **50%**, **80%**, and **100%** of credits consumed (sent once per threshold, not recurring)
- Recipients: all administrators and subscription owners
- AEs can track customer credit usage in **Salesforce** (not Tableau)

#### Duo Agent Platform (DAP) Metrics Dashboards

Use these Tableau dashboards to track DAP adoption, engagement, and credit consumption during and after POVs and customer deployments. See also the [SA Visibility Dashboards](/handbook/solutions-architects/sa-practices/subject-matter-experts/sme-collateral/#ai--duo-agent-platform-dap--sa-visibility-dashboards) for the full reference.

##### Usage Billing Analytics

{{% alert title="Draft dashboard" color="info" %}}This workbook is under active development by the Product Data Insights team. Views and metrics may change. See [gitlab-data/product-analytics#3227](https://gitlab.com/gitlab-data/product-analytics/-/issues/3227) for status.{{% /alert %}}

Workbook: [Usage Billing Analytics](https://10az.online.tableau.com/#/site/gitlab/workbooks/3888582/views)

| Dashboard | Purpose | Link |
|-----------|---------|------|
| Duo KPI Dashboard | Key performance indicators for Duo adoption | [Duo KPI Dashboard](https://10az.online.tableau.com/#/site/gitlab/views/UsageBillingAnalytics_17685202519710/DuoKPIDashboard?:iid=2) |
| Consumption Deep Dive Metrics | Detailed credit consumption breakdown | [Consumption Deep Dive Metrics](https://10az.online.tableau.com/#/site/gitlab/views/UsageBillingAnalytics_17685202519710/ConsumptionDeepDiveMetrics?:iid=3) |
| Customer Report Dashboard | Per-customer consumption reporting | [Customer Report Dashboard](https://10az.online.tableau.com/#/site/gitlab/views/UsageBillingAnalytics_17685202519710/CustomerReportDashboard?:iid=4) |

##### DAP Usage & Engagement

| Dashboard | Purpose | Link |
|-----------|---------|------|
| Duo Daily Usage | Daily DAP usage trends | [Duo Daily Usage](https://10az.online.tableau.com/#/site/gitlab/views/DAPUsage/DuoDailyUsage?:iid=1) |
| Agent Success Metrics | Agent task completion rates, success/failure breakdown | [Agent Success Metrics](https://10az.online.tableau.com/#/site/gitlab/views/AgentUsageEngagement/AgentSuccessMetrics?:iid=2) |
| Agent Engagement Trends | Usage trends, adoption curves, engagement patterns | [Agent Engagement Trends](https://10az.online.tableau.com/#/site/gitlab/views/AgentUsageEngagement/AgentEngagementTrends?:iid=1) |

##### DAP Monetization Metrics

Workbook: [DAP Monetization Metrics](https://10az.online.tableau.com/#/site/gitlab/workbooks/3489989/views)

| Dashboard | Purpose | Link |
|-----------|---------|------|
| DAP Monetization Insights | Credit consumption per agent type, cost trends | [DAP Monetization Insights](https://10az.online.tableau.com/#/site/gitlab/views/DuoAgentPlatformMonetizationMetrics/DuoAgentPlatformMonetizationInsights?:iid=2) |
| Full Report Dashboard | Comprehensive DAP monetization report | [Full Report Dashboard](https://10az.online.tableau.com/#/site/gitlab/views/DuoAgentPlatformMonetizationMetrics/FullReportDashboard?:iid=2) |
| Token Consumption Metrics | Token-level consumption analysis | [Token Consumption Metrics](https://10az.online.tableau.com/#/site/gitlab/views/DuoAgentPlatformMonetizationMetrics/TokenConsumptionMetrics?:iid=1) |

##### AI Gateway Reporting

| Dashboard | Purpose | Link |
|-----------|---------|------|
| AI Gateway Overview | AI Gateway request volume, latency, error rates | [AI Gateway Overview](https://10az.online.tableau.com/#/site/gitlab/views/AIGatewayReporting/Overview?:iid=1) |

##### Duo Subscription Utilization

Workbook: [Duo Subscription Utilization](https://10az.online.tableau.com/#/site/gitlab/workbooks/2484649/views)

| Dashboard | Purpose | Link |
|-----------|---------|------|
| Duo Subscription Utilization | Seat usage, activation rates, subscription health | [Duo Subscription Utilization](https://10az.online.tableau.com/#/site/gitlab/views/DuoProSubscriptionUtilization/DuoSubscriptionUtilization?:iid=2) |
| Tier Enabled Duo Core Utilization | Duo Core feature utilization by tier | [Tier Enabled Duo Core Utilization](https://10az.online.tableau.com/#/site/gitlab/views/DuoProSubscriptionUtilization/TierEnabledDuoCoreUtilization?:iid=3) |
| Duo Subscription Account Report | Per-account subscription report | [Duo Subscription Account Report](https://10az.online.tableau.com/#/site/gitlab/views/DuoProSubscriptionUtilization/DuoProSubscriptionUtilizationReport?:iid=1) |

##### Duo Feedback

| Dashboard | Purpose | Link |
|-----------|---------|------|
| Duo Feedback Dashboard | User feedback, satisfaction signals, feature requests | [Duo Feedback Dashboard](https://10az.online.tableau.com/#/site/gitlab/views/DuoFeedbackDashboard/DuoFeedbackDashboard?:iid=1) |

**Product Roadmap:** [DAP Product Roadmap Q1 FY27](https://gitlab.com/groups/gitlab-operating-model/-/work_items/41)

### Other POV Scope and Acceptance

SA working with SAE and AE can define the POV scope with the customer, with alignment to the business values and the GitLab solution. For each solution, the typical scope and acceptances are listed for reference but the team should define the scope, time and execution with acceptance for each engagement.

- [DevSecOps](/handbook/solutions-architects/playbooks/pov/devsecops/)
- [Automated Software Delivery](/handbook/solutions-architects/playbooks/pov/automation/)
- [DevOps Platform cumulatively](/handbook/solutions-architects/playbooks/pov/platform/)

## AI engagements in general

### Discovery - adapt to the customer's context

As early as possible, actively discover your customer's specific context. For the foundational discovery methodology, see the [Sales Discovery Playbook](/handbook/sales/playbook/discovery/) and ensure [MEDDPPICC](/handbook/sales/meddppicc/) fields are populated in the [Command Plan](/handbook/sales/command-of-the-message/command-plan/). For AI evaluations specifically, consider a [Value Stream Discovery workshop](/handbook/solutions-architects/sa-practices/value-stream-discovery/) to establish baseline metrics before the POV, and use [whiteboard-based facilitation](/handbook/solutions-architects/sa-practices/whiteboard-based-facilitation/) (Current State Discovery, Day-in-the-Life templates) for interactive discovery sessions.

Before presenting GitLab's vision or positioning, ask the customer if they have an existing company strategy or guidelines, or personal opinions on Gen-AI in general, and for development.

Inquire about the following topics

- Vision on Gen-AI
  - Sentiment: afraid of AI vs excited about the technology vs cautious about security implications
  - How much is expected: a complete overhaul of practices, or punctual help for developers
  - Understanding of the market: awareness of the multiple vendors and products? Do they see AI models as a "winner-takes-all" or as a commodity?
- Company strategy
  - Is Gen-AI for software development an isolated effort, or part of a bigger initiative? In the latter case, it might be useful to understand the topics, metrics, timeline, and decision-makers involved.
  - Are other Gen-AI tools already used?
  - Are developers authorized to use Gen-AI tools that were not vetted and purchased by the company? What are the security and privacy implications? Are there control mechanisms in place to prevent this kind of shadow IT?
- Use cases and workflows
  - Providing comfort and productivity for developers (code generation performance)? Or broader vision over the broader picture = SDLC performance.
  - Metrics
  - Objectives and key results
- Constraints. Depending on the answers to the following questions, some AI features might not be immediately available. Or they may not apply to a subset of projects.
  - Self-managed or Dedicated? Cloud licensing possible? Premium or Ultimate?
  - Security and Privacy: allow for API calls outside their infrastructure? Including sending proprietary code?

Examples of customer inputs that had a significant influence on the technical evaluation:

- "Code suggestions are not useful for us, we don't want to activate that feature. Instead, we're looking to leverage GitLab Duo to make the most out of our existing applications: documenting, refactoring, adding tests, innersourcing, etc."
- "We only want to use AI features if they're connected to self-hosted, custom AI models, without any data leaving our network"

#### DAP Trial Discovery Questions

{#dap-trial-discovery-questions}

The following questions supplement the [general discovery guidance above](#discovery---adapt-to-the-customers-context) and are specific to DAP credit-based trials. Use them to identify high-value use cases, understand pain points, and build the case for adoption. For broader sales discovery questions (including competitive positioning against GitHub, Azure DevOps, and Bitbucket), see the [Qualification Questions](/handbook/sales/qualification-questions/) page.

##### Preliminary DevOps / Platform Team Discovery

For DAP trials, the most likely-to-succeed teams will be moving fast, doing greenfield development with high business impact. When working with DevOps or Platform teams, use these questions to identify which teams fit that criteria.

1. What is the typical mix of feature development versus maintenance work for the key teams you support?
2. Which teams are leveraging GitLab and looking to continue to innovate?
3. Which teams are working on new projects or greenfield development versus maintaining legacy systems?
4. Are there any teams building new services, microservices, or net-new applications?

##### Development Bottlenecks

1. Where does development slow down most significantly in your process?
1. How much time do your developers spend writing boilerplate code versus differentiating work?
1. What is the average time spent on code reviews per developer per week, and what is the quality/satisfaction level?
1. How long does it take for a new developer to become productive on your codebase?
1. What percentage of developer time is spent on undifferentiated toil versus new feature development?

##### CI/CD and Testing

1. What is your current pipeline failure rate, and how long does it take to diagnose failures?
1. What are your most common pipeline failure causes and their frequency?
1. What is your current test coverage (unit/integration/E2E), and where are the gaps?
1. How much time do developers spend maintaining pipelines versus building features?

##### Security and Compliance

1. What is your false positive rate from security scans, and how much time is spent triaging them?
1. What is your mean time to remediate (MTTR) security vulnerabilities?
1. Where do security requirements create the biggest bottlenecks in your development process?
1. How strong is your developers' security knowledge — can they fix vulnerabilities independently?

##### Use Case Validation

1. For your top 3 pain points, what would "good" look like, and how would you measure success?
1. What is the minimum improvement threshold you need to see to justify moving forward?
1. What would prove that an AI solution actually solves your specific problems?
1. Is this pain point a deal-breaker if not solved, or nice to have?

##### Business Impact

1. If you could quantify the annual cost of your current approach to a specific pain point, what would it be?
1. What realistic productivity gain percentage would make this initiative worthwhile?
1. Who needs to see value from this solution for it to be considered successful?

##### Organizational Readiness

These questions assess whether the customer has the capacity and culture to run a successful 30-day trial. A customer who lacks bandwidth, is mid-reorg, or has no internal champion will waste evaluation credits.

1. Beyond the tooling challenges, what's making this hard from an organizational standpoint — skills, bandwidth, competing priorities, or alignment across teams?
1. If you had the perfect AI-powered DevSecOps platform tomorrow, would your developers be ready to adopt it fully? What would need to be true for that to happen?
1. Do you have a dedicated team or champion resourced to lead the evaluation, or would you need help accelerating the rollout?
1. What's been your experience adopting new developer tools in the past — what worked and what didn't?
1. Is there executive sponsorship for this initiative, or does that still need to be secured?

##### Organizational Impact

Map the "chain of pain" across the organization to build the multi-stakeholder business case for DAP adoption. Ask questions in three directions:

**Looking up** (leadership impact):

1. How does this problem impact your leadership's priorities or KPIs?
1. If this isn't solved in the next 6 months, what does that mean for the business?

**Looking down** (team impact):

1. Who on your team feels this pain most acutely?
1. What workarounds have people created, and what do those cost?

**Looking across** (cross-team impact):

1. Which other teams are impacted by this — security, platform, QA, operations?
1. Who else needs to be part of solving this and would benefit from seeing DAP in action?

Use this framework to identify additional trial participants and stakeholders for the [Evaluation Plan](#dap-trial-evaluation-plan). For deeper stakeholder analysis, see [MEDDPPICC](/handbook/sales/meddppicc/) (Economic Buyer, Champion, Competition) and the [Strategic Solution Selling](/handbook/solutions-architects/playbooks/strategic-solution-selling/) practice.

#### Handling discovery pushback

In AI evaluations, customers have often spoken to multiple vendors (GitHub Copilot, Amazon Q, Cursor, etc.) and may resist another discovery conversation. Use the **acknowledge-validate-reframe** pattern:

| Step | Action | Example |
|------|--------|---------|
| 1. Acknowledge | Make them feel heard | "I hear you — you've probably had this conversation multiple times already." |
| 2. Validate | Respect their perspective | "It's frustrating when these discussions don't lead to real value for you." |
| 3. Reframe | Show differentiated value | "What I've found is that when we dig into [specific area like CI/CD pipelines or security remediation], we often uncover things that change the whole approach. Would you be open to exploring that?" |

The key differentiator: GitLab's AI is embedded across the entire SDLC, not just in the IDE. Discovery should surface pain points across the full software delivery lifecycle — not just code generation — where DAP's agentic capabilities (pipeline fixing, security remediation, code review) provide unique value.

For deeper discovery methodology, see the [Sales Discovery Playbook](/handbook/sales/playbook/discovery/) (TED questioning, Five Whys, multi-threading) and [Qualification Questions](/handbook/sales/qualification-questions/).

#### Using demos as discovery

SAs are frequently brought into AI evaluations mid-flight — the customer already has a scorecard, wants a demo next week, and formal discovery hasn't happened. When this occurs:

1. **Be transparent** — "I want to make sure I show you the things that matter most to your team. Can I ask a few questions to tailor this?"
2. **Use the demo as discovery** — demonstrations create natural opportunities for questions:
   - "Is this the kind of workflow your team follows today?"
   - "What tools do you currently use for this step?"
   - "How does this compare to your current process?"
3. **Probe for KPIs during technical discussions** — "When your pipeline fails, how long does it typically take to diagnose? How often does that happen?"
4. **Capture insights for follow-up** — document what you learn and use it to build the case for a structured [DAP Trial Evaluation Plan](#dap-trial-evaluation-plan)

This approach works particularly well when demonstrating DAP's agentic workflows (security remediation, pipeline fixing) since these naturally surface the customer's current pain points and processes. For demo preparation and systems, see the [SA Demonstrations](/handbook/solutions-architects/demonstrations/) page and the [Workshops practice guide](/handbook/solutions-architects/sa-practices/workshops/).

### Elements of perspective and communication on Gen-AI features

The following elements proved effective to influence positively the way AI-powered features are perceived.

**Pioneer/learning mindset**: Gen-AI is relatively new for everyone everywhere. As early adopters, we'll learn the best patterns to interact with it, and be creative to surface new use cases where AI will prove most useful

- Customers might ask for features that are not currently available, and which could sound too ambitious or not technically feasible. Try to be open, don't dismiss these ideas too quickly. Consider how a combination of GitLab's existing or roadmap features could serve this purpose, specifically GitLab Duo Chat which is very versatile.
- Encourage this kind of reflection with questions like: Without considering any technical constraints, what use cases would you like AI to perform? Can you think of any creative use that could be made of the current feature set?
  - This is meant to put attendees in a position to find potential solutions, rather than finding potential issues.
- Examples of creative use cases that can be achieved
  - "I'd like the AI to document legacy applications" could be achieved by customizing the /explain action
  - "I'd like to convert Python code to Java" or "Convert a Jenkins pipeline to GitLab CI". This could be achieved by customizing the /refactor action
  - "I'd like an answer in a language other than English". This typically works pretty well, although our Product team does not actively optimize for multi-language support.

**Playfulness**: The element of "randomness" in AI can be fun. Early-stage, experimental

- When demonstrating GitLab Duo Chat, encourage attendees to try it themselves, or give you creative prompts.
- Even out-of-context questions like "give me the recipe for apple pie" add some fun, and demonstrate that there are some guardrails in place - AI typically responds that this is not the kind of question they can answer.

**AI as an assistant to developers**, as opposed to an autonomous software delivery system
highlights the importance of the developer's role and skill: review, adjust, use AI as a tool

- Mention the [reason behind the name "GitLab Duo"](https://about.gitlab.com/blog/2023/06/22/meet-gitlab-duo-the-suite-of-ai-capabilities/):
  > The name GitLab Duo is rooted in You + GitLab AI = the AI dynamic duo.
- Be mindful that some companies or individuals might have a pre-existing bias against Gen-AI. Some might even see any Gen-AI effort as dangerous, or as a way to replace human workers. If this is the case
  - try to understand why
  - consider giving a presentation to popularize Gen-AI to explain how it works, and explore its strengths and limitations. This could go a long way towards putting it under a more favorable light.
  - Convey the message that any Gen-AI suggestion is only useful if used in the right context, reviewed, and adjusted as needed by an expert.
  > GitLab Duo is a customer-centric approach focused on privacy first, where customers know their intellectual property is secured.

### Expect the unexpected

Gen-AI won't necessarily give the same answer to the same prompt.
You will run into use cases where AI gives unexpected, wrong, or no answers in your demos. Also keep this in mind when leading a workshop, as a portion of the students will probably experience this.
While this could typically be interpreted as "failing" in a regular context, it doesn't necessarily have to be the case for AI conversations. Use the following to mitigate the negative impact this might have, and even turn it to your advantage:

- Manage expectations and mindset, both for a person running a demo or for someone following a workshop
  - Mention that this is expected, and inherent to Gen-AI. It is neither a bug that will be fixed nor something specific to GitLab's Gen-AI features.
- As a presenter, be prepared for these "happy incidents"
  - Be prepared to brush it off of laugh it off. One wrong suggestion is not a big deal. After all, it's not a true demo until something goes wrong.
  - Use them as opportunities to adopt pioneer/learning/playful mindset, or convey the messaging that AI is meant as an assistant to development teams.
    > "If you want to dig into this later, I'm sure we'll be able to find the right prompt to make this work"
    > "Good thing I'm following best practices and reviewing AI suggestions"
    > "Glad to see I'm not obsolete just yet!"
  - The unexpected answer might be at least partially useful, or serve another purpose
  - Re-try with the same prompt, or with a very slight change
  - Have alternative prompts or use cases ready
- If you are presenting in a high-stakes setting where "nothing should go wrong" use video recordings as a backup

### Reporting issues during trials

When you discover bugs or customer-blocking issues during a DAP trial, follow the [DAP Rapid field reporting process](/handbook/solutions-architects/tools-and-resources/dap-issue-reporting/). SAs can file bugs directly in GitLab issues with severity labels — no Zendesk ticket required. For issues that meet the [definition](/handbook/engineering/infrastructure-platforms/incident-management/#incident-management) of an incident, [declare an incident using incident.io](/handbook/engineering/infrastructure-platforms/incident-management/#reporting-an-incident) and ensure the "Affects Duo Agentic Platform (DAP)" field is set to YES.
