---
title: "Sandbox Cloud Realm"
description: "This handbook section defines the latest iteration of infrastructure standards for AWS and GCP sandboxes across all departments and groups at GitLab."
---

### Quick links

#### User Portal

- [gitlabsandbox.cloud](https://gitlabsandbox.cloud)

#### Documentation

- [Global infrastructure standards](/handbook/company/infrastructure-standards/)
- [Global labels and tags](/handbook/company/infrastructure-standards/labels-tags/)
- [Infrastructure policies](/handbook/company/infrastructure-standards/policies/)

#### Issue Tracking and Collaboration

- [HackyStack issue tracking](https://gitlab.com/gitlab-com/gl-security/identity/eng/hackystack-enhanced/-/issues) (feature development and bugs)
- [CorpSec issue tracking](https://gitlab.com/gitlab-com/gl-security/corp/issue-tracker/-/issues) (GitLab-specific topics and requests)
- `#sandbox-cloud-questions` Slack channel to ask questions and get help.

#### Code and Examples

- [HackyStack Enhanced source code](https://gitlab.com/gitlab-com/gl-security/identity/eng/hackystack-enhanced)
- [HackyStack Enhanced README](https://gitlab.com/gitlab-com/gl-security/identity/eng/hackystack-enhanced/-/blob/main/README.md)

#### Infrastructure-as-Code

- [Sandbox Cloud - Project Templates](https://gitlab.com/gitlab-com/infra-standards/project-templates)
- [Sandbox Cloud - Terraform Modules](https://gitlab.com/gitlab-com/infra-standards/terraform-modules)
- [Sandbox Cloud - Ansible Roles](https://gitlab.com/gitlab-com/infra-standards/ansible-roles)
- [IT Infrastructure Realm IaC - Terraform Configuration for gitlabsandbox.cloud](https://ops.gitlab.net/it-infra-realm/environments/gcp/gcp-project-hackystack-mgmt/gitlabsandbox-cloud-app-tf) - Restricted access
- [IT Infrastructure Realm IaC - Ansible Configuration for gitlabsandbox.cloud](https://ops.gitlab.net/it-infra-realm/environments/gcp/gcp-project-hackystack-mgmt/gitlabsandbox-cloud-ansible) - Restricted access

## Overview

The Sandbox Cloud is an automated provisioning platform for creating an AWS account or GCP project that you can use for demo, sandbox, testing and production-esque purposes, paid for by GitLab with consolidated invoice billing (no credit card required).

This platform is powered by [HackyStack Enhanced](https://gitlab.com/gitlab-com/gl-security/identity/eng/hackystack-enhanced), an open source Laravel application maintained by Vlad Stoianovici. HackyStack automates the access request process using Okta integration, auto-assigns roles and permissions based on your department, and uses cloud provider APIs for provisioning your AWS account and GCP project.

The Sandbox Cloud is managed by the [CorpSec Identity](/handbook/security/corporate/) team. Please ask in `#sandbox-cloud-questions` on Slack with any questions, or tag `@vlad` in a CorpSec issue.

### How to Get Started

#### Individual AWS Account or GCP Project

Any team member can use the self service instructions below to provision an AWS account or GCP project for your individual use (sandbox, testing, etc.). You cannot invite other team members to individual accounts for security reasons.

1. Visit [https://gitlabsandbox.cloud](https://gitlabsandbox.cloud) and sign in with your Okta account.
1. Navigate to **Cloud Infrastructure** in the top navigation.
1. Click the purple **Create Individual Account** button.
1. Choose the *cloud provider* and *cloud organization unit* from the dropdown list. **If no options are present in the dropdown list for the organization unit, your department has not been created in our database yet due to a department name change or addition in the HRIS. Please ask in `#sandbox-cloud-questions` to have it added.**
1. Click the green **Create Account** button.
1. Your account will take 2-5 minutes for the AWS API to finish the provisioning process while the AWS services are activated for your account.
1. Please refresh your browser window every ~60 seconds until you see that your user account has changed from `Provisioning` to `Active`.
1. See the instructions below for [Accessing your AWS Account](#accessing-your-aws-account) or [Accessing your GCP Project](#accessing-your-gcp-project).

> You can sign-in with Okta, however please don't create a Cloud Account unless you intend to provision AWS resources.

**Is your current AWS account experience problems?** Please ask for help in `#sandbox-cloud-questions`. If your problems are validated and approved for getting a new AWS account, please use the [New AWS Individual Account Rebuild Request](https://gitlab.com/gitlab-com/gl-security/corp/infra/issue-tracker/-/issues/new?issuable_template=aws_individual_account_rebuild_request) issue template.

#### Automated Shutdown Policy

For cost saving and exposure reduction measure, any GCP compute engine instances in an individual account (ex. `dmurphy-a1b2c3d4`) are powered down every Friday at 23:59 UTC starting 2023-02-03. You will receive a Slack bot notification 24 hours in advance for any instances that are affected with instructions for adding a label to the instance if you need to prevent power off.

If an instance is powered off, you can simply power the instance back on when you're ready to work again.

We are not charged for the hours that compute instances that are not powered on (e2-standard-4/4vCPU/16GB costs $0.13/hr or $96.48/mo). Storage for a powered down instance is cheap and a 20GB persistent disks cost $0.80/month.

This has immediate 28%+ cost savings by not having ephemeral infrastructure running on Saturdays and Sundays. Additional cost savings since we are not charged until you power the instance back on (could be days, weeks, or months later). This also covers abandoned instances that were only used for a few hours for a demo.

We will be working on AWS accounts in a future iteration.

#### Collaborative AWS Account or GCP Project (Non-Production)

Any team member can request a new AWS account or GCP project for a specific project or working group, or for general usage by their department group for shared non-production resources. These are called Collaborative Accounts/Projects, as opposed to Individual Accounts/Projects, which every team member can self-provision from Sandbox Cloud.

**No RED data is allowed in these accounts/projects.** Any RED data must be hosted in production AWS accounts or GCP projects managed by the appropriate Infrastructure Realm administrators (ex. `eng-infra-saas`, `it-infra`, etc.).

Collaborative Accounts/Projects self-service creation and IAM management is not available yet for end users in HackyStack. In the meantime, we use access request style issue templates as our boring solution for security compliance reasons and the HackyStack administrators provision accounts and users using the Admin CLI.

- [Issue Template](https://gitlab.com/gitlab-com/gl-security/corp/issue-tracker/-/issues/new?issuable_template=aws_account_create): New AWS Group Workload (Multi-user) Account Request
- [Issue Template](https://gitlab.com/gitlab-com/gl-security/corp/issue-tracker/-/issues/new?issuable_template=aws_account_iam_update): Add/Remove IAM Users from AWS Group Workload Account
- [Issue Template](https://gitlab.com/gitlab-com/gl-security/corp/issue-tracker/-/issues/new?issuable_template=aws_account_delete): Decommission an AWS Account
- [Issue Template](https://gitlab.com/gitlab-com/gl-security/corp/issue-tracker/-/issues/new?issuable_template=gcp_project_create): New GCP Group (Multi-user) Project Request ([Provisioner Runbook](https://gitlab.com/gitlab-com/gl-security/corp/infra/runbooks/-/blob/main/gitlab-sandbox-cloud/add-group-project-for-gcp.md))
- [Issue Template](https://gitlab.com/gitlab-com/gl-security/corp/issue-tracker/-/issues/new?issuable_template=gcp_project_iam_update): Add/Remove IAM Users from GCP Group Project
- [Issue Template](https://gitlab.com/gitlab-com/gl-security/corp/issue-tracker/-/issues/new?issuable_template=gcp_project_delete): Decommission a GCP Project

#### Production Environments

##### Product Related

For any staging or production(-esque) infrastructure services that are customer facing, contain [Red or Orange data](/handbook/security/policies_and_standards/data-classification-standard/#data-classification-levels), related to the GitLab product or GitLab.com SaaS, or Engineering sponsored services, please contact the [Reliability Engineering](/handbook/engineering/infrastructure-platforms/) team for guidance on next steps in the `#infrastructure_lounge` Slack channel.

Most environments are typically created in the [config-mgmt project](https://gitlab.com/gitlab-com/gl-infra/config-mgmt) using the [Create a new environment](https://gitlab.com/gitlab-com/gl-infra/config-mgmt/#creating-a-new-environment) instructions.

You can learn more about GitLab.com SaaS on the [Production Architecture](/handbook/engineering/infrastructure-platforms/production/architecture/) handbook page.

Any projects with [yellow or green](/handbook/security/policies_and_standards/data-classification-standard/#data-classification-levels) data usually are better suited for self management using [Group Projects](#collaborative-aws-account-or-gcp-project-non-production) using [Infrastructure Standards](/handbook/infrastructure-standards) guidelines.

##### Business Related

For any infrastructure services related to business operations and our tech stack, please contact IT via the Compass app in Slack (type "Compass" in the top search bar to find it) or it-help@gitlab.com. Most of our [tech stack](/handbook/business-technology/tech-stack-applications/) are SaaS-based and hosted by the respective vendor.

New SaaS applications should go through the [Procurement Process](/handbook/finance/procurement/) and are managed by the respective department's [system owners](/handbook/business-technology/#cross-department-system-owners).

Self-hosted application infrastructure is determined on a case-by-case basis and is architected in collaboration with [CorpSec Identity Engineering](/handbook/security/corporate/engineering/identity), [Infrastructure Security](/handbook/security/product-security/infrastructure-security/), [Application Security](/handbook/security/product-security/security-platforms-architecture/application-security/), and [3rd Party Risk](/handbook/security/security-assurance/security-risk/third-party-risk-management/). Please tag `@vlad` in an issue for preliminary guidance on new services. If you do not have an issue yet, please create one in the [CorpSec issue tracker](https://gitlab.com/gitlab-com/gl-security/corp/issue-tracker/-/issues).

#### Accessing your AWS Account

1. Sign in to [https://gitlabsandbox.cloud](https://gitlabsandbox.cloud) and navigate to [Cloud Infrastructure](https://gitlabsandbox.cloud/cloud).
1. If you have not created an account yet, click the [Create Individual Account](https://gitlabsandbox.cloud/cloud/accounts/create) button and use the form to create a new account. If you already have an account, click on the title or the gear icon for the AWS account you want to access.
1. On the `Cloud Account` details page, click the `View IAM Credentials` button in the top right corner to open up a popup modal window.
1. You will see the `AWS Console URL`, `Username`, and `Password` that you can use to sign in to your AWS account. The 12 digit number at the beginning of the URL is your AWS Account ID/Number.
1. Create a new 1Password record in your Private vault to save these credentials.
1. You can click on the link to open the AWS console, or you can close the modal window and click the `Open AWS Web Console` button on the `Cloud Account` details page.
1. Use the provided **URL**, **Username**, and **Password** to sign in to your new AWS account. *Be careful that your browser doesn't automatically fill in saved credentials for a different account.*
1. After you sign in, you should navigate to IAM and add a Virtual MFA device for your user account and add a One-Time Password (OTP) to your 1Password record.
1. Your IAM user account has `AdministratorAccess` to be able to perform any action inside of your AWS account. We do not provide team members access to the `root` user account since we only use this for break glass security incidents or related administrative activity by the [Infrastructure Realm Owners](/handbook/company/infrastructure-standards/#realm-owners).

#### Accessing your GCP Project

1. Sign in to [https://gitlabsandbox.cloud](https://gitlabsandbox.cloud) and navigate to [Cloud Infrastructure](https://gitlabsandbox.cloud/cloud).
1. If you have not created an account yet, click the [Create Individual Account](https://gitlabsandbox.cloud/cloud/accounts/create) button and use the form to create a new account. If you already have an account, click on the title or the gear icon for the GCP project you want to access.
1. On the `Cloud Account` details page, click the `View Credentials` button in the top right corner to open up a popup modal window.
1. You will see the `GCP Console URL` and username. Since GCP uses Google authentication, you simply need to be signed in with your GitLab email address on Google. HackyStack has added the `Owner` GCP IAM role to your email address when the project was created. Your project ID is in the format of `{emailHandle}-{cloudAccountShortId}`. You can choose this project from the dropdown list when accessing a different project in the GCP console.
1. After accessing your project for the first time, you will be prompted to enable the service for each of the GCP services that you want to use in your GCP project. This is expected behavior and will take a few seconds and is a one time step during project initial configuration.

## Domain Names

See the [Domain Names and DNS Records](https://internal.gitlab.com/handbook/security/product_security/infrastructure_security/guides/domains-dns/) InfraSec guide internal handbook page for more details.

## Terraform Environments

### How Terraform Environments Work

- New GitLab Omnibus instance for securely hosting GitLab Terraform (GitOps) projects for all team members when they create a Cloud Account with GitLab Sandbox Cloud.
- New [GitLab Project templates](https://gitlab.com/gitlab-com/infra-standards/project-templates) with Terraform scaffolding and [easy-to-use Terraform modules](https://gitlab.com/gitlab-com/infra-standards/terraform-modules). We provide the foundation for you to use any of the [Terraform.io Registry providers or modules](https://registry.terraform.io/) with built-in support for the Google Cloud provider.
- Every GitLab Sandbox Cloud GCP project now has an automatically created GitLab group and a [starter GitLab project with a GitOps Terraform configuration scaffolding](https://gitlab.com/gitlab-com/infra-standards/project-templates/gcp-sandbox-environment-template) with provisioning automation powered by GitLab CI. This allows team members to start deploying resources with Terraform in just a few minutes without dealing with Terraform set up, while complying with security best standards.
- We will have additional project templates released throughout the coming months that provide pre-configured environments that you can provision with just a few clicks. This includes [Omnibus/Runner/Cluster all-in-one environments](https://gitlab.com/gitlab-com/infra-standards/terraform-modules/gcp/gitlab-omnibus-sandbox-tf-module), Kubernetes cluster environment, etc. We also have the foundation to be able to explore how to support [GitLab Environment Toolkit](https://gitlab.com/gitlab-org/gitlab-environment-toolkit).
- You can also easily create additional Terraform projects in the Sandbox Cloud UI for different environments or configurations in the same Cloud Account to allow you to isolate your module/resource configuration based on the use case that you're experimenting with.

### How to Create a Terraform Environment

1. Sign into [https://gitlabsandbox.cloud](https://gitlabsandbox.cloud)
1. Create a Cloud Account in GCP (GCP Project) or navigate to an existing project.
1. Click the **Create Terraform Environment** button and fill out the form:
   1. Choose your Cloud Account from the **Cloud Account** dropdown list.
   1. Choose the template you wish to use from the **Environment Template** dropdown list. If this is your first time, use the `gcp-sandbox-environment-template-v2-########` template.
      - If you are looking for a more detailed template (where you can set the version and enable a runner) use `support-resources-template-v2`.
   1. Input a name for your environment in the **Environment Name (`Alphadash` Slug)** text field.
1. After the Environment is created, click the **View Terraform Configuration** button. This is hosted on a new GitLab instance at [https://gitops.gitlabsandbox.cloud](https://gitops.gitlabsandbox.cloud). Your GitLab instance credentials can be found in the View GitOps Credentials button modal.
   - You can create multiple Terraform Environments, subject to GCP resource quotas and cost considerations. Every Friday, your GCP compute instances will automatically be powered down for cost savings and security best practices.

### How to Use Terraform Environments

1. Sign into [https://gitops.gitlabsandbox.cloud](https://gitops.gitlabsandbox.cloud) using your generated credentials on [https://gitlabsandbox.cloud](https://gitlabsandbox.cloud). Keep in mind that this is `{firstInitial}{lastName}-{hash}` and not your normal GitLab username.
1. Navigate to the project for the Terraform environment that you just created. You can quickly access the project from the link on the Cloud Account page on [https://gitlabsandbox.cloud](https://gitlabsandbox.cloud).
1. On your local computer navigate to your `~/.ssh` folder and generate an SSH key

   ```shell
   ssh-keygen -t rsa -b 4096 -C <name_of_project>
   ```

1. Navigate to terraform/main.tf on this project and copy and paste your public key. See the example below

   ```shell
   #     -------------------------------------------------------------------------    ----
   # Add your Terraform modules and/or resources below this line
   #     -----------------------------------------------------------------------------

   locals {
     ssh_key               = "<RSA public key here>"
     normalized_env_prefix = "sr-${var.env_prefix}"
    tags                  = ["sr-firewall-rule", "${local.normalized_env_prefix}-firewall-rule"]
   }
   ```

1. Run a new CI pipeline. After the `Plan` job completes, trigger the `Deploy` job. (Notice how you haven't had to do any configuration).
1. Watch the `terraform apply` outputs as your new environment is spun up with a sample Ubuntu virtual machine for testing with. You can add additional Terraform resources as you see fit (see below).
1. Navigate to the GCP console using the link on [https://gitlabsandbox.cloud](https://gitlabsandbox.cloud) to view the deployed VM. Feel free to connect to the VM through SSH using the `gcloud` command or Cloud Shell.
1. Run the GitLab CI job for `Destroy` to clean up your resources.
1. You can update the `terraform/main.tf` file in the Git repository to add more Terraform resources or modules.
1. Simply run the `Deploy` CI pipeline job to deploy your resources.

### Navigate Terraform Environments in a GCP environment

1. Once on your GCP account page you will see the test environments you've created on the bottom of the page.
1. To view CI Pipelines, locate your environment in the list and click on the rocket icon (🚀) in the actions column on the far right side of the row.
   1. Log on to your GitLab Sandbox Cloud GitOps Environments.
    - To find your GitOps URL credentials, go to your GCP sandbox account homepage and click **View Credentials**.
1. You are now able to view your environment.

## Delete an AWS account or GCP project

### Individual accounts

Individual accounts can be deleted through self-service in the Sandbox Cloud portal. Before deleting, make a best effort to delete all resources within the account to avoid continued costs during the grace period.

1. Sign in to [https://gitlabsandbox.cloud](https://gitlabsandbox.cloud) and navigate to **Cloud Infrastructure**.
1. Click on the account you want to delete.
1. Use the **Delete Account** option on the account details page.
1. The account enters a grace period before permanent deletion (90 days for AWS, 30 days for GCP). During this period, the account can be restored by contacting `#sandbox-cloud-questions`.

When a team member departs GitLab, their individual sandbox accounts are automatically deprovisioned through Okta integration.

### Collaborative accounts

To decommission a collaborative (multi-user) AWS account or GCP project, file a request using the appropriate issue template. Manager approval is required.

- [Decommission an AWS Account](https://gitlab.com/gitlab-com/gl-security/corp/issue-tracker/-/issues/new?issuable_template=aws_account_delete)
- [Decommission a GCP Project](https://gitlab.com/gitlab-com/gl-security/corp/issue-tracker/-/issues/new?issuable_template=gcp_project_delete)

Before requesting deletion, coordinate with your team to delete all resources within the account. If you have questions, ask in `#sandbox-cloud-questions`.

## Background and History

Over the years, GitLab's non-production infrastructure resources grew organically without accountability, cost controls, or security best practices across GCP and AWS. In FY21-Q3, company-wide [infrastructure standards](/handbook/company/infrastructure-standards/) were established with [labels, tags, and naming conventions](/handbook/company/infrastructure-standards/labels-tags/) and the concept of [realms](/handbook/company/infrastructure-standards/#gitlab-infrastructure-realms) to create separate security boundaries for different use cases.

The first release of [HackyStack](https://gitlab.com/hackystack/hackystack-portal) was developed as an open source project to automate sandbox provisioning end-to-end. The codebase was later forked to [HackyStack Enhanced](https://gitlab.com/gitlab-com/gl-security/identity/eng/hackystack-enhanced) under the CorpSec Identity team for active development, and is now owned and maintained by Vlad Stoianovici and the CorpSec Identity team.

### Business and financial impact

- All infrastructure resources are associated with a user and department for cost allocation
- Reduced or eliminated expense reports with AWS invoices for individual usage (consolidated billing)
- Budgets and cost controls with Slack notifications to reduce abandoned test environment costs
- Automated access request and provisioning process
- Standardized organizational hierarchy and naming schema for AWS accounts and GCP projects
- Automated security best practice controls and least privilege rights
- Automated cleanup of departed team members' cloud resources through Okta integration (implemented November 2025), eliminating over $600K in annual cloud spend from abandoned accounts in FY26

### Tech Stack

- [Laravel 11](https://laravel.com/docs/11.x) (PHP 8.1) — web portal, CLI application, API provisioning handler
- MySQL — database
- [Terraform](https://www.terraform.io/) — infrastructure-as-code configuration
- [AWS SDK for PHP](https://github.com/aws/aws-sdk-php)
- [Google Cloud Client for PHP](https://github.com/googleapis/google-api-php-client)
- [GitLab API](https://github.com/GitLabPHP/Client) — Git SCM of Terraform configurations
- [GitLab CI](https://docs.gitlab.com/ee/ci/) — automated Terraform deployments
- MCP Server (TypeScript) — programmatic access to Sandbox Cloud operations through HTTP API

### Recent developments

- **MCP HTTP API** (March 2026) — HTTPS endpoints on gitlabsandbox.cloud for programmatic access to Sandbox Cloud operations, eliminating the SSH/VPN dependency for automation
- **Per-user MCP API keys** (March 2026) — individual API keys per user with SHA-256 hashing, replacing the shared API key model
- **Okta integration** (March 2026) — OAuth client credentials flow with Okta for automated profile sync (department, title, manager) and webhook-driven account deprovisioning on employee departure
- **Slack notifications framework** (March 2026) — cost digests, billing alerts, and decommission warnings delivered to users through Slack
- **Bulk departed-user cleanup** (February 2026) — 263 accounts from departed users cleaned up across AWS and GCP, eliminating over $600K in annual cloud spend

### Current priorities

See the [Sandbox Cloud issues](https://gitlab.com/gitlab-com/gl-security/corp/issue-tracker/-/work_items?label_name%5B%5D=corpsys-sandbox-cloud) in the CorpSec issue tracker for the latest priorities and planned work.

### How to contribute

Please post your ideas in `#sandbox-cloud-questions` on Slack or in the [CorpSec issue tracker](https://gitlab.com/gitlab-com/gl-security/corp/issue-tracker/-/issues/new) so we can discuss the best ways to implement them.

The Sandbox Cloud is maintained by the CorpSec Identity team. For questions, feature requests, or bug reports, tag `@vlad` in a CorpSec issue or ask in `#sandbox-cloud-questions`.
