---
title: "AI Usage Principles"
description: "How Infrastructure Platforms uses AI tools responsibly and effectively."
---

We use AI tools to help us work. These principles exist to make sure that help doesn't come at someone else's expense, and instead raises the bar for everyone.

## Keep empathy in the loop

People are affected by our work. Be respectful of the time it takes someone to respond to your comment, review your code, and the stress that being on-call creates when there are incidents. If AI helps you work faster, use some of that additional free time to make your communication with others more thoughtful and impactful.

## Communicate as yourself

Using AI to help frame or structure a response is fine. The end result should still be yours. When you're talking to another person, whether in an MR comment, a Slack thread, or (for some reason) an email, they deserve a response that reflects your actual understanding in your own voice. Using AI to summarise a long thread or large amounts of text is okay, but let people know that's what you've done so they can give it the appropriate level of scrutiny.

## Good input, good output

AI is only as useful as the context it has to work with. Our documentation and code are that context. Keeping them accurate, well-structured, and up to date isn't just good practice, it directly improves the quality of what AI can help us produce.

## Own what you ship

Whether hand-written or generated, the work you produce should be something you're proud to put your name against. That doesn't only mean code quality. A largely generated internal tool that solves a pain point for the team is something to be proud of, even if the code itself is throwaway.

## Match scrutiny to impact

Not all code carries the same risk. Infrastructure configuration, our observability stack, anything with SLAs or on-call implications: these need the same rigorous review regardless of how they were produced. Plausible is not the same as correct, and if you haven't verified it, don't merge it.

On the other hand, internal tooling with a minor or non-existent failure mode doesn't need the same level of rigour. If it's something you wouldn't have had time to build by hand anyway and worst case of it not working is a small inconvenience, treat it accordingly.
