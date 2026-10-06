---
title: "Snowflake CLI"
description: "Installing and configuring the Snowflake CLI for local development"
---

## What and why

The [Snowflake CLI](https://docs.snowflake.com/en/developer-guide/snowflake-cli/index) (`snow`) is a command-line tool for interacting with Snowflake directly from your terminal. It is the standard for local Snowflake access on the Data team, enabling ad-hoc SQL execution, local dbt development workflows, and integration with OpenCode agent sessions.

## Prerequisites

- macOS with [Homebrew](https://brew.sh/) installed
- An active Snowflake account with Okta SSO access

## New setup

If you are setting up your machine for the first time, the onboarding script handles both installation and configuration. Download the script from your browser (you must be logged into GitLab):

[Download the onboarding script](https://gitlab.com/gitlab-data/analytics/-/raw/master/admin/onboarding_script.zsh)

Then run the full onboarding script from your terminal, passing your role:

```zsh
zsh ~/Downloads/onboarding_script.zsh --role analytics-engineer
```

The script will install the Snowflake CLI and configure it as part of the standard setup. See the [Data Onboarding issue template](https://gitlab.com/gitlab-data/analytics/-/blob/master/.gitlab/issue_templates/Team:%20Data%20Onboarding.md) for full instructions.

## Existing users

If your machine is already set up and you only need to install or configure the Snowflake CLI, use one of the following approaches.

`setup_snowflake_config` will prompt for your GitLab email address, write `~/.snowflake/config.toml` with the `GITLAB` connection, set the required file permissions, and test the connection. Your browser will open briefly for Okta SSO.

**Note:** If `~/.snowflake/connections.toml` exists on your machine, the Snowflake CLI gives it priority over `config.toml`. The script will detect this, show you the file contents, and prompt you to remove it before writing a fresh `config.toml`.

If you have custom connections in that file you want to keep, rename it first and fix permissions manually, then re-run `setup_snowflake_config`:

```zsh
mv ~/.snowflake/connections.toml ~/.snowflake/config.toml
chmod 0600 ~/.snowflake/config.toml
```

`setup_snowflake_config` will detect that `config.toml` now exists, ensure permissions are correct, and test the connection. You can add any additional `[connections.*]` blocks to the file manually afterward.

**Note on `snowsql`:** `snowsql` uses a separate config file (`~/.snowsql/config`) and is not affected by removing or renaming `~/.snowflake/connections.toml`.

### Method 1: Via local repo

If you already have the analytics repo cloned, update it and source the script directly:

```zsh
jump analytics
git checkout master
git pull

cd admin/
source onboarding_script.zsh
install_snowflake_cli
setup_snowflake_config
```

### Method 2: Via download

If you do not have the analytics repo locally, download the script from your browser (you must be logged into GitLab):

[Download the onboarding script](https://gitlab.com/gitlab-data/analytics/-/raw/master/admin/onboarding_script.zsh)

Then source it and run the two relevant functions directly:

```zsh
source ~/Downloads/onboarding_script.zsh
install_snowflake_cli
setup_snowflake_config
```

## Verify

```zsh
snow connection test
snow sql -q "SELECT CURRENT_USER(), CURRENT_ROLE()"
```

`snow connection test` will open your browser for Okta SSO authentication. Once authenticated, the second command should return your Snowflake user and active role.

## Common usage

Run an inline query:

```zsh
snow sql -q "SELECT CURRENT_DATE()"
```

Run a SQL file:

```zsh
snow sql -f path/to/query.sql
```

Use a named connection explicitly:

```zsh
snow sql -c GITLAB -q "SELECT CURRENT_USER()"
```

Switch to a larger warehouse for a heavy query by prepending a `USE WAREHOUSE` statement:

```zsh
snow sql -q "USE WAREHOUSE DEV_L; SELECT COUNT(*) FROM prod.common.fct_orders"
```

## OpenCode integration

The `snowflake` tool in OpenCode wraps `snow sql` and uses the `GITLAB` connection from `~/.snowflake/config.toml` by default. No additional configuration is needed once the CLI is set up. Agents will use this tool automatically for any Snowflake queries during a session.
