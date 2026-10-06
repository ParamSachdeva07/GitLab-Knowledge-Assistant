---
title: "Build Team Strategic Vision"
description: "Fast, Secure, and Scalable Component Delivery Across All Platforms"
---

## **Build Strategy: Fast, Secure, and Scalable Component Delivery Across All Platforms**

### **I. Diagnosis: Build Process Constraints & Product Velocity Impact**

#### **Current State**

GitLab's build system evolved to serve an increasingly complex product landscape: 80+ application components must be packaged, tested, and delivered across multiple deployment models that include GitLab.com, GitLab Dedicated, Omnibus GitLab, and Cloud Native GitLab. While the build process is similar for most components, each deployment model differs significantly in velocity and feedback.

The GitLab.com and GitLab Dedicated teams directly manage their own infrastructure. They may ship updates multiple times per day with rapid iteration processes that allow quick recovery from failures. This directly contrasts with the much slower cadence for self-managed customers. Self-managed instances rely on a formal build, test, and release process. This process delays feedback and bug fixes follow the same build, test, and release processes. The lengthy release cycle to release features and fix bugs diminishes the the GitLab experience for self-managed customers.

Additionally, some components can only ship to GitLab.com and GitLab Dedicated because they do not follow the standard build and release process required for Omnibus GitLab and Cloud Native GitLab. These components typically do not meet the quality customers expect and require significant rework to ship to Self-Managed customers.

The primary bottleneck for Build is the one-to-multiple quarters time required to onboard new components for Self-Managed customers. It requires active co-ordination and capacity across the entire Delivery stage. Without a streamlined, self-service path to onboard new GitLab components the Delivery Stage becomes a serial gate in the product delivery pipeline.

The bifurcation between Self-Managed and GitLab managed deployments created a downward spiral into technical debt. Component teams bypass processes to onboard their components more quickly but without sufficient rigor. The generated quality debt often forces re-work or even a complete re-write to bring the component into Self-Managed customers. Increased complexity creates more delays which pushes more teams to circumvent standardized processes and requirements validation. This cycle leads large increases to operational burden and multiplies the threat surfaces for security and compatibility.

---

#### **Pain Points Impacting Product Delivery**

**1\. Feature Delivery to Self-Managed is Constrained by Onboarding Complexity & Lack of Self-Service**

Teams building new features, especially AI/ML components critical to GitLab's competitive position, cannot ship to Self-Managed without a complex, non-standardized onboarding process. This complexity stems from the high quality bar required for Self-Managed that includes robust packaging, support across diverse customer environments, and operational excellence combined with the lack of a standardized, repeatable path for integration. Onboarding a component requires active involvement from multiple teams across the Delivery Stage.  There is no standardized "paved path" for self-service integration, no clear platform abstractions, and no consistent automation to reduce coordination burden. Component teams cannot onboard themselves; they are entirely dependent on Delivery Stage assistance each step.

* Example: OpenBao onboarding for GitLab Secrets Manager has taken multiple quarters across packaging, infrastructure, and configuration work—with active coordination required from multiple teams at every stage

**Impact**: GitLab cannot ship new and important features to Self-Managed fast enough, directly impacting time-to-market and competitive advantage. Delivery Stage becomes a serial gate where every component waits for coordinated capacity and handoffs. Progress stalls if any team is blocked, and no parallelization is possible without clear, self-serviceable mechanisms. Additionally, when teams bypass the standard onboarding process to reach customers faster, they risk quality and user experience issues that compound operational burden and customer satisfaction.

---

**2\. Decentralized Dependency Management Slows Feedback & Extends Cycle Time**

Each component team manages dependencies independently, creating a fragmented dependency landscape. When updates are attempted, conflicting dependency versions often surface during package assembly—requiring coordination across multiple teams to resolve. This decentralization compounds with slow build feedback loops.

* Dependency updates are slow and error-prone  
* Security patches are delayed waiting for conflict resolution across teams  
* Build pipelines for MRs routinely take **30 minutes to 2.5 hours** because the entire stack rebuilds from scratch for every MR across all supported OS distributions—regardless of which components changed  
* This architectural decision does not scale: as the number of components, supported distributions, architectures, and offerings grows, so does the pipeline burden  
* Developers get late feedback on critical issues because build failures surface near release time rather than during development

**Impact**: Slow feedback loops discourage rapid iteration. Dev teams lose confidence in the canonical build process and invest in local, divergent build environments, deepening drift and creating a vicious cycle that further delays issue detection.

---

**3\. Fragmented Build Infrastructure & Inconsistent Environments Mask Problems Until Late**

