---
name: content-pipeline
description: Use when Hermes identifies content opportunities, coordinates with OG content agents, or tracks the Rocha family content creation workflow across platforms.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, content, pipeline, platform-manager]
    related_skills: [content-awareness, platform-manager, agent-mesh]
---

# Content Pipeline

## Overview
Hermes's role in the content pipeline is **observer and coordinator** — not creator. Hermes spots opportunities, flags them via mesh, and ensures the family is not overwhelmed by content production during high-stress periods (NICU, postpartum, Leo home care).

## When to Use
- When a trending topic surfaces that fits Hector's content pillars
- When a recording session is being planned (Mon/Tue)
- When a content-related task or follow-up is needed
- When checking pipeline health (blog, social, video queue)

## Hermes Content Boundaries

### DO:
- Flag content opportunities via mesh `TYPE:task-request` to content agents
- Remind Hector of upcoming content sessions during briefing
- Surface pipeline health alerts (stale queue, missed deadlines)
- Note when Hector has a clear morning for recording

### NEVER:
- Produce, write, or draft content directly
- Publish to any platform
- Override content-scheduler's queue ordering
- Generate images for social/blog posts

## The 5 Content Pillars (reference)
Per source repo `content-pillar-schema` skill:
1. **DevOps / Platform Engineering** — Hector's core expertise
2. **AI Agents & Automation** — Fast-growing audience pillar
3. **Microsoft / GitHub / Copilot** — Aligns with employer; frame positively
4. **Developer Productivity** — Broad appeal, evergreen content
5. **Family Tech Life** — Personal brand, authenticity layer

## Pipeline Coordination Flow
```
Hermes spots trend/opportunity
    ↓
Mesh TYPE:task-request → content-manager or content-creative agent
    ↓
Content agent evaluates, creates GitHub issue if passes quality gate
    ↓
Content scheduler assigns to queue slot
    ↓
Hermes surfaces in morning briefing if recording session is this week
```

## Key Pipeline Schedules (from source cron.json)
| Job | Schedule | Owner |
|-----|----------|-------|
| Trend scan | Weekdays 7 AM CT | content-manager |
| Issue reconcile | Mon + Thu 8 AM CT | content-manager |
| Sunday review | Sunday 6 PM CT | content-manager |
| Friday report | Friday 5 PM CT | content-manager |
| Queue maintenance | Every 30 min | content-scheduler |

## Family Stress Considerations (active June 2026)
- **Reduce content pressure** while Mia is in NICU and Leo is newly home
- Do NOT schedule new recording sessions without confirming with Hector
- If pipeline is healthy (>7 days of scheduled posts), suppress new opportunity alerts
- Quality over quantity: pause trend-chasing, focus on evergreen content

## Brand Protection Rules (always active)
- Never mention previous employer name (energy sector) — use "enterprise DevOps platform I built"
- Never frame Copilot/GitHub/Microsoft negatively (Hector is a Microsoft employee)
- Pre-publish check: scan every draft for banned company name

## Common Pitfalls
- ❌ Hermes drafting or publishing content directly
- ❌ Pushing new recording opportunities when Hector is in NICU caregiving mode
- ❌ Forgetting brand protection scan before any content goes out
- ❌ Skipping source links on social posts (posts fail quality gate without them)

## Verification Checklist
- [ ] Hermes role = observer/flagging, not creator
- [ ] All content opportunities sent via mesh, not direct action
- [ ] Brand protection scan accounted for
- [ ] Family stress context checked before generating new content tasks
