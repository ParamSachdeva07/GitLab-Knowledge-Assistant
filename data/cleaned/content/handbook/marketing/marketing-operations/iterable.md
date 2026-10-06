---
title: Iterable
description: Iterable Overview
twitter_image: /images/tweets/handbook-marketing.png
twitter_site: "@gitlab"
twitter_creator: "@gitlab"
---


## DRIs

| DRI            | Role            |
| -------------- | --------------- |
| Amy Waller     | Business Owner  |
| TBD | Technical Owner |
| Allie Klatzkin | Campaigns Owner |

## Overview

[Iterable](https://iterable.com/) is a powerful email marketing automation platform that allows us to create, send, and track personalized email campaigns. It provides a user-friendly interface and a wide range of features to help us engage with our customers and users effectively.

## Iterable Journeys

Journeys are a powerful feature that enable us to create complex, multi-step customer engagement campaigns. With Journeys, you can design personalized customer experiences across multiple channels, including email and SMS. Map out customer journeys, set up triggers and conditions, and deliver targeted messages at each step of the customer lifecycle.

**List of journeys implemented:**

| Journey Name   (Folder)       | Link                                                                                    |
| --------------------- | --------------------------------------------------------------------------------------- |
| SaaS Trial Onboarding + Post  | [Link](https://app.iterable.com/workflows/361081/edit?mode=beta&workflowType=Published) |
| Free User + Invited Onboarding| [link](https://app.iterable.com/workflows?folderId=68331&page=1)|

## API Custom Events

Iterable's API is designed to handle large volumes of data and high request rates. It ensures scalability and reliability, allowing us to deliver personalized messages to in-product user segments.

```mermaid
graph LR
  GitLab.com --> CustomersDot
  CustomersDot --> Workato API
  Workato API --> Iterable
```

For more information on the API custom events, visit the internal handbook page.

## Subscription Preferences

Iterable subscriptions are structered in message types and channel, with each individual type having it's own subscription policy. Each template or email is atributed a message type when created and adopts its subscription policy.

**_ NB: Do not use the Marketing Message type as it uses an opt-out policy and will result in the possibility of emailing un-subscribed records _**

Subscription schema in the GitLab instance comproises of the following:

| Message Type      | Channel               | Subscription Policy | Notes                                                     |
| ----------------- | --------------------- | ------------------- | --------------------------------------------------------- |
| GitLab Marketing  | Marketing Channel     | opt-in              | This is the main message type used in templates and email |
| Marketing Message | Marketing Channel     | opt-out             | Default message type, will be deleted                     |
| Transactional     | Transactional Channel | opt-out             |                                                           |

**Unsubscribe Event**
Whenever an `unsubscribe` event occurs in Marketo, an event is sent to Workato and then Iterable to `opt-out` that person if it exists.

## Data Sync

[Hightouch](/handbook/marketing/marketing-operations/hightouch/) is a data integration platform that specializes in real-time data synchronization, allowing us to leverage the power of Snowflake's data and transfer it to Iterable for personalized and targeted marketing campaigns. It automates the data synchronization process between Snowflake and Iterable, reducing manual effort. Hightouch can handle large datasets and ensure that all data is accurately synced to Iterable, enabling us to scale marketing operations effectively.

For more information on Hightouch models and Iterable, visit the internal handbook page.
