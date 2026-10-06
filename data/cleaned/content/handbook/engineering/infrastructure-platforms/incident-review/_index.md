---
title: "Incident Review"
---

> The primary goals of writing an Incident Review are to ensure that the incident is documented, that all contributing root cause(s) are well understood, and, especially, that effective preventive actions are put in place to reduce the likelihood and/or impact of recurrence.[^1]

## Introduction

An Incident Review is a **crucial opportunity for fostering deeper understanding** within a blameless culture. Its purpose extends beyond collecting action items to prevent recurrence; it is a process for learning about both the **systems** and the **engineering culture** that contribute to incidents. By discussing and analyzing how these components operate and interact, we gain valuable insights into the technical environments we support and the broader organizational context in which they function.

At GitLab we are committed to the practice of blameless incident reviews. This means we intentionally focus on understanding the "why" and "how" of incidents, rather than assigning blame or seeking to identify individuals at fault. Incident Reviews may contain references to individuals or team names to help provide a first hand account and valuable context, but these references are never intended to cast blame. Instead, they serve as a means to better understand the sequence of events, the decision-making processes involved, and the challenges faced during the incident.

We adhere to this blameless model to encourage open communication, trust, and close collaboration. It allows everyone to share their perspectives and observations without fear of retribution.

While continuous learning is the primary and paramount focus of these blameless reviews, they also serve a practical purpose. They lead to the identification and implementation of actionable improvements that enhance the resilience and reliability of our systems, ultimately strengthening our engineering culture and improving our ability to serve our users.

## Template

