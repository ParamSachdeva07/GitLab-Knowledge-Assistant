---
title: Opportunistic Attacks
no_list: true
---

Opportunistic attacks are more spontaneous initiatives than [Stealth Operations](../stealth-operations.md). They can be done at any time, from any source IP address, and against any GitLab-managed asset without prior approval or notification.

One key differentiator is that Stealth Operations are generally modeled around a specific adversary or campaign, closely emulating those tactics to improve our resilience against a specific threat. Opportunistic Attacks, however, are the creative and relentless pursuit of a goal using whatever it takes to achieve it.

For example, a Red Team member may identify an exploitable service or behavior that could lead to initial access. Instead of a long formal planning process, they will jump on the opportunity and execute as complete of an attack path as possible. Strict documentation is still required for auditing and report writing.

Benefits include:

- They give GitLab more opportunities to practice detecting and responding to realistic threats in a controlled environment, allowing faster iteration on our defensive capabilities and investigation skills.
- They allow us to quickly demonstrate the real impact of security concerns.
- They can help prioritize investigations to uncover potential historical threat actor behavior.

If vulnerabilities are discovered, we exploit them and work to safely demonstrate maximum impact. This may involve establishing persistence, escalating privileges, and other common attack techniques.

When immediate action is required, we follow the standard process for [reporting an incident](/handbook/security/#reporting-an-incident). For vulnerabilities that appear wide-spread or recurring, we create an issue inside the [Vulnerability Management issue tracker](https://gitlab.com/gitlab-com/gl-security/product-security/vulnerability-management/vulnerability-management-internal/vulnerability-management-tracker/-/issues) to implement automated scanning capabilities.

We list examples of [opportunistic attack techniques](../how-we-operate/rules-of-engagement.md#opportunistic-attack-techniques) inside our rules of engagement.

## Club Red

Club Red is our program that allows GitLab team members to help us discover and develop initial access vectors and optionally, collaborate with us to carry them out.

Occasionally team members reach out with a cool hack idea, often based on knowledge they have. Club Red aims to provide a way for them to collaborate with us develop their idea for a greater overall security result for GitLab.

If you are an internal GitLab team member with an interesting idea, please [contact us](../_index.md#contact-us).
