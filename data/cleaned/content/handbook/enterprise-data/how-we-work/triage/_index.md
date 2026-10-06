---
title: "Data Triage Guide"
---

### Enterprise Data Program Triage

GitLab has a robust and vibrant Data Program which includes a Central Data Team and many Functional Analytics Teams. GitLab total team members are growing as well and we need to uplevel our triaging process to keep up with GitLab's growth.

Steps to uplevel triaging process:

1. Incorporate Functional Analytics Teams into the #data channel triaging process.
1. Create Slack Aliases so that GitLab Team members can ping a group of folks to get help with their questions in #data.
1. Create a Triage Schedule for the Data Program to follow on the Data Program Calendar. Ask for a commitment of one team member, per Business Team, per day to help triage.

### Enterprise Data Triage Groups

| Triage Group Name   | Triage Slack Alias  | Triage Group Members  |
| -------------- | ------------------- | -------------------- |
| Go To Market Analytics Triage | `@GTMAnalyticsTriage` |  Revenue Strategy & Analytics Team, Marketing Strategy and Performance Team, Business Insights and Analytics Team, GTM Data Fusion Team |
| R&D Analytics Triage | `@R&DAnalyticsTriage` | Product Data Insights Team, R&D Data Fusion Team |
| People Analytics Triage | `@PeopleAnalyticsTriage` | People Group Analytics Team, G&A Data Fusion Team |
| Data Platform Triage | `@DataPlatformTriage`   | Data Platform Team |

### Enterprise Data GitLab Projects

