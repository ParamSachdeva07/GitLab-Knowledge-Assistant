---
title: "PSIRT Holiday and Friends and Family Day Coverage"
---

This runbook describes the process for times when the Product Security Incident Response Team has team members available during holidays, Friends and Family days, or other events where many team members are expected to be out of office.

Since PSIRT is not on-call, we aim to provide this best-effort coverage that may or may not be available in every region.

If you need assistance:

- Post in `#security_help` with details
- Find the PSIRT engineer providing coverage - see [Communicating the coverage](#communicating-the-coverage) below
- Reach out to the team member via Slack `@` mention
- If urgent or the team member does not respond in a timely manner, reach out via text message or phone call after checking the contact preferences listed on their Slack profile
- If it is unclear who is providing coverage, ping the `@psirt-team` in Slack

## Expectations for those doing coverage

- In the event that PSIRT is needed to respond to an S1 incident or otherwise urgently assist another team, the team member providing coverage should be reachable by Slack or phone
- PSIRT team members providing coverage are not expected to be at the keyboard and working, but they should be able to get online within one hour if needed
- If they are not actively working during coverage times, they should try to check Slack occasionally for pings
- They should occasionally check for potential S1s coming in through HackerOne and take action if it requires immediate attention
- If an S1 incident occurs or PSIRT assistance is urgently needed by another team, the expectation is that the PSIRT team member will attempt to triage the situation and escalate as needed to a security manager

## Planning

When holidays or Friends and Family days are coming up, the PSIRT team should try to find a team member who can swap their day off. Ideally a team member for each region would be available, but it is not necessarily required.

Use the [Rotation Management](https://gitlab.com/gitlab-com/gl-security/product-security/appsec/tooling/rotation-management) issue tracker to assign & coordinate coverage.

## Communicating the coverage

The [HackerOne Triage Rotation](/handbook/security/product-security/security-platforms-architecture/application-security/runbooks/triage-rotation/) handbook page has information on the rotations and who is assigned.

The PSIRT team will post a Slack message in `#security_help` with information on who is available, when they are available, and how to get in contact if PSIRT assistance is urgently needed. This should be cross-posted to the `#security` and `#security-division` channels for extra visibility.

Each PSIRT team member providing coverage will have their mobile phone number available in their Slack profile.

Should an incident occur, the ["Handling S1/P1s procedure"](/handbook/security/product-security/psirt/runbooks/handling-s1p1/) will be followed, which includes handing over to the next PSIRT engineer.
