---
name: dual-calendar
description: Use when checking Hector's availability or scheduling any event. Enforces dual-calendar (Google Cal + WorkIQ) availability check — never rely on a single calendar.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, scheduling, calendar]
    related_skills: [family-coordinator, daily-briefing, hermes-governance]
---

# Dual-Calendar Protocol

## Overview
Hector maintains TWO calendars: **Google Calendar** (personal) and **WorkIQ** (work). True availability requires checking BOTH. A slot free on one calendar may be blocked on the other. This rule is non-negotiable and applies to every scheduling action — morning briefings, event creation, task due dates, appointment reminders.

## When to Use
- Any time you need to determine if Hector is available at a given time
- Before creating, suggesting, or confirming any calendar event
- When computing drive times or leave-by windows
- During daily briefing preparation (must show conflicts across both)
- When scheduling gym slot or any standing routine

## Dual-Calendar Rule

### The Invariant
> **True availability = free on Google Cal AND free on WorkIQ**
> If either calendar is blocked → slot is unavailable. No exceptions.

### Why It Matters
- Hector's WorkIQ calendar includes meetings, client calls, deadlines
- Google Cal has personal appointments, NICU visits, childcare pickups
- Showing only one creates false "free" windows → missed commitments

### Check Sequence
1. Query Google Calendar for target time window
2. Query WorkIQ calendar for same window
3. Compute intersection of free slots
4. Use intersection ONLY for scheduling

### Personal → Work Calendar Flow
When adding personal events that need work blocking:
1. Create Google Cal event
2. Call `get_agents()` → `send_message(workspace="msix-home")` to create matching Outlook block
3. Use `showAs=oof` (out-of-office) — NOT busy — for personal blocks on work calendar

## Daily Briefing Integration
- Every morning briefing MUST include conflicts from BOTH calendars
- Flag any day where personal + work calendars have overlapping demands
- Gym slot scheduling requires dual-calendar check first (prefer 11 AM–2 PM, default 12–1 PM)

## Event Scheduling Rules

### Date Verification (CRITICAL)
- NEVER guess day-of-week — always compute numerically
- Before creating event: verify `(Get-Date 'YYYY-MM-DD').DayOfWeek`
- If weekday label ≠ numeric date → BLOCK scheduling, fix first

### Leave-By Time Pattern
- Always add +15 min buffer to drive times
- Leave-by = appointment time − drive time − 15 min buffer
- Include traffic risk for Houston (I-10, I-610 during rush hour = +20–30 min)

### NICU Visit Scheduling
- Hector's NICU visits require both calendars clear (morning 8–11 AM block typical)
- Never schedule other commitments inside confirmed NICU visit windows
- After NICU visit: assume 30 min buffer for transition

## Post-Discharge Adaptations (Active: June 3, 2026+)
- Leo home → overnight feeds → Hector may be low-energy mornings
- Avoid scheduling high-complexity tasks before 9 AM when overnight feeds expected
- Paula's medical appointments (postpartum, pumping schedule) are on Google Cal — include in conflict check
- Mia still NICU — daily NICU visits remain in schedule until discharge

## Gym Slot Standing Order
Execute during daily briefing:
1. Run dual-calendar check for 11 AM–2 PM
2. Preferred slot: 12–1 PM → fallback 11–12 → fallback 1–2 → outside window (flag to Hector)
3. Create Google Cal event
4. Block Outlook as OOF via msix-home agent
5. If no slot found → flag in briefing, do NOT silently skip

## Common Pitfalls
- ❌ Checking only Google Cal and declaring "available"
- ❌ Creating WorkIQ block as "busy" instead of "oof" for personal time
- ❌ Assuming day-of-week from date without computing it
- ❌ Scheduling NICU visit windows without checking work calendar
- ❌ Forgetting +15 min traffic buffer for any Houston drive
- ❌ Setting gym slot without dual-calendar check first

## Verification Checklist
- [ ] Both calendars queried before any scheduling action
- [ ] Availability computed from intersection only
- [ ] Date/day-of-week verified numerically
- [ ] +15 min buffer added to all drive times
- [ ] NICU windows protected (not double-booked)
- [ ] Work blocks created as `showAs=oof` for personal time
- [ ] Gym slot found and confirmed on both calendars
