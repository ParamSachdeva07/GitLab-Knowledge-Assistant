---
title: Zoom Security
description: Configure passcodes and authentication
---

To ensure that only invited attendees join your meetings, please ensure to use passcodes wherever possible.

## Index

- [Enable Passcodes for all Meetings](#enable-passcodes-for-all-meetings)
- [Enable Passcodes for Existing Meetings](#enable-passcodes-for-existing-meetings)
  - [Method 1 (recommended)](#method-1-recommended)
  - [Method 2](#method-2)
- [Enable Authenticated-Only Meeting Attendees](#enable-authenticated-only-meeting-attendees)
  - [Steps for a new Meeting](#steps-for-a-new-meeting)
  - [Steps for Editing an Existing Meeting](#steps-for-editing-an-existing-meeting)
  - [Enable for all Future Meetings](#enable-for-all-future-meetings)

## Enable Passcodes for all Meetings

1. Sign into the Zoom web portal and navigate to [Settings](https://zoom.us/profile/setting)
1. CLick on the **Meeting** tab
1. Under `Security`, verify that your passcode settings are enabled for new meetings, personal meeting ID meetings and instant meetings.
1. If the settings are disabled, click the toggle to enable them. If a verification dialog displays, choose Turn On to verify the change.

## Enable Passcodes for Existing Meetings

*Please remember that if you are part of an interview team, your personal meeting room that is used for scheduling interviews should not have passwords on them but should have the waiting room enabled.*

### Method 1 (recommended)

1. Once you have identified the meetings that need to be updated **and** have enabled passcodes for all meetings, go to your Google Calendar
1. Edit the calendar event
1. Remove the zoom meeting
1. Add a new meeting
1. Save for This and following events or All events

### Method 2

1. Log into Zoom
1. Go to `Meetings` > `Upcoming meetings`
1. Click on the meeting you want to update and scroll to the bottom of the page to find the `Edit this meeting` button
1. Under the Security section, check the Passcode box
1. **IMPORTANT:** If you add Passcodes within Zoom to an existing meeting, calendar invites will need to be resent to include the Passcode

## Enable Authenticated-Only Meeting Attendees

- As an added security measure, you can restrict the meeting by requiring any attendee to be authenticated to Zoom with a GitLab zoom account
- This is meant to ensure only people who have logged in to Zoom can attend the meeting
- This is not recommended for meetings with attendees that are not GitLab team members such as customers or someone interviewing for GitLab employment
- It should be noted that this needs to be set up before the meeting, not during the meeting

Here is a quick video tutorial how to do this:

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/ZvaLolwKfAI/0.jpg)](https://www.youtube.com/watch?v=ZvaLolwKfAI)

### Steps for a new Meeting

1. During the meeting creation, in the Security section there is an option in the Zoom client that says: `Only authenticated users can join: GitLab Internal Only` or select the `Sign in to Zoom` option so users with any Zoom account can join. Click the check box next to this option
1. If you are in Zoom via the browser, the option is still in the Security section but is labeled: `Require authentication to join`
1. Proceed as normal with your meeting creation, and click **Save**

**Note:**

- This process only works in the Zoom client or from the [GitLab Zoom website](https://gitlab.zoom.us/)
- If you're scheduling it within Google calendar, schedule as normal and edit the meeting following the steps in the next section for an existing meeting

### Steps for Editing an Existing Meeting

1. Authenticate into Zoom, either via the client or via the web in a browser.
1. Navigate to "Meetings". In the Zoom client this is at the top, in the browser this is on the left side.
1. Find the meeting you wish to change and click on it.
1. Click on the Edit button.
1. In the Security section, select the option to require authentication, and click Save.

### Enable for all Future Meetings

1. Authenticate into Zoom via the browser at gitlab.zoom.us.
1. Select Settings on the left menu.
1. In the Security section, scroll down and find "Only authenticated users can join meetings". Click on the button on the right to turn this on.
1. Save your settings with the Save button at the bottom.
1. You can still selectively turn it off for a specific meeting by editing that meeting using the steps in the previous section and turning it off
