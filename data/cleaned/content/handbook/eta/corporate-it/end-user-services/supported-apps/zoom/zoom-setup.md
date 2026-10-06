---
title: Zoom Setup
description: Basic installation and setup steps
---

## Index

- [Installation](#installation)
  - [MacOS](#macos)
  - [Linux](#linux)
- [Setup](#setup)
- [Connect Zoom to Other Apps](#connect-zoom-to-other-apps)
  - [Google Chrome](#google-chrome)
  - [Google Calendar](#google-calendar)
  - [Slack](#slack)

## Installation

If you are using a GitLab-provided MacBook Zoom should be installed automatically when you first set up the laptop. To install the app manually, please see the steps below.

### MacOS

- Open the **Self Service** app found by opening **Finder** and going to **Applications**. Search for Zoom and select the Install option.
- Alternatively, you can also download and install Zoom directly from [the official Zoom download page](https://zoom.us/download?os=mac)

### Linux

- You can download the most recent version of Zoom [here](https://zoom.us/download?os=linux)

## Setup

1. Open the **Zoom** app
1. Under `or sign in with`, click on **SSO**
1. Chrome should open automatically and bring you to an Okta login page where you'll need to sign in with your Okta credentials
1. Click on the blue **Launch Zoom Workplace** button in your Chrome tab. You should now see your profile picture in the top-right corner of the Zoom app window

## Connect Zoom to Other Apps

### Google Chrome

1. The Zoom extension should be installed by default
   1. If not, you an install it from the [Chrome Web Store](https://chromewebstore.google.com/detail/zoom-chrome-extension/kgjfgplpablkjnlkjmjdecgdpfankdle)
1. Click on the Zoom Chrome extension button next to the URL bar (You may need to click on the puzzle piece button first)
1. Click on **Sign in to Zoom**
1. On the subsequent screen, click on **SSO**
1. Enter **gitlab** in the `Company Domain` field and click **Continue**
1. Sign in with Okta and confirm that you want to allow Chrome to access Zoom if prompted

### Google Calendar

The Chrome extension will allow you to create Zoom meetings through Google Calendar. However, you can also create a normal meeting and add Zoom links manually via the `Add video conferencing` option

1. Open [Google Calendar](https://calendar.google.com/) in Chrome
1. Click on the **Zoom** icon on the right-side of the screen
   1. If the icon is not available, click on the `+` button on the right-side of the screen and install the `Zoom` extension from the `Google Workspace Marketplace`
1. Click the blue **Sign in** button
1. Review the app permissions and click **Allow**
1. On the `Confirm Connection Between Your Zoom and Google Workspace Accounts` screen, click **Confirm**
1. Close the pop-up screen with the `Authorization Successful!` notification
1. Enable [Bidirectional sync for Zoom meeting data between Zoom web portal and calendars](https://zoom.us/profile/setting?tab=zoomMailCalendar#CalendarEventSyncBackToMeeting) to better sync Google Calendar and Zoom

### Slack

It's possible to start Zoom meetings directly from Slack using the `/zoom` command in any Slack channel or chat

1. Open Slack and search for **Zoom** in the search bar and click on **Zoom**`App`
1. Type **/zoom** in the chat with the Zoom App and press **Enter**
1. Click on **Authorize Zoom**
1. Review the app permissions and click **Allow**
1. On the `Sign in to Zoom with Slack` screen, click on **Accept and continue** followed by **Confirm**
1. Review the integration settings and click **Save** once you're done
1. You'll now be able to use the Zoom extension in Slack
1. You can review additional settings by searching for **Zoom** in the the Slack app
