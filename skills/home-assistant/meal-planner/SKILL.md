---
name: meal-planner
description: Use when managing weekly meals, generating grocery lists, or handling dinner reminders. Never suggests what to cook — Hector decides, Hermes manages logistics.
version: 2.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, meals, grocery, nutrition]
    related_skills: [family-profile, nutrition-chef, health-coach, finance-manager]
---

# Meal Planner Skill

## Overview
Meal logistics, grocery management, and food coordination for the Rocha family.

## When to Use
- Saturday morning meal planning workflow
- Grocery list generation
- Dinner reminder (3 PM daily)
- When Hector shares what he's cooking

## Core Rule: NO Recipe Suggestions
**NEVER suggest what to cook.** Hector decides meals — Hermes manages logistics.

**Exception:** Saturday morning → send 3 easy meal ideas (name + one-line reason, under 30 min, minimal dishes).

## Saturday Workflow
1. **Ask Hector**: "What are you cooking this week?" — wait for his input
2. **Check context**: Dietary needs, any special flags (Paula postpartum, HJ preferences)
3. **Set the plan**: Save based on Hector's choices; ask about gaps if partial days
4. **Generate grocery list**: Cross-reference, avoid duplicates
5. **Send to family**: Meal plan + grocery list + prep tips + flags

## Telegram Output Format
```
🍽️ This Week's Meals
Mon: [Hector's choice]
Tue: [Hector's choice]
...

🛒 Grocery List
Produce: ...
Protein: ...
Pantry: ...

👩‍🍳 Prep Tips: [make-ahead opportunities]
⚠️ Flags: [missing ingredients, timing conflicts]
```

## Measurement Standard
All food measurements in **grams only** — Hector uses a kitchen scale. Never use tablespoons, cups, or ounces.

## Dietary Context
| Track | Person | Notes |
|-------|--------|-------|
| 1 | Hector | High protein, macro-focused |
| 2 | Paula | Postpartum — low glycemic, breastfeeding support |
| 3 | HJ | Picky eater, finger food, no choking hazards |

## Store Assignments
- **H-E-B**: produce, staples, fresh
- **Costco**: bulk, proteins

## Communication
- 3 PM daily: dinner reminder + check if anything needed from store
- Saturday/Sunday: next week meal preview
- Telegram: 2–5 lines max, result-first

## Common Pitfalls
- Suggesting meals outside of Saturday exception
- Using cups/tablespoons instead of grams
- Starting dinner suggestion without ingredient confirmation

## Verification Checklist
- [ ] Did Hector choose the meal (not Hermes)?
- [ ] All measurements in grams?
- [ ] Grocery list deduplicated?
- [ ] Store assignments included?

*Last updated: 2026-06-03 | Migrated to SKILL.md format (Session 18)*
