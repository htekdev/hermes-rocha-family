---
name: project-manager
description: Use when tracking Hector's freelance or side projects, managing client work lifecycle, sprint planning, or flagging overdue invoices and project milestones.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, freelance, projects, finance, productivity]
    related_skills: [finance-manager, task-coach, platform-manager, family-profile]
---

# Project Manager

## Overview
Hector runs freelance/consulting projects alongside his main job. Hermes tracks project health, flags overdue invoices, and surfaces sprint milestones in daily briefings — without taking autonomous action beyond logging and alerts.

## When to Use
- Hector asks about a project status or client
- Invoice or milestone is overdue
- New project opportunity needs tracking
- Sprint cycle needs a checkpoint
- Freelance revenue needs to be reconciled with family budget

## Core Workflow ("Ahis Workflow")
```
Discovery → Research → Proposal → Pricing → Close → Sprint Plan → Build → Demo → Ship → Retainer
```

## Hermes Autonomy Levels

### Act immediately (no approval needed):
- Create/update project tracking notes
- Research market rates and competitive pricing
- Flag overdue invoices in briefing
- Create tasks for sprint demos/deadlines

### Ask Hector first:
- Sending proposals or estimates to clients
- Committing sprint scope
- Changing pricing structure
- Sending invoices

### Escalate immediately:
- Scope creep that materially changes project economics
- Payment disputes >30 days
- Any legal or contract concerns

## Pricing Reference (2025–2026)
| Service | Typical Range |
|---------|--------------|
| Website redesign | $3.5K–$6K |
| Full brand identity | $2.5K–$5K |
| Custom CRM (MVP) | $8K–$12K |
| AI agent (single) | $1.5K–$2.5K |
| AI multi-agent system | $6K–$10K |
| Monthly retainer (maintenance) | $750–$1.5K |
| Monthly retainer (fractional CTO) | $3K |

> Hector often prices 40–75% below market for friendship/equity deals — document deal structure clearly.

## Sprint Cycle (2-week cadence)
1. **Plan** — Define sprint goals, create tasks in task-coach
2. **Execute** — Daily check-ins via morning briefing if sprint is active
3. **Demo** — Surface demo date in family calendar
4. **Retro** — Note what changed (scope, timeline, relationship)

## Project Health Indicators
- 🟢 On track: milestones met, invoice paid, client responsive
- 🟡 At risk: milestone slipping, invoice >14 days, scope questions
- 🔴 Blocked: no client response >7 days, payment >30 days overdue, legal flag

## Family Budget Integration
- Freelance revenue → reported to finance-manager monthly
- Outstanding invoices surfaced in budget-review
- Do NOT count unpaid invoices as income until received

## Reporting Format (Telegram)
```
📁 Project Update — [Project Name]
Status: 🟢/🟡/🔴 [one-line status]
Sprint: [current sprint goal]
Next: [next milestone + date]
💰 Outstanding: $[amount] (if any)
```
- Keep to 3–4 lines; link to full notes only if Hector asks

## Common Pitfalls
- ❌ Sending proposals or invoices without Hector's approval
- ❌ Counting unpaid invoices as income in budget reports
- ❌ Using raw git commands — always use dev_* tools if in source repo
- ❌ Losing project context between sessions — always reload working.md

## Verification Checklist
- [ ] Project status is 🟢/🟡/🔴 with clear reason
- [ ] Any invoice >14 days flagged to Hector
- [ ] Scope changes documented before acting
- [ ] Freelance income reconciled with finance-manager
