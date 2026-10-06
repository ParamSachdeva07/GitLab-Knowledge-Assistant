---
title: Collaboration on shared feature and experience areas
description: "Collaboration process and documentation of shared feature areas for product groups"
---

## Cross-stage feature collaboration

Each stage is responsible for building functionality that furthers their vision and direction. Even if some components of that functionality happen to cross into spaces typically owned by other stages, they should still build it (if it's important to them).

If the feature isn't _necessary or urgently needed to move forward_ (for example, it won't block another feature's development), then you can always consider putting it on the backlog of the stage that owns that feature.

Here are some guidelines for thinking about "Which stage should do this work?":

1. If a stage wants to develop new functionality that is core to their value, even if it _happens to live inside_ a feature owned by another stage, they should still build it.
1. Alternately, if the functionality lives inside another stage's feature, but is also very-much a _"nice-to-have"_, they should consider putting it in an issue and labeling it appropriately. This way, the stage that owns that feature can prioritize it at a later date when it makes sense for them to do so.
1. External requests for integration with 3rd-party systems should be routed to the group closest to the integrations value proposition or affected area.

### Ownership of existing integrations

The tables below show the ownership of integrations living in the GitLab codebase.

#### Security Related Integrations

| Integration | DRI Group | Rationale |
|---|---|---|
| Akismet | group Authorization | Security monitoring integration |
| Arkose Protect | group Authorization | Security monitoring integration |
| ReCAPTCHA | group Authorization | Security monitoring integration |

#### CI/CD Integrations

| Integration | DRI Group | Rationale |
|---|---|---|
| Bamboo CI | group Pipeline Execution | CI/CD pipeline integration |
| Drone CI | group Pipeline Execution | CI/CD pipeline integration |
| GitHub | group Pipeline Execution | CI/CD pipeline integration |
| Jenkins | group Pipeline Execution | CI/CD pipeline integration |
| JetBrains TeamCity CI | group Pipeline Execution | CI/CD pipeline integration |
| Diffblue Cover | group Pipeline Execution | CI/CD pipeline integration |

#### External Issue Trackers

| Integration | DRI Group | Rationale |
|---|---|---|
| [Asana](https://docs.gitlab.com/ee/user/project/integrations/asana.html) | group Plan:Work Items | Aligns with project management tooling |
| [Bugzilla](https://docs.gitlab.com/ee/user/project/integrations/bugzilla.html) | group Plan:Work Items | Issue tracking functionality |
| [ClickUp](https://docs.gitlab.com/ee/user/project/integrations/clickup.html) | group Plan:Work Items | Project management integration |
| [Custom issue tracker](https://docs.gitlab.com/ee/user/project/integrations/custom_issue_tracker.html) | group Plan:Work Items | Generic issue tracking framework |
| [EWM - IBM Engineering Workflow Management](https://docs.gitlab.com/ee/user/project/integrations/ewm.html) | group Plan:Work Items | Enterprise project management integration |
| [Jira issue integration](https://docs.gitlab.com/ee/integration/jira/configure.html) | group Plan:Work Items | Core issue tracking integration |
| [GitLab for Jira Cloud app](https://docs.gitlab.com/ee/integration/jira/development_panel.html) | group Plan:Work Items | Extension of Jira integration |
| [Pivotal Tracker](https://docs.gitlab.com/ee/user/project/integrations/pivotal_tracker.html) | group Plan:Work Items | Agile project management integration |
| [Redmine](https://docs.gitlab.com/ee/user/project/integrations/redmine.html) | group Plan:Work Items | Issue tracking and project management |
| [YouTrack](https://docs.gitlab.com/ee/user/project/integrations/youtrack.html) | group Plan:Work Items | Issue tracking integration |
| [ZenTao integration](https://docs.gitlab.com/user/project/integrations/zentao/) | group Plan:Work Items | External issue tracking integration |

#### Source Code Integrations

| Integration | DRI Group | Rationale |
|---|---|---|
| PlantUML | group Source Code | Diagram generation integration |
| Sourcegraph | group Source Code | Code search integration |
| Beyond Identity | group Source Code | Identity integration |
| GitGuardian | group Source Code | Security scanning integration |
| [Gitpod integration](https://docs.gitlab.com/ee/integration/gitpod.html) | group Remote Development | Development environment integration |
| [Visual Studio Code extension](https://docs.gitlab.com/ee/user/project/repository/vscode.html) | group Editor Extensions | IDE integration |

#### Project Management Integrations

| Integration | DRI Group | Rationale |
|---|---|---|
| Kroki diagrams | group Project Management | Diagram integration |
| Mailgun | group Project Management | Email service integration |

#### Authentication Integrations

| Integration | DRI Group | Rationale |
|---|---|---|
| [Google Cloud IAM](https://docs.gitlab.com/integration/google_cloud_iam/) | group Authentication | Authentication integration |

#### Container and Package Integrations

| Integration | DRI Group | Rationale |
|---|---|---|
| Google Artifact Management integration | group Container Registry | Container registry integration |
| Harbor integration | group Container Registry | Container registry integration |
| Packagist | group Package Registry | Package registry integration |

#### Search Integrations

| Integration | DRI Group | Rationale |
|---|---|---|
| Elasticsearch integration | group Global Search | Search integration |
| Zoekt integration | group Global Search | Search integration |

#### Mobile DevOps Integrations

| Integration | DRI Group | Rationale |
|---|---|---|
| Apple App Store Connect | group Mobile DevOps | Mobile app distribution integration |
| Google Play | group Mobile DevOps | Mobile app distribution integration |

#### Notification Integrations

| Integration | DRI Group | Rationale |
|---|---|---|
| [Slack Notifications](https://docs.gitlab.com/ee/user/project/integrations/slack.html) (deprecated) | group Plan:Work Items | Team communication with incident management capabilities |
| [Discord](https://docs.gitlab.com/ee/user/project/integrations/discord_notifications.html) | group Plan:Work Items | Team communication and alerting notifications |
| [Google Chat](https://docs.gitlab.com/ee/user/project/integrations/hangouts_chat.html) | group Plan:Work Items | Enterprise team communication and incident alerting |
| [Irker](https://docs.gitlab.com/ee/user/project/integrations/irker.html) | under group Plan:Work Items | IRC-based communication for alerts and notifications |
| [Mattermost notifications](https://docs.gitlab.com/ee/user/project/integrations/mattermost.html) | group Plan:Work Items | Team communication platform with incident management features |
| [Microsoft Teams](https://docs.gitlab.com/ee/user/project/integrations/microsoft_teams.html) | group Plan:Work Items | Enterprise team communication with operational alerting |
| [Pumble](https://docs.gitlab.com/ee/user/project/integrations/pumble.html) | group Plan:Work Items | Team communication platform for notifications |
| [Unify Circuit](https://docs.gitlab.com/ee/user/project/integrations/unify_circuit.html) | group Plan:Work Items | Team communication platform for operational alerts |
| [Webex Teams](https://docs.gitlab.com/ee/user/project/integrations/webex_teams.html) | group Plan:Work Items | Enterprise team communication with incident response features |
| [Telegram](https://docs.gitlab.com/ee/user/project/integrations/telegram.html) | group Plan:Work Items | Mobile-focused team communication for alerting |
| Campfire | group Plan:Work Items | Chat/notification integration |
| Flowdock | group Plan:Work Items | Chat/notification integration |
| Pushover | group Plan:Work Items | Notification integration |

#### Other Integrations

| Integration | DRI Group | Rationale |
|---|---|---|
| [Slack slash commands](https://docs.gitlab.com/ee/user/project/integrations/slack_slash_commands.html) | group Create:Import | Run slash commands from a Slack workspace to operate on GitLab data |
| [GitLab for Slack app](https://docs.gitlab.com/ee/user/project/integrations/slack.html) | group Agent Foundations:AI Catalog (External Agents feature team) | Combination of Slack slash commands integration, and Slack notifications integrations, with additional incident management flows. See the [release and manifest process](/handbook/engineering/ai/agent-foundations/ai-catalog/slack-app-release-process/) |
| [Mattermost slash commands](https://docs.gitlab.com/ee/user/project/integrations/mattermost.html) | group Plan:Work Items | Run slash commands from a Mattermost environment to operate on GitLab data |
| [Trello PowerUp](https://docs.gitlab.com/ee/integration/trello_power_up.html) | group Plan:Work Items | Board-based project management integration |
| [Pipeline status emails](https://docs.gitlab.com/ee/user/project/integrations/pipeline_status_emails.html) | group Verify:Pipeline Execution | CI/CD pipeline notification integration |
| [Emails on push](https://docs.gitlab.com/ee/user/project/integrations/emails_on_push.html) | group Create:Source Code | Source code event notification integration |
| [Gmail Actions Buttons](https://docs.gitlab.com/ee/integration/gmail_action_buttons_for_gitlab.html) | group Plan:Work Items | Email integration with operational response capabilities |
| [Squash TM](https://docs.gitlab.com/ee/user/project/integrations/squash_tm.html) | group Plan:Portfolio Planning | Test management integration |
| [Datadog integration](https://docs.gitlab.com/ee/integration/datadog.html) | group CI Platform | Monitoring integration |

### DRI Group Responsibilities

Product groups designated as DRIs for integrations are responsible for:

- Deciding if new community-contributed integrations should be added to GitLab codebase based on their domain strategy
- Determining if existing integrations should remain in GitLab codebase according to domain strategy
- Following proper process for deprecating and removing integrations when needed
- Maintaining integration documentation
- Re-assigning and triaging integration-related issues to determine prioritization
- Remediating bugs and security vulnerabilities within target SLOs
- Addressing infradev issues and responding to urgent requests
- Responding to Requests for Help and iterating on the integration

Product groups may also designate certain integrations as Community-supported for improvements and additional features at their discretion.

This model allows teams to be flexible and calibrate their priorities accordingly, and no team should ever be "blocked." Exceptions may be items where a change requires anything that a software engineer would not be allowed to do, such as a production change, in which case the infrastructure team would be the blocker.

While any team can contribute features to any stage, it is recommended to loop in the most relevant PM from that Group to provide strategic support to help the contributing team align to the Group's broader plan and vision.

Below is a guide to help other product groups understand how to work on these areas and quickly locate the best parties who may assist on the subject matter.

This section is modeled after the engineering handbook version of [ownership of shared services and components](/handbook/company/infrastructure-standards/realms/infra-shared-services/).

### Existing Cross-Stage Capabilities

- [Merge Requests](https://docs.gitlab.com/user/project/merge_requests/) - also see [collaboration process](/handbook/product/cross-stage-features/merge-requests)
- [Define your CI/CD pipelines directly in your repository](https://docs.gitlab.com/ci/yaml/)
- [Releases associated to milestones](https://docs.gitlab.com/user/project/releases/#associate-milestones-with-a-release)
- [Generate a Release from .gitlab-ci.yml](https://docs.gitlab.com/ci/yaml/#release)
- [Create a GitLab or Jira issue from a vulnerability](https://docs.gitlab.com/user/application_security/vulnerabilities/#create-an-issue-for-a-vulnerability)
- [Create a merge request from an issue](https://docs.gitlab.com/user/project/repository/web_editor/#create-a-new-branch-from-an-issue)
- [Measure DevOps success via the DORA metrics](https://docs.gitlab.com/api/dora/metrics/)
- [Create Incidents as an Issue Type](https://docs.gitlab.com/operations/incident_management/manage_incidents/#from-the-issues-list)
- [Connect your clusters via the CI/CD Tunnel](https://docs.gitlab.com/user/clusters/agent/ci_cd_workflow/)
- [Relate issues and Feature Flags](https://docs.gitlab.com/operations/feature_flags/#feature-flag-related-issues)
- [Run multiple pipelines and project dependencies with multi-project pipelines](https://docs.gitlab.com/ci/pipelines/downstream_pipelines/#multi-project-pipelines)
- [Enable concurrency control during deployments with Resource Groups](https://docs.gitlab.com/ci/resource_groups/)
- [Associate job artifacts, or a generic package to a Release](https://docs.gitlab.com/user/project/releases/)

### Planned Cross-Stage Improvements

- [Software Supply Chain Security](https://about.gitlab.com/direction/supply-chain/)
