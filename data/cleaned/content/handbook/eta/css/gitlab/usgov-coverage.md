---
title: 'US Government Coverage'
description: 'Documentation on US Government Coverage'
---

This guide covers what the US Government Coverage is and how it works.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
- Project: [US Government Coverage](https://gitlab.com/gitlab-support-readiness/usgov-coverage)
- Pages: [https://usgov-coverage-0aa7ea.gitlab.io/](https://usgov-coverage-0aa7ea.gitlab.io/)

{{% /alert %}}

## What is it

US Government Coverage is a project that generates GitLab Pages to display coverage information for the US Government Support team.

## How is it generated

Every 4 hours via pipeline schedules, the `bin/generate_pages` script is run, which does the following:

- Reads Support team information via the [Support Team project](https://gitlab.com/gitlab-support-readiness/support-team)
- Removes all non-US Government support engineers from the Support team information
- Creates variables storing the list of people per shift (1st, 2nd, 3rd)
- Fetches Google calendar events for the next 365 days
- Analyzes the events (separating them into variables for later parsing)
- Generates event objects (that will work with the [FullCalendar JS library](https://fullcalendar.io/))
- Updates templated HTML and JS files

The end result are modified files in a `public` folder, which is then deployed via GitLab Pages.

## Common issues and troubleshooting

This is a living section that will have items added to it as needed.
