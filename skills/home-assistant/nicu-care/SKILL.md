---
name: nicu-care
description: Use when tracking NICU status, pumping schedules, discharge readiness, or preemie-care milestones for Leo and Mia. Governs daily NICU check-in patterns, pump-log management, and family communication during split-home period.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, nicu, twins, preemie, pumping, health]
    related_skills: [family-profile, wellness-coach, health-coach, parenting-coach, family-coordinator]
---

# NICU Care

## Overview
Leo and Mia Rocha were born April 16, 2026 — premature (~10 weeks early). Leo was discharged around June 3, 2026 (Day ~48). Mia remains in NICU. This skill governs Hermes's role in supporting the family during the split-home period: one twin home, one twin in NICU.

## When to Use
- Pumping schedule reminders and log tracking
- Discharge readiness checklist for Mia
- Proactive wellness monitoring tied to NICU progress
- Pediatric follow-up coordination post-discharge
- Baby-care quality-of-life flags (feeding, weight gain, breathing events)

## NICU Status (as of 2026-06-03)

| Twin | Status | Location |
|------|--------|----------|
| **Leo** | HOME ✅ | Rocha home — discharged ~June 3 |
| **Mia** | NICU 🏥 | Still inpatient — discharge TBD |

## Domain Split (Hermes vs OG)
| Domain | Owner |
|--------|-------|
| Daily NICU log / pump log | OG agent |
| Proactive wellness monitoring | **Hermes** |
| Pediatric follow-up scheduling | **Hermes** |
| Pumping reminders (15 min before session) | OG cron |
| Paula postpartum nutrition | **Hermes** (via nutrition-chef) |
| Baby-dog safety coordination | **Hermes** (via dog-parent) |

## Preemie Rules (ALWAYS Apply)
- **Adjusted age**: Leo and Mia are ~10 weeks premature. ALWAYS use adjusted age (chronological age minus ~10 weeks) when assessing milestones.
- **No milestone alarmism**: Never flag as concern unless adjusted age standard is missed.
- **RSV caution**: Preemie immune systems are vulnerable. Flag any crowded event, sick visitor, or cold season risk.
- **Temperature**: Nursery 68–72°F. Non-negotiable for preemie thermoregulation.
- **Weight gain**: Expect 0.5–1 oz/day as normal pace post-discharge.

## Pumping Schedule Context
- Paula Day ~48 post-birth at Leo discharge
- Baseline: ~220 mL/day
- Sessions typically every 3–4 hours
- Pump output = leading wellness indicator (see wellness-coach skill)
- Decline 3+ consecutive days → flag proactively before Paula self-reports

## Mia Discharge Readiness Checklist
Track these before flagging Mia's discharge as imminent:
- [ ] Off supplemental oxygen
- [ ] Maintaining body temperature independently
- [ ] All feeds by breast or bottle (no NG tube)
- [ ] Consistent weight gain 3+ consecutive days
- [ ] Car seat tolerance test passed
- [ ] Family CPR/infant care training completed
- [ ] Pediatrician follow-up appointment scheduled
- [ ] Nursery second space ready (Mia's section)

## Leo Post-Discharge Care (Week 1–4)
- First pediatrician visit: within 48–72 hours of discharge
- Weight check at every visit (preemies monitored closely)
- No sick visitors for 4+ weeks minimum
- Adjusted age: use for all milestone tracking
- Vitamin D supplement: confirm with pediatrician

## Communication Rules
- **Paula**: 2–3 lines max. No rapid questions. No TTS. Drip-feed hours apart.
- **Hector**: Result-first. Include TTS via speak param. Max 5 lines.
- NICU status updates: send Hector only unless Paula explicitly asks.
- Never speculate on Mia's discharge date — only relay what NICU team confirmed.

## Cron Reference (Source Pattern)
```
nicu-care-checkin: 6 7,9,11,13,15,17,19,21 * * *
  → Pumping reminders 15min before session
  → Logs to pumping-log.json (OG domain)
```
Hermes does NOT duplicate this. Hermes monitors trends, not individual sessions.

## Common Pitfalls
- ❌ Stating Mia's discharge date as known — it isn't; say "TBD per NICU team"
- ❌ Using chronological age for milestones — always use adjusted age
- ❌ Alarming Paula about NICU data without context — calibrate against adjusted norms
- ❌ Duplicating OG's pump log tracking — Hermes monitors output trends, not individual logs
- ❌ Forgetting RSV risk window — preemies discharged in spring/summer still need protection

## Verification Checklist
- [ ] Adjusted age used for all milestone references
- [ ] Mia's discharge status not stated as known unless confirmed
- [ ] Pump output tracked as trend indicator, not session-by-session log
- [ ] Nursery temperature in range (68–72°F) before flagging as ready
- [ ] Pediatric follow-ups in family-coordinator/working.md
