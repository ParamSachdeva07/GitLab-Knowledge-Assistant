---
title: "Incident Review Bar Raiser"
description: "What it means to be an Incident Review Bar Raiser, how reviews are assigned, and how to become one."
---

This page covers the [Bar Raiser](/handbook/engineering/infrastructure-platforms/incident-review/#bar-raiser) role in
detail: what the role is, how reviews are assigned, and how to get involved. For the incident review process itself,
including the other roles and the completion criteria, see the
[Incident Review](/handbook/engineering/infrastructure-platforms/incident-review/) page.

## What a Bar Raiser is

The Bar Raiser panel reviews all incident reviews. **A review must have Bar Raiser approval before it can be closed.**

The Bar Raiser upholds high standards in our incident reviews in the same way maintainers uphold standards in our code. A high level overview of the role is in the [Incident Review Bar Raiser](/handbook/engineering/infrastructure-platforms/incident-review/#bar-raiser) section.

## What a Bar Raiser is not

1. **Not the author.** The Bar Raiser does not write the review, fill in the timeline, or create the corrective actions.
1. **Not the schedule owner.** Missing the [review SLO](/handbook/engineering/infrastructure-platforms/incident-review/#timeline-that-we-expect-for-reviews-to-be-completed)
   is the DRI's responsibility, not the Bar Raiser's.
1. **Not an approver of record for the fix.** Approval means the review meets our standard for understanding and
   corrective actions, not that the Bar Raiser has verified the code or configuration changes themselves.
1. **Not a gate on blame.** Reviews are [blameless](/handbook/engineering/infrastructure-platforms/incident-review/#introduction).
   A Bar Raiser who sees blame in a review should ask for it to be reframed.

## Process

### Finding a Bar Raiser

Bar Raisers are assigned on a rotation using
[the Bar Raiser on-call schedule](https://app.incident.io/gitlab/on-call/schedules/01M0DVR0FZKQ2DSAKKGJQY26FX),
which has a Primary and a Secondary rotation.

To find the Bar Raiser for a review:

1. Visit [the Bar Raiser on-call schedule](https://app.incident.io/gitlab/on-call/schedules/01M0DVR0FZKQ2DSAKKGJQY26FX)
   and request review from the **Primary**.
1. If the Primary is out of office, use the **Secondary**.
1. If both are out of office, ping `@gitlab-com/gl-infra/incident-review-bar-raisers` in
   [#incident-review-bar-raisers](https://gitlab.enterprise.slack.com/archives/C0BPK9Y6GMR) to request help.

The rotation exists so that the work is shared evenly and so that a DRI never has to guess who to ask. It is not an
on-call obligation in the way an incident rotation is: reviews are asynchronous, so being Primary does not require
immediate response, and it should not affect vacation time or other commitments. When you are away, the Secondary and
the wider panel cover for you.

### Requesting a Bar Raiser review

The [DRI](/handbook/engineering/infrastructure-platforms/incident-review/#dri) should seek a review from the Bar Raiser as soon as the incident review is initially drafted so the BR can provide feedback quickly. The DRI requests review by 'at'-mentioning the Bar Raiser on the incident review issue.

### Giving a bar raiser review

Bar Raisers give feedback in comments on the incident review issue so that the discussion stays with the review. When
the review meets our standard, the Bar Raiser records their approval on the issue, which unblocks the DRI to close it.

The Bar Raiser shall:

1. Strive to have a first response within 12h of a mention/ask for review - including a response to ask other Bar Raiser's for help.

1. Read the review with fresh eyes and ask the questions that have not been asked yet, or re-ask questions that haven't
   been answered deeply enough
1. Probe whether the contributing causes are genuinely understood, not just described
1. Challenge whether the corrective actions address the real problem, and whether they are sized and prioritized
   appropriately
1. Push back when a review is incomplete, superficial, or leaves obvious threads unpulled
1. Approve the review when it meets our standard, unblocking the DRI to close it

The [Guidance for conducting a review](/handbook/engineering/infrastructure-platforms/incident-review/#guidance-for-conducting-a-review)
section lists the questions a Bar Raiser is likely to ask, including how corrective actions should match the type of
root cause. Those questions are the shared standard for both roles: the DRI should be considering them while writing,
and the Bar Raiser should be checking them while reviewing.

## How to become a Bar Raiser

Being a bar raiser is open to anyone with interest in building a culture of operational excellence and reliability for our customers. If you want to help raise the quality of our incident reviews:

1. Join [#incident-review-bar-raisers](https://gitlab.enterprise.slack.com/archives/C0BPK9Y6GMR) in Slack.
1. Ask an existing Bar Raiser in that channel to add you as an Owner of the
   [incident-review-bar-raisers group](https://gitlab.com/groups/gitlab-com/gl-infra/incident-review-bar-raisers/-/group_members).
1. When you are ready to start taking on reviews, ask Steve Abrams to add you to the Primary and Secondary rotations in
   [the Bar Raiser on-call schedule](https://app.incident.io/gitlab/on-call/schedules/01M0DVR0FZKQ2DSAKKGJQY26FX).

A good way to build context before joining is to read recent incident reviews, follow the discussion in
[#incident-review-bar-raisers](https://gitlab.enterprise.slack.com/archives/C0BPK9Y6GMR), and attend or watch recordings of the
[Weekly Incident Review Meeting](/handbook/engineering/infrastructure-platforms/incident-review/#weekly-incident-review-meeting),
where recent high severity incidents are discussed while they are fresh and reviews may still be in progress.
