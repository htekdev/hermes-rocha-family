---
name: hermes-cron-schedule
description: Use when viewing or updating the Hermes-specific cron schedule. Defines the complete post-discharge cron schedule with energy matching and Paula/Hector timing rules.
version: 2.1.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, cron, schedule, automation]
    related_skills: [cron-patterns, checkin-orchestrator, family-profile]
---

# Hermes Cron Schedule — Rocha Family

## Overview
Complete Hermes cron job schedule. **POST-DISCHARGE MODE ACTIVE** (Leo home June 3, 2026).

## When to Use
- Adding or modifying a cron job
- Checking for schedule conflicts
- Reviewing post-discharge timing rules

## Schedule Philosophy
- Energy matching: Complex AM, nudges active hours, reflection PM
- Minimum 3-min gap between jobs in same hour
- POST-DISCHARGE: Overnight feeds expected — quiet until 7 AM; Paula msgs 9 AM+

## Cron Jobs

### Daily Briefing
| Job | Schedule | Notes |
|-----|----------|-------|
| morning-briefing | `0 7 * * 1-5` | Weekday — Hector only |
| weekend-briefing | `0 8 * * 0,6` | Weekend — lighter format |

### Family Pulse
| Job | Schedule | Notes |
|-----|----------|-------|
| wellness-coach-morning | `3 9 * * *` | Paula BP/sleep/pump check |
| wellness-coach-midday | `10 13 * * *` | Pump trend check |
| wellness-coach-evening | `0 18 * * *` | Daily summary |
| nicu-care-checkin | `6 9,11,13,15,17,19 * * *` | Mia NICU + pumping reminders |
| parenting-coach-morning | `6 9 * * *` | HJ sibling adjustment |
| dinner-reminder | `0 15 * * *` | 3 PM dinner + grocery check |
| luna-checkin | `10 10,14,18 * * *` | Paula emotional check-ins |

### Weekly / Monthly
| Job | Schedule | Notes |
|-----|----------|-------|
| weekly-planner | `10 19 * * 0` | Sunday 7-section brief |
| budget-review | `0 10 1 * *` | 1st-of-month deep dive |

### Maintenance
| Job | Schedule | Notes |
|-----|----------|-------|
| nightly-reflection | `0 21 * * *` | 5-phase detect→fix→report |
| context-audit | `5 6 * * *` | Daily quiet scan |
| context-audit-weekly | `0 20 * * 0` | Sunday full audit |

### Mesh (every run)
- Send heartbeat FIRST — before any other action
- Poll messages → respond → primary task → broadcast

## Energy Matching (Post-Discharge)
| Time | Load | Jobs | Notes |
|------|------|------|-------|
| 6–7 AM | High | Context audit (silent) | Hector-only OK |
| 7–9 AM | Med-High | Hector briefing | No Paula msgs |
| 9 AM–12 PM | Medium | Paula wellness, NICU | Paula msgs start |
| 12–5 PM | Medium | Midday checks, grocery | ≤3 lines Paula |
| 5–9 PM | Low | Dinner, evening wellness | Drip-feed |
| 9–10 PM | Low | Nightly reflection | Wind-down tone |
| 10 PM–7 AM | Silent | None | Overnight feeds |

## Post-Discharge Rules
1. No Paula messages before 9 AM
2. No non-critical messages after 9 PM
3. Overnight 10 PM–7 AM = silent (overnight feeds active)
4. Hector briefings remain at 7 AM (he manages his own schedule)

## Scheduling Hygiene
1. No two jobs at same minute+hour
2. Heartbeat sent every run
3. Respond to mesh messages before primary task
4. Broadcast progress summary after each run

## Common Pitfalls
- Scheduling Paula-related jobs before 9 AM
- Skipping heartbeat
- Two jobs at same time slot
- Not broadcasting at end of run

## Verification Checklist
- [ ] No minute conflicts?
- [ ] Paula jobs start 9 AM+?
- [ ] Heartbeat included in every run?
- [ ] End-of-run broadcast included?

*Last updated: 2026-06-03 | Migrated to SKILL.md format (Session 18)*
