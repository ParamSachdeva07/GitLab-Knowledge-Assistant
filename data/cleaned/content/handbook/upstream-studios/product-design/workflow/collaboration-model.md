---
title: Collaboration Model
description: "A shared language for the two modes of product design work: Design for Discussion and Design for Development."
---

Product design work at GitLab moves between two modes: Design for Discussion and Design for Development. These modes are not a rigid process or a set of gates. They give the trio (Product Management, Product Design, and Engineering) a way to name what a piece of work is for at any given moment, and to pick the tools and fidelity that fit. Anyone in the trio can put work forward in either mode; the mode matters more than who made it.

Naming the mode tells everyone how to read what they are looking at and what response is useful. A concept meant to open a conversation deserves a different response than a solution ready to build.

Anyone in the trio can propose a solution. What matters is not who made it, but what it is for. Naming the mode tells everyone how to read what they are looking at and what response is useful. A concept meant to open a conversation deserves a different response than a solution ready to build.

## Two Modes

### Design for Discussion (diverging)

Design for Discussion explores possibilities and tests assumptions. These are rough concepts meant to spark conversation, gather feedback, and align on direction before we invest in details. A lot of vision work lives here.

The goal is to test concepts and iterate. You are getting internal alignment by validating with customer zero and design partners. This is **divergent** thinking: going wide to generate and communicate ideas. Production code pulls toward convergence: it asks for correct states, established patterns, and buildable detail. Without room to first diverge, a team may converge on the first buildable idea instead of the best one.

Use the tool that lets you do that fastest, whether that is Figma, FigJam, a standalone prototype, or the development environment. The artifact may be a decision guide, a mental-model pressure test, an alignment diagram, and/or a prototype.

### Design for Development (converging)

Design for Development is the work of getting a solution live. These are production-ready, annotated, have held up with customers and been reviewed with engineering for feasibility. This is **convergent** thinking. You have aligned on a direction, and now you bring it together to be production-ready. This is where the seamless handoff in a development environment (GDK/Caproni) becomes ideal, where a chosen solution is refined and made real.

## Choosing a mode (and moving between them)

Most non-trivial projects (XL, L, M) start with Design for Discussion. The most common question is: _"At what point is it no longer for discussion and now for development?"_ There is no single gate, but a useful test is:

- **You are still in Discussion** while the direction is a hypothesis. The question is _"is this the right thing to build?"_ and you are still gathering feedback and buy-in.
- **You have moved to Development** once the trio has aligned on a solution. The question becomes _"how do we make this real, in all its states, ready to build?"_
 
Movement goes both ways. Work returns to Discussion when the direction stops holding up, whether that is a validation session that goes sideways or a constraint that changes what is possible. That is the system working, not the project slipping.

## Tooling by mode

The mode determines the tool, not the other way around.

| | Design for Discussion (diverging) | Design for Development (converging) |
|---|---|---|
| **Goal** | Align on direction; test assumptions | Validate and build the aligned solution |
| **Thinking** | Divergent: go wide, generate options | Convergent: refine one direction |
| **Fidelity** | Whatever communicates the idea fastest | Moving towards production-ready, all states defined |
| **Typical tools** | Figma, FigJam, decks, live code prototypes | Draft MR, design specs and annotations |
| **Ownership** | Design facilitates the conversations with the trio | Design owns the experience, Engineering owns the production code |

## Where prototyping happens

GDK is the right environment for Design for Development. Once a direction is set, designing in the real product with real components and real constraints is what makes the work production-ready.

Discussion work has a different requirement: getting an idea in front of people fast enough to change your mind about it. Three practical differences make lighter-weight prototypes the faster path there today.

- **Sharing and feedback.** A static prototype publishes to a URL anyone can open and comment on. A GDK-derived prototype is much harder to share and comment on today, so the return on getting feedback isn't there yet. Teams across the org are working on this gap.
- **Setup and seed data.** Designers often design for a job to be done. Creating that exact data condition live in code takes far more effort than vibing a prototype about it.
- **Speed of divergence.** Concepting means generating and discarding many ideas quickly. Throwaway prototype code is a fast way to get an interaction in front of people and reach alignment.