| Link to GitLab Data Projects |
| -------------- |
| [Data Team](https://gitlab.com/gitlab-data/analytics) |
| [Sales Strategy and Analytics](https://gitlab.com/gitlab-com/sales-team/field-operations/analytics) |
| [Marketing Strategy and Performance](https://gitlab.com/gitlab-com/marketing/marketing-strategy-performance) |
| [Product Data Insights](https://gitlab.com/gitlab-data/product-analytics) |
| [Business Analytics](https://gitlab.com/gitlab-com/business-analytics) |
| [People Analytics](https://gitlab.com/gitlab-com/people-group/people-analytics) |
| [Customer Success Operations - Use CSAnalytics label](https://gitlab.com/gitlab-com/sales-team/field-operations/customer-success-operations) |
| [Online Sales and Self-Service](https://gitlab.com/gitlab-com/sales-team/self-service) |

#### Weekly rotation schedule

The Data platform team and the analytics engineers share a weekly triage schedule. The schedule is maintained on the Data Program Google Calendar

#### Tableau Support

The BI / Tableau Administration team supports requests and ad hoc questions in the #data-tableau channel. There is no individual on triage - any team member can help with Tableau needs. The team also facilitates Tableau Office Hours each week.

### Enterprise Data Program Triage Instructions

All triage team members, regardless of their team, share the following responsibilities:

1. Each week, a single shared triage issue is opened for AEs and DEs. Confirm whether one has already been opened, if not, create it and assign both yourself and your DE/AE counterpart as owners
1. Triagers should review Slack messages in #data
1. Triagers should respond in Slack threads by linking to relevant handbook pages, dashboards, or pointing team members to others who may have deeper expertise on the topic
1. If a request requires more than five minutes of investigation from a Data Program team member, triagers should direct the requestor to the channel description. The description includes links to the various Data Program projects where an issue can be created
1. Triagers should support team members who are new to the issue labeling process by reviewing issues with the `clean-up::review` label and offering guidance on proper labels to use
1. Triagers are responsible for monitoring and triaging all issues labeled with their team’s label to ensure timely responses and resolution of team-specific requests.

A team member who is off, on vacation, or working on a high priority project is responsible for finding coverage and communicating to the team who is taking over their coverage. This should be updated on the [Data Program's Google Calendar](https://calendar.google.com/calendar?cid=Z2l0bGFiLmNvbV9kN2RsNDU3ZnJyOHA1OHBuM2s2M2VidW84b0Bncm91cC5jYWxlbmRhci5nb29nbGUuY29t).

Having dedicated triagers on the team helps address the bystander affect. The schedule shares clear daily ownership information but is not an on-call position. Through clear ownership, we create room for everyone else on the team to spend most of the day around deep work. The triager is encouraged to plan their day for the kind of work that can be accomplished successfully with this additional demand on time.

#### Triage responsibilities by team

Data triagers are the first responders to requests and problems for the Data Program.

[**Data Platform triage guide**](/handbook/enterprise-data/how-we-work/triage/data-platform-triage)

[**Analytics Engineers triage guide**](/handbook/enterprise-data/how-we-work/triage/analytics-engineering-triage)

**Functional Analysts Responsibilities**

- The Functional Analyst triage handle is primarily responsible for responding to GitLab team member requests that relate to their functions via Slack in **#data**.

**Data Science Responsibilities**

The Data Science triager is primarily responsible for reviewing model run issues / breakages and supporting operational requests such as executing field replacements due to dbt model updates.

We will iterate on triage responsibilities to include additional activities such as extract refresh failure review, job failure review, etc. as the team expands.

- For more information on responsibilities of a triager watch the [Data Engineer triage training session video](https://www.youtube.com/watch?v=0eGpgaQgEGg).

## Triage FAQ

**Is Data Triage 24/7 support or a shift where we need to be available for 24 hours?**

No. Triage responsibilities are performed during your normal working hours. Complete the tasks listed in the [Triage Template (internal link)](https://gitlab.com/gitlab-data/analytics/-/issues/new?issuable_template=Triage:%20Data%20Triage) during your standard work day

**If any issue is found do we directly jump to fix it in production or take it as part of the incident and solve it within the defined time?** <br>

On the Triage day the data team member present will look for all the failures, questions or errors in:

- The Slack-channels; #data-pipelines #analytics-pipelines and #data
- Newly added [issues](https://gitlab.com/groups/gitlab-data/-/boards/1917859?&label_name[]=Priority%3A%3A1-Ops&label_name[]=Triage)

It includes all the failures since the last person did sign off and will create an issue for all the failures since then till the person signs off.
If any data pipeline has broken and there is expected to be a delay in getting data loaded or refreshed. The concerned team has to be notified using the [Triage Template (internal link)](https://gitlab.com/gitlab-data/analytics/-/issues/new)

**Is there ETA for a different kind of issue?** <br>

If the pipeline is broken it needs to be fixed, currently we are working on defining SLO's for our data assets. For our data extraction pipelines, there is a comprehensive overview [here](/handbook/enterprise-data/platform/).

**If I work normal hours on my triage day (e.g., ending at 11 AM US time), what happens when a pipeline breaks after my shift ends and causes data availability delays?**

Our global team coverage means we can address issues across multiple time zones. When the triager is in an earlier time zone than US hours, we can resolve issues before they impact US-based stakeholders. However, this does mean we don't have complete coverage for later US hours on those days. We recognize this gap and are working to improve coverage in the future.

## Automated Triage Management

### Triage Bot

The Data Team uses the [GitLab Triage gem](https://gitlab.com/gitlab-org/gitlab-triage) to automate issue management and keep the analytics project organized. The triage policy for the analytics repo is defined in the [.triage-policies.yml](https://gitlab.com/gitlab-data/analytics/-/blob/master/.triage-policies.yml?ref_type=heads) file.

### Label Enforcement

Triagers use labels to identify and prioritize work within their domain. If you're unsure which labels to apply to an issue, just add the `clean-up::review` label and the team will help with proper labeling. This automation ensures that every issue includes the required scoped labels: `team`, `work category`, `champion`, and `workflow`. Labels like `Documentation`, `Iteration Planning`, and `Discussion` are excluded from this requirement.

- **After 3 days**: If an issue is missing required labels, the bot adds a comment listing the missing labels and applies both `Needs Triage` and `clean-up::warning`. The comment includes instructions on how to ask for help using the `clean-up::review` label.
- **After 14 days**: If the labels are still missing, the bot adds a reminder comment.
- **After 30 days**: If there's still no update, the issue is automatically closed. The bot adds the `clean-up::close` label and a comment explaining why. Team members can reopen these issues at any time. To prevent future auto-closure, make sure to add the required labels.

When a closed issue is reopened, the bot removes the `clean-up::close` label and checks for the required labels. If any are still missing, it adds `clean-up::warning` and includes a comment listing what's needed.

Once the correct labels are in place, the bot automatically removes any warning labels. This creates a self-maintaining system where issues either get labeled correctly or are closed for review.

### Stale Issue Management

The triage bot flags issues that haven’t had any activity in over a year to help keep the backlog manageable. When that happens, it adds the `stale::warning` label and posts a comment. From that point, the issue has 14 days before it is automatically closed unless someone takes action.

To prevent an issue from being closed, you can do one of the following:

- Leave a comment on the issue with an update on its current status, then remove the stale::warning label.
- Add the `stale::exempt` label if the issue should remain open without needing regular updates

**Just adding a comment won't stop the process**. The warning label needs to be removed or replaced with `stale::exempt`.

Here's how the timeline works:

1. **After 1 year of inactivity**: The bot adds `stale::warning` and posts a comment
2. **7 days later**: It adds `stale::7day_warning` as a final reminder
3. **After another 7 days (14 since initial warning)**: The issue is closed and tagged with `stale::closed`

Closed issues can be reopened at any time. Once reopened, make sure to update the issue or apply the `stale::exempt` label so it is not flagged again in the future.

### Testing Policy Updates

To test changes to the triage policy file, run the `dry-run:triage` CI job in the `Stage: Triage` of your merge request. This job will not make any actual changes but simulates the outcome of applying the policy file and prints what actions *would* be taken.

> **Important:** A successful job (green check) only means the bot ran without errors. It does **not** mean your triage rules are correct or effective. You must open the job logs and carefully review the output to confirm that the rules match your expectations.

The logs will show:

- Which triage rules were triggered
- How many issues matched each rule
- What actions would be taken (like labels added, comments posted)
