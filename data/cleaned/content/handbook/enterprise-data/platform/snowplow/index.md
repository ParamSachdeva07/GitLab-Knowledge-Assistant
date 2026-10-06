---
title: Snowplow
description: Snowplow Infrastructure Management
---

### Snowplow Overview

Snowplow is an open-source event analytics platform that collects and processes behavioral event data. The platform's architecture overview and source code are available in the [Snowplow repository](https://github.com/snowplow/snowplow/#snowplow-technology-101), which provides comprehensive documentation on its architecture and implementation.

GitLab has managed its own Snowplow infrastructure since June 2019, when we transitioned from a third-party service to self-hosted infrastructure. From the data team's perspective, the core event flow remained the same: events are sent through the collector and enricher, then stored in S3.

As of December 2024, we have upgraded to a new Snowplow environment called `aws-snowplow-prd`. For comprehensive details on the current infrastructure, see the [Snowplow Data Pipeline documentation](https://internal.gitlab.com/handbook/enterprise-data/platform/pipelines/snowplow/).