Component teams and the Build Team operate in divergent build environments. This fragmentation—combined with the need to maintain multiple package variants—creates a complex, manual operational burden that masks integration problems until the final release stage.

* **80+ component teams** each maintain their own build environments (custom containers, divergent toolchains)  
* **Build Team operates the canonical environment** used for release artifacts—but this divergence means conflicts only surface during final package assembly  
* **56 distinct Linux packages** must be maintained (14 distributions × 2 architectures × 2 offerings)  
* Vulnerability triaging is manual and inefficient: a single CVE requires analyzing and understanding impact across all supported OS distributions, then coordinating patching across the entire matrix of variants  
* **Build and distribution processes are tightly coupled**: Omnibus and Cloud Native GitLab have separate build pipelines and artifact production processes, preventing a single artifact from being reused across distribution methods

**Impact**: High operational toil; slow security response; resource-intensive vulnerability remediation. Late-stage surprises delay releases and increase emergency escalation overhead. Adding new OS distributions or managing new dependencies multiplies this burden exponentially across all supported variants.

---

### **II. Guiding Policy**

#### **Strategic Principle**

Enable component teams to self-serve their onboarding to Self-Managed by decoupling the build process from distribution methods, allowing the same artifacts to flow securely through Omnibus, Cloud Native GitLab, and other paths. Build Team provides the build platform, standardized tooling, and guardrails—ensuring company-set standards (language frameworks, dependency versions, etc.) are met—but does not dictate those standards or perform manual gatekeeping.

#### **Objectives**

**Objective 1: Fast, Self-Serviceable Component Onboarding**

Reduce build-related onboarding work from multiple quarters to **1 month for known and existing patterns** by enabling component teams to integrate independently via standardized tooling and paved paths.

*Addresses: Pain Point 1*

---

**Objective 2: Unified, Reproducible Builds Across All Platforms**

Establish a canonical build environment and toolchain shared by all component teams and Build Team. Detect **100% of build issues before final package assembly** (or upstream in CI), enabling early feedback and preventing late-stage surprises.

*Addresses: Pain Points 2 & 3*

---

**Objective 3: Scalable Build Infrastructure**

Decouple build process from distribution methods and standardize artifact production, enabling the same artifact to flow through Omnibus, Cloud Native GitLab, and other paths. Reduce operational burden and enable simpler scaling to new platforms.

*Addresses: Pain Point 3*

---

#### **Design Principles**

**Organizational Principles**

**1\. One Way to Build Everything**

There is a single, canonical build process and environment that all components use. No exceptions, no alternate paths. This is essential for scalability and enables fast innovation with reduced coordination overhead.

**2\. Build Team as Enablers, Not Gatekeepers**

Build Team provides platform, tooling, and standards. Component teams own their onboarding and perform integration work. Build Team supports and guides, enabling autonomy rather than orchestrating handoffs.

**3\. Enable Early Validation**

Developers validate builds in the canonical environment as early as possible—ideally in development or CI. Early feedback prevents quality issues from accumulating until release.

**4\. Standardization Over Customization**

Default to standardized solutions. Custom solutions require clear business justification and approval. This prevents tool sprawl and ensures shared improvements benefit all teams.

---

**Technical Principles**

**5\. Decouple Build From Distribution**

The build process produces a single canonical artifact. Distribution methods consume and package it for their environment. This separation enables reuse and prevents divergence.

**6\. Reproducible Builds**

Every build with identical inputs produces identical outputs through:

* Canonical, immutable build environment  
* Unified toolchain (UBT)  
* Deterministic dependency resolution  
* Complete visibility of all dependencies and sources

**7\. Complete Provenance and Supply Chain Integrity**

Every artifact includes metadata tracing back to source code, build environment, and dependencies. This enables traceability, security compliance, and rapid vulnerability response.

**8\. Comprehensive Platform Coverage Testing**

Automated testing across all supported OS distributions and architectures validates that components work together as a coherent product. With UBT, a single binary must function everywhere—comprehensive testing ensures this.

---

### **III. Coherent Action**

#### **Key Initiatives**

**1\. Platform Foundation (UBT \+ TUBE \+ Metapackages)**

Establish a unified build environment, dependency management, and standardized build process across all components. This includes:

* Universal build toolchain (UBT) providing consistent compiler, build tools, and system libraries  
* Standard build environment and centralized dependency management (TUBE)  
* Modular metapackaging enabling customers to select and install only the components they need, reducing resource waste and operational complexity  
* Decoupling of build process from distribution methods, enabling single artifacts to flow through multiple paths  
* Incremental component-level builds where only changed components are rebuilt (avoiding full-stack rebuilds on every pipeline run)

