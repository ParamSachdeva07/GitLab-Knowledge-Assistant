---
title: 'Sentiment'
description: 'Documentation on Zendesk Copilot sentiment'
---

## What is sentiment

As per [Zendesk](https://support.zendesk.com/hc/en-us/articles/4550640560538-Automatically-classifying-tickets-with-intelligent-triage):

> Intelligent triage uses AI to automatically classify new customer support tickets by topic, sentiment, language, and entities, such as product names. By incorporating these AI classifications into your workflows, you can automate repeatable requests, eliminate manual triage, guide agents in real time, and act quickly on high-risk tickets.

## Current settings

- Zendesk Global
  - Sandbox:
    - [x] Detect sentiment
    - Dynamic detection
      - [x] Update sentiment based on the latest interaction
    - Channels
      - Email and async
        - Web form
        - Email
        - Web service (API)
        - Closed ticket
      - Messaging: none
      - [ ] Voice
    - Exclusion conditions
      - [x] Skip triaging email, messaging, and other asynchronous tickets created by agents
  - Production:
    - [x] Detect sentiment
    - Dynamic detection
      - [x] Update sentiment based on the latest interaction
    - Channels
      - Email and async
        - Web form
        - Email
        - Web service (API)
        - Closed ticket
      - Messaging: none
      - [ ] Voice
    - Exclusion conditions
      - [x] Skip triaging email, messaging, and other asynchronous tickets created by agents
- Zendesk US Government
  - Sandbox:
    - [x] Detect sentiment
    - Dynamic detection
      - [x] Update sentiment based on the latest interaction
    - Channels
      - Email and async
        - Web form
        - Email
        - Web service (API)
        - Closed ticket
      - Messaging: none
      - [ ] Voice
    - Exclusion conditions
      - [x] Skip triaging email, messaging, and other asynchronous tickets created by agents
  - Production:
    - [x] Detect sentiment
    - Dynamic detection
      - [x] Update sentiment based on the latest interaction
    - Channels
      - Email and async
        - Web form
        - Email
        - Web service (API)
        - Closed ticket
      - Messaging: none
      - [ ] Voice
    - Exclusion conditions
      - [x] Skip triaging email, messaging, and other asynchronous tickets created by agents
