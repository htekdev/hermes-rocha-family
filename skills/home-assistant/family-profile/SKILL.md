---
name: family-profile
description: Use when loading family context before any domain action. Master single-source-of-truth for Rocha family members, location, standards, and rules.
version: 2.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, family, profile, context]
    related_skills: [constitution, standing-orders, health-coach, wellness-coach]
---

# Rocha Family Profile

## Overview
Master family context — load before any domain-specific action. Single source of truth for all family facts.

## When to Use
- Start of any cron job
- Before sending any Telegram message
- Before making any decision about a family member

## Family Members

### Hector Rocha
- **Role:** Father, primary contact
- **Telegram Chat ID:** 7729308746
- **Traits:** ADD — one task at a time, celebrate wins, no streak interruptions
- **Communication:** Direct, result-first; 2–5 lines preferred; TTS enabled
- **Finance authority:** All Tier 3+ decisions route to Hector first

### Paula Rocha
- **Role:** Mother
- **Status:** Postpartum recovery; pumping ~220mL/day (Day ~49 as of June 3)
- **Communication:** 2–3 lines max, NO TTS, drip-feed only (hours apart), no rapid-fire
- **Message window:** 9 AM–9 PM CT only
- **Note:** Leo home June 3, 2026. Isolation risk window active. Dual-track stress (Leo home + Mia NICU).

### HJ (Hector Jr.)
- **Role:** Older sibling
- **Status:** Sibling adjustment period ACTIVE — Leo home June 3
- **Protocol:** Hector greets HJ first on Leo's homecoming day; 15 min/day 1-on-1 priority
- **Approach:** Acting out = processing, not misbehavior; connect → redirect

### The Twins — Leo & Mia
- **Born:** April 16, 2026 (~10 weeks premature)
- **Adjusted age standard:** ALWAYS use adjusted age for milestones (subtract ~10 weeks)
- **Leo:** HOME as of June 3, 2026 ✅
- **Mia:** NICU as of June 3, 2026 — confirm status; NEVER speculate on discharge date
- **Preemie home rules:** Nursery 68–72°F; RSV caution; no crowds 4+ weeks

## Location
- **City:** Houston, TX
- **Climate:** Gulf Coast — hot/humid summers, mild winters, freeze risk Dec–Feb
- **Drive time rule:** Always add +15 min buffer to estimated drive times

## Communication Standards
- Telegram is primary channel for Hector
- Quiet hours: 10 PM–7 AM CT (no non-urgent messages) — extended for overnight feeds
- Morning window: 7 AM for Hector; 9 AM for Paula
- Result-first, no process narration
- Never ask "would you like me to..." — do it, then report

## Safety Absolutes
- Child location: NEVER state as current fact — caveat with time-of-knowledge
- Medical advice: always defer to licensed professionals
- Financial decisions >$200: ask first
- Contractor scheduling: confirm someone will be home

## Home Facts
- HVAC filter size: 20x25x1 MERV 13 (Amazon recurring)
- Seasonal risk: Summer AC load, winter freeze pipes

## Financial Defaults
- Currency: USD
- Expense approval threshold: $200
- Budget categories: groceries, household, medical, subscriptions, baby/nursery

## Measurement Standards
- Kitchen: grams only (kitchen scale in use)
- Never suggest recipes without being asked (Saturday exception only)
- Drive times: always include +15 min buffer

## Agent Domain Map
| Domain | Primary Agent |
|--------|--------------|
| Daily briefing | Hermes |
| Wellness/postpartum | Hermes |
| Home maintenance | Hermes |
| Dog care | Hermes |
| NICU trends/pediatric follow-up | Hermes |
| Calendar/tasks/finance/content | OG (rocha-family) |
| Meal logistics | OG + Hermes coordination |
| Coding/extensions | Pi |

## Common Pitfalls
- Stating Leo/Mia locations without time caveat
- Using chronological age for Leo/Mia milestones
- Sending Paula messages before 9 AM
- Using cups/tablespoons instead of grams

## Verification Checklist
- [ ] Correct family member communication rules applied?
- [ ] Adjusted age used for Leo/Mia?
- [ ] Child location caveated?
- [ ] Quiet hours respected?

*Last updated: 2026-06-03 | Migrated to SKILL.md format + Leo home status updated (Session 18)*
