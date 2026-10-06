---
title: "GitLab Model Vendor Selection Guidelines"
description: "The framework GitLab uses to evaluate and select AI model vendors."
---

## Purpose and Scope

These guidelines establish GitLab's framework for evaluating and selecting the vendors who develop the models powering GitLab Duo, including GitLab Duo Agent Platform, features ("Model Developers") and the vendors who host those models ("Model Hosts," and together "Model Vendors"). Model Vendors only include (1) GitLab subprocessors and (2) vendors whose models are hosted by GitLab or a GitLab subprocessor, and exclude vendors whose models are supported in GitLab Duo Self-Hosted. These guidelines apply to all new Model Vendor selections.

## Core Requirements

### 1. Data Privacy

We built GitLab Duo to be privacy-first, and we hold our Model Hosts to this same standard.

At a minimum, we require our Model Hosts to:

- Refrain from training on GitLab's and GitLab's customers' private data, and commit to doing so contractually; and
- Limit data retention of GitLab customer inputs and outputs to what is necessary for service operation.

### 2. Ethical Concerns

GitLab is dedicated to responsibly incorporating AI into our comprehensive DevSecOps platform. We know that, without guardrails, AI features may give rise to ethical concerns.

We require our Model Developers to take these ethical concerns into account and work to address them, including by demonstrating that they have taken steps to mitigate bias and potential harms in the training data process.

### 3. Risk Allocation

We look for Model Hosts who will partner with us as we strive to build powerful and trustworthy GitLab Duo features. We require that Model Hosts (a) allow our customers to retain ownership over their inputs, and (b) assign to the customer all output generated for that customer (to the extent permitted by applicable law).

### 4. Reputational Risks

Our Model Vendors' products help power some of our most important features. We are thus careful to evaluate potential reputational risks when selecting new Model Vendors.

In considering reputational risks posed by new Model Vendors, we consider:

- How long they've been operating for, and whether they have an established track record in the industry;
- Whether, and to what extent, they have funding;
- Which entities they are affiliated with;
- What countries they operate in; and
- Whether they have received any negative publicity in the past.

### 5. Transparency

Transparency is one of GitLab's [core CREDIT values](/handbook/values/), and we expect our Model Vendors to prioritize this value as well.

In order to be considered, Model Hosts must provide processes for bug reporting and resolution.

### 6. Security

GitLab is a DevSecOps platform, and we strive to integrate security throughout all GitLab Duo features. In keeping with this practice, we expect the Model Hosts powering our AI features to implement:

- Robust security measures against model poisoning and adversarial attacks;
- Industry standard authentication, authorization, access, system and network security, data governance, and risk management controls;
- Resilient Business Continuity and Disaster Recovery controls;
- Regular security updates and patch management; and
- Appropriate incident response and breach notification procedures.

We require our Model Hosts to have a SOC2 Type 2 report covering at least the Security, Confidentiality, and Availability trust principles, and active ISO 27001 certification.

### 7. Performance and Quality

GitLab expects Model Hosts to provide globally available model deployments and demonstrate strong metrics with respect to latency, accuracy, output quality, and cost efficiency. In some cases, we will consider a model with strong latency performance even if it is not globally deployed.

### 8. Sustainability

We expect Model Vendors to adopt sustainable practices throughout the development and deployment of AI models when possible. GitLab aims to gather details such as estimated energy consumption for typical workloads, carbon emissions per inference/training session, calculation methodologies used, and optimization techniques implemented.
