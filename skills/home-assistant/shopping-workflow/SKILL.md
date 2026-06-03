---
name: shopping-workflow
description: Use when generating grocery lists, assigning store runs, or coordinating post-shopping closeout. Manages H-E-B/Costco split and weekly meal-prep logistics.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, grocery, meal-planning, nutrition]
    related_skills: [nutrition-chef, family-coordinator, finance-manager, family-profile]
---

# Shopping Workflow

## Overview
Grocery and shopping coordination for the Rocha family. H-E-B handles produce/fresh; Costco handles bulk staples. Always check kitchen inventory before committing to a shopping trip.

## When to Use
- Generating a weekly grocery list after Saturday meal selection
- Assigning items to correct store
- Tracking post-trip closeout
- Flagging missing kitchen equipment before a meal plan is set

## Store Assignments

| Store | Category |
|-------|----------|
| **H-E-B** | Produce, fresh proteins, dairy, specialty items |
| **Costco** | Bulk staples, pantry items, household supplies |

## Weekly Workflow
1. **Saturday morning** — Nutrition Chef sends 3 meal proposals (names + one-line reason only)
2. **Hector selects** → `set_meal` populates plan
3. **Check kitchen inventory** → `data/family/kitchen-inventory.md` (flag missing equipment before confirming)
4. **Generate grocery list** organized by store (H-E-B section / Costco section)
5. **Add to shopping list** with quantities in **grams only** (kitchen scale standard)
6. **Create prep tasks** — thawing, marinating, any overnight prep needed

## Measurement Standard
- ALL quantities in **grams only** — no cups, tablespoons, ounces, or volume measures
- Family uses a kitchen scale; this is non-negotiable

## Dietary Tracks (for list generation)

| Track | Person | Notes |
|-------|--------|-------|
| 1 — High protein | Hector | Macro-focused, fitness/TRT |
| 2 — GD-safe/postpartum | Paula | Low glycemic, no high-sugar produce |
| 3 — Kid-friendly | HJ (~3-4 yr) | Finger food, hidden veggies, no choking hazards |

**Overlap strategy:** Shared dinner base + per-person modifications (e.g., grilled chicken + rice — Hector gets extra protein portion, Paula gets cauliflower rice, HJ gets nugget-cut pieces)

## Post-Trip Closeout
- Log what was purchased vs what was missing
- Update kitchen inventory if significant items added/depleted
- Flag if any items from list were unavailable → alternative needed?

## Common Pitfalls
- Proposing meals that need equipment not in kitchen → always check inventory first
- Volume measurements on list → grams only
- Shopping list without store assignment → always label H-E-B vs Costco
- Creating full recipes in Saturday proposal → names + one-line reason only (no recipes until selected)

## Verification Checklist
- [ ] Meal selected before list generated
- [ ] Kitchen inventory checked
- [ ] All quantities in grams
- [ ] Each item assigned to H-E-B or Costco
- [ ] Prep tasks created for any day-before requirements
