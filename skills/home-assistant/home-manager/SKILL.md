---
name: home-manager
description: Use when managing home maintenance, seasonal tasks, contractor coordination, or nursery readiness. Manages the Rocha home with a preventive-maintenance mindset in Houston/TX climate.
version: 2.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, home, maintenance, houston]
    related_skills: [family-profile, finance-manager, family-coordinator, health-coach]
---

# Home Manager Skill

## Overview
Preventive home maintenance, seasonal care, contractor coordination, and nursery readiness for the Rocha family in Houston, TX. Motto: "Fix it before it breaks."

## When to Use
- Maintenance item due or overdue
- Contractor needed
- Seasonal calendar reminder
- Nursery/baby-proofing updates
- Appliance flagging

## Domain Coverage
| Area | Responsibilities |
|------|----------------|
| Maintenance | HVAC filters, gutters, pest control, dryer vents, smoke detectors, water heater, roof |
| Contractors | Directory, ratings, quotes, who excels at what |
| Repairs | Full lifecycle: report → resolution; priority: Safety > Water/Structural > Comfort > Cosmetic |
| Appliances | Age, brand, model, warranty; proactively flag end-of-life |
| Nursery | Readiness for preemie twins; temp 68–72°F; RSV precautions |
| Yard | Lawn care, fencing, seasonal cleanup |

## Task-First Guardrail
When anything actionable is discovered → create a task BEFORE sending a reminder.

| Trigger | Task Example |
|---------|-------------|
| HVAC filter overdue | "Replace HVAC filter — overdue since [date]" — priority: high |
| Gutter cleaning due | "Schedule gutter cleaning" — priority: medium |
| Contractor needed | "Call [provider] for [issue]" — include phone in notes |

## Decision Framework
| Act Immediately | Ask First (>$200) | Escalate Urgent |
|----------------|-------------------|--------------------|
| Send reminders | Scheduling contractors | Gas smell / electrical |
| Log maintenance | Major contractor selection | Water damage |
| Update memory | Change maintenance schedules | Structural concerns |

## Seasonal Calendar (Houston/TX)
| Season | Key Tasks |
|--------|-----------| 
| Spring (Mar–May) | AC tune-up, lawn fertilize, termite inspection, sprinkler check |
| Summer (Jun–Aug) | Monitor AC, weatherstripping, pressure wash |
| Fall (Sep–Nov) | HVAC heat check, gutter clean, smoke detector batteries, pest control |
| Winter (Dec–Feb) | Freeze pipe protection, insulation check, plan spring projects |

## HVAC Filter
- Size: 20x25x1 MERV 13 (Amazon recurring order)
- Reminder: every 90 days

## Nursery Status (June 2026)
- Leo home June 3 — nursery active
- Mia NICU — nursery prep for eventual dual-twin occupancy
- Temp must stay 68–72°F for preemies
- No crowd visitors for 4+ weeks post-discharge

## Integrations
- `finance-manager` → home expenses, major purchases
- `health-coach` → baby-proofing, nursery safety
- `family-coordinator` → contractor scheduling (someone must be home)

## Common Pitfalls
- Acting on contractor scheduling without confirming someone will be home
- Forgetting seasonal task windows (Houston: AC critical in spring before summer heat)
- Not creating task before sending reminder

## Verification Checklist
- [ ] Task created before reminder sent?
- [ ] Cost >$200 flagged before acting?
- [ ] Someone-home confirmed for contractor visits?
- [ ] Nursery temp in 68–72°F range?

*Last updated: 2026-06-03 | Migrated to SKILL.md format (Session 18)*
