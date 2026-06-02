---
name: budget-review
description: Use when performing monthly budget review or user asks for spending summary, budget vs actual, financial report, or recurring charges audit. Generates 6-section Telegram report on 1st of month.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, finance, budget, monthly]
    related_skills: [finance-manager, family-profile, telegram-bridge]
---

# Budget Review Skill

## Overview

Monthly (1st of month) deep-dive budget report for the Rocha family. Covers spending breakdown, budget vs actual, trends, recurring charges, upcoming bills, and recommendations. Also includes a **Baby/Twins Expense** section given NICU twin context.

Sourced from: `budget-review.agent.md` + `budget-reporting/SKILL.md`

## When to Use

- Scheduled: 1st of each month (cron trigger)
- On-demand: Hector asks for "budget report", "spending summary", "budget check", "where did money go"
- Weekly planner: include Steps 1 + 5 only (spending context for week)
- Daily briefing: Step 5 only (bills due next 3 days)

## Report Structure (6 Steps — Canonical Order)

### Step 1: Spending Summary
```
get_spending_summary(start_date: "YYYY-MM-01", end_date: "YYYY-MM-DD")
```
**Format:**
```
💰 Monthly Summary (Month YYYY)
━━━━━━━━━━━━━━━━━━━━━━
Total Spent: $X,XXX
Total Income: $X,XXX
Net: +/-$X,XXX
```
Break down by top 5 categories with amounts and %.

### Step 2: Budget vs Actual
Compare each category against target:
- 🟢 Under budget — celebrate
- 🟡 At budget (90-100%) — note
- 🔴 Over budget — flag amount over

Calculate overall adherence: (at/under) / total × 100%

### Step 3: Trends
Compare to prior month:
```
get_spending_summary(prior_period_start, prior_period_end)
```
- Note increases/decreases by category
- Flag unusual one-time expenses
- Identify patterns (subscription creep)

### Step 4: Recurring Charges Audit
```
get_recurring(min_occurrences: 3)
```
- List all subscriptions + monthly cost
- Flag new recurring charges since last review
- Total monthly subscription burn

### Step 5: Upcoming Bills
- Monthly review: full next month view
- Weekly planner: next 7 days
- Daily briefing: next 3 days only

### Step 6: Recommendations
1–3 actionable items:
- Over-budget → specific reduction idea
- Unused subscriptions → cancellation suggestion
- Positive trend → reinforcement ("kept food budget tight — 👏")

### Section 7 (Rocha-specific): 👶 Twins/NICU Expenses
- Track NICU co-pays, baby gear, nursery, medical supplies
- Compare to baby budget if set
- **Medical costs are non-negotiable** — never recommend cutting baby/medical/NICU line items
- Report without judgment; these are expected

## Integration Map

| Consumer | Steps Used |
|----------|-----------|
| `budget-review` (monthly) | All (1–7) |
| `daily-briefing` | Step 5 only |
| `finance-manager` (on-demand) | Steps 1, 2, 4 |
| `weekly-planner` | Steps 1, 5 |

## Delivery Rules

- Send via Telegram to **Hector** (7729308746)
- Include `speak` param: 1-sentence TTS of net result (e.g. "Down $200 vs last month, net positive by $400.")
- Paula: DO NOT send full budget report. At most a 2-line summary if she asks directly
- Quiet hours: no delivery 10 PM – 7 AM CT
- Length: use sections/bullets for Telegram-friendly layout; full report is OK monthly

## Tone Rules

- Financial HEALTH framing, never guilt
- Lead with the number, then context
- Emojis for visual scanning: 💰 📊 🎯 📈 📋 💡
- No moralizing about spending categories
- Positive reinforcement when budget is healthy

## Common Pitfalls

- ❌ Don't lecture about spending — report and suggest, never judge
- ❌ Don't recommend cutting NICU/medical/baby expenses
- ❌ Don't send detailed finance report to Paula (message limits)
- ❌ Don't skip Section 7 — twins expenses are always relevant right now
- ❌ Don't fabricate data if spending tools are unavailable — report "data unavailable" explicitly

## Verification Checklist

- [ ] Report includes all 6 standard steps + Section 7 (twins)
- [ ] Delivered to Hector with `speak` param
- [ ] Budget vs actual uses correct emoji tiers (🟢/🟡/🔴)
- [ ] Recommendations are 1–3, actionable, not moralizing
- [ ] Recurring charges audit flags any new subscriptions
- [ ] NICU/baby line items are never flagged as cut candidates
