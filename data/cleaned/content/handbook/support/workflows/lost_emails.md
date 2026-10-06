---
title: Lost Email Account
category: GitLab.com
subcategory: Accounts
description: "Workflow for cases when users are no longer able to receive security emails for account verification"
---

## Overview

This workflow covers cases when a user requests that their email address be changed, for example due to having lost access to all email addresses on their account and being asked to perform [Account email verification](https://docs.gitlab.com/security/email_verification/#accounts-without-two-factor-authentication-2fa) in order to access their account.

## **Stage 0:** Ticket Triage

Ensure the ticket has the correct:

- Form `SaaS Account`
- Category, such as `Cannot access account`
- Subcategory, such as `Need to change my username/email`
- Impacted email address

## **Stage 1:** Process

As the user has reportedly lost access to the email address associated with their GitLab.com account, they have likely raised the ticket using an alternate email address. As with all account activities, you should be particularly mindful of this and take care to not share any information related to the account which is not publicly available, or where applicable, account verification has not been successfully completed.

The actions support can take on accounts are different for free users and paid users. To confirm the user's tier status, search for the user using the User Lookup GitLab Super App in Zendesk to confirm the user's group memberships, if the user is not a member of any premium group they are considered a free user.

### Paid user

Refer to [Making Changes and Taking Actions on a user's behalf](/handbook/support/workflows/account_changes) for the options available to paid users.

### Free user

Free users who have lost access to all email addresses on their GitLab.com account have the following options:

1. **Self-Service (Preferred):** If the user can still log in, direct them to update their email in [Profile Settings](https://gitlab.com/-/user_settings/profile).
1. **Purchase a Subscription:** Free users may purchase a GitLab subscription to gain access to Priority Support for customer account recovery assistance. However they will still need to pass the [account verification challenge questions](https://internal.gitlab.com/handbook/support/#account-verification-challenge-questions).

If neither option applies, apply the Zendesk macro `Support::SaaS::GitLab.com::Email::Free user verification code` and submit the ticket as `Solved`. Note that this will close the ticket, removing any opportunity for further response from the user, do not use the macro if you believe further dialogue is needed.

**Note:** If a free user raises data subject rights concerns regarding their account data, do not close the ticket. Instead, refer to the [Free User Data Correction Request](https://internal.gitlab.com/handbook/support/workflows/data-subject-requests/#free-user-data-correction-requests) process for additional guidance.
