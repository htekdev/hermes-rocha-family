---
name: daily-briefing
description: Use when generating a morning daily briefing for Hector. Formats and delivers a concise daily summary covering weather, calendar, deadlines, bills, and action items.
version: 2.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, briefing, daily]
    related_skills: [family-profile, morning-briefing, weekly-planner, constitution]
---

# Daily Briefing Skill

## Overview
Deliver a concise morning briefing to Hector covering what matters for the day. Skip empty sections — only surface what's relevant.

## When to Use
- Morning cron (weekdays 7 AM, weekends 8 AM CT)
- On-demand: "Give me today's briefing" / "What's on today?"

## Briefing Structure
Deliver in this order — skip sections if nothing relevant:

1. **Weather** — Current conditions + today's high/low
2. **Today's calendar** — Events in chronological order with leave-by times (+15 min traffic buffer)
3. **Upcoming deadlines** — Anything due in the next 48 hours
4. **Bills/Finance** — Any bills due this week
5. **Action items** — Top 1–3 things Hector should do today (specific, not vague)
6. **Family/Twins** — NICU status (Mia), Leo home updates, Paula wellness flag if needed

## Format Rules
- Total message: **10 lines max** for Telegram
- Each section: 1–2 lines
- Omit empty sections entirely
- Result-first: no "Good morning! I've checked your calendar and..."
- Acceptable opener: "📋 Today, [Date]:" then items
- POST-DISCHARGE: Keep light — household is in overnight-feed recovery mode

## Example Output
```
📋 Today, Tue Jun 3:
• 10 AM dentist — leave by 9:40 (traffic)
• 3 PM call with contractor
Bills: Internet bill due Fri ($89)
Action: Confirm dentist insurance before 9 AM
Mia: NICU (confirm status at morning visit)
```

## Implementation Notes
- Always compute current date — never assume
- For appointments: leave-by = appointment time − (drive time + 15 min)
- If calendar unavailable, say "calendar unavailable" rather than guessing
- Dual-calendar check is MANDATORY: personal + family calendar

## Common Pitfalls
- Checking only one calendar
- Including empty sections
- Starting with "Good morning, I've checked..."
- Missing leave-by times for appointments

## Verification Checklist
- [ ] Both calendars checked?
- [ ] Leave-by times computed with +15 min buffer?
- [ ] Empty sections omitted?
- [ ] Total message ≤10 lines?
- [ ] Date computed, not assumed?

*Last updated: 2026-06-03 | Migrated to SKILL.md format (Session 18)*
