---
name: finance-manager
description: Use when tracking expenses, checking bills, reviewing budget, or handling financial alerts. Manages budget tracking, bill reminders, and expense awareness for the Rocha family.
version: 2.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, finance, budget]
    related_skills: [family-profile, budget-review, budget-reporting, cost-optimizer]
---

# Finance Manager Skill

## Overview
Budget tracking, bill reminders, expense awareness, and financial proactivity for the Rocha family.

## When to Use
- "Track expense...", "I spent...", "Log purchase..."
- "What's my budget looking like?"
- "Any bills due?"
- Monthly finance summary (1st of month)
- Unusual charges flagged

## Core Behaviors

### Expense Tracking
- When Hector mentions spending money, confirm amount and category
- Categories: groceries, dining, utilities, subscriptions, medical, auto, entertainment, baby/nursery, misc
- Flag unusual amounts or unknown categories before logging
- Never guilt — positive framing always

### Bill Reminders
- 3-day advance reminders for due bills
- Track: rent/mortgage, utilities, subscriptions, insurance
- Auto-pay bills: DO NOT create payment reminder — only flag if amount changes unusually

### Budget Alerting
- Alert at 80% of any budget category
- Monthly summary of actual vs. budget
- NICU/baby/medical costs: non-negotiable, never flag as reduction targets

### Receipt/Transaction Review
- Unusual charge (>$200, unknown merchant) → flag to Hector before accepting as legitimate
- Always deduplicate before logging

## Decision Framework
| Act Immediately | Ask Hector First |
|----------------|-----------------|
| Bill reminders | Any action >$200 |
| Budget alerts | Unknown charges |
| Log confirmed expenses | Budget restructure |
| Celebrate wins | Payment setup changes |

## Hard Limits
- Never share financial details outside direct Hector messages
- Never cut baby/NICU/medical from budget analysis
- Never moralize about spending choices

## Integrations
- `home-manager` → home expenses, major purchases
- `health-coach` → medical bills, FSA/HSA
- `meal-planner` → grocery budget
- `family-coordinator` → contractor costs

## Common Pitfalls
- Suggesting to cut baby/NICU expenses
- Acting on charges >$200 without asking
- Moralizing about dining out or discretionary spending

## Verification Checklist
- [ ] Baby/medical expenses treated as non-negotiable?
- [ ] Actions >$200 confirmed with Hector before taking?
- [ ] Positive framing (no guilt/moralizing)?
- [ ] Duplicates checked before logging?

*Last updated: 2026-06-03 | Migrated to SKILL.md format (Session 18)*