---

**2\. Self-Service Onboarding (CI Templates & Paved Paths)**

Enable component teams to integrate independently into Self-Managed without Build Team orchestration. This includes:

* Standardized CI templates and configuration standards that teams can use directly  
* Comprehensive documentation and onboarding guides (paved paths)  
* Tooling and automation to reduce manual handoffs and coordination overhead  
* Support and guidance from Build Team as enablers, not gatekeepers

---

**3\. Quality & Validation Infrastructure**

Implement comprehensive automated testing and validation across all supported platforms. This includes:

* Automated testing pipelines (QA, end-to-end, smoke tests) across all supported OS distributions and architectures  
* Integration of provenance tracking and supply chain visibility into the build process  
* Early issue detection and feedback mechanisms for developers

---

**4\. Operational Excellence**

Establish monitoring and observability for the build platform. This includes:

* Real-time visibility into build performance and health  
* Metrics and dashboards tracking build success rates, cycle times, and resource utilization  
* Incident response and alerting mechanisms

---

#### **Implementation Roadmap**

**Timeline Overview (FY27)**

The roadmap shows parallel workstreams with dependencies. All timelines are estimates and will be refined as scope and planning are completed in each phase.

---

**Q1 FY27**

| Initiative | Status | Notes |
| ----- | ----- | ----- |
| **Platform Foundation** | UBT: Final phase, targeting completion end of April | Quality & Validation work ongoing as part of UBT requirements |
| **Platform Foundation** | TUBE: Scope definition and planning phase | Implementation to begin once scope is finalized |
| **Self-Service Onboarding** | Blocked pending UBT/TUBE foundation | Scope definition and POC can begin in parallel with TUBE planning |
| **Operational Excellence** | POC in progress, formalizing scope | Building pipeline observability foundation with metrics and dashboards |

---

**Q2 FY27**

| Initiative | Status | Notes |
| ----- | ----- | ----- |
| **Platform Foundation** | UBT: Complete (end of April) | All components migrated to unified toolchain; incremental component builds and performance improvements realized |
| **Platform Foundation** | TUBE: Implementation begins | Estimated 2-3 quarter delivery timeline |
| **Self-Service Onboarding** | Scope and POC phase | Initial templates and paved paths definition begins |
| **Quality & Validation** | Expanding platform coverage | Building on UBT foundation with full test automation |
| **Operational Excellence** | Scope formalization and implementation | Establishing metrics and dashboards for pipeline visibility; preparing to capture UBT/TUBE value metrics |

---

**Q3-Q4 FY27**

| Initiative | Status | Notes |
| ----- | ----- | ----- |
| **Platform Foundation** | TUBE: Implementation in progress | On track for completion by end of FY27 |
| **Self-Service Onboarding** | Early adoption phase | Potential for first self-onboarded components by end of FY27 if TUBE/UBT complete |
| **Quality & Validation** | Full deployment | Comprehensive platform coverage testing operational across all distributions |
| **Operational Excellence** | Full implementation | Build platform monitoring and observability live; metrics tracking UBT/TUBE impact |

---

**End of FY27 Target State**

* ✓ UBT complete: all components migrated to unified toolchain by end of April  
* ✓ TUBE complete: all existing and new components hooked into centralized dependency management  
* ✓ Incremental component-level builds reducing full-stack rebuild cycles; performance improvements measurable  
* ✓ Quality & Validation infrastructure operational across all supported platforms  
* ✓ Build platform monitoring, observability, and metrics in place; UBT/TUBE value demonstrated  
* **Target (pending scope/planning)**: Self-service onboarding framework in place; early components successfully onboarded independently

---

**Key Dependencies & Assumptions**

* Self-Service Onboarding is dependent on UBT and TUBE being largely complete  
* TUBE adoption depends on component teams' prioritization and willingness to migrate—Build Team can provide the platform, but component teams control adoption pace  
* TUBE scope and implementation timeline to be finalized in Q4 FY26 / Q1 FY27  
* Operational Excellence POC provides foundation for capturing and demonstrating UBT/TUBE value through metrics  
* Timelines are estimates and will be refined as planning progresses in each phase

#### **Success Metrics & Outcomes**

\[To be populated\]

#### **Risks & Mitigations**

\[To be populated\]

---

### **Appendix**

#### **Related Documents & Context**

\[To be populated\]

#### **Glossary**

\[To be populated\]
