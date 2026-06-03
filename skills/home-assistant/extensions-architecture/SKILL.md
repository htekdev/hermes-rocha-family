---
name: extensions-architecture
description: Use when building or reasoning about tool extensions, guard patterns, hooks, or integration capabilities. Codifies the Node.js ESM extension model, 4 lifecycle hooks, guard-extension patterns (calendar-date-guard, tool-fishing-guard), and ask-via-telegram confirmation routing.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, extensions, hooks, guards, telegram, architecture]
    related_skills: [telegram-bridge, hermes-governance, checkin-orchestrator, constitution]
---

# Extensions Architecture

## Overview

Extensions give agents their **tools** — Node.js ESM modules that expose callable functions, intercept lifecycle events, or enforce governance policies. Two categories: **Tool extensions** (add capabilities) and **Hook/Guard extensions** (enforce policies, block bad actions).

Hermes does not run Copilot CLI directly but studies these patterns to understand the tool ecosystem, guard philosophy, and how to reason about extension-backed capabilities available to OG and other agents on the mesh.

## When to Use

- Reasoning about what tools are available to mesh agents (OG, Pi, etc.)
- Understanding why a guard blocked an action
- Designing Hermes-specific governance rules analogous to hook guards
- Evaluating whether a proposed action would be blocked by an extension guard

---

## Extension Categories

### Tool-Based Extensions
Expose API capabilities agents call by name:

| Extension | Key Tools | Hermes Relevance |
|-----------|-----------|-----------------|
| `telegram-bridge` | `telegram_send_message`, `telegram_send_photo`, `telegram_get_status` | Primary delivery channel |
| `ask-via-telegram` | `ask_user` | Confirmation routing for high-stakes actions |
| `google-services` | `gcal_today`, `gcal_upcoming`, `gcal_create_event`, `gmail_search` | Calendar + email backbone |
| `action-tracker` | `add_task`, `complete_task`, `task_summary` | Task handoff to OG via TYPE:task-request |
| `budget-tracker` | `add_expense`, `budget_summary`, `upcoming_bills` | Finance domain (OG owns) |
| `home-maintenance` | `add_maintenance_task`, `maintenance_due`, `log_maintenance` | Home domain (Hermes owns monitoring) |
| `meal-planner` | `set_meal`, `get_meal_plan`, `generate_grocery_list` | Nutrition domain (split: OG logistics, Hermes Paula nutrition) |
| `google-maps` | `get_drive_time`, `get_directions` | Drive time + 15-min buffer rule |
| `agent-launcher` | `launch_agent`, `list_agents_on_disk` | Mesh delegation pattern |
| `cron-scheduler` | `cron_list_jobs`, `cron_next_run` | Schedule inspection |

### Hook/Guard Extensions
Use `onPreToolUse` to intercept and block tool calls before execution:

```
onSessionStart   → inject context (load family profile, working memory)
onPreToolUse     → BLOCK bad actions (date errors, forbidden paths, tool fishing)
onPostToolUse    → observe + auto-commit after data changes
onUserPromptSubmitted → pre-prompt checks
```

---

## Guard Patterns

### calendar-date-guard
**Purpose**: Block wrong dates being passed to `gcal_create_event` and calendar tools.

**Problem it solves**: Agents frequently off-by-one on dates, especially:
- Using today's date for events that are tomorrow
- Wrong year at year boundaries (Jan 1 risk)
- Scheduling in the past silently

**How it works** (onPreToolUse):
1. Intercept any call to `gcal_create_event` or similar
2. Validate: `event_date >= today` (no past scheduling without explicit override)
3. Validate: date is parseable ISO format
4. Validate: end_time > start_time
5. If fail → BLOCK + return error explaining the date issue
6. Agent reads error, corrects date, retries

**Hermes analog** (in SKILL form):
- Before reporting any date-based fact: verify date is correct for current context
- `today = June 3, 2026 CT` — always anchor relative dates to this
- Leo discharge date = June 3 ✅ (confirmed); Mia discharge = TBD (do NOT speculate)

### tool-fishing-guard
**Purpose**: Prevent speculative/exploratory tool calls — block when agent doesn't have all required parameters.

**Problem it solves**: Agents sometimes call tools to "see what happens" or with placeholder values, wasting API quota and causing side effects.

**How it works** (onPreToolUse):
1. Inspect tool call arguments for placeholder patterns (`"TODO"`, `"UNKNOWN"`, empty strings where required)
2. Detect calls without sufficient context (e.g., searching calendar with no date range)
3. If speculative → BLOCK + return: "Do not call this tool until you have [missing param]"

**Hermes analog**:
- Never send a Telegram message with placeholder content
- Never broadcast to mesh without actual content to share
- Never create a task without assignee, description, and priority
- If missing required context → ask (Hector) or log a clarification-needed item

### ask-via-telegram Guard
**Purpose**: Route high-stakes confirmation prompts to Telegram instead of blocking silently.

**Pattern**:
```
agent needs confirmation → call ask_user(question, chat_id) → user replies via Telegram → agent proceeds
```

**Hermes analog** (4-tier decision framework):
- Tier 1 (routine): act silently
- Tier 2 (reversible, medium stakes): act + notify
- Tier 3 (irreversible or high-stakes): ask first via Telegram → wait for reply
- Tier 4 (destructive/financial/medical): ALWAYS ask, never assume

---

## Extension Architecture Rules

From copilot-hooks-starter:
1. **Zero external dependencies** — only `node:*` + `@github/copilot-sdk`
2. **Graceful degradation** — missing env vars → warning, not crash
3. **Idempotent tools** — safe to retry (especially important for Telegram sends)
4. **Clear descriptions** — the AI uses descriptions to decide WHEN to call the tool

### Post-Error Feedback Loop (gh-hookflow)
When a post-lifecycle validation fails:
1. hookflow writes `error.md` to session directory
2. Next `onPreToolUse` → DENY all tools with "Read error file at {path}"
3. Agent reads the error file (exempted as read-only primitive)
4. `onPostToolUse` for the read → delete error file
5. Agent proceeds with fix

This turns post-hooks into **blocking validators** — critical for data quality guards.

---

## Integration Map for Hermes

| Hermes Domain | Tools Required | Extension |
|--------------|---------------|-----------|
| Wellness monitoring | `telegram_send_message` | telegram-bridge |
| Pediatric follow-up reminders | `add_task` | action-tracker |
| Home maintenance | `add_maintenance_task` | home-maintenance |
| High-stakes confirmations | `ask_user` | ask-via-telegram |
| Drive time calculations | `get_drive_time` | google-maps |
| Morning briefing data | `gcal_today`, `gcal_upcoming` | google-services |

---

## Common Pitfalls

1. **Calling tools speculatively** — triggers tool-fishing-guard; always have full params first
2. **Wrong date format** — triggers calendar-date-guard; use ISO 8601
3. **Rapid-fire Telegram calls** — rate limits + annoys users; batch messages
4. **Missing ask_user for Tier 3+** — always route high-stakes decisions to human
5. **Forgetting idempotency** — if tool is retried due to error, ensure no duplicate side effects

## Verification Checklist

- [ ] Extension category identified (tool-based vs hook/guard)
- [ ] All required parameters available before tool call
- [ ] Date arguments verified against current date (June 3, 2026)
- [ ] Tier-appropriate decision routing (Tier 3+ → ask_user)
- [ ] Telegram messages are batched, not rapid-fire
- [ ] Post-error feedback loop understood if guard blocks action
