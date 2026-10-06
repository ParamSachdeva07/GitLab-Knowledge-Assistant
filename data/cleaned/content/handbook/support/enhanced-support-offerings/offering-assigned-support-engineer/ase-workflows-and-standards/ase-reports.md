---
title: Reports and Dashboards for ASEs
description: Descriptions of each standard report and dashboard available to ASEs
---

## Introduction

## Reports and dashboards for ASE accounts

### Fetching ticket data from Snowflake

As an ASE, you [can request access](/handbook/security/corporate/systems/lumos/ar/) to the GitLab [SnowFlake](/handbook/enterprise-data/platform/snowflake) instance, and this can be quite useful in preparing reports or keeping documentation on your assigned customer's environments up to date.

There are a few steps required to generate data for each customer, and these notes will assume that you already have working access to Snowflake and Zendesk.

As we do not have access to the Zendesk API, you will first need to manually scrape the list of ticket IDs that you'd like to include in your report.

To start, you will need to go to the appropriate organization page for your customer, in Zendesk, and then open the Chrome Developer tools panel, and paste either of the following blocks of code;

#### Single page

To get only the tickets visible on the current Zendesk page - so filtered by your chosen customer, but this could be extended to only include open tickets or a specific requester, part of this information is not easily available in Snowflake - use this code:

```javascript
copy(Array.from(document.querySelectorAll('[data-test-id="generic-table-cells-id"]'))
        .map(cell => cell.textContent.trim().replace('#', ''))
        .join(', '));
```

Will copy a comma seperated list of the ticket numbers from that page.

#### All of the customer's tickets

If you need to fetch more than 30 tickets, you can use this js to fetch all of the tickets for your specific customer:

```javascript
window.allTicketIds = [];

async function collectAllPages() {
  let pageCount = 0;

  while (true) {
    pageCount++;

    // Wait for content to load
    await new Promise(resolve => setTimeout(resolve, 1500));

    // Collect current page
    const ids = Array.from(document.querySelectorAll('[data-test-id="generic-table-cells-id"]'))
.map(cell => cell.textContent.trim().replace('#', ''));

    if (ids.length === 0) {
console.log('Waiting longer for page to load...');
await new Promise(resolve => setTimeout(resolve, 2000));
continue;
    }

    window.allTicketIds.push(...ids);
    console.log(`Page ${pageCount}: Collected ${ids.length} IDs. Total: ${window.allTicketIds.length}`);

    // Find next button
    const nextButton = document.querySelector('button[aria-label="Next page"]');

    // Check if button is hidden (last page indicator)
    if (!nextButton || nextButton.disabled || nextButton.hasAttribute('hidden') ||
  nextButton.getAttribute('aria-disabled') === 'true') {
console.log('No more pages');
break;
    }

    nextButton.click();
  }

  console.log(`\n✓ Collected ${window.allTicketIds.length} ticket IDs total:`);
  console.log(window.allTicketIds.join(', '));
}

collectAllPages();
```

This will output the array to the console window.

#### Querying Snowflake

You are now ready to use fetch the ticket data from Snowflake.

Using [this](https://app.snowflake.com/ys68254/gitlab/w3cd6hFh6KvV#query) Snowflake worksheet as an example, you can query the summarized data, using the ticket IDs you retrieved earlier:

```sql
SELECT TICKET_ID,AI_INSPECTED_SUMMARY,AI_INSPECTED_FEATURES,AI_INSPECTED_PRODUCT_GROUP,AI_INSPECTED_CURRENT_VERSION FROM PROD.COMMON_PREP.PREP_ZENDESK_PROCESSED_TICKETS WHERE
TICKET_ID IN ( #TICKET_ARRAY_GOES_HERE ) ORDER BY TICKET_ID DESC;
```

Do note that this is not an exhaustive list of the fields available, that the ```CREATED_AT``` and ```SYNCED_AT``` fields _do not_ reflect the date of the ticket, and that Snowflake uses a reasonably standard SQL query format so this query could easily be extended.

#### Querying Snowflake in Glean

1. Enable Snowflake glean connector by going to Your Settings -> Connectors
1. Get Zendesk Organization ID for the org from the [assigned-support-engineers repository](https://gitlab.com/gitlab-com/support/assigned-support-engineers/-/tree/main?ref_type=heads).
1. Ask Glean to fetch tickets using this query and prompt it to produce a report based on the data returned:

   ```sql
   select
       zdt.*
   from
       prod.common.fct_support_ticket as a,
       PROD.COMMON_PREP.PREP_ZENDESK_PROCESSED_TICKETS as zdt
   where
       a.dim_support_organization_id = ZD_ORG_ID
       and a.dim_support_ticket_id = zdt.ticket_id
   order by a.solved_at desc

Note, `PREP_ZENDESK_PROCESSED_TICKETS` table in Snowflake only contains solved tickets that were created after November 2022.

#### Use Cases

##### Detailed infrastructure and features report

You can use Snowflake data with GitLab Duo to create a draft of a report about their architecture and features used. This might be useful when you are onboarding a new customer. Give Duo the exported ticket data as a context with this prompt:

```plaintext
I am an Assigned Support Engineer at GitLab, and I am onboarding a new customer. I want to use the data about customer tickets to build out a report of used features and their architecture.
The ticket summaries can be found here: Customers/FILE_WITH_DATA.csv 
If you run into contradictions, use the data from the ticket with highest ticket ID. If Gitaly Cluster is not mentioned anywhere, it is likely a Sharded Gitaly. Do not make assumptions about license based on features, make sure that license name is specified explicitly. Additionally, give me overview of what features they raise the most tickets about. Be concise. 

EXAMPLE REPORT:

Deployment Platform: On-prem, Fully air-gaped
GitLab Deploymnet: 3K reference architecture, Omnibus, not Cloud-Native, not Dedicated
Runners Deployment: Docker executor with Podman.
Container registry: no
Package registry: no
GitLab pages: n/a
GitLab Kubernetes Agent: n/a
License: Ultimate with Duo Enterprise
Which secure features are they using: This customer is not using compliance and secure features, like sast, dast scanners.
Security scanners they don't use: they don't use any of our security scanners at the moment
AI features: They are using Duo chat with custom models deployed on vllm. They use both Duo chat, code generation features and code review.
GEO used: Yes
Advanced search solution: Zoekt
Database solution: Highly Available database with Patroni, Consul and PgBouncer as per our 3K reference architecture
Gitaly deployment type: Gitaly cluster, with TLS enabled, Gitaly cluster deployed in GEO secondary as well
What integrations are they using: Jira integration
Are they using GitLab for Plan stage: no
How do they manage user access to GitLab: LDAP with LDAP group sync
Zero-downtime upgrade process implemented: yes, zero-downtime is important to them
```

### Zendesk organization data dashboard

You can use [Organization Performance dashboard](https://gitlab.zendesk.com/explore/studio#/dashboards/47EB07BFD95FB76D1FB0F697673A6A6348E2804DC81A2A0608B09458AF9E4ABC) in Zendesk to prepare reports for Monthly/Quarterly review meetings depending on what the customer is interested in.

## Reports and dashboards for ASEs