- The [Review Initiator](#review-initiator), most commonly the incident lead, will open an incident review issue in the [GitLab.com Production Tracker](https://gitlab.com/gitlab-com/gl-infra/production/-/issues/new) or the [Dedicated issue tracker](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team/-/work_items/new?description_template=internal_incident_review) following the Post-incident task assigned in the incident slack channel or incident issue dashboard.
- Incident review template can be edited here: https://app.incident.io/gitlab/settings/post-mortem

## Roles

There are three roles in every incident review: the **Review Initiator** who opens the review, the **DRI** who drives it to completion, and the **Bar Raiser** who approves it as complete. There may be many other participants contributing to the RCA, corrective actions, and incident details beyond these roles.

### Review Initiator

The Review Initiator is most commonly the Incident Lead. For all `Severity::1` and `Severity::2` incidents, the Incident Lead is responsible for opening the review issue as part of the post-incident tasks. For all other incidents, anyone can request a review by applying the `Review-Requested` label to the incident issue and opening the review issue themselves.

The Review Initiator is responsible for opening the review issue using the appropriate template and adding the initial metadata. This includes:

- Setting the appropriate issue title
- Linking the review to the incident
- Finding the appropriate DRI to own the review and assigning them the issue

### DRI

The team owning the service or feature is the DRI for the incident review - there are no exceptions. The Engineering Manager may delegate driving the review to a team member, but the EM ultimately owns the review and is responsible for its completion.

The DRI is responsible for driving the review by pulling appropriate people in for further input and details and engaging them in discussion.

The service owner has the most context around the service, even when they were not directly involved in the incident, and they ultimately own the reliability of their service. This ensures the right people understand what happened and why.

The DRI shall:

- Engage people that were involved in the incident (EOC, IMOC, CMOC, other engineers and stakeholders) in discussion
- Ask probing questions to gain further insight leading to corrective actions
- Do the corrective actions ensure a similar issue will not reoccur? If not, keep probing and consider expanding who is involved in the review.
- Link and create [corrective actions](/handbook/engineering/infrastructure-platforms/incident-management/#corrective-actions), [infradev](/handbook/engineering/workflow/#infradev) issues, or any other actions or outcomes from the incident. All actions need to be assigned to a team before the review can be closed.
- Own the [public RCA](#public-rca) where one is required
- Request [Bar Raiser](/handbook/engineering/infrastructure-platforms/incident-review/bar-raiser/) review once the review is initially drafted and again once it is ready for closing. See [Finding a Bar Raiser](/handbook/engineering/infrastructure-platforms/incident-review/bar-raiser/#finding-a-bar-raiser) for who to ask.
- Close the review before the due date, after Bar Raiser approval.

### Bar Raiser

The Bar Raiser panel reviews all incident reviews. **A review must have Bar Raiser approval before it can be closed.**
See the [Bar Raiser](/handbook/engineering/infrastructure-platforms/incident-review/bar-raiser/) page for how reviews are
assigned to Bar Raisers and how to become one.

The Bar Raiser upholds high standards in our incident reviews in the same way maintainers uphold standards in our code. They are not there to tell people how to run a review or what they are doing wrong. They are there to ask hard questions, to probe in ways others have not thought of, and to ensure the resulting corrective actions make sense and are truly what is needed to improve our reliability and prevent recurrence.

The Bar Raiser panel is a group of peers to the incident review DRI: Engineering Managers, Product Managers, and Staff+ engineers who are well versed in the value a high quality incident review can deliver.

The Bar Raiser is not responsible for driving or owning the incident review they are participating in and are not responsible for ensuring it meets our SLO. That is the responsibility of the DRI.

## Guidance for conducting a review

These are questions every DRI should be considering, and that a Bar Raiser is likely to ask. If they apply, the answers should be clear through the incident review and the resulting corrective actions.

1. Is the root cause clearly identified?
1. Do the corrective actions reflect what the type of root cause was?
1. Did we have the right observability?
1. Did we have the right process?
1. For changes, did we release it through the right control flow?
1. Did we miss it in testing?
1. How could we have detected faster?
1. How could we have mitigated faster?
1. Are there areas outside of this specific impact that need to be addressed in the same fashion?
1. Have we truly eliminated risk of recurrence through the corrective actions?

Not every question applies to every incident, and a review is not a form to fill out. Where a question does apply and the review does not answer it, that gap is often where the most valuable corrective action is hiding.

### Match corrective actions to the type of root cause

Fixing the immediate breakage is rarely enough. The corrective actions should also address whatever allowed that class of problem to reach production in the first place, and what that means depends on the kind of cause we identified:

- **A code change**: what let the defect escape? Look at test coverage, code review, feature flag usage, staged rollout, canary, and how quickly the change could be reverted. If a code change caused the incident and none of the corrective actions reduce the chance of a similar defect escaping again, the review is not finished.
- **An infrastructure or configuration change**: was the change made through the expected control flow, was it reviewed, was it applied progressively, and could it be rolled back?
- **Capacity or saturation**: were the limits known, were they monitored, and did we have headroom and alerting ahead of the failure point rather than at it?
- **A dependency or external service**: did we degrade gracefully, and did we have a timeout, retry, or fallback appropriate to that dependency?
- **A user caused incident (malicious or non-malicious)**: did we have the right limits, could we detect and identify the user and cause quickly, did we have the tools to stop the problem?

The same logic applies to detection and mitigation. If it took an unexpectedly long time to notice or to recover, that is its own contributing cause and deserves its own corrective action, separate from whatever triggered the incident.

## Incident Review Completion

A review is complete and may be closed when:

- The DRI has finished the narrative and RCA
- Corrective actions have been created and assigned to the appropriate team
- A Bar Raiser has approved it
- The [public RCA](#public-rca) has been published, where one is required

## Public RCA

For `Severity::1` incidents, customers expect a public RCA to be available as soon as possible.

**The DRI owns the public RCA.** This is not a separate hand-off to another team - the same person or team that owns the incident review is responsible for the public version being available within the [SLO](#timeline-that-we-expect-for-reviews-to-be-completed). Sometimes this includes coordinating with support or specific technical account managers.

When the internal incident review can be published as-is, the DRI makes it public to publish it directly. When it cannot be made public because it contains RED data, customer identifying information, security sensitive detail, or internal-only context, the DRI is responsible for writing a public-facing version of the review and publishing that within the same [SLO](#timeline-that-we-expect-for-reviews-to-be-completed). Needing separate internal and public facing reviews is not a reason to miss the deadline.

A public-facing version should still tell the customer what happened, what the impact was, what caused it, and what we are doing to prevent it happening again. It is a shorter and less internal document, not a vaguer one.

For GitLab Dedicated, external RCAs additionally follow the [Dedicated external RCA process](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team/-/blob/main/runbooks/on-call.md#external-rcas) which may require additional comms approvals before release to the customer.

See also the general [Root Cause Analysis](/handbook/engineering/workflow/root-cause-analysis/) handbook page.

## Weekly Incident Review Meeting

The Weekly Incident Review meeting is a working session where we review all high severity incidents from the past week, whether or not their incident reviews have been completed.

- **Cadence**: Weekly
- **Audience**: Open to all Engineering Managers and individual contributors. Representatives from the DRI team for the incidents under discussion are expected to attend.
- **Scope**: All `Severity::1` and `Severity::2` incidents from the previous week

This meeting complements the [Operational Excellence](/handbook/engineering/infrastructure-platforms/operational-excellence/) incident deep dives. Where Operational Excellence reviews a small number of completed incident reviews with Engineering leadership, the Weekly Incident Review creates a setting for EMs and ICs to come learn about recent incidents and provide input and feedback while reviews are still in progress. Feedback raised in this meeting can and should feed directly into ongoing incident reviews.

Discussion in the meeting does not replace the async review or Bar Raiser approval. The DRI is responsible for summarizing any relevant discussion back onto the incident review issue.

## The criteria which triggers a review

1. All user facing high severity (Severity::1 and Severity::2) incidents require a review
1. Any incident where a `Review-Requested` label has been added to the incident issue
1. Any incident where more information is required outside of the scope of the incident itself

## Customer Engagement

Incident reviews may require customer engagement through a point of contact such as a Technical Account Manager (TAM).
In case of a customer requiring a sync to discuss a finding that comes out of review, the TAM can engage with the Infrastructure management to organize the discussion with important stakeholders.

[^1]: Google SRE Chapter 15 - Postmortem Culture: Learning from Failure

## Unowned Services

There may be some services which do not have a team which owns it. When ownership is unclear, a team closest to or with the most knowledge of the service is expected to step up and own the review.

## Timeline that we expect for reviews to be completed

It is expected that the incident review will be closed **within 5 working days of the incident resolution**. Customers should expect the [public RCA](#public-rca) to be available within **7 days** of the incident resolution for Severity 1 incidents. [Internally, we hold ourselves to a tighter SLO](https://internal.gitlab.com/handbook/engineering/infrastructure/rca-publication-slo/), please be familiar with the expected completion date.
