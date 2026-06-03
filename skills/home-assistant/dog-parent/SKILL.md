---
name: dog-parent
description: Use when managing pet care, vet reminders, feeding schedules, or baby-dog introduction protocol. Manages the Rocha family dog(s) with Phase 1 baby-introduction active.
version: 2.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, pets, dogs, baby-safety]
    related_skills: [family-profile, health-coach, home-manager, family-coordinator]
---

# Dog Parent Skill

## Overview
Pet care management for Rocha family dogs. Warm, proactive, playful. 🐕🐾

## When to Use
- Feeding/medication schedule times
- Vet appointment approaching
- Supply running low
- Baby-dog introduction protocol steps
- Behavioral change detected

## Domain Coverage
| Area | Responsibilities |
|------|----------------|
| **Feeding** | Schedules, portions, supply monitoring |
| **Vet Care** | Appointments, vaccinations, annual checkups |
| **Medications** | Tracking, refills 2 weeks out, monthly heartworm/flea/tick |
| **Grooming** | Schedule, groomer contacts, seasonal needs |
| **Behavior** | Triggers, training progress, vet-flag changes |
| **Baby Intro** | Leo home June 3 — Phase 1 ACTIVE |

## Decision Framework
- **Act immediately:** Feeding/med reminders, shopping list additions, health logging
- **Ask first:** Vet scheduling, food changes, grooming, expenses >$100
- **Escalate:** Sudden health changes, behavioral issues near HJ, major medical decisions

## Task-First Rule
Every discovery → task:
- Low food → "Buy [brand] dog food" — priority: high, category: shopping
- Vet due → "Schedule vet appointment for [dog]" — priority: medium, category: health
- Flea/tick due → "Apply flea/tick treatment" — priority: high, due: [date]

## Annual Care Calendar
- **Monthly:** Heartworm, flea/tick, nail check
- **Quarterly:** Dental chews, toy rotation, collar/leash check
- **Biannually:** Professional grooming, vet checkup
- **Annually:** Vaccinations, wellness exam, license renewal

## Baby-Dog Introduction Protocol (CRITICAL)
**Leo home June 3 — Phase 1 ACTIVE**

### Phase Sequence
1. **Phase 1 — Scent Introduction** (ACTIVE): Baby blanket/item in dog space; dog rewards for calm sniffing; establish baby zone boundaries
2. **Phase 2 — Sound Introduction**: Play baby sounds (recordings); reward calm behavior
3. **Phase 3 — Visual Introduction**: Dog sees baby from distance; calm reward
4. **Phase 4 — Supervised Meeting**: On leash, short duration, both calm
5. **Phase 5 — Monitored Coexistence**: Never fully unsupervised

### Hard Rules
- NEVER leave infant unattended with any dog (Phase 5 or any phase)
- Advance phases only when checklist items complete
- Behavioral regression → pause phases, consult vet
- Define and enforce: nursery = dog-free zone; dog retreat = baby-free zone

## Communication
- Telegram: 2–5 lines max, warm + playful 🐕🐾
- Feeding reminders at scheduled times
- Vet reminders: 1 week out + day-of
- Urgent health → immediate alert (bypass quiet hours)

## Common Pitfalls
- Advancing baby-intro phases without completing checklist
- Missing monthly heartworm/flea-tick window
- Not flagging behavioral changes during twins transition

## Verification Checklist
- [ ] Baby-dog zones enforced (nursery = dog-free)?
- [ ] Phase advance checklist complete before moving forward?
- [ ] Vet escalated for behavioral changes?
- [ ] Monthly meds tracked?

*Last updated: 2026-06-03 | Migrated to SKILL.md format (Session 18)*
