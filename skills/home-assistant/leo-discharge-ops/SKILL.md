---
name: leo-discharge-ops
description: Use when managing Leo's post-discharge homecoming transition and ongoing preemie care protocols at home. Status ACTIVE — Leo home June 3, 2026.
version: 1.1.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, nicu, twins, leo, discharge, preemie]
    related_skills: [nicu-care, family-profile, wellness-coach, parenting-coach, dog-parent]
---

# Leo Discharge Operations

## Overview
Leo Rocha came home June 3, 2026 — approximately 7 weeks after birth (April 16, preterm). This skill governs post-discharge home protocols for a preemie: temperature management, RSV exposure rules, feeding cadence, adjusted age milestone tracking, and family transition support.

## When to Use
- Any question about Leo's care at home
- Scheduling pediatric follow-ups
- Assessing environment safety (visitors, temperature, exposure)
- Milestone check-ins or weight-gain monitoring
- Escalating concerns to medical team

## Status: ACTIVE — Leo Home June 3, 2026 ✅

## Current Profile (as of June 3, 2026)
- **Leo** — born April 16, 2026 (preterm, ~10 weeks early)
- **Chronological age**: ~7 weeks
- **Adjusted age**: ~-3 weeks (corrected for prematurity)
- **Discharge weight**: TBD (confirm at discharge appointment)
- **Feeding**: breast milk (Paula pumping, baseline ~220 mL/day pump log Day 48)
- **Primary concern**: RSV season caution, preemie immune system

## Home Environment Requirements

### Temperature
- **Nursery**: 68–72°F (preemie requirement — tighter than standard 68–76°F)
- Monitor continuously; flag to Hector if outside range
- AC must maintain in Houston summer

### RSV / Infection Control
- **No visitors with cold/flu symptoms** — enforce strictly
- **Handwashing before handling**: family + all visitors
- **Minimize crowded public spaces** for 8+ weeks post-discharge
- RSV season: October–March (plan ahead for fall 2026)
- Palivizumab (RSV shot): confirm with pediatrician at first follow-up

### Feeding Cadence
- Preemies typically feed every 2–3 hours
- Wake to feed if sleeping > 3 hours (until cleared by pediatrician)
- Track: volume per feed, frequency, any refusal
- Paula's pump output is the primary supply — flag decline to wellness-coach

## Pediatric Follow-Up Schedule
| Appointment | Timing | Notes |
|-------------|--------|-------|
| First pediatric visit | Within 48–72h of discharge | Weight check mandatory |
| 1-month corrected age | ~April 2027 adjusted | Developmental screen |
| Cardiology/pulmonology | As directed by NICU team | Any discharge conditions |
| RSV prophylaxis | Before October 2026 | Coordinate with pediatrician |

**Hermes role**: Proactive reminders for all follow-ups. Create tasks when dates confirmed. Do NOT diagnose — route all medical questions to healthcare team.

## Adjusted Age Standard (MANDATORY)
- All milestone reporting uses **adjusted age** (chronological age − 10 weeks)
- Leo at 7 weeks chronological = ~-3 weeks adjusted (not yet at term equivalent)
- Never compare to full-term newborn milestones at this stage
- At term equivalent (~June 25, 2026): newborn milestone baseline begins

## Mia Status (twin, still in NICU)
- Mia remains in NICU as of June 3, 2026
- Discharge date: TBD — confirmed only when NICU team announces
- Hermes tracks Mia NICU status via nicu-care/SKILL.md
- **NEVER speculate on Mia's discharge date**

## Family Transition Context
- **Paula**: Postpartum + split-care stress (Leo home, Mia NICU) — dual-track monitoring active
- **Hector**: Managing two households (hospital + home) + work
- **HJ**: 4-year-old sibling adjustment — Leo intro protocol per parenting-coach/SKILL.md
- **Bella** (dog): Phase 1 baby introduction ACTIVE — scent-first protocol per dog-parent/SKILL.md

## Escalation Triggers
Escalate to Hector immediately (with `speak` param):
- Leo not feeding for > 4 hours
- Nursery temp outside 68–72°F and not correctable
- Any respiratory distress (grunting, flaring, labored breathing)
- Fever > 100.4°F in a preemie — treat as URGENT
- Paula's pump output drops > 20% for 3 consecutive days

## Common Pitfalls
- **Using chronological age for milestones**: Always use adjusted age
- **Speculating on Mia's discharge**: TBD until confirmed
- **Relaxing RSV protocols early**: 8 weeks minimum; pediatrician clears
- **Skipping first pediatric visit**: Must happen within 72h of discharge
- **Over-alerting Paula**: Route Leo concerns to Hector first; brief Paula gently

## Verification Checklist
- [ ] Nursery temp confirmed 68–72°F
- [ ] Feeding on schedule (≤ 3h intervals until cleared)
- [ ] First pediatric follow-up scheduled (within 72h of June 3)
- [ ] RSV exposure protocols communicated to family
- [ ] Adjusted age used for all milestone language
- [ ] Mia status noted as TBD (no speculation)
- [ ] Bella Phase 1 active — no unsupervised Leo-Bella contact
