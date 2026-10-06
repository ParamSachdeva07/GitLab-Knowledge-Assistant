---
title: "GitLab Security Project Classification"
description: "How GitLab uses security attributes to classify projects for security workflows"
---

## How classification works

GitLab projects are classified using [security attributes](https://docs.gitlab.com/user/application_security/attributes/). This helps Security identify product-related projects, prioritize security work, and support security workflows that rely on project classification.

A centralized pipeline keeps security attributes aligned with the [Data team's product inventory](https://gitlab.com/gitlab-data/analytics/-/blob/master/transform/snowflake-dbt/seeds/seed_engineering/projects_part_of_product.csv). For implementation details, see the [related project](https://gitlab.com/gitlab-private/gl-security/engineering-and-research/security-research/sec-attributes/security-attribute-automation).

## Security attributes schema

The current schema covers product classification. Expansion is planned for future use cases.

| Category       | Attribute | Description                          |
|----------------|-----------|--------------------------------------|
| Classification | Product   | Project contains code we ship to customers, or is part of building and delivering that code |
| Business Impact | Mission Critical   | Projects classified as product, may be expanded to other types of projects in the future |

## Making changes

1. **New projects**: Follow the [creating a new project](/handbook/engineering/workflow/gitlab-repositories/#creating-a-new-project) guidelines. Classification will be applied automatically once the project appears in the product inventory.
1. **Incorrect or missing classification**: Submit an MR to the [Data team's product inventory](https://gitlab.com/gitlab-data/analytics/-/blob/master/transform/snowflake-dbt/seeds/seed_engineering/projects_part_of_product.csv) to add or correct the entry. The sync pipeline will apply the attribute change within 24 hours.
1. **Proposed schema changes**: Open an issue in [product-security-meta](https://gitlab.com/gitlab-com/gl-security/product-security/product-security-meta) to discuss with the product security team before making changes.
