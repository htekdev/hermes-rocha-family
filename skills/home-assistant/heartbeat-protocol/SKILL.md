---
name: heartbeat-protocol
description: Use when executing Hermes's hourly autonomous check-in cycle. Defines 4-phase execution (watch→email→calendar→tasks), Telegram prefix standards, and detect-act-notify behavior.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, heartbeat, automation, telegram]
    related_skills: [checkin-orchestrator, family-coordinator, task-coach, telegram-bridge]
---

# Heartbeat Protocol

## Overview
The heartbeat is Hermes's periodic autonomous check-in cycle. Pattern: **detect → act → notify**. Never ask permission before routine actions — create tasks, send reminders, update records, then report what was done.

## When to Use
- Every hourly cron run
- Any autonomous monitoring cycle
- When determining what to do and in what order

## Core Behavior Rules
- **Default to action**, not to reporting
- **Report what you DID**, not what the family should do
- Always read constitution/family-profile before acting
- **NEVER narrate internal steps** — only output actionable results
- If nothing actionable: stay silent (return `[SILENT]`)

## Telegram Message Prefixes
| Prefix | Meaning |
|--------|---------|
| 🔴 **ACTION REQUIRED** | Must be done personally — include contact/deadline |
| ⏰ **LEAVE BY** | Departure time with travel estimate (+15 min buffer always) |
| ✅ **AUTO-HANDLED** | Already taken care of by Hermes |
| 📋 **CREATED** | Proactively created task/event |
| ⚠️ **HEADS UP** | Non-urgent awareness |

## 4-Phase Execution

### Phase 0: Watch List (ALWAYS FIRST)
- Check items on the watch list with status `pending`
- Tiered escalation:
  - 1–2 days: recheck
  - 3+ days: create human task
  - 7+ days: Telegram escalation
- Skip if already actioned today

### Phase 1: Email / Inbound Scan
- Scan unread messages/inbound signals from last 3 hours
- Actually **read and act** — don't just count
- For each lead/inquiry: extract info → create follow-up task → auto-notify if urgent
- No emojis in subject lines (UTF-8 encoding issues)

### Phase 2: Calendar Awareness
- Check today + tomorrow
- Events within 90 min: calculate drive time → send leave-by reminder (+15 min buffer)
- Doctor/OB/pediatric appointments: add "Bring: insurance card, questions list"
- Tomorrow events before 10 AM: send prep reminder tonight
- Flag scheduling conflicts immediately

### Phase 3: Task Management
- **Overdue tasks** → reschedule to tomorrow, notify
- **High-priority due today** → specific action reminder
- **Ready tasks** (dependencies met) → nudge to start
- **Bills due within 3 days** → amount, company, date, auto-pay status
- **Overdue maintenance** → create task if none exists
- Skip if already reminded today (check task notes)

### Phase 4: Housekeeping
- Create follow-up tasks from any phase
- Update/complete resolved items
- If **nothing actionable**: stay silent

## Batching Rules
Send **max 2–3 Telegram messages** per cycle:
1. Urgent/time-sensitive (immediate)
2. Summary batch (everything else)
3. Tomorrow prep (if applicable)

## Key Constraints
- **Quiet hours**: 10 PM–6 AM CT; only CRITICAL overrides permitted
- Task rescheduled **3+ times** → escalate as urgent, flag to Hector
- Messages: **2–5 lines max**, bullet points
- Pregnancy/newborn context: appointment reminders always **critical**
- Paula messaging limits: 2–3 lines, one question at a time, no rapid-fire

## Common Pitfalls
- Starting with a summary instead of action
- Sending more than 3 Telegram messages per cycle
- Pinging Paula outside her limits during feeding/sleep windows
- Forgetting adjusted age when referencing Leo/Mia milestones
- Narrating "I am now checking email..." — never do this

## Verification Checklist
- [ ] Watch list checked first
- [ ] All actions were taken, not deferred
- [ ] Telegram prefixes used correctly
- [ ] Quiet hours respected (or CRITICAL override justified)
- [ ] Paula message limit respected
- [ ] Batched to ≤3 Telegram messages
