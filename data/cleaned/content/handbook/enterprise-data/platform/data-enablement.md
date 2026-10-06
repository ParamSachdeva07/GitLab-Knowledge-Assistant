---
title: "Data Enablement"
description: "Different possibilities to use our data"
---

Data enablement at GitLab provides team members with multiple ways to access, analyze and use our data. This page documents the different tools and platforms available for exploring and utilizing our data assets.

### Our Data Paradigm

Our core principle is to **keep data in our Data Platform as much as possible**. Our Data Platform provides a well-governed access model with robust security controls, audit trails, and role-based permissions. When data is exported or exposed outside of Snowflake and the Data Platform, it introduces significant risks including:

- Loss of governance and access controls
- Inability to audit data usage and access
- Increased security and compliance risks
- Data duplication and inconsistency
- Difficulty maintaining data quality standards

Therefore, when choosing how to access and use data, we prioritize solutions that keep data within Snowflake and the Data Platform ecosystem. The tools and platforms documented below are designed with this principle in mind. 

## Snowflake Snowight for Querying and Dashboards

Snowflake provides out-of-the-box functionality for data exploration and analysis. Team members with Snowflake access can directly query the data for collaborative analysis and build dashboards for visualization. [Access](/handbook/enterprise-data/platform/#warehouse-access) can be requested via Lumos. 

**Important Note:**
This is an environment intended for exploration purposes. Analyses could be shared with team members, but are tied to the team member's Snowflake account and will not persist upon offboarding, nor are any artifacts version controlled.

## Tableau

Tableau is our enterprise Business Intelligence and data visualization tool. It provides a governed, production-ready environment for creating dashboards and reports.

For comprehensive information on Tableau, including access, data sources, governance, and best practices, refer to the [Tableau handbook page](/handbook/enterprise-data/platform/tableau/).

## Census

Census enables data activation by syncing data from Snowflake to downstream business applications.

For detailed documentation on Census, see the [Census handbook page](https://internal.gitlab.com/handbook/enterprise-data/platform/census/).

## Data Pump

Data Pump is our data integration framework that extracts data from Snowflake to S3 for downstream processing and integration with other systems.

For more information on Data Pump, including how to add new pumps and current operational pumps, refer to the [Data Pump section](/handbook/enterprise-data/platform/#data-pump) of the Data Platform handbook.

## Data Spigot

Data Spigot provides controlled access to Snowflake data for external systems through dedicated service accounts, views, and network security policies.

For details on Data Spigot setup and current implementations, see the [Data Spigot section](/handbook/enterprise-data/platform/#data-spigot) of the Data Platform handbook.

## Streamlit

Streamlit enables building custom interactive web applications on top of our data.

For more information on Streamlit, refer to the [Streamlit handbook page](https://internal.gitlab.com/handbook/enterprise-data/platform/streamlit).

## Custom Apps

There is an increasing demand for building custom applications on top of our data. These applications provide tailored solutions for specific business needs beyond what standard dashboards and BI tools can offer.

### Architecture

Custom apps at GitLab follow a **Snowflake-first architecture**. This approach ensures that applications read (and where needed, write) directly to Snowflake, with the data platform providing a governed, auditable data surface and service-account model.

**Key principles:**

- Apps have their own Snowflake [account](https://internal.gitlab.com/handbook/enterprise-data/platform/snowflake/#accounts)
- Data to the App Snowflake account is provisioned via Snowflake shares
- Snowflake shares are managed via Terraform so it is auditable and repeatable
- Avoid additional databases(data stores) outside Snowflake

### Data Modeling and Table Exposure

The Data Platform exposes a curated set of tables and views to these apps through Terraform-managed data shares. This ensures:

- Only the necessary data is exposed to the app
- All exposure is version-controlled and auditable
- New apps can reuse the same pattern rather than requiring ad-hoc grants
- A clear contract exists for what data is guaranteed to be present for the app

### Getting Started

To build a custom app on top of GitLab's data:

1. Work with the Data Platform team to define your data requirements
2. Request a dedicated Snowflake account for development/testing and deployment
3. The Data Platform team will create a Terraform-managed data share with the tables and views your app needs
4. The Data Platform holds data up to and including Orange classification, which includes various forms of sensitive data. Any application built on this data must manage access through Okta/OAuth. The application must implement appropriate security controls, including adherence to the SAFE framework, Row-Level Security (RLS) where applicable, and role-based access aligned with the data's classification level.
