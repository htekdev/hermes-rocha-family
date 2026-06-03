---
name: orchestrator-protocol
description: Use when running a system-wide agent check-in or coordinating multiple domain agents. Implements the Discover→Filter→Dispatch→Collect→Compile→Notify orchestration pattern.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, orchestration, agents, parallel]
    related_skills: [parallel-coordination, checkin-orchestrator, checkin-agent-orchestrator, heartbeat-protocol]
---

# Orchestrator Protocol

## Overview
The orchestrator coordinates all specialized domain agents during check-ins. Its role is to **delegate, collect, and compile** — it NEVER does domain work itself. All agents run in parallel for performance; the orchestrator only merges and reports.

**Core pattern**: `Discover → Filter → Dispatch (parallel) → Collect → Compile → Notify`

## When to Use
- Scheduled system check-ins (hourly/daily)
- When multiple domain agents need simultaneous status reports
- Weekly planning compilation
- Any time a consolidated view across all domains is needed

## Step-by-Step Workflow

### Step 1: Discover
```
glob(".github/agents/*.agent.md")
```
Extract agent names by stripping `.agent.md` suffix.

### Step 2: Filter (do NOT dispatch these)
| Category | Agents |
|----------|--------|
| Self | `orchestrator` |
| Own cron schedule | `daily-briefing`, `weekly-planner`, `budget-review`, `meal-planner` |
| Runs own cycle | `heartbeat` |
| Team agents | any `*-team` agents |
| Utility/meta | `platform-manager`, `context-auditor`, `test-*` |

### Step 3: Dispatch in Parallel
Launch ALL remaining domain agents **simultaneously** via `task` tool with `mode: "background"`.

> ⚠️ All task calls go in **ONE response batch** — splitting across responses makes them sequential, not parallel.

**Standard prompt template for each dispatched agent:**
```
Scheduled check-in. Current time: {CURRENT_TIME}.
Check your domain for updates, urgent items, and anything noteworthy.
TASK-FIRST: If you discover anything actionable, CREATE A TASK via add_task — don't just report it.
Only send messages for URGENT items.
Return:
- STATUS: [updates/nothing]
- URGENT_SENT: [yes/no]
- TASKS_CREATED: [list or none]
- REPORT: [2-4 bullet points or "All clear."]
```

### Step 4: Collect Reports
```
read_agent(agent_id, wait=true)
```
Parse structured fields: `STATUS`, `URGENT_SENT`, `TASKS_CREATED`, `REPORT`

**Failure handling:**
- Timeout/error → note: `"⚠️ {Agent}: check-in failed — will retry next cycle"`
- Never block compilation on one failure
- 3+ failures → include diagnostic alert

**Critical agent timeout (wellness-coach/nicu-care):**
- Immediate retry — do NOT wait for next cycle
- Failure of these agents = escalate to Hector via Telegram

### Step 5: Compile Report
```
🤖 Agent Check-In — {DAY}, {DATE} {TIME}

{emoji} {Agent Name}:
{agent_report}

✅ All agents checked in. {X}/{TOTAL} had updates.
```

**Compilation rules:**
- **Omit** agents reporting "All clear" / "nothing" — silence is the default
- Note `(⚡ urgent alert sent)` if agent already messaged directly
- Max 2–4 lines per section
- **If ALL agents report nothing → stay completely silent** (return "No activity")

### Step 6: Send ONE Message
Send **one** consolidated message. No per-agent piecemeal messages. Stay silent if nothing actionable.

## Performance Targets
| Metric | Target |
|--------|--------|
| Per-agent completion | 2–3 min |
| Full orchestration | ≤ 5 min |
| Early-termination trigger | 3 consecutive all-clear cycles |

## Early-Termination (Cost Optimization)
After 3 consecutive cycles where ALL agents return "nothing":
1. Skip dispatch for next cycle
2. Run only watch-list check (Phase 0)
3. Reset counter if any agent returns updates
4. Reset counter if any critical event is active (NICU, discharge, medical)

> ⚠️ Never apply early-termination when: Leo/Leilani NICU active, Paula PPD window (4–8 wk post-Leo-discharge), active proposal window

## Hermes-Specific Integration

### Hermes as Sub-Orchestrator
Hermes doesn't have a full agent fleet, but applies this pattern for:
- Hourly mesh check (heartbeat → poll → health-scan → work → broadcast)
- Wellness domain parallel checks (wellness-coach + nicu-care simultaneously)
- Morning briefing compilation (family-coordinator + health-coach + home-manager)

### Agent Eligibility for Hermes Dispatch
| Domain | Agent | Notes |
|--------|-------|-------|
| Wellness | wellness-coach | Never early-terminate |
| NICU/health | nicu-care | Never early-terminate |
| Family | family-coordinator | Standard |
| Dog | dog-parent | Standard |
| Home | home-manager | Standard |
| Finance | finance-manager | Standard |

### Excluded from Hermes Check-In Dispatch
- `budget-review` — runs 1st of month cron only
- `weekly-planner` — runs Sunday 7 PM only
- `meal-planner` — runs Saturday 10 AM only
- `content-*` — OG agent domain (Hermes is observer only)
- `project-manager` — OG agent domain

## Finishing Rule
When orchestration is complete: write the final compiled report as text and STOP.
Do NOT call any "complete" or "done" tool after compilation.

## Common Pitfalls
- ❌ Launching agents in separate responses (sequential, not parallel)
- ❌ Including agents in dispatch that have their own cron schedule
- ❌ Blocking on one failed agent — always compile with partial results
- ❌ Sending per-agent messages instead of one consolidated report
- ❌ Applying early-termination when NICU/PPD critical state is active
- ❌ Doing domain work inside the orchestrator (delegate, never inline)

## Verification Checklist
- [ ] All eligible domain agents dispatched in a single response batch
- [ ] Excluded agents (budget-review, weekly-planner, etc.) not dispatched
- [ ] Reports collected with `read_agent(wait=true)`
- [ ] Compilation omits all-clear agents
- [ ] One final message sent (or silence if all clear)
- [ ] Early-termination counter NOT active during critical family states
