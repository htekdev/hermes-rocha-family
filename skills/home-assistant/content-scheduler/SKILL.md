---
name: content-scheduler
description: Use when managing content queue ordering, detecting scheduling collisions, running weekly lineup briefings, or optimizing post timing across platforms. Covers queue rules, reorder technique, and Hermes observer role.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, content, scheduling, social-media]
    related_skills: [content-pipeline, content-analytics, morning-briefing]
---

# Content Scheduler Skill

## Overview
The content scheduler owns queue ordering, cascade timing, weekly briefings, and schedule optimization across Hector's 5 social platforms (~1,400+ scheduled posts). **Does NOT create content.** Hermes's role here is observer/coordinator — flag issues, never touch the queue directly.

## When to Use
- Reporting queue issues or scheduling collisions to Hector
- Requesting a lineup briefing on Mondays
- Understanding content cascade timing rules
- Routing scheduling-related flags to OG via mesh

## Queue Ordering Rules (Priority Order)
| Rule | What | Priority |
|------|------|----------|
| No Collisions | No two posts at same time/platform | Critical |
| Platform Cascade | Long-form before short-form per topic | Highest |
| Topic Clustering | Same-topic posts within 24–48h | High |
| Platform Spacing | Min 2h gap on same platform | Medium |
| Diversity | Don't stack same topic 5x in a row | Low |

## Maintenance Cycle
- **Every 30 min, 8 AM–10 PM CT**: Near-term pass (7-day window, max 6 swaps)
- **Every 3rd cycle (~hourly)**: Deep queue scan (max 5 swaps)
- **Never touch posts within 30 minutes of scheduled publish**
- Clean cycle → log "✅ Near-term clean — no changes needed." and exit silently

## Weekly Lineup Briefing
- Auto-runs Monday mornings (first cron of day)
- Format: clustered by topic, platform icons, totals, issues
- After presenting → await Hector prioritization input → execute reorders

## Reordering Technique
Zernio does NOT support direct queue reordering. Only approved method: **update `scheduledFor` field** via `late_reschedule_post`.
- `post_id`, `scheduled_for` (ISO 8601), `timezone` always required
- For date-swaps: reschedule **both** posts (priority forward, displaced fills old slot)
- On API failure: log and skip — pick up next cycle

## Platform Cascade Rule
Long-form content MUST publish before short-form on same topic:
- Blog/article → LinkedIn long post → LinkedIn short/tweet → IG/TikTok
- Violating this rule reduces reach (followers see summary before substance)

## ⛔ Zero Deletion Authority
**NEVER delete posts.** Only reschedule or reorder. If a post must be removed, escalate to Hector.

## Hermes Domain Boundary
- Hermes **does not touch queues** — only observes and flags
- Scheduling decisions route to OG/content-scheduler agent
- Hermes can report: "Content queue has a collision on Thursday at 2 PM CT" but does not fix it

## Common Pitfalls
- ❌ Touching posts within 30 min of publish (race condition with platform)
- ❌ Deleting posts instead of rescheduling
- ❌ Violating platform cascade (short-form goes out before long-form)
- ❌ Stacking 5+ same-topic posts consecutively (diversity rule)
- ❌ Skipping timezone param in reschedule calls

## Verification Checklist
- [ ] Platform cascade respected (long-form before short-form)
- [ ] No collisions in 7-day window
- [ ] Minimum 2h gap on same platform
- [ ] No posts touching the 30-min publish window
- [ ] Timezone included in all reschedule calls
- [ ] Zero deletions — only reschedule/reorder
