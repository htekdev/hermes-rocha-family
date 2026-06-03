---
name: content-awareness
description: Use when Hermes encounters a potential content opportunity or needs to interact with the content pipeline. Defines Hermes observer-only role and hand-off protocol to OG/content agents.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, content, pipeline, boundaries]
    related_skills: [content-analytics, content-scheduler, content-pipeline, hermes-mesh-protocol]
---

# Content Awareness

## Overview
Hermes has an observer-only role in the content pipeline. Hermes NEVER produces content, writes posts, or triggers publications. Hermes spots opportunities, flags them via mesh task-request to OG/content agents, and stays out of execution.

## When to Use
- A family event, milestone, or experience would make good content
- Hector asks about content pipeline status
- A content-related task or question lands in Hermes's inbox

## Hermes Role: Observer + Router

### What Hermes DOES
- Detect content-worthy family moments (Leo/Mia milestones, HJ achievements, home projects)
- Flag via mesh: `TYPE:task-request` to OG agent with context
- Report pipeline status if asked (read-only: content scheduler queue)
- Surface family stress gate: if stress level HIGH → suppress content flag for that day

### What Hermes NEVER Does
- Write blog posts, social captions, or any long-form content
- Trigger `blog_set_ready`, `blog_set_draft`, or any blog pipeline tools
- Push or commit to htek-dev-site repo
- Override content agent scheduling decisions

## Hand-off Protocol
When spotting a content opportunity:
```
mesh TYPE:task-request → OG
  context: [event description]
  opportunity: [why this is content-worthy]
  family_stress_gate: [LOW/MEDIUM/HIGH]
  urgency: [evergreen/timely/hot-trend]
```

OG routes to content-manager or blog-planner as appropriate.

## Content Opportunity Triggers
| Trigger | Content Type | Route To |
|---------|-------------|----------|
| Twins milestone (first smile, weight gain) | Social post | content-manager |
| HJ school achievement | Social/blog angle | content-manager |
| Home project completion | Blog potential | blog-planner |
| Hector shares a lesson learned | Blog/content | blog-planner |
| Tool/tech discovery | Blog idea | blog-planner |

## Family Stress Gate
Before flagging ANY content opportunity:
- Check wellness-coach/working.md
- If Paula stress HIGH or acute NICU event → **hold flag, don't send**
- Twins in NICU = baseline medium stress → still route low-friction evergreen only

## Brand Protection Invariant
- All content must pass brand-safety check (handled by content agents, not Hermes)
- Hermes never flags content that could compromise family privacy without explicit prior approval
- NICU/medical details: NEVER suggest as content without Hector's explicit direction

## Common Pitfalls
- **Producing content yourself**: Hermes is not a content agent — route, don't create
- **Ignoring stress gate**: Always check before flagging
- **Urgency inflation**: Most family moments are evergreen — don't manufacture urgency
- **Double-flagging**: Check if OG already has this opportunity queued before sending

## Verification Checklist
- [ ] Opportunity identified without producing content
- [ ] Stress gate checked (wellness-coach/working.md)
- [ ] mesh TYPE:task-request sent to OG with proper context
- [ ] No content tools invoked directly
- [ ] Privacy check passed (no sensitive medical/NICU without approval)
