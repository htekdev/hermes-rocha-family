---
name: budget-reporting
description: Use when generating budget reports, spending summaries, or monthly financial reviews. Covers step-by-step canonical report format for Rocha family finances.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, finance, budget, reporting]
    related_skills: [finance-manager, weekly-planner, daily-briefing, telegram-bridge]
---

# Budget Reporting Skill

## Overview

Canonical pattern for generating family budget reports used across budget-review, finance-manager, and daily-briefing agents. Every report follows a consistent 6-step structure.

## When to Use

- Monthly budget reviews (1st of month)
- Weekly finance digests
- On-demand "how are we doing?" queries
- Daily-briefing finance section (bills only)
- Any time a structured spending summary is needed

## Report Structure (Canonical Format)

Steps can be used as a subset — but ordering and format are fixed.

### Step 1: Spending Summary

Pull current-period spending:
```
get_spending_summary(start_date: "YYYY-MM-01", end_date: "YYYY-MM-DD")
```

Output format:
```
💰 Monthly Summary (Month YYYY)
━━━━━━━━━━━━━━━━━━━━━━
Total Spent: $X,XXX
Total Income: $X,XXX
Net: +/-$X,XXX
```

Break down by top categories with amounts and % of total.

### Step 2: Budget vs Actual

Compare each category to its target:
- 🟢 Under budget — celebrate
- 🟡 At budget (90–100%) — note
- 🔴 Over budget — flag with dollar overage

Calculate **overall adherence**: (categories at/under budget) / (total categories) × 100%

### Step 3: Trends

Compare current period vs prior period:
```
get_spending_summary(start_date: prior_start, end_date: prior_end)
```
- Note increases/decreases by category
- Flag unusual one-time expenses
- Identify growing patterns (subscriptions added, recurring charges growing)

### Step 4: Recurring Charges Audit

```
get_recurring(min_occurrences: 3)
```
- List all subscriptions with monthly amounts
- Flag any new recurring charges since last review
- Calculate total monthly subscription burn

### Step 5: Upcoming Bills

Show bills due in next:
- **Daily-briefing**: next 3 days
- **Weekly-planner**: next 7 days
- **Monthly review**: full next month

### Step 6: Recommendations

Generate 1–3 actionable recommendations:
- Over-budget categories → specific reduction ideas
- Unused subscriptions → cancellation suggestions
- Positive trends → reinforcement

## Consumer Map

| Agent | Steps Used |
|-------|-----------|
| `budget-review` (monthly) | All 6 steps |
| `finance-manager` (on-demand) | Steps 1, 2, 4 |
| `daily-briefing` | Step 5 only |
| `weekly-planner` | Steps 1, 5 |

## Special Section: Baby/NICU Expenses

When running monthly reviews, include a **Section 6b: 👶 Baby & NICU Spending**:
- Track twin preparation expenses (nursery, baby gear, medical co-pays, supplies)
- Compare against any baby budget set
- Medical co-pays are **non-negotiable** — never flag as reduction targets

## Tone Rules

- Positive and constructive — financial HEALTH, not guilt
- Use emojis for visual scanning: 💰 📊 🎯 📈 📋 💡
- Lead with the number, then context
- Keep concise — Telegram delivery requires brevity

## Common Pitfalls

- ❌ Lecturing about debt morally
- ❌ "You spent too much on X" without context
- ❌ Recommending cutting essentials (baby, medical, food)
- ❌ Ignoring NICU/twin context — medical costs are non-negotiable
- ❌ Running steps out of order

## Verification Checklist

- [ ] Report leads with net result (spending summary first)
- [ ] Budget vs actual uses 🟢🟡🔴 system
- [ ] Recurring audit included in monthly reviews
- [ ] Baby/NICU spending section present in monthly report
- [ ] Recommendations are actionable and specific
- [ ] Tone is constructive, not guilt-inducing
