---
title: Zoom Recording
description: Zoom Recording - Setup and Configuration
---

## Index

- [Recording in Zoom](#recording-in-zoom)
  - [Record All Participants using Gallery View](#record-all-participants-using-gallery-view)
  - [Recording Zoom meetings in HD](#recording-zoom-meetings-in-hd)
  - [Auto-Recording](#auto-recording)
  - [Shared Drive Recording](#shared-drive-recording)
  - [How to Identify the Meeting Host With Recording Permissions](#how-to-identify-the-meeting-host-with-recording-permissions)
  - [How to allow recording when the host is not present](#how-to-allow-recording-when-the-host-is-not-present)
    - [Using the website](#using-the-website)
    - [Using the Zoom app](#using-the-zoom-app)
  - [Recording video transcripts](#recording-video-transcripts)

## Recording in Zoom

In order to be able to record your Zoom meetings you must first enable recordings in your Zoom profile.\
You can access this page at [Recording Settings](https://zoom.us/profile/setting?tab=recording).\
You need to be signed in to have the ability to record.

### Record All Participants using Gallery View

Consider setting your default recording view to `Gallery view`.

To do this:

1. Login to zoom.us.
1. Click the Settings tab on the left side bar, then the Recording tab on the top horizontal options
1. Make sure you have `Record gallery view with shared screen` selected
1. Unselect `Record active speaker with shared screen` and `Record active speaker, gallery view and shared screen separately`
1. Remember to save.

You can also read through General information on recording on the zoom support [here](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0059856)

### Recording Zoom meetings in HD

1. Navigate to your [Zoom profile settings](https://gitlab.zoom.us/profile/setting)
1. Click on the `Meeting` tab in the top menu
1. Click on the `In Meeting (Advanced)` side tab
1. Scroll down to the `Meeting-HD Video Quality` section and press the toggle
1. Select the `Full HD (1080P)` radio button
1. Press the `Save` button

Your settings will now be updated to record zoom meetings in full HD.

### Auto-Recording

To auto-record meetings set up [cloud recording](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0067954)

You can also configure Zoom to save to the cloud automatically.

1. Go to "My Meeting Settings" and find the "Recording" section, then click on "Cloud Recording"
1. Setting the topic of the meeting is important, otherwise all meetings will be recorded with a generic name
1. Once recording is complete, your videos will not appear in the "Recordings" section of your Zoom account

### Shared Drive Recording

{{% alert title="Attention!" color="warning" %}}
Recordings saved using this method are visible to the entire company. Do not use this for meetings containing private or confidential information.
{{% /alert %}}

- If the meeting topic in Zoom (editable by logging into <https://zoom.us/>) contains the text `[REC]`, these recordings will automatically be saved to a folder on Google Drive under `GitLab Videos Recorded` (accessible from [Google Hidden shared drives](https://drive.google.com/drive/shared-drives-hidden))
- The name of the folder will be prefixed by the host's e-mail address. For example, if the host is `someuser@gitlab.com` and the meeting title is `Company Training [REC]`, the folder will appear as `someuser@gitlab.com-Company Training`
- [The script](https://gitlab.com/gitlab-com/zoom-sync/-/blob/a73aee8f5921ac3fec16b74232ac17add4e33afb/zoom-sync.rb) (from [the zoom-sync project](https://gitlab.com/gitlab-com/zoom-sync)) will sync the recordings every hour
- To make it easier for meetings to be uploaded automatically without changing the title, the sync script also uses an [allow list](https://gitlab.com/gitlab-com/zoom-sync#allow-list)
- If a meeting title matches the provided regex with the given host's e-mail address, the meeting will also be uploaded to Google Drive. File a merge request to change [the current list](https://gitlab.com/gitlab-com/zoom-sync/-/blob/master/zoom_sync.yml).

### How to Identify the Meeting Host With Recording Permissions

You can use one of the below methods to find this information after joining the meeting.

1. Via participants sidebar
   1. Navigate to the participants icon on the bottom of the window
   1. You will be presented with the list of participants on the right panel of the window
   1. The host will be listed in parentheses at the end of their name. (A resize of the participants window may be needed)
1. Via meeting info pop-up
   1. Navigate to the upper left corner, where you will be presented with an i icon
   1. Select the icon to locate the meeting host who will have the ability to record the call

### How to allow recording when the host is not present

This usually happens on recurring meetings where the host can't always attend.

The meeting creator should add colleagues as `Alternative Hosts` in case they can't attend so that others can still start the recording.

#### Using the website

1. Navigate to `https://gitlab.zoom.us/meeting/<meeting id>/edit`
1. Scroll to the bottom to find "Alternative Hosts"
1. Add the email address for one or more colleagues separated by a comma
1. Click Save

#### Using the Zoom app

1. Click "Meetings"
1. Find your meeting on the left-hand side of the app
1. Click "Edit" on the right-hand side of the app
1. Expand the "Advanced Options" drop-down on the bottom of the window
1. Find the "Alternative Hosts" box at the bottom
1. Add the email address for one or more colleagues separated by a semi-comma
1. Click Save.

### Recording video transcripts

- [Closed captioning and live transcription](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0062490) is enabled by default for all users, however the subtitles will not show for participants unless a host manually enables it once the meeting starts
- At the end of a recorded meeting, the transcription will be available in a text file under the same folder as the other recording files
- For local recordings, a transcription is saved to `closed_caption.txt` but only if enabled by a co-host
- For cloud recordings, the file name ends with `.transcript.txt` and the full transcription is always available. Processing takes about 15 minutes, so the video files appear before the transcription
