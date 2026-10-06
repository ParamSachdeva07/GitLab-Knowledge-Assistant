---
title: 'Round robin'
description: 'Documentation on our ticket round robin'
---

This guide covers our ticket round robin, an automation system that performs the assignment of tickets based on specific criteria.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
- Project repo: [Zendesk US Government](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/tickets/round-robin)

**Note**: This only applies to Zendesk US Government at this time.

{{% /alert %}}

## Understanding our ticket round robin

### How it works

{{% alert title="Technical Details" color="primary" %}}

- Ruby version: `3.2.2`
- Gem list:
  - [activesupport](https://rubygems.org/gems/activesupport)
  - [base64](https://rubygems.org/gems/base64)
  - [concurrent-ruby](https://rubygems.org/gems/concurrent-ruby)
  - [faraday](https://rubygems.org/gems/faraday)
  - [faraday-multipart](https://rubygems.org/gems/faraday-multipart)
  - [faraday-retry](https://rubygems.org/gems/faraday-retry)
  - [json](https://rubygems.org/gems/json)
  - [openssl](https://rubygems.org/gems/openssl)
  - [yaml](https://rubygems.org/gems/yaml)
- CI/CD Images:
  - `curlimages/curl:latest`
  - `ruby:3.2.2`
- Scheduled runtime: Every 10 minutes, Monday-Friday, 0500-1659 Pacific (`*/10 5-16 * * 1-5`)

{{% /alert %}}

Before each job runs, it performs a few actions to setup the image to perform the needed actions:

- Clones the repo at [support-team](https://gitlab.com/gitlab-support-readiness/support-team) to `data/support-team`
- Output the response from running the command `ruby -v`
- Install the `bundler` gem
- Run the `bundle` command
- Put the values of the environment variable `SERVICE_CREDS` into the file `data/config.json`

After this, the `./bin/round_robin` script is executed.

Using a pre-made view, the script will get a list of tickets to round robin. If there are no tickets, the script will exit with a status code of 0.

The script will then determine the currently available agents by checking the [support-team](https://gitlab.com/gitlab-support-readiness/support-team) information, remove any agents on PTO, and remove any agents not currently within working hours. In the event no agents are available, it will post a notification to a Slack control via a Support controlled Slack incoming webhook (and exit with a status code of 0).

Using the list of currently available agents, it will then determine the current workloads of said agents (this is done by looking at assigned tickets with a status lower than solved) using the `Ticket Weight` field on the tickets it locates (a numeric value dictating the complexity of a ticket).

After gathering the tickets in need of being round robin'd (using the [Not round robined view](https://gitlab-federal-support.zendesk.com/agent/filters/360240736651)), the script will then assign them out to the agent with the lowest workload (incrementing their workload by 1).

## Administrator tasks

### Modifying the round robin

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

To modify the round robin, you will need to create a MR in the project repo. The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR. Once merged, it will be used on the next scheduled pipeline run.

## Common issues and troubleshooting

This is a living section that will have items added to it as needed.
