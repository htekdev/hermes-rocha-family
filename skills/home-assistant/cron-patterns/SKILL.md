---
name: cron-patterns
description: Use when designing, reviewing, or scheduling cron jobs for Hermes. Defines scheduling principles, energy matching, slot hygiene, and the recommended Hermes cron schedule.
version: 2.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, cron, scheduling, automation]
    related_skills: [hermes-cron-schedule, checkin-orchestrator, platform-manager]
---

# Cron Patterns Skill

## Overview
Scheduling principles and hygiene for all Hermes cron jobs. Adapted from htekdev/copilot-home-assistant cron.json architecture.

## When to Use
- Adding a new cron job
- Reviewing schedule conflicts
- Evaluating job model tier (haiku vs sonnet)
- Post-discharge timing adjustments

## Key Principles
- No two jobs share the same minute+hour
- Minimum 3-minute gap between jobs in the same hour
- Lightweight/haiku model for frequent polling
- Sonnet/full model for complex daily tasks
- Early-exit pattern: jobs check if there's anything to do before running
- **POST-DISCHARGE**: No Paula messages before 9 AM; quiet hours extended to 7 AM

## Schedule Slot Architecture
| Slot | Minutes | Job Type |
|------|---------|----------|
| Backbone | `:00–:03` | Heartbeat, mesh, briefings |
| Family care | `:06–:10` | NICU, wellness, parenting |
| Daily tasks | `:15–:30` | Finance, context audit |
| Content | `:30–:42` | Content pipeline (OG domain) |
| Platform | `:45–:53` | Reflection, health scan |

## Recommended Hermes Jobs

### Daily Briefing
- `morning-briefing` | `0 7 * * 1-5` | Weekday briefing (Hector only before 9 AM)
- `weekend-briefing` | `0 8 * * 0,6` | Weekend briefing

### Family Pulse
- `wellness-coach-morning` | `3 9 * * *` | Paula check-in (9 AM, not 8)
- `nicu-care-checkin` | `6 9,11,13,15,17,19 * * *` | Mia NICU monitoring
- `parenting-coach-morning` | `6 9 * * *` | HJ sibling adjustment

### Weekly/Monthly
- `weekly-planner` | `10 19 * * 0` | Sunday evening 7-section brief
- `budget-review` | `0 10 1 * *` | 1st-of-month deep dive

### Maintenance
- `nightly-reflection` | `0 21 * * *` | 5-phase reflection cycle
- `context-audit` | `5 6 * * *` | Daily quick scan (silent if clean)

## Energy Matching
| Time | Cognitive Load | Job Type |
|------|---------------|---------|
| 6–7 AM | High | Context audit (silent) |
| 7–9 AM | Medium-High | Hector briefings only |
| 9 AM–5 PM | Medium | Nudges, wellness, NICU |
| 5–9 PM | Low | Dinner, evening wellness |
| 9–10 PM | Low | Reflection, memory updates |
| 10 PM–7 AM | Silent | No non-urgent messages |

## Schedule Hygiene Rules
1. No two jobs share the same minute+hour
2. Always send mesh heartbeat at job start
3. ≤3 jobs within any 15-minute window
4. Disable jobs when their purpose is met (no zombie crons)
5. `[SILENT]` return if nothing to action (saves tokens)

## Common Pitfalls
- Scheduling two jobs at the same minute
- Running heavy sonnet jobs at high frequency
- Not respecting quiet hours for Paula-related jobs
- Forgetting heartbeat-first invariant

## Verification Checklist
- [ ] No minute conflicts with existing jobs?
- [ ] Correct model tier for job complexity?
- [ ] Paula-related jobs start at 9 AM or later?
- [ ] Heartbeat-first in every run?

*Last updated: 2026-06-03 | Migrated to SKILL.md format (Session 18)*
