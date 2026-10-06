---
title: Google Mail (Gmail)
description: Gmail usage and configuration guides
---

Gmail is our primary mail application. You can access the app via the `G Suite SSO Mail` tile in your Okta Dashboard or by directly going to [the gmail page](https://mail.google.com/).

This page aims to provide solutions for some of the most commonly asked questions we have received. For more in-depth support, please visit the [official Gmail support page](https://support.google.com/mail/).

## Index

- [Gmail Access Requests](#gmail-access-requests)
- [Set up Out-of-Office Replies](#set-up-out-of-office-replies)
- [Using Aliases](#using-aliases)
- [Set Up Delegate Access](#set-up-delegate-access)
- [Setting up Filters and Labels](#setting-up-filters-and-labels)
  - [Labels](#labels)
- [Reporting Spam Messages](#reporting-spam-messages)
- [Additional Support](#additional-support)

## Gmail Access Requests

You can use [this AR template](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?description_template=Google_Gmail_Request) to request the following:

- Access to someone's Gmail
- An out of office message set for someone else's Gmail
- An alias created for your own Gmail account

## Set up Out-of-Office Replies

1. Go to your Gmail's [General Settings](https://mail.google.com/mail/u/0/#settings/general) page
1. Scroll down to `Out-of-Office AutoReply:`
1. Configure the start and end date for the message
1. Write your out-of-office reply message. Please be sure to include contact details for whoever is taking over your responsibilities while your are away.

## Using Aliases

1. Request an alias to be added to your account by creating a [Gmail support AR](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?description_template=Google_Gmail_Request)
1. Once granted, go to your [Gmail Accounts Settings page](https://mail.google.com/mail/u/0/#settings/accounts)
1. Under `Send mail as:` click on `Add another email address`
1. Enter your alternate email address in the resulting pop-up, and click `Next Step`
1. The new email address will now appear on your account and you can choose to make it the default or not

## Set Up Delegate Access

To allow others to access to your account to perform tasks such as sending messages, you first need to enable the feature for your account.

1. Go to your [Gmail Accounts Settings page](https://mail.google.com/mail/u/0/#settings/accounts)
1. Under `Grant access to your account:`, click on `Add another account`
1. Follow the instructions in the resulting pop-up to verify your ID
1. Enter the email address of the person you'd like to grant delegate access to
1. Ask the person receiving delegate access to check their emails for the confirmation message
1. Once they accept, they'll be able to send messages on your behalf by clicking on their profile picture in the top-right corner of their Gmail account and then selecting your account name

## Setting up Filters and Labels

You can use filters and labels to automatically sort incoming emails to better organize your inbox or even automatically delete unwanted messages.

1. Go to the [Filters and blocked addresses](https://mail.google.com/mail/u/0/#settings/filters) tab in your Gmail Settings
1. Click on `Create a new filter`
1. Specify the conditions for the filter (Eg. all emails from a certain sender)
1. Click `Create Filter`
1. Specify how Gmail should handle the all emails that match the conditions you specified
1. Click `Create filter`

### Labels

While specifying how Gmail should handle emails that match your specified conditions, you'll notice a check box for `Apply the label:...`. These labels can be used to easily mark and filter incoming emails based on their contents.

1. Click on the arrow next to `Apply the label: Choose label..` and select `New label..`
1. Give your label a name (E.g. EUS support emails)
    1. You'll also be able to nest the label under an already existing label
1. Make sure to check the box next to the `Apply the label..` field and select your label from the drop-down menu
1. Continue configuring your email filters

## Reporting Spam Messages

1. On the right-hand-side of your inbox, click on the `PhishArm` add-on icon
1. Click on the suspicious email **DO NOT CLICK ON ANY LINKS IN THE EMAIL**
1. Click on the `Report Email` button in the PhishArm panel

## Additional Support

If you need any additional support, please contact IT via the Compass app in Slack (type "Compass" in the top search bar to find it) or [it-help@gitlab.com](mailto:it-help@gitlab.com).
