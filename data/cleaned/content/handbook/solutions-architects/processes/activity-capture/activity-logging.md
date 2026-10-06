---

title: Solutions Architecture Activity Logging
description: >-
  Process manual for SA activity logging: why the change, how to log common scenarios, known limitations, and an FAQ for the Phase 1 rollout of the GitLab SA Activity Form.

---

Everything from the Phase 1 rollout: the why, the how, edge-case logging, known limitations, and an FAQ — in one place for the whole Solutions Architecture organization.

**Status:** Phase 1 effective 2026-09-07 · Rattle activity logging retired · Last updated 2026-09-09

## 1. Why This Change

Better activity data lets leadership argue for SA headcount, coverage, and investment with evidence instead of anecdote — and shows where teams are stretched thin. This is about recognition and visibility for the work SAs already do, not oversight.

- **Pilot · 2026-09-07** - Q3 is the first real data set. The goal is building the habit, not perfect numbers — log honestly, even when messy.
- **Phase 1 · now** - A lightweight GitLab-hosted form replaces Rattle as the single method for SA activity tracking.
- **Phase 2 · coming months** - An automated MCP capability (pending approval) cuts manual entry and writes directly to Salesforce.

## 2. What You Need To Do

1. **Stop using Rattle** for SA activity tracking as of Monday, 2026-09-07 — its Slack integration turns off that day. (Rattle stays live for other functions: SFDC case triage/SA Requests and other notifications are unaffected for now.)
1. **Start logging through the [GitLab SA Activity Form](https://sa-activity-e4fb10.gitlab.io/).**
1. **Sign in before you start entering data.** It is easy to enter activity in Demo mode and not realize it — your entries will not be recorded against you. Always confirm you are signed in first.
1. **Log same-day if possible**, or as soon as the activity is fresh — weekly at the latest.
1. Watch the short ["day in the life" demo](https://drive.google.com/file/d/1thOkWwPBM_B7Q3qHyYJYfCsAwAkA_eVy/view) (walks through logging both customer and non-customer activity) before starting.
1. Bring hard questions to your team leader — that's what the leadership walkthroughs are for.

**Rattle post-meeting notifications:** Rattle still sends post-meeting Slack notifications for customer-facing meetings as before. The `Log Activity` button has been replaced with a `Capture Activity` link that opens the new SA Activity Form. These notifications cover customer meetings only — you still need to proactively log broader activities (prep, research, travel, follow-up, internal contributions) yourself.

## 3. How to Log Common Scenarios

| Scenario | How to log it |
|---|---|
| Broad marketing events (summits, conferences, webinars, multi-customer workshops) | Use the Salesforce **Campaign ID** (starts with `701`, 15 or 18 characters). Find it via the campaign picker near the bottom of the form, or paste the ID directly if it's not listed — get it from the Campaign record's URL in Salesforce. |
| Partner work (partner enablement, MDF-funded on-sites) | Partners appear as **accounts** in Salesforce — use the partner's **Account ID**. Any SA can log against a partner/customer account number; useful signal for the Ecosystem team. |
| Early-stage work (lead or account, no opportunity yet) | Field accepts free text. Use the **Account ID** if one exists; if there's no account or opportunity at all, enter **"Pipeline Gen"**. |
| Internal contributions (blog posts, internal procedures, onboarding buddy, interviews) | Choose **Non-Customer Facing** → Activity Type **Other** → explain in Notes. |
| Community and technology events (meetups, conference talks, DevSecOps presentations) | Yes, log these — they represent real SA time and often generate pipeline. Use the Salesforce Campaign ID if a campaign exists; otherwise use the Account ID of the primary customer/partner involved, or "Pipeline Gen" if no account is attached yet. |
| Aggregated travel (multi-stop trip across several customers/partners) | For the travel portion: either enter multiple opportunity IDs in the "Opportunity, Campaign or Account" field, or pick one main customer and log travel there. Then log each onsite/workshop separately against its own customer or partner. Travel time can also simply be logged under **Non-Customer Facing** — travel itself isn't customer-facing time, even when the trip is for customer meetings. |
| Customer event with no Salesforce marketing campaign | Open question as of 2026-09-07 — no confirmed answer yet beyond logging against the partner/customer account directly. |
| Internal meetings (1:1s, team calls, coffee chats, mentorship) | **Do not log these** — same as under the old Rattle process. Only record customer-related prep, pre-call, post-call, or planning. |

Finding an account or opportunity ID in Salesforce: an account URL looks like `.../Account/0016100000SwqPFAAZ/view` (ID starts with `0016`); an opportunity URL looks like `.../Opportunity/006Qq00000qM2jcIAC/view` (ID starts with `006`). The dropdown does not require a validated selection — you can paste an ID directly.

## 4. Notes Field and Salesforce Fields

**Notes field behavior:**

1. **Customer-facing activities:** Notes are optional. The primary goal of the tracker is to capture where your time goes, not to replace Salesforce activity notes.
1. **Non-customer-facing activities:** Notes are mandatory — they help build a picture of what non-customer work SAs actually do.
1. Your manager may ask for additional notes on customer-facing activities depending on team-specific requirements.

**Salesforce fields to keep up to date (these are not replaced by the new form):**

1. **SA Next Steps** and **SA Feasibility Rating** remain on the Opportunity record — keep these current as you do now.
1. **PoV Object** is the required system of record for all proof-of-value and trial work — maintain it and keep it linked to the relevant opportunity.
1. **SA Validated Tech Eval fields** on the Opportunity are being phased out in favor of the PoV Object. Discuss with your manager whether your team still requires them in the interim.

## 5. Known Issues and Limitations

- **Opportunity sync delay.** The opportunity list refreshes on a 4-hour cycle from Salesforce, then caches for ~15 minutes; campaign lists and geo lookups also cache 15 minutes, token-to-email lookups cache 5 minutes. Right after a Salesforce Connector refresh or query edit, the form can serve a stale list for up to 15 minutes.
- **Missing opportunities in the dropdown.** New Business SAs (and others) report seeing far fewer opportunities than they're actually assigned in SFDC — possibly because they're assigned at the Opportunity level, not the Account level (same root cause flagged for Command Center). Unresolved as of 2026-09-07 — workaround is to paste the opportunity ID manually.
- **No way to review past submissions.** There's no in-tool history or dashboard of what you've already logged. The "Download backup CSV" button exists, but only shows Salesforce IDs, not readable names — consider adding the account/opportunity name in Notes for your own reference.
- **Local backup is fragile.** Entries are saved as a "local backup on this device"; clearing your browser cache deletes them. During the first weeks of rollout, download a local CSV backup daily as a precaution.
- **No calendar integration yet.** Unlike Rattle's Slack meeting prompts, the new form has no calendar-driven logging or automatic meeting detection. Top requested feature for Phase 2; submit and track requests in the [SA Activity Form feedback issue](https://gitlab.com/gitlab-com/customer-success/solutions-architecture-leaders/sa-initiatives/-/work_items/744).
- **Category gaps for Ecosystem/Partner SAs.** "Customer-facing" doesn't fit most Ecosystem SA work, and "Partner enablement" versus "Workshop" categorization is ambiguous. Flagged for adjustment after the first months of data.
- **Missing activity type.** "Post-sales support" (available in Rattle) is not yet an option in the new form's dropdown — requested but not yet added.
- **No category for time spent on the form itself.** Requested so the overhead of the new process itself can be measured.
- **Accessibility/workload concern.** Several SAs (especially those with large account pools or who are neurodivergent) flagged that manual, non-automated logging adds cognitive load and risk of under-reporting, without calendar-driven prompts like Rattle/Troops had.
- **Automation in progress.** A tool to help facilitate data entry is under internal review as of 2026-09-07.

**Feedback and feature requests:** Use the [SA Activity Form feedback issue](https://gitlab.com/gitlab-com/customer-success/solutions-architecture-leaders/sa-initiatives/-/work_items/744) for structured feedback, bug reports, and feature requests. Use the Slack thread for general questions (e.g., "How should I record this activity?").

## 6. FAQ

**Do I need to log every internal meeting — 1:1s, team calls, coffee chats, mentorship?**

No. Log only if the meeting is about a customer (prep, pre-call, post-call, planning). This hasn't changed from the old process.

**How long does it take for a new opportunity (not previously assigned to me) to show up in the dropdown?**

The sync runs every 4 hours, with a further ~15-minute cache. If you need to log against something not yet synced, paste the opportunity ID directly — the field doesn't require a validated dropdown selection.

**Does the opportunity/account field require a valid dropdown pick, or can I just type an ID?**

You can just type the ID in directly.

**How do I log a broad event like a marketing summit or webinar with multiple customers?**

Use the Salesforce Campaign ID (starts with `701`). It's in the campaign picker near the bottom of the form; if not listed, paste the ID directly.

**How do I log partner enablement or MDF-funded on-site work?**

Use the partner's Salesforce Account ID — partners are tracked as accounts.

**What do I do if there's no opportunity or account yet (early pipeline / lead stage)?**

Use the Account ID if one exists; if there's genuinely nothing yet, type "Pipeline Gen" into the field.

**How do I log internal contributions like blog posts, onboarding buddy work, or interviews?**

Choose Non-Customer Facing → Activity Type "Other" → describe it in Notes.

**Should I log community events, conference talks, or technology meetups where I'm promoting GitLab?**

Yes — these represent real SA time and often generate pipeline. Log them using the Campaign ID if a Salesforce campaign exists, or the Account ID of the primary customer/partner, or "Pipeline Gen" if nothing is attached yet.

**I'm traveling to visit multiple customers/partners on one trip — how do I log the travel itself?**

Either enter multiple opportunity IDs, or pick one main customer and log the travel there; log each onsite/workshop separately against its own account. Travel can also simply go under Non-Customer Facing, since travel time itself isn't customer-facing.

**Is Rattle going away completely?**

Not entirely. Its use for SA activity tracking stops 2026-09-07, but it stays in place (for now) for other functions like Salesforce case triage (SA Requests) and other automations/notifications. Post-meeting Rattle notifications still fire — the `Log Activity` button has been replaced with a `Capture Activity` link to the new form.

**Can I see a list of everything I've already submitted?**

Not directly in the tool yet. The "Download backup CSV" button exists but only shows Salesforce IDs, not names — consider adding account/opportunity names to your Notes for easier reference. Clearing your browser cache deletes the local backup, so back it up before doing that.

**Will this connect to my calendar so I don't have to log manually after every meeting?**

Not yet — that kind of automation is planned for Phase 2 (an MCP capability writing directly to Salesforce), still in the coming months, subject to approval, as of 2026-09-07. Submit feature requests in the [SA Activity Form feedback issue](https://gitlab.com/gitlab-com/customer-success/solutions-architecture-leaders/sa-initiatives/-/work_items/744).

**As a New Business SA, I don't see most of my assigned opportunities in the dropdown — why?**

Likely because New Business SAs are assigned at the Opportunity level rather than the Account level in Salesforce (same issue affects Command Center). Confirmed as an open, unresolved issue as of 2026-09-07 — for now, paste the opportunity ID manually.

**What if I forget to log something or fall behind?**

Log as close to same-day as possible, weekly at the latest — the message from leadership is that messy-but-honest data beats clean-but-made-up data.

**Where do I submit feedback or feature requests about the form?**

Use the [SA Activity Form feedback issue](https://gitlab.com/gitlab-com/customer-success/solutions-architecture-leaders/sa-initiatives/-/work_items/744) for structured feedback, bugs, and feature requests. Use the Slack thread for quick questions about how to log a specific activity.

## 7. Activity Types

These are the activity types available when logging an activity. They carried over from the previous process; some descriptions still reference Rattle field names and are being updated as the form's dropdown evolves.

### Enterprise and Commercial SA Activity Types

Select these types when capturing activities by Enterprise and Commercial SA teams.

- **Customer No Show** - The SA has the opportunity to log an activity for a scheduled client meeting whereby the customer has not attended. In collaboration with the SAE/AE/Channels Manager, the SA should try to understand the underlying reason for the customers absence and record under the [SA] Activity Description.
- **Customer Strategy Plan Review** - (Note: While this activity type still uses the legacy name "Customer Strategy Plan", it refers to Customer Success Plan activities) Collaborative session between SA and a customer identifying and documenting business stakeholders, high-impact strategic requirements and key technologies, the current state of their technology ecosystem, current and desired capabilities, operational alignment with strategic objectives, and perceived gaps and deficiencies in current capabilities. See [Customer Success Plans](/handbook/solutions-architects/processes/activity-capture/customer-success-plans) for details. When reporting this activity a link to the latest Customer Success Plan must be included.
- **Demo** - The SA can record the activity when a planned GitLab product demonstration has been
delivered to the client. In the [SA] Activity Description field in Rattle, the SA should
also refer to insights around the demonstration purpose and area of product walkthrough. Options could be a full high-level end-to-end GitLab overview, or a specific GitLab stage demonstration, a partial GitLab platform overview or a very specific technical deep dive into the product.
- **Discovery Session** - The SA has the opportunity to record major insights during the initial discovery session with the client. The SA could work with the client in collaboration to understand whether the current environment is restrictive in the project deliverables or whether there is a need to extend the existing platform with our offering. Examples of categorized discovery sessions could be;
  - DevOps discovery discussion
  - Continuous Integration discussion
  - Deployment environment discussion
  - Application front- and back-end discussion
  - Cloud journey and strategy discussion
- **Other** - The SA should utilise this [SA] Activity type to record any activity not listed in the options dropdown list and is reserved for all non-anticipated types of SA services. It is imperative when using this activity type to be precise under the [SA] Activity Description field in Rattle to record the detail of the activity.
- **Post-sales technical account management** - SA uses this type to record technical account management work for accounts that don't qualify for CSM and for collaboration with CSM as part of post sales cadence calls. For growth opportunities to expand the account using the cadence calls, log the activity in other appropriate types.
- **PoV related activity** - It is assumed that the client's indication of a PoV and/or Technical Evaluation would be shared in either a Discovery session or during another [SA] Activity and the PoV related activity would be used by the SA as an activity record pertaining to the preparation, execution and completion of a PoV or a Technical Evaluation. Examples of PoV related activities could be;
  - PoV/Technical Evaluation scoping: The SA has the opportunity to record their activity towards engaging with the client on understanding the requirements and work in collaboration to agree on the type of evaluation [PoV or Technical Evaluation] and on the in-scope success criteria. The client on the other hand has the opportunity to define whether a high- or lite-touch PoV is required. Optionally the client may prefer to decide that a self-managed Technical Evaluation is sufficient and the SA assists ad-hoc.
  - Technical Evaluation cadence: The SA has the opportunity to record their activity with their client specific in relation to the Technical Evaluation. Upon agreeing to a plan, specific requirements and the definition of success, a regular or irregular cadence may be set by the SA with collaboration with the customer.
  - PoV cadence: The SA will often agree to a PoV plan, duration, sign off the in-scope PoV success criteria and work with their client on a regular cadence [weekly, bi-weekly, multi-weekly]. This [SA] Activity is an opportunity to capture the frequency and progress on the PoV. The SA should consider hosting a final cadence session with their client to agree on the sign off of the final completion of the evaluation.
- **Presentation / pitch** - The SA has the opportunity to record their preparation for a presentation to the client as well as the actual delivery. Sometimes a Pitch is requested by our SAEs/AEs due to significant client discussion without a SA, which is completely acceptable. Consideration for this type of [SA] activity are:
  - The SA attended an initial Technical Discovery session with the client and first requirements have been clearly collaborated on with the SA to take initiative to prepare for a presentation.
  - The SA debriefed internally with their SAE/AE/Channels Managers to understand the requirements of a first-time SA connect with the client and the expectation on an initial Presentation / Pitch
- **Ride Along** - This activity type is used when one SA is shadowing another SA to help support the opportunity, provide feedback for the primary solutions architect, and to learn how the primary solutions architect works. Please leverage [the Ride Along](/handbook/solutions-architects/sa-practices/ride-alongs/) handbook page to learn more about how Ride Alongs work. Record this activity on Account level. Recording at the account level is required because ride along that are inter-segment or inter-region will not have their opportunities available to the riders.
- **Guided Trial** - This activity type is used in case a prospect or existing customer needs support from an SA during their self-evaluation by using the GitLab Free trial offering.
- **Security Questionnaire / RFP** - The SA should use this activity type to record actions related to completing security assessments or progressing opportunities through tender processes. Examples of activities that fit into this category are;
  - Security Assessment: Although technically speaking part of the tendering process, Security Assessment generally involve the SA to interact with GitLab governing divisions ensuring accuracy and legal responses. As such, the SA engages with a GitLab division internally to address those Security specific requirements but ahead of the process, the SAs have a responsibility to attempt in the form of a first attempt to the queries.
  - Procurement / Tender process (RFx - RFP, RFQ, RFI, FRB, RFT - Request for Anything): The SA is engaged with the client and an indication has been given that their organisation will be undergoing a public tendering process. Tendering processes could be requesting a proposal, quote, information, expressions of interest and generally result in the SA responding to functional and/or non-functional queries of the GitLab platform as part of a request. Often tendering processes are indicated early, shared fairly with the approaches to take it to market and require a formal process involving the SA addressing technicalities required in form of written artifacts.
- **Technical Deep Dive** - SA should record client sessions on in-depth review of technology and GitLab capabilities, and creating the client solutions.
- **Technical Support** - SA conducts the technical support sessions as the account team and with GitLab Support to troubleshoot and address specific technical issues and challenges.
- **Positioned Professional Services** - This activity type should be used when positioned Professional services as part of the [Solution Architects Processes](/handbook/solutions-architects/processes/#positioning-professional-services)
- **Professional Service Support** - SA have a clear understanding of the client's available internal skills and capabilities and assist their clients in ways to become successful in a quicker way when skills gaps are identified. As a result of that, GitLab Professionals Services support adds customer value to mitigate risk and accelerate speed to success. Since the SA owns the initiation of the ProServ division at GitLab for our customers outlined here - and a significant amount of follow up and cadence is expected as a SA service to our regional customers.
- **SA Assistance - Subject Matter** - A [SA] is requested to support another GitLab Team Member with their advanced knowledge and understanding in a certain subject, without owning the particular engagement or opportunity.

- **SA Assistance - Manager** - To be used by [SA] Manager in case of assisting a customer engagement.

### Strategic Field SA Activity Types

Select these [SA] Activity types when capturing activities by the Strategic Field team but other activity types for Enterprise can also be used.

- **SA Assistance - Strategic Field** - Calls with client's management and executives to review enterprise DevOps strategy and alignment to the overall company initiatives such as digital or cloud transformation.
- **Executive Solution Plan** - Calls with client's management and executives to discuss, strategize and review DevOps solution for organization wide transformation, develop the trusted advisory relationship with industry thought leadership and guide the enterprise for DevOps adoption with best practices.

### Ecosystem SA Activity Types

Select these [SA] Activity types when capturing activities by the Ecosystem team but other activity types for Enterprise can also be used. There is an implied priority with higher value activities listed highest / first to lowest / last.

Multiple activity types can be used on a single activity, please try to tag only the single highest value activity that took place.  For instance, don't add **Partner Cadence Call** if you leveraged the call to conduct **Partner Enablement**.  

Please DO add an MBO related Activity Type on an activity as an overlay tag when you are proposing that Activity be counted toward one of your MBOs.  Add links to Docs, Issues, or place justifying content in the Activity Description when you use the MBO Types.

:movie_camera: Video on [How to quickly Log, Classify and Triage lots of Rattle Entries for the busy Solutions Architect 9:17, Highspot.](https://gitlab.highspot.com/items/67be46c991e055ef7c36de79?lfrm=shp.0) Supplements the below text.

- **ESA MBO Strategic** - _Strategic Partner Activation_ - Partner Activation Plans in place to drive mutual partner technical relationship goals against an agreed timeline.  Leverage the PAP to track partner capabilities, champions, people resources, and Activation Outcomes.
- **ESA MBO Contribution** - _Partner Contribution to Pipeline_ - Elevate partner technical presales capabilities through a structured readiness program defined in the PAP that generates qualified pipeline and revenue contribution
- **ESA MBO Capability** - _Ecosystem Services Capability_ - Accelerate customer onboarding and adoption through integration of services offerings in customer account relationships
- **ESA MBO Commitment** - _Commitment and Advocacy_ - Leverage the GitLab Champions program to drive high-value technical investment and advocacy from partner technical resources

Additionally, Also tag each Rattle Activity with one (and only one) of the following Rattle tags. Partner Opportunity :money_with_wings: :money_with_wings: :money_with_wings: :money_with_wings: :money_with_wings: is the most valueable activity, Partner Cadence Calls is the least valuable activity.

- **Partner Opportunity** - :money_with_wings: :money_with_wings: :money_with_wings: :money_with_wings: :money_with_wings: Sales opportunity # aligned work alongside field SA on specific sales opportunities with a partner involvement. This includes being an overlay SME on partner technologies and its joint value proposition with GitLab and/or helping a channel/services partner become successful with joint customers.
- **Partner Assisted Demand Gen** - :money_with_wings: :money_with_wings: :money_with_wings: :money_with_wings: Delivering or developing customer facing webinars, workshops, roadshows and similar activities in collaboration with a partner, focussed on demand generation / lead generation.
- **Partner VSA Enablement** - Activities involving enablement of partners to pitch or execute Value Stream Assessment and similar presales value selling motions.
- **Partner Technical Evangelism** - :money_with_wings: :money_with_wings: :money_with_wings: Delivering or developing partner facing (not customer facing) events and evangelism, including partner internal conference, meetup, webinar, open-invite bootcamp, blog and customer success stories.
- **Internal Enablement and SME Assistance** - :money_with_wings: :money_with_wings: GitLab facing internal calls, meetings, webinars for partner promotion and GitLab field team assistance.
- **Partner Solutioning** - :money_with_wings: :money_with_wings: Solution architecture work for defining and developing partner solutions and integration with GitLab.  For a work done on a specific sales opportunity, consider "Partner Opportunity."
- **Partner Services Attach** - :money_with_wings: :money_with_wings: Develop partner services catalog and/or SoW for future services engagements.
- **Partner Enablement** - :money_with_wings: Partner facing calls, meetings, workshops, webinars, including prep work to enable partner Champions on GitLab product and pre-sales.
- **Partner Cadence calls** - Cadence calls with partners for partnership building and presales activities on customer opportunities and account strategy.

### Value Stream Workshop (Assessment) Activity Types

**Note:** These options still refer to the old naming of "VSA" but due to ongoing data tracking reasons, we are unable to update the selections. Please be aware of this.

- **VSA Pitch** - This is an initial VSW pitch to the customers/prospects to get their buy in, discuss next steps, send follow ups before the VSW planning meeting
- **VSA Execution** - External customer/prospects calls for VSW planning, VSW workshop, VSW executive presentations.
