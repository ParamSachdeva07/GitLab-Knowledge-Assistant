---
owning-stage: "~devops::verify"
title: "Nix Package Manager for GitLab Steps"
toc_hide: true
---

## Nix Package Manager for GitLab Steps

## Problem Statement

CI/CD pipelines face critical dependency management challenges:

- **Version Conflicts**: Different steps require incompatible tool versions
- **Setup Overhead**: Each step wastes time installing dependencies
- **Reproducibility Failures**: "Works on my machine" problems persist
- **Container Bloat**: Docker images become massive bundling all dependencies

## Solution: Nix Package Manager Integration

Extend GitLab Steps' compilation model with a `nix:` keyword that compiles to canonical setup steps, providing reproducible dependency isolation without containers.

## How It Works

The `nix:` keyword provides syntactic sugar that compiles to two sequential canonical steps:

1. **Setup step** creates isolated environment with exact package versions
2. **Execution step** runs user command in that environment
3. **Environment variables** passed between steps through outputs

Unlike Docker containers, Nix integration runs as regular processes with native filesystem access. This enables seamless sharing of build directories across steps without volume mounting configuration.

**Key Point**: "Isolation" refers to dependency isolation (preventing version conflicts), not filesystem isolation. Steps naturally access shared directories, build artifacts, and workspace files.

### Compilation Example

**User writes:**

```yaml
spec:
  inputs:
    data_file: { type: string }
---
nix:
  packages: ["python311", "python311Packages.pandas"]
exec:
  command: ["python", "./analyze.py", "${{inputs.data_file}}"]
```

**Compiles to:**

```yaml
run:
  - name: setup_nix_environment
    step: gitlab.com/gitlab-org/runner-tools/nix@v1
    inputs:
      packages: ["python311", "python311Packages.pandas"]

  - name: execute_in_nix_env
    step: gitlab.com/gitlab-org/runner-tools/exec@v1
    inputs:
      command: ["python", "./analyze.py", "${{inputs.data_file}}"]
    env:
      PATH: "${{steps.setup_nix_environment.outputs.PATH}}"
      PYTHONPATH: "${{steps.setup_nix_environment.outputs.PYTHONPATH}}"
```

### Multi-Step Workflow Example

```yaml
# Step 1: Build artifacts in shared directory
nix:
  packages: ["go"]
exec:
  command: ["go", "build", "-o", "./build/myapp"]

---

# Step 2: Test using same build directory (no volume mounting needed)
nix:
  packages: ["python311"]
exec:
  command: ["python", "./test_binary.py", "./build/myapp"]
```

## Benefits Over Docker

| Aspect | Nix Integration | Docker |
|--------|-----------------|--------|
| **Dependency Isolation** | Exact package versions through Nix store paths | Container-level with full OS |
| **Filesystem Access** | Native (shares host filesystem) | Requires explicit volume mounts |
| **Size** | Minimal (packages only) | Large (base image + layers) |
| **Startup** | Fast (no container runtime) | Slower (container lifecycle) |
| **Caching** | Store-based, content-addressable | Layer-based |
| **Reproducibility** | Perfect (functional package manager) | Good (depends on base image) |
| **Multi-version** | Natural (different store paths) | Requires separate images |

## Distribution Strategies

The canonical Nix step supports multiple distribution approaches to balance performance, size, and network requirements:

### On-Demand Download (Default)

```yaml
nix:
  packages: ["python311", "numpy"]
  # Downloads from cache.nixos.org at runtime
```

**Pros**: Small runner images, shared cache, always current
**Cons**: Requires network, slower cold start

### Bundled in Runner Image

```yaml
nix:
  step: gitlab.com/gitlab-org/runner-tools/nix@bundled
  packages: ["python311", "numpy"]
```

**Pros**: Works offline, faster startup
**Cons**: Larger runner images, potential duplication

### Hybrid Approach

```yaml
nix:
  packages: ["python311", "rare-package"]
  bundled: ["python311"]  # Bundle common, fetch rare
```

**Pros**: Balanced size/speed optimization
**Cons**: More configuration complexity

## Implementation Path

1. **Schema Extension**: Add `NixConfig` struct to step definitions
2. **Compilation Logic**: Implement `compileNixStep()` in step compiler
3. **Canonical Step**: Build `gitlab.com/gitlab-org/runner-tools/nix@v1`
   - Uses nix-portable for cross-platform support
   - Outputs environment variables (PATH, PYTHONPATH, etc.)
   - Implements caching for performance
4. **Distribution Options**: Add bundled variants and dependency sharing

## Key Characteristics

- **Cross-Language**: Works for Python, Node.js, Go, Rust, and system tools
- **Modular Architecture**: Core step runner unchanged, complexity in canonical steps
- **No Root Required**: User-space installation and execution
- **Cross-Platform**: Linux native, Windows through WSL, macOS supported

This approach transforms dependency management from a configuration burden into declarative package specifications that compile to reliable, reproducible execution environments.
