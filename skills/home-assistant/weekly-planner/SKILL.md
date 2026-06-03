---
name: weekly-planner
description: Use when generating a Sunday evening weekly preview for the Rocha family. Delivers a 7-section structured weekly plan covering review, calendar, tasks, meals, finance, home, and family.
version: 2.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, weekly, planning, briefing]
    related_skills: [family-profile, daily-briefing, morning-briefing, finance-manager]
---

# Weekly Planner Skill

## Overview
Sunday evening weekly review and preview. Covers the full family picture in 7 structured sections.

## When to Use
- Sunday evening cron (7:10 PM CT)
- On-demand: "Give me a week preview"

## Weekly Summary Format

Send to Hector via Telegram. 7 Sections:

### 1. 🔙 Week in Review
- Tasks completed vs. carryover
- Notable wins

### 2. 📅 Upcoming Calendar
- All events this week, organized by day
- Label personal 🏠 vs. work 💼
- Include drive times (+15 min buffer)

### 3. 🎯 Priority Tasks
- Urgent items
- High-priority items
- Due-this-week items

### 4. 🍽️ Meal Plan
- Current week's plan status
- Any gaps to fill

### 5. 💰 Finance Snapshot
- Spending summary vs. budget
- Upcoming bills this week

### 6. 🏠 Home Maintenance
- Items due within 14 days

### 7. 👨‍👩‍👧 Family
- Health appointments
- Child school/activity notes
- NICU update (Mia status)
- HJ sibling adjustment notes
- Paula wellness flag if relevant
- Any coordination needed

## Closing
End with a brief encouraging note — warm but genuine, not generic.

## Output Quality
- Structured with bullets/sections for dense data
- Concise where possible — Hector can ask for detail on any section
- Result-first: lead with the most important thing
- No worklog narration

## Common Pitfalls
- Missing the Family section (Section 7 is critical during NICU period)
- Generic closing note ("Have a great week!")
- Checking only one calendar

## Verification Checklist
- [ ] All 7 sections present (or explicitly skipped if empty)?
- [ ] Drive times with +15 min buffer?
- [ ] Finance snapshot accurate?
- [ ] NICU/twins update in Family section?
- [ ] Closing note genuine and specific?

*Last updated: 2026-06-03 | Migrated to SKILL.md format (Session 18)*
