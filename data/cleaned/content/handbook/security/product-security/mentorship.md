---
title: "Product Security mentorship program"
description: "An opt-in mentorship pilot that pairs ProdSec team members who want to learn something with people who can help."
---

## Overview

The ProdSec mentorship program gives Product Security team members a structured way to find a mentor, or to become one. You tell us what you want to learn or what you can help with, we pair people up, and each pair works toward a concrete, work-related goal.

We're starting with a pilot that runs for one quarter: Q4 FY27, November 2026 to January 2027. At the end we'll measure how it went against the goals on this page, then decide whether to run another cohort, change the approach, or stop.

The program runs out of a [GitLab project](https://gitlab.com/gitlab-com/gl-security/product-security/mentorship). That's where you'll find profiles, matches, and templates. This page covers the why and the guidance for the program.

[Zach Bright](https://gitlab.com/zbright2), VP of Product Security, sponsors the program. The program team responsible for keeping it running are the [CODEOWNERS](https://gitlab.com/gitlab-com/gl-security/product-security/mentorship/-/blob/main/.gitlab/CODEOWNERS) of the project.

## Goals

### For GitLab

For GitLab, the goal is to grow and develop talented team members so they can produce their best work. We want more depth of expertise across ProdSec, and our senior team members are expected to help build that expertise. Team members across ProdSec already do a lot of mentoring, either implicitly in the work they do or less formally outside it. But some ProdSec teams skew toward Staff and Principal engineers, so the people best placed to mentor have few people to mentor inside their own team. Meanwhile, team members elsewhere in ProdSec want a mentor and don't have an obvious one within their own teams. This program connects mentors and mentees across team boundaries, and makes those pairings explicit and formal. It's designed to help both the mentor and mentee carve out the time, set concrete professional goals, and go beyond day-to-day project or technical help. It also gives us a clearer picture of where the team wants to grow and who can help, while also giving us a partial picture of our current skills and capabilities (for those that have signed up).

### For team members

For individuals, the goal is to line up professional development goals with support. Everyone has something they want or need to learn, and it takes time, opportunity, and support to get there. Plenty of ProdSec team members already find their own mentors, but that doesn't work for everyone. Knowing which skill you want is one thing; knowing who across ProdSec could help you with it is harder. The program does that matching for you and gives the relationship some structure to get started.

### How this connects to our values

These goals line up with GitLab's values and [operating principles](/handbook/company/operating-principles/):

- **Ownership mindset:** The people closest to the work decide and own the result. A mentor who's been there gives you more to draw on when you make those calls, even for situations you haven't faced yet.
- **Speed with quality:** Learning from someone who's already done it is faster than working it out alone. Learning from someone with different experience also helps you approach familiar problems more completely, which leads to better outcomes.
- **Collaboration:** Pairs work across team boundaries, and mentees see how someone else approaches a problem in practice.
- **Culture of excellence and belonging:** This culture expects depth of understanding, skills that produce results, and being good humans to each other. The outcome of mentoring contributes to all three. People who give each other regular feedback also get to know each other, and that builds belonging.

### What it isn't

- Performance management.
- An input to promotion decisions. You can mention your own mentoring work in a promotion document or feedback, the same as any other work you've done, but the program doesn't feed into those decisions.
- A replacement for 1:1s with your manager.
- Mandatory. Nobody has to join as a mentor or a mentee.
- A directory we publish and forget. The program team looks after the project, checks in with pairs during the pilot, announces a new cohort schedule based on team interest, and changes things when they aren't working. The wider ProdSec team contributes what time it can, opting in or out of cohorts based on its capacity. The sponsor and mentee managers encourage the team to reserve time for this program and support the team when they need to defend this time from other priorities. It works when all three groups work together.

## Mentoring and coaching

Mentoring and coaching are both likely to show up during this program, and they're different skills. GitLab's coaching page describes them as [different hats](/handbook/leadership/coaching/#different-hats-for-different-conversations) you can wear in a conversation, and [Lara Hogan](https://larahogan.me/blog/coaching-reflections/) draws the same line:

- **Mentoring** is sharing advice and perspective from your own experience. "Here's how I handled that."
- **Coaching** is helping someone think through their own challenge without handing them the answer. The coach asks questions and listens, and the other person works out next steps.

You'll probably wear a third hat too. Teaching, passing on knowledge to build someone's skills, comes up a lot in the job or project-specific track.

In this program, mentees say in their profile which one they need, or that they're not sure yet. Mentors should know which hat they're wearing during a conversation and switch on purpose. A pair might mostly mentor in one meeting and mostly coach in the next, and that's fine. For how mentoring works across GitLab more broadly, see [Mentoring at GitLab](/handbook/people-group/learning-and-development/mentor/).

Coaching here means peer coaching between ProdSec team members. If you're looking for a professional coach, see [selecting a coach](/handbook/leadership/coaching/#selecting-a-coach).

### Coaching with the GROW model

If coaching is new to you, the [GROW model](https://www.coachingcultureatwork.com/the-grow-model/) gives a conversation a rough, starting shape. It's the same model GitLab's [coaching page](/handbook/leadership/coaching/#grow-model) uses. You don't need to follow it in order. Most conversations start with the goal and where things stand, then move around.

| Stage | What you're doing | Questions to try |
|---|---|---|
| **Goal** | Agree what the mentee wants, from this conversation or from the pairing | What do you want to walk away with today? How will you know you've got there? |
| **Reality** | Look at where things stand right now | What's happening at the moment? What have you tried so far? What's getting in the way? |
| **Options** | Open up possible ways forward before picking one | What could you do? What else? Who could help with this? |
| **Will (to commit; or Way Forward)** | Commit to a next step | What will you do first, and by when? How committed are you to that, out of 10? |

For something lighter, Michael Bungay Stanier's [The Coaching Habit](https://www.mbs.works/coaching-habit-book/) boils coaching down to seven questions, like "What's the real challenge here for you?"

## Requirements

These requirements came from the ProdSec team through [RFC: Building out a mentorship program](https://gitlab.com/gitlab-com/gl-security/product-security/product-security-meta/-/work_items/254) in September 2026 (Q3 FY27).

| # | Requirement | Must / should | How the program meets it |
|---|---|---|---|
| R1 | Mentee-initiated, opt-in on both sides | Must | You join by opening an MR with your own profile. Mentees set their own goal, and Mentors set the skills or experiences they can assist with. Pairing is focused on making sure all mentees get a mentor (with an excess of mentors being preferred over an excess of mentees). |
| R2 | Flexible format that allows for job/project-specific mentoring and broad career mentoring | Must | Two mentorship tracks with light structure to support specific jobs/projects, or more broad mentorship. Profiles say which track a mentee needs or a mentor can support. |
| R3 | Anchored to something concrete and work-related | Must | Every pair records a goal and success criteria at kickoff. Even if small (e.g. be able to demonstrate a skill in a controlled dev / practice environment) or big (e.g. finish delivering a project where new skills were required). |
| R4 | A perspective from outside your own team is reachable | Must | The matching pool is all of ProdSec. |
| R5 | Coaching and mentoring defined | Should | [Mentoring and coaching](#mentoring-and-coaching) on this page, and the mentor guide in the project. |
| R6 | Templates to start, organic afterwards | Must | A kickoff template for the first meeting, then a recommended (not required) structure for the meetings after that. |
| R7 | Time-boxed and formal enough (with documentation, templates, leadership support) to be taken seriously | Should | A one-quarter pilot, sponsored by the VP of Product Security and measured against its goals at the end. See [Measuring the pilot](#measuring-the-pilot). |
| R8 | We know what skills people can teach | Must | Mentor profiles list what they can help with, which is input into matching. |
| R9 | Mentors are prepared (especially if mentorship is new to them) | Must | A written mentor guide in the project, covering how to be an effective mentor and when to mentor versus coach. |

## How it works

### Tracks

- **Job or project-specific.** You want to get better at something you need for your work right now, like a specific technology, a part of the GitLab codebase, or security skill.
- **Broader career.** You want perspective on where you're heading, such as moving to Staff, trying management, or getting better at influencing without authority.

Be upfront about what you can offer or need. Job or project-specific mentoring usually takes more hands-on time than broader career conversations, so mentors should only list the tracks they have time for. If you only have time for broader support, that's fine: say so in your profile. Mentees, pick the track you need, so we can match you with someone who can support it.

### Joining

1. Read this page, including the [expectations](#expectations).
1. Open an MR in the [program project](https://gitlab.com/gitlab-com/gl-security/product-security/mentorship) using the profile template, and pick the cohort you're joining. Mentees describe what they want to learn, which track, and what "done" looks like. Mentors describe what they can help with and which track they can support. Your profile lists the cohorts you've joined. Sit one out by not adding it, and add the next one when you're ready.
1. Join [#security-mentorship-program](https://gitlab.enterprise.slack.com/archives/C0C5R9VPWCW). It's where we post program updates and check-ins, and where you can ask questions.

Your profile is visible to all of GitLab internal. Only include things you're happy for those people to see.

When you sign up you can also fill in an optional baseline form. It records where you're starting from, so you can compare yourself at the end. Forms record your name, so we can follow up on blockers and show you your baseline next to your final answers. Only the program team sees responses, and anything we share is in aggregate and never traced back to an individual.

### Matching

The program team pairs mentees with mentors based on what each mentee wants to learn and what each mentor can help with. Each match is recorded in the project along with why the pair was matched.

To draft pairings, we use a Claude skill in the program project. It only reads what's in the profiles, and someone on the program team reviews every pairing before it's final.

Matching makes sure every mentee gets a mentor first. If there aren't enough mentors in ProdSec, the program team contacts the mentee and their manager to find a mentor outside ProdSec. That pairing is arranged outside the program, but the mentee still gets a match file. That way they're included in the check-ins and the final measurement, and can be matched in ProdSec next cohort if they want.

We don't pair anyone with their own manager or a direct report, and the program team checks this on each match.

If it's your first time mentoring, we'll pair you with one mentee who has, where we can, a more focused goal.

### Getting started as a pair

The mentor is responsible for scheduling the first meeting and preparing its agenda from the kickoff template, and the mentee keeps their calendar up to date so it's easy to set up. The kickoff template includes a short set of discovery questions for you both to work through. They help you learn how the other person works, and they end with a goal. Write that goal down in one line: "By the end of the pilot I want to \_\_\_, and I'll know it worked if \_\_\_."

From the second meeting on, the mentee leads, the same way [mentoring works across GitLab](/handbook/people-group/learning-and-development/mentor/#expectations) and the same way you lead your own 1:1s. The project has a recommended structure for ongoing meetings, but there's no fixed template. Keep a shared agenda at whatever level of detail suits you both. If you're in different time zones, pick a recurring slot early and try to stick to it.

### Support for mentors

Read the mentor guide before your first meeting. GitLab's [mentor and mentee training](/handbook/people-group/learning-and-development/mentor/#mentor-and-mentee-training) is also a good self-paced place to start. Mentors in the pilot are invited to a private Slack channel, #security-mentor-club, to compare approaches and ask each other for help. It's private on purpose, so mentors can build trust with each other as a peer group. Keep discussions about how you mentor, not about your mentees: what you and your mentee talk about stays between you. That's separate from [#security-mentorship-program](https://gitlab.enterprise.slack.com/archives/C0C5R9VPWCW), the public channel for everyone in the program, mentees included. If you need help with a specific pairing, DM the program team. Once sign-ups close, we'll look at how many mentors are new to this and add more support if we need to.

### Time commitment

Plan on at least 30 minutes a week for each mentee. Mentors with more than one mentee should plan for that time per mentee.

### Check-ins

We'll send a few check-ins during the pilot. Each one is a handful of questions that takes a couple of minutes. They're there to catch blockers early, not to grade anyone, and they ask whether things are happening (not what you talked about). You can expect:

- **2 weeks in:** Have you met, and have you set a goal? Is anything in the way?
- **6 weeks in:** How's it going, and is anything in the way?
- **2 weeks before the end:** Would you like to join another cohort?
- **After the pilot ends:** How did it go overall?

Forms record your name, so we can follow up on blockers and show you your baseline next to your final answers. Only the program team sees responses, and anything we share is in aggregate.

### If a pairing isn't working

Either of you can end a pairing at any time. For mentors, we expect you to have a closing conversation with your mentee rather than stopping quietly. For both, reach out to the program team if you want to end a pairing and let us know why. That stays with the program team, and it helps us with a rematch (if you want one) and with improving the program.

## Expectations

GitLab's [mentoring expectations](/handbook/people-group/learning-and-development/mentor/#expectations) apply here too. That includes confidentiality: what you talk about stays between you unless you both agree to share it. On top of those, this program asks for a few specific things.

### Mentees

- Own your goal. You decide what you're working on and what "done" means.
- Lead your meetings after kickoff, and bring topics to the shared agenda.
- Keep your calendar up to date so it is easy to schedule (or re-schedule as needed).
- Tell your mentor what's helping and what isn't.

### Mentors

- Read the mentor guide before your first meeting.
- Schedule the first meeting and prepare its agenda from the kickoff template.
- Be clear whether you're mentoring or coaching, and ask which one your mentee wants.
- Respect your mentee's choices. Your role is to guide, and they decide what to do with it.
- Be honest about how much time you have, and don't overcommit. If you're unsure, start with a smaller commitment for a cohort, like one mentee or one track, and see how it goes.

### Both

- Plan for the [time commitment](#time-commitment) and protect it.
- Answer the check-ins.
- Tell the program team early if something's getting in the way.
- Keep the goal in view. Revisit it every few meetings and adjust it if it's changed.
- (Optional) Fill in the baseline Google Form to help yourself and the program team track how the pilot is performing.

## Pilot timeline

The current pilot runs through Q4 FY27 (2 November 2026 to 31 January 2027). Dates below are approximate until the program team confirms them.

| Milestone | When | Approximate date |
|---|---|---|
| Announce the program and open sign-ups | 3 weeks before Q4 FY27 | Week of 12 October 2026 (Q3 FY27) |
| Sign-ups close | 10 days before Q4 FY27 | 23 October 2026 (Q3 FY27) |
| Pair mentors and mentees; share kickoff templates | Week before Q4 FY27 | Week of 26 October 2026 (Q3 FY27) |
| Pilot starts | Start of Q4 FY27 | 2 November 2026 (Q4 FY27) |
| First check-in | 2 weeks in | Week of 16 November 2026 (Q4 FY27) |
| Second check-in | 6 weeks in | Week of 14 December 2026 (Q4 FY27) |
| Gauge interest in the next cohort | 2 weeks before the end | Week of 18 January 2027 (Q4 FY27) |
| Pilot ends | End of Q4 FY27 | 31 January 2027 (Q4 FY27) |
| Final check-in opens (closes 19 February 2027) | Week after the pilot | Week of 1 February 2027 (Q1 FY28) |

## Measuring the pilot

One quarter is too short to show long-term career impact, and we're not asking anyone to commit beyond it. What it can tell us is whether the program works well enough to keep running and keep measuring. At the end, we'll decide whether to continue, change the approach, or stop, based on these questions:

| Question | What we'll look at | We'd call it working if |
|---|---|---|
| Do people want it? | Sign-ups as mentees and mentors, and whether every mentee got a mentor | Every mentee who signed up was matched |
| Do pairs actually meet? | How often pairs met, from the 6-week and final check-ins | At least 70% of pairs met every other week or more |
| Are mentees getting somewhere? | Where mentees ended up with their goal | At least 70% reached, got closer to, or reframed their goal |
| Is it worth the time? | Satisfaction, and whether people would take part again | At least 70% would take part again |
| Did support get better? | The support and confidence questions, baseline next to final | Scores go up, for those who filled in both |
| Were mentors ready? | Mentor confidence, and whether the mentor guide helped | Most mentors found the guide useful |
| Do we know more about the team? | What mentees want to learn, next to what mentors can help with | We can see where the gaps are |

We'll also look at how many pairings ended early and why. Results are shared in aggregate only, never for groups small enough to identify someone. We'll post what we learn and the decision in the program project.

## Training and expenses

The program doesn't come with its own budget. If training opportunities are identified for a mentee or mentor to take (separately) to grow skills they need, this can be discussed (with their managers) as part of their G&D budget.

## Related resources

- [Mentoring at GitLab](/handbook/people-group/learning-and-development/mentor/), which covers mentor and mentee training, goal setting, sample agendas, and how to end a mentorship
- [Become a mentor](/handbook/people-group/learning-and-development/mentor/#become-a-mentor) on the GitLab team page, if you'd like to be findable outside this program too
- [Coaching](/handbook/leadership/coaching/), including the GROW model and how to find a professional coach
- [Growth and development benefit](/handbook/people-group/learning-and-development/growth-and-development/)

## Questions and feedback

Feedback on how the program works is welcome, especially before the first cohort starts. Ask in [#security-mentorship-program](https://gitlab.enterprise.slack.com/archives/C0C5R9VPWCW) or open an issue in the [program project](https://gitlab.com/gitlab-com/gl-security/product-security/mentorship/-/issues).
