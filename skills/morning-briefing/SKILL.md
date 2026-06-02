---
name: morning-briefing
description: Use when running the Rocha family morning briefing — compile weather, calendar, tasks, NICU/baby updates, meals, and bills into a warm Telegram summary.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, daily-briefing, morning, telegram]
    related_skills: [constitution, family-profile, telegram-bridge, nicu-care, hermes-cron-schedule]
---

# Morning Briefing

## Overview
The morning briefing starts the Rocha family's day with a concise, actionable summary. It runs weekdays at 6 AM CT and weekends at 8 AM CT. Hector receives TTS-enabled messages; Paula receives 2–3 line max with ONE question.

## When to Use
Run automatically on cron or when Hector/Paula asks for a morning update.

## Briefing Sections (in order)

### 1. Time & Date Anchor
Always compute current time first (CT). Use this to filter past events.

### 2. Weather
- Current conditions + day forecast
- Flag anything that affects plans (rain for Bella walk, extreme temps)

### 3. Calendar (DUAL — personal + work)
- List events for today only
- Work calendar is MANDATORY — never skip
- Flag conflicts between parents

### 4. Baby / NICU Update (ACTIVE — Mia post-discharge, Leo home)
- **Leo**: Home since ~June 3. Feeding schedule, overnight status, any appointments
- **Mia**: NICU status, next visit time, any milestones or concerns from prior evening
- Pump schedule reminder for Paula if AM pump window is coming up
- Send to BOTH parents

### 5. Tasks for Today
- Source: Paula's daily input (primary), Hector additions (secondary)
- Suppress physical chores during meeting-heavy blocks
- Max 3–5 highlighted tasks; don't overwhelm

### 6. Meals
- Today's meal plan if set
- Quick prep reminder if anything needs thawing/prep

### 7. Bills / Finance Flags
- Any bills due today or tomorrow
- Urgent budget alerts only (not routine summaries)

### 8. Proactive Actions
- Create any obvious tasks discovered during compilation (via add_task first, then notify)
- Flag gym slot suggestion for Hector if 11 AM–2 PM window is clear

## Delivery Format

**Hector (speak=true):**
```
Good morning, Rocha family! ☀️ [Day, Date]

📍 Weather: [X]°F, [condition]
📅 Today: [2–3 calendar items]
👶 Leo: [1-line status] | Mia: [1-line status]
✅ Top tasks: [2–3 items]
🍽️ Dinner: [plan or "not set"]
💰 [Only if urgent bill/flag]
```

**Paula (speak=false, 2–3 lines max):**
```
Morning! 🌅 Leo: [status]. Mia: [status]. [One practical heads-up]. [ONE question if needed.]
```

## Post-Discharge Adaptations (active as of June 2026)
- Leo is HOME — overnight feed recovery affects morning energy; keep Paula messages light
- Bella dog-baby protocol still in Phase 1 (supervised intro); note any Bella/baby incidents
- Hector may have reduced gym windows — brief him on calendar blocks
- NICU visits for Mia: confirm timing daily

## Common Pitfalls
- ❌ Sending briefing during quiet hours (10 PM–6 AM CT)
- ❌ Using `speak=true` for Paula
- ❌ Skipping work calendar (dual calendar is MANDATORY)
- ❌ Overwhelming Paula with more than one question
- ❌ Omitting baby/NICU section when either parent is on active baby duty

## Verification Checklist
- [ ] Current CT time computed before filtering
- [ ] Personal AND work calendar queried
- [ ] Baby/NICU section present
- [ ] Paula message ≤3 lines with ≤1 question
- [ ] Hector message includes speak=true
- [ ] Any actionable items → add_task called first
