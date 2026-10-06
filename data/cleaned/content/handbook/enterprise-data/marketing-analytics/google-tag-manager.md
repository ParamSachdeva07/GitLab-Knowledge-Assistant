---
title: "Google Tag Manager"
---

Google Tag Manager (GTM) is a web tagging management tool that configures web tracking rules and sends data to various analytics and advertisement platforms such as [Google Analytics 4](/handbook/enterprise-data/marketing-analytics/google-analytics-4/), Google Ads, and LinkedIn Ads.

The [GTM code snippets](https://docs.google.com/document/d/1fPu19k55Xjeoz5PWziBrIoYTbbHT9saPLunzG6RzD04/edit?tab=t.0#heading=h.9yoza8raahpo) are deployed across GitLab's main subdomains including:

- about.gitlab.com
- gitlab.com (trial onboarding and sign up pages)
- docs.gitlab.com
- forum.gitlab.com
- handbook.gitlab.com
- page.gitlab.com
- advisories.gitlab.com
- learn.gitlab.com
- internal.gitlab.com
- explore.gitlab.com
- customers.gitlab.com (ecommerce page)
- university.gitlab.com
- contributors.gitlab.com
- support.gitlab.com

## Key Components

[Tags](https://support.google.com/tagmanager/answer/3281060) contain the event name from website activities (page views, video plays, link clicks, scrolling), specify where the data should be sent, and include additional event information. Each tag has a trigger that determines when and how it fires, and may include variables to capture extra details like page names or video titles.

- [Triggers](https://support.google.com/tagmanager/answer/7679316) determine when tags should fire. While GTM offers built-in event listeners, we primarily use custom event triggers based on dataLayer events and reliable built-in triggers for clicks and scrolling.

- [Variables](https://support.google.com/tagmanager/answer/7683056?hl=en) capture additional information about events and store them as parameters in GA4. These can pull data from the browser's HTML, URL components, cookies, or custom dataLayer implementations.

## Click Tracking

Each call-to-action (CTA) link on about.gitlab.com contains the following data attributes:

- data-ga-location: the section of the page (e.g. header, hero, body, feature, and footer)
- data-ga-name: the name of the element (e.g. free trial, sales, and buy premium)

Each CTA in the Utility header section of about.gitlab.com should contain:

- data-nav: the element name within the utility header section (e.g. register, login, logo)

Each link in the navigation menu should contain:

- data-nav-levelone: The navigation menu tab name
- data-nav-leveltwo: The navigation menu element name

A click-listening trigger on GTM will fire the associated GA4 event tag based on the data attributes. Links without data attributes will still be tracked, however the cta_location event parameter on GA4 will contain a generic "in-line" value and the cta_name event parameter will contain the link's text and URL.

## Data Layer Tracking

Custom events on the website are tracked via the [dataLayer method](https://developers.google.com/tag-platform/tag-manager/web/datalayer). A javascript code is placed on the website when the desired action is performed. The dataLayer code sends an event name and variables to the browser. A custom event trigger on GTM listens to the dataLayer event name from the browser.

Example of a dataLayer code:

```javascript
dataLayer.push({
  'event': 'videoStart',
  'videoTitle': 'The One DevOps Platform'
});
```

## Server-Side Google Tag Manager

Server-Side Google Tag Manager (sGTM) is a server-based tracking solution that processes marketing and analytics data through our own server infrastructure instead of directly from users' browsers.

**Traditional tracking:** Website → Third-party services (Google Analytics, Facebook, etc.)

**Server-side tracking:** Website → Our servers → Third-party services

### Our Infrastructure Setup

#### Architecture Overview

We run a global server-side GTM infrastructure with three regional Cloud Run services:

- **US Region:** Handles traffic from North and South America
- **EU Region:** Handles traffic from Europe, Middle East, and Africa
- **Asia Region:** Handles traffic from Asia-Pacific

All traffic routes through a single domain: analytics.gitlab.com

#### How Traffic Routing Works

1. **User visits our website** from anywhere in the world
2. **Tracking data gets sent** to analytics.gitlab.com
3. **Load balancer automatically routes** the request to the closest regional server
4. **Regional server processes** the data and forwards it to appropriate analytics platforms
5. **Geographic optimization** ensures fast response times globally

#### Regional Benefits

The multi-region setup provides several key advantages. Lower latency ensures data is processed closer to users for faster response times. Data residency compliance is achieved since EU data can stay within EU infrastructure to meet regulatory requirements. Our system includes built-in redundancy where if one region experiences issues, traffic automatically redirects to maintain service availability. Most importantly, users get a consistent tracking experience regardless of their location, as the same setup works globally through our unified domain.

#### Infrastructure Implementation

For detailed technical documentation on how our Infrastructure team set up the global load balancer, regional Cloud Run services, SSL certificates, and DNS configuration, see the complete implementation guide in [GitLab issue #2183](https://gitlab.com/gitlab-com/marketing/marketing-strategy-performance/-/issues/2183#note_2523358771).

### Server Google Tag Manager Container

#### Client-Side to Server-Side Data Flow

Our implementation uses a dual-container approach with both client-side and server-side Google Tag Manager containers working together.

**Client-Side Container:** Captures user interactions and website events, then forwards this data to our server-side container using the Data Tag template from Stape.io. This acts as the data collection layer that runs in users' browsers.

**Server-Side Container:** Receives data from the client-side container and processes it before sending to various third-party platforms like Google Analytics, Facebook, LinkedIn, Reddit, and others. This runs on our own servers at analytics.gitlab.com.

#### Supported Third-Party Platforms

Our server-side setup currently forwards data to multiple marketing and analytics platforms. Each advertisement platform receives properly formatted data through server-side APIs rather than client-side pixels. Additionally, we have other functional or analytics platform scripts on the website that are client-side.

**List of Current Platforms**

| Platform | Cookie Category | Trigger | DRI Team(s) | Method |
|----------|----------------|---------|-------------|---------|
| Google Ads | Advertisement | All pageviews, conversions | Digital Marketing, Brand | API |
| LinkedIn | Advertisement | All pageviews, conversions | Digital Marketing, Brand | API |
| Facebook | Advertisement | All pageviews, engagement, conversion | Digital Marketing, Brand | API |
| Reddit | Advertisement | All pageviews, engagement | Brand | API |
| Microsoft Ads | Advertisement | All pageviews, conversions | Digital Marketing | API |
| StackAdapt | Advertisement | All pageviews, engagement | Brand | API |
| Google Analytics | Analytics | All pageviews, engagement, conversion | Marketing Analytics, Digital Experience | API |
| Snowplow | Analytics | All pageviews | Marketing Analytics | Javascript |
| Adobe Measure (Bizible) | Analytics | All pageviews | Marketing Operations, Marketing Analytics | Javascript |
| Marketo | Analytics | All pageviews | Marketing Operations | Javascript |
| PathFactory | Functional | All pageviews | Marketing Operations, ABM | Javascript |
| 6Sense | Functional | All pageviews | Marketing Operations, ABM | Javascript |
| Mutiny | Functional | All pageviews | Marketing Operations, ABM | Javascript |
| Qualified | Functional | Most pageviews | Marketing Operations | Javascript |

*Table last updated: 2025-07-01*

To request the placement of a new tag on the website, please first ensure that the platform is listed on [tech_stack.yml](https://gitlab.com/gitlab-com/www-gitlab-com/-/blob/master/data/tech_stack.yml), as all platforms must undergo approval by the legal team.

Once the platform has received legal approval, create a new issue under the [Marketing Analytics project](https://gitlab.com/gitlab-com/marketing/marketing-strategy-performance/-/issues/new), utilizing the `/script_onboarding.md` template. Complete the “Script Context” sections to the best of your abilities. The issue will be automatically assigned to @DennisCharukulvanich, who will assess the remaining tasks.

#### Consent Management Integration

Server-side GTM still respects user privacy preferences through integrated consent management tool OneTrust. Consent states are captured client-side and forwarded to the server-side container, ensuring that data is only sent to platforms when users have provided appropriate consent for analytics, marketing, or other functional uses.
