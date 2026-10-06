---
title: "AI Usage Recommendations"
description: Suggestions for getting better results from LLM tools
---

AI tools can return results of varying utility depending on how and what the tool is requested to do. This guide provides strategies for Support Engineers to get more effective results when using LLMs for troubleshooting, research, and customer interactions.

## How to talk with LLMs

When doing research, be as factual and straightforward as possible. Do not provide opportunities for shortcuts, such as either-or questions or confirmations. Think of what kind of answer that is needed and formulate a request with that in mind.

Specific data (such as log messages) can be included to give the LLM context; these data give the model additional context to process. The LLM may not need an explanation of the issue; passing in a log snippet is enough to start a discussion.

## Open versus closed questions

Asking questions that are pointed at providing specific answers can be more effective than open-ended questions. This attempts to guide the machine in a direction that is more likely to be useful.

## State your goal

Combining a goal or pointed question with a pasted log snippet constrains the problem space and helps keep everything on track.

## Examples

Good:

- "Show me where authentication is handled in the API controllers"
- "This GitLab CI job fails with 'executor not found'. Here's the .gitlab-ci.yml and the runner config. Tell me what you think." \[paste configs]
- "What do you think of this Sidekiq log? \[paste error]"

Bad:

- "Is this error caused by SSL or DNS? \[paste error]"
- "This exception was thrown while a pipeline was running. Why did the pipeline cause the exception? \[paste error]"
- "Was this issue caused by a misconfiguration or a bug? \[paste error]"

## Don't count on LLMs

LLMs are terrible with numbers and math. Do not count on their abilities to do math or understand numbers in relation to each other.

## Things to watch out for

LLMs get confused about dates easily. They can suggest versions that are older than expected, or suggest that a version is invalid because it "hasn't been released". This may also apply to _relative_ dates: something that "released last year" might not be.

The model may confidently suggest documentation, API endpoints, versions, or almost anything else. Always ground-truth verify suggestions. This can be especially insidious with API and CLI options.

## Human-in-the-loop

AI doesn't have taste or judgement. Use it as a tool to gather the data you need to move the task forward while validating from the source material.

- AI can summarize, rephrase, rank, or brainstorm.
- You decide, validate, experiment, and communicate.

---

## Troubleshooting with LLMs

LLMs can be used to debug in a variety of ways. Agentic tools can be used at different stages of the debugging process to reduce friction — creating simplified YAML, or code that will trigger an exploit scanner, for example. When using these tools, be cognizant that ZenDesk data is ORANGE, but attachments are RED. Not all LLM tools are cleared for RED data.

These examples use logs, configs, and/or snippets gathered from the user as an input to move debugging forward.

### Build minimal repro projects and pipelines

Draft minimal project config.

Good usage:

- “From this `.gitlab-ci.yml`, remove everything unrelated to the job and produce the smallest pipeline that should still reproduce the error.”  
  \[paste `.gitlab-ci.yml` and job log]
- "From this summary, build a simplified `.gitlab-ci.yml` to reproduce the issue and commit to this project.  
  \[paste ticket summary]

### Code generation for debugging security scanners

LLMs can create code snippets needed for debugging. Reproducing a scanner failure can be easier when we vulnerable code can be created for testing.

Examples:

- “Write a program that would be vulnerable to CVE-123-456 and commit to this project so I can debug a security scanner”
- “Create a small `docker-compose.yml` and vulnerable dependency list that should produce at least one dependency-scanning finding for `openssl`.”

### Generating fake secrets for debugging

LLMs know what secrets look like. Ask for example secrets for debugging.

Examples:

- “Can you generate me a fake GitLab API key for secret detection?”
- “Generate an example key that matches the Anthropic key format”

### Interpreting logs and errors

Treat AI as a second pair of eyes on logs and stack traces you paste in.

Examples:

- “Tell me what you see in this stack trace. Do you have any suggestions?”  
  \[paste stack trace + version]
- “Please review these logs. Tell me what you think.”  
  \[paste selected job logs]

Use it here to get a first pass on the logs that might highlight things of interest.

---

## Customer communication

LLMs may be useful to turn your notes into more conversational text, but they're not the final authority. Carefully review anything generated for correctness and tone.

Ideas:

- Go from a bullet-point analysis to a draft reply.
- Adjust tone (more concise, more empathetic, less jargony) without changing the technical content.
- Propose alternative phrasings
- Have it review your text and suggest edits

Good usage:

- “Here are my notes for an update. Write a concise, professional reply that a GitLab Senior Support Engineer would send. Don’t add any new claims.”  
  \[paste your own bullet points / outline]

- “Review this explanation and let me know what you think; would a new GitLab admin understand it?”  
  \[paste your draft]

- “Shorten this update by about 30% while preserving the key actions, results, and next steps.”  
  \[paste your draft]

Guardrails:

- You verify every technical statement before sending.
- Don’t ask, “What should I tell the customer?” without giving your own analysis first.

---

## AI as a debugging partner, not a decision-maker

LLMs can be used to aid structured thinking; it can ask questions related to a ticket, help organize data into a testable hypothesis, or challenge your reasoning while you drive the investigation.

Patterns:

- Request a critique for a testing plan
- Validate if you've missed data in an analysis

Good usage:

- “Here is the situation, my current hypothesis, and the steps I’ve taken. Act as a critical peer reviewer: evaluate what assumptions I'm making and if there is more data I need to gather for validation?”  
  \[paste case summary]

- “Given this job log and my notes, suggest some possible root causes and suggest ways to test each root cause.”  
  \[paste log + notes]

- “Here's an error. What data do we need to gather to understand this error? Please don't draw any conclusions yet.”  
  \[paste symptom summary]

---

## Comparing configs, feature flags, and environments

LLMs can be great at "spot the difference" issues, such as when there's a configuration difference between config files.

Good usage:

- “Compare these two `gitlab.rb` files: one from a working environment, one from a failing one. Highlight only the differences that are plausibly related to Sidekiq performance.”  
  \[paste config A]  
  \[paste config B]

- “Here is a `.gitlab-ci.yml` and my repro `.gitlab-ci.yml`. List which differences could explain why the repro does _not_ fail in the same way.”  
  \[paste both files]

- “Given these two sets of feature flag settings (customer vs. GitLab.com default), identify flags that are plausibly related to the reported behavior.”  
  \[paste redacted feature flag dumps]

---

## Summarizing long threads, tickets, and logs for yourself

Agents can be great for summarizing data; this ranges from the Glean ticket summary bot to 

Good usage:

- “Summarize this Zendesk ticket thread into: (1) customer’s current understanding, (2) what we’ve already tried, (3) open questions, and (4) potential next steps. Do not propose new technical facts; just reorganize what’s there.”  
  \[paste ticket thread or key excerpts]

- “Summarize this issue discussion into a one-paragraph status update plus a bullet list of remaining blockers.”  
  \[paste issue comments] or ask Duo from the issue

---

## Brainstorming test cases and edge conditions

If you fail to reproduce an issue in a test project use an AI for ideas about edge cases or suggestions for additional test cases.

Good usage:

- “Given this minimal repro project and the bug I’m seeing give me some options for test cases and/or extra jobs to understand the scope of the issue.”  
  \[describe repro + symptoms]

- "I fixed this issue by changing the job definition; could that have any downstream effects I should be aware of for the user?"
  \[paste MR description]

---

## Building example commands and scripts

Scripts and/or commands can be generated by AI. These should be tested before being provided to a user.

Good usage:

- “Write a Python API script that walks all projects in a group and turns off this feature”  
  \[paste details]

- “Build an example API query to check variables for a pipeline”  
  \[paste steps]
  