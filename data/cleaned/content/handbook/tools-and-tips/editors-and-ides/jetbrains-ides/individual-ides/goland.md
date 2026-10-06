---
title: "GoLand"
---

## Overview

Website: <https://www.jetbrains.com/go/>

Best for: Applications written primarily in Go.

## Common JetBrains Setup and Configuration

JetBrains IDEs are standardized, so much of the setup and configuration information applies to all IDEs, and can be found under [Common JetBrains Setup and Configuration](../setup-and-config/_index.md).

Specific config for GoLand can be found in the sections below.

## GoLand-specific Setup and Configuration

### GoLand Settings

- This assumes you have installed `go` via [mise](https://gitlab-org.gitlab.io/gitlab-development-kit/howto/mise/).
- Under `Go` section:
  - `GOROOT`
    - Press `+`, and add `$HOME/.local/share/mise/installs/go/latest`
    - After you have added it, select it.
