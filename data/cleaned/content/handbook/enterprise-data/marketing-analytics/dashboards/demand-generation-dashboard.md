---
title: "Demand Generation Dashboard"
description: "The Demand Generation Dashboard is a single pane of glass to understand Marketing Campaigns and Pipeline Contribution."
---

## Demand Gen Dashboard User Guide

## Overview & Purpose

[The Demand Gen Dashboard](https://10az.online.tableau.com/#/site/gitlab/views/WIPMarketingDemandGenFunnelDash/CampaignPerformance) is our central hub for analyzing marketing campaign performance and marketing contribution to company pipeline. This unified dashboard provides  insights into touchpoints, MQLs, and Marketing Generated Pipeline across all campaigns, channels, and GEOs.

**Who should use this dashboard:**

- Campaign managers analyzing individual campaign results
- Marketing leaders reviewing channel effectiveness and overall demand generation
- Field marketing managers tracking event and regional campaign performance

## Dashboard Tabs

Currently, the Dahsboard has one tab, Campaign Performance. We plan to add more executive level views in FY26-Q3.

### Campaign Performance Tab

This tab offers a flexible view in Campaign Performance. The sections below outline its components.

#### Executive Summary

At the top of the dashboard, you'll find four key performance indicators:

- **Touchpoints**: Total marketing interactions
- **MQLs**: Marketing Qualified Leads using linear attribution
- **MGP SAOs**: A count of Sales Accepted Opportunities that qualify for Marketing Generated Pipeline
- **MGP**: Marketing Generated Pipeline dollar amount

Below the executive summary, is an interactive view to filter the dashboard by GEO. Clicking on a GEO, the dashboard will update to show a single GEO, the dashboard also has filters on the side to select more than one GEO.

### How to Navigate the Dashboard

The dashboard is designed to work from top to bottom, allowing for building a progressively more refined drill down view from high-level insights to specific campaign details.

Clicking on Offer Type or Marketing Channel will filter the dashboard. From there, the filters on the left side can further refine the data shown on the dashboard. This allows starting with broad questions like the ones below and filtering the dash to quickly gain insight.

- How are my EMEA email campaigns performing this quarter?
- Which content campaigns are driving the highest MGP per touchpoint?
- What's the pipeline contribution from my recent events?

**Understanding Tooltips**

Both the Channel Performance and Campaign Performance tables include helpful tooltips that appear when you hover over rows. These tooltips show:

- Percentage of total touchpoints, MQLs, and MGP represented by that row
- Conversion rates and efficiency metrics
- Ranking information (e.g., "9th highest MGP per Touchpoint")

## Key Metrics Explained

### Touchpoints

Touchpoints represent individual marketing interactions or engagements with prospects and customers. This includes form fills, online event registrations, pathfactory interactions, and other measurable marketing activities. [Our Bizible handbook page as more details.](/handbook/marketing/marketing-operations/bizible/)

### Linear MQLs

Linear MQLs use a fractional attribution model that distributes credit for an MQL across all touchpoints that occurred before the person became an MQL.

**How it works:**

- If someone had 3 touchpoints before becoming an MQL, each touchpoint receives 33% of the credit
- When you filter for a specific campaign or channel, you only see the portion of MQL credit attributed to those touchpoints
- This provides a more accurate view of each campaign's contribution to MQL generation

### Marketing Generated Pipeline (MGP) & MGP SAOs

MGP is our primary pipeline attribution metric, representing the dollar value of opportunities that can be attributed to marketing activities. [Our Marketing Attribution handbook page has more details on MGP.](https://internal.gitlab.com/handbook/marketing/marketing-ops-and-analytics/marketing-analytics/marketing_pipeline_attribution/) We also show MGP by SAO count, showing the number of SAOs we're counting in the dollar amount.

### Timeline View

Below the main tables, the timeline view shows performance trends over your selected time period. The dashboard has filters too:

- Switch between calendar week and fiscal quarter views
- See how performance changes over time based on your current filters

### Opportunity Detail View

At the bottom of the dashboard, is an opportunity view that shows specific opportunities that make up MGP metrics. This enables users to:

- See individual opportunities contributing to your MGP numbers
- Click through to view accounts and opportunities directly in Salesforce
- Group opportunities by order type or segment for additional analysis

## Using Filters & Interactivity

### Interactive Filtering

The dashboard is highly interactive. Clicking on elements will filter the entire view:

- **Region tiles**: Filter to a specific geographic region
- **Channel names**: Filter to show only that marketing channel
- **Offer Type names**: Filter to show only that Offer Type name
- **Campaign names**: Drill down to specific campaigns

### Sidebar Filters

Use the filters in the left sidebar for more granular analysis:

- **Offer Type**: Filter by the type of marketing offer
- **Source/Medium**: UTM-based traffic source information
- **Form URL Domain**: Filter by specific domains
- **Landing Page**: Filter by landing page
- **Account Segment**: Filter by account size or type
- **Campaign filters**: Name, region, sub-region, type, budget holder

## Advanced Features

### Cohort Data Field

The "Cohort Data on" dropdown changes how the entire dashboard calculates and displays data. Most users should not need to update it, but it unlocks powerful reporting features.

**Touchpoint Cohort** (Default)

- Data is organized by when the touchpoint occurred
- Shows all touchpoints within your selected date range
- Best for understanding: "What marketing activities happened this quarter?"

**Marketing Generated Pipeline Cohort**

- Data is organized by when the pipeline was created
- Only shows touchpoints that are associated with pipeline created in your selected date range
- Touchpoints can occur up to 1 year before the Pipeline was created, but not occur after.
- Best for understanding: "What marketing activities contributed to pipeline we generated this quarter?"

**MQL Cohort**

- Data is organized by when the MQL occurred
- Only shows touchpoints associated with people who became MQLs in the selected date range
- Best for understanding: "What marketing activities contributed to MQLs we generated this quarter?"

**When to use each cohort:**

- Use **Touchpoint** for campaign performance analysis and general activity reporting
- Use **MGP** for pipeline attribution and ROI analysis
- Use **MQL** for MQL generation campaign analysis

### MQL Selector

The `MQL Type` selector on the Dashboard changes what MQL metric is shown.
The default state, Worked MQLs, shows Linear MQLs that have been worked by Sales Dev. This default is set to match our Sales Dev Reporting and how Marketing sets MQL targets.

**The Options Are:**

- Worked MQLs - The default, shows Linear MQLs that have been worked by Sales Dev.
- All MQLs - Shows Linear MQLs, regardless of whether they have been worked by Sales Dev.
- Member MQLs - Shows all MQLs regardless of when their MQL date occurred, only restricts to the cohort (e.g. Touchpoints) date range. This is a legacy calculation method from the previous dashboard.

**Key differences:**

- Worked/All MQLs use linear attribution and respect the timeline (touchpoint must occur before MQL date)
- Member MQLs ignore MQL timing and simply count any person with an MQL date who had touchpoints in your selected timeframe
