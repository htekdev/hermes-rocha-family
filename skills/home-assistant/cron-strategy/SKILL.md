---
name: cron-strategy
description: Use when designing, auditing, or modifying Hermes's cron job schedule. Defines backbone slots, job spacing rules, cost-optimized tiers, and family-care scheduling priorities.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, cron, automation, scheduling, cost]
    related_skills: [hermes-cron-schedule, checkin-orchestrator, heartbeat-protocol, cost-optimizer]
---

# Cron Strategy

## Overview
Cron scheduling for Hermes is constrained by three factors: **cost** (model tier selection), **conflict avoidance** (3-min minimum gap), and **family-care priority** (family jobs run before all others). The source-of-truth pattern is the htekdev/copilot-home-assistant cron.json structure.

## When to Use
- Adding a new cron job to Hermes
- Auditing the current schedule for conflicts or inefficiency
- Selecting appropriate model tier (Sonnet vs Haiku) for a job
- Deciding job frequency for a monitoring loop
- Investigating why a job is silent or overactive

## Backbone Slots (Reserved Minute Offsets)

| Minute | Purpose | Jobs |
|--------|---------|------|
| `:00–:03` | Heartbeat / task-coach | checkin, task-coach-nudge |
| `:06–:10` | Family care | nicu-care, parenting-coach |
| `:10–:20` | Daily lightweight | wellness-coach, meal-planner, luna |
| `:30–:42` | Content pipeline | content-scheduler, content-analytics |
| `:45–:53` | Platform / dev | platform-manager, repo-maintainer |

**Rule:** Minimum 3-minute gap between any two jobs in the same hour. Never stack jobs at `:00`.

## Cost-Optimized Model Tiers

| Tier | Model | Use For |
|------|-------|---------|
| Full | claude-sonnet-4.6 | Morning briefing (2x/day), nightly reflection, weekly planner |
| Lightweight | claude-haiku-4.5 | All other heartbeats (6x/day), task-coach nudges, checkins |

**Heartbeat optimization:** 2x full/day (6 AM + 9 PM) + 6x lightweight. Was 8x full — high savings, same coverage.

**Lightweight checkin MUST:**
- Only scan urgent emails (last 2h), upcoming events (next 2h), HIGH/URGENT tasks
- Stay completely silent if nothing urgent
- Skip: sub-agent dispatches, working memory updates, full categorization

## Family Care Jobs — Always Protected

These jobs run regardless of cost optimization passes. Never reduce frequency or disable without explicit approval:

| Job | Schedule | Agent |
|-----|----------|-------|
| nicu-care-checkin | `:06` every 2h (7–21) | nicu-care |
| wellness-coach-morning | 8:03 AM daily | wellness-coach |
| wellness-coach-midday | 1:10 PM daily | wellness-coach |
| wellness-coach-evening | 6:00 PM daily | wellness-coach |
| parenting-coach-morning | 8:06 AM daily | parenting-coach |
| parenting-coach-afternoon | 2:00 PM daily | parenting-coach |

**NICU/PPD state:** While NICU or PPD window is active, these jobs are **exempt from early-termination and cost-opt**. Never disable nicu-care or wellness-coach during active NICU phase.

## Daily Job Schedule (Rocha-Adapted)

### Weekday
| Time | Job |
|------|-----|
| 6:00 AM | morning-briefing (Sonnet) |
| 6:15 AM | daily-finance-review |
| 7:00 AM | cost-optimizer |
| 7:33 AM | heartbeat (full) |
| 8:03 AM | wellness-coach-morning |
| 8:06 AM | parenting-coach-morning |
| 9:00 AM | heartbeat-lightweight |
| 9:03 AM | task-coach-nudge |
| 10:00 AM | task-coach-ask-Paula |
| …etc | (backbone repeats each 2h) |
| 9:10 PM | nightly-reflection |

### Weekend
| Time | Job |
|------|-----|
| 8:00 AM | weekend-briefing |
| 9:30 AM | meal-plan-prompt (Saturday) |
| 10:05 AM | meal-planner (Saturday) |

## Content Pipeline Jobs

Backbone slot: `:30–:42`. All 4x-daily cadence.

| Job | Schedule |
|-----|----------|
| content-schedule-maintenance | 7:30, 11:30, 15:30, 19:30 |
| content-analytics-check | 8:13, 14:13, 20:13 |
| content-creative-daily | 7:12 Mon–Fri |

**Content blitz:** Disabled as of 2026-05-22 — hallucination risk at high pace. Do not re-enable without explicit approval.

## Cost Optimizer Protected Agents

Cost-optimizer MUST NEVER touch these regardless of usage:
```
nicu-care, wellness-coach, health-coach, content-*, 
entrepreneur-*, coding-agent, finance-manager
```

## Adding a New Job — Checklist

1. Identify backbone slot (or gap ≥ 3 min from nearest job)
2. Choose model tier (Haiku for routine checks, Sonnet for planning/reporting)
3. Confirm job is NOT duplicating an existing job
4. Verify it does NOT run inside quiet hours (10 PM – 6 AM) unless exempt
5. Add to `~/.hermes/cron.json` with unique ID
6. Test with single dry-run before enabling recurring

## Common Pitfalls
- ❌ Scheduling two jobs at the same minute → queue collision
- ❌ Using Sonnet for lightweight checkins → unnecessary cost
- ❌ Disabling family-care jobs during cost optimization pass
- ❌ Running content jobs during quiet hours
- ❌ Overlapping content-blitz with content-analytics (separate concerns)
- ❌ Forgetting 3-min minimum gap in busy slots like 8 AM

## Verification Checklist
- [ ] New job assigned to backbone slot or gap ≥ 3 min
- [ ] Model tier appropriate (Haiku routine / Sonnet planning)
- [ ] Family care jobs intact and protected
- [ ] No quiet-hours violations (10 PM – 6 AM)
- [ ] cost-optimizer protected-agents list updated if new critical agent added
