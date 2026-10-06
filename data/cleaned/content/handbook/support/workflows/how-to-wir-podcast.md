---
title: How to do a WIR Podcast
category: References
description: General guide for creating a Support Week-in-Review Podcast
---

## Overview

Use this workflow as a general guide when you need to record and publish a Support Week-in-Review Podcast.

Much of this is done in the [Support Week in Review Project](https://gitlab.com/gitlab-com/support/readiness/support-week-in-review). For more information about the CI/CD jobs used in this guide and what they do, refer to the project [readme](https://gitlab.com/gitlab-com/support/readiness/support-week-in-review/-/blob/main/README.md).

---

## Workflow

You'll find an appointment in the Support Team Google calendar for the recording session (near the end of the week). Use the Zoom link in there so that others can participate in the recording if they want to.

### Before the Recording

There are 3 steps - please take them in the documented order. This ensures the draft SWIR digest issue email notification includes everything except for the phrase of the week.

1. [Prepare customer feedback](#1-prepare-customer-feedback-from-tickets-input)
1. [Prepare the metrics](#2-prepare-the-metrics)
1. [Prepare the digest issue](#3-create-the-digest-work-item)

#### 1. Prepare customer feedback from tickets input

- Feedback is gathered into the SSAT work item in the [SWIR project](https://gitlab.com/gitlab-com/support/readiness/support-week-in-review/-/issues)
- Some input will have been provided by managers during the week, but most will need to be ingested using the `populate_ssat_v2` job from the pipeline
- Run `populate_ssat_v2` job - this will gather any open positive feedback into the SSAT work item
- Review the content (automated or other) and make corrections and remove anything that is not actually positive. 
- Note that anything received through mid-ticket feedback will not have an assignee name populated but instead a placeholder of `checkticket` - it is doubly important to review the feedback in these to verify the words are affirming feedback appropriate to share in this Kudos section, and also replace the placeholder with the name of the ticket assignee if the feedback will be included. 
  If there is a lot of content, consider reducing the number by removing some items that are short and not personalised - use your judgement here. Remove the line about "automated content".

#### 2. Prepare the metrics

- Edit the `Metrics - <date>` work item
- Observe the current number of total pairings in the [open pairings milestone](https://gitlab.com/groups/gitlab-com/support/-/milestones?search_title=pairing&state=&sort=). Compare it to the previous week's SWIR to determine how many new pairings were created since then. Add these details to the work item.
- Take screenshots of the key metrics from the [MM: Support KPIs](https://gitlab.zendesk.com/explore/studio#/dashboards/3DC60497A02C9E0EDB02ECE9C20153733D4AF220B656C550418FF2E42B7E2329) Zendesk dashboard and insert them into the work item where indicated. The following 4 items need to be included:
  - From the SWIR tab: the top row of 4 graphs, from `Total average CES` through to volume
  - From the SWIR tab: scroll to the bottom of `Total FRT SLA achievement - Last 4 Weeks` and capture the current week
  - From the SWIR L&R tab: the top row of 4 graphs, from `Total average CES` through to volume
  - From the SWIR L&R tab: scroll to the bottom of `L&R FRT SLA achievement - Last 4 Weeks` and capture the current week
- Type the key metrics values into the appropriate sections of the work item
- Refer to the [U.S. Government team call document](https://drive.google.com/drive/u/0/search?q=U.S.%20Government%20Support%20Team%20Call) for the USGov metrics and add them to the work item
- Save the Metrics work item

#### 3. Create the Digest work item

- run the `create_digest_issue` job. This will collate all of the team contributions, customer feedback, KB Articles & Metrics into a new digest work item
- Edit the SWIR digest work item and add a phrase of the week as the title

### Making the recording

1. Join the Zoom room in the team calendar appointment for SWIR
1. Determine speaking order for narrators. A useful set of conventions is:

   - Read in alphabetical order by your first initials.
   - If you have an item and it comes up, you will read it which will reset the order.

1. Review the content of the items you'll be narrating

   - review each link and understand what is being expressed by the point
   - check you know how to pronounce any names you'll need to read
   - by convention, we verbalize work item and MR links by reading out their project name and number, such as "Support Team Meta 1234", or "Handbook MR 4321". You can see these while narrating by hovering over the link. This is particularly important when the item has a "here-link" such as "see **this work item**".
   - typically we'll read new team member introductions in 1st person and note that we are doing that before reading it out

1. When everyone is ready, begin recording. It's easiest for the person publishing the recording to "Record locally", so that they'll have the audio on their computer for processing and upload.

### After the recording

1. [Publish](#publish-the-podcast) the podcast
1. [Prepare SWIR for the next week](#prepare-swir-for-the-next-week)

#### Publish the Podcast

Once you have completed the recording and Zoom has finishing processing it:

1. Optional: add the theme music to the recording if you have it
1. Upload it to the [Support Week in Review - Audio Edition](https://drive.google.com/drive/search?q=%22Support%20Week%20in%20Review%20Audio%20Edition%22%20type:folder) folder
1. Change the Sharing Settings to "Anyone within GitLab can View"
1. Copy/paste the URL into the Digest work item below the TOC (there is a placeholder to add it into)
1. Share the link into Slack - there is a slackbot reminder in #support_team-chat at 23:00 UTC on a Thursday - you can share the audio link and a link to the digest work item as a threaded reply to that conversation.

#### Prepare SWIR for the next week

1. Run the `close_week_and_create_new_milestone` job
1. You're done!

#### Notes on customer feedback content

The purpose of including customer feedback content in the Support Week in Review is two-fold:

1. To highlight behaviors and ways of interaction that customers value in their own voices.
1. To highlight the excellent work on the part of individuals and groups of individuals that take place in ticket interactions.

We do not include every piece of feedback every week, both for brevity and because not every item fulfills the purposes above.

With the above purposes in mind, customer feedback comments in the Support Week in Review should:

- be truly positive! Avoid feedback that disparages other engineers, GitLab teams or are back-handed compliments that include a mix of praise and negative feedback.
- have significant, thoughtful or interesting comments.
- be for a mix of Engineers. Sometimes a particular engineer may have multiple positive reviews in a week: try to get a cross-section of the team included.
- highlight the accomplishments of new team members when possible: a first positive feedback in the SWIR should be called out and celebrated!
