---
name: checkin-agent-orchestrator
description: Use when running the multi-agent check-in dispatch cycle. Orchestrates parallel domain agent runs, compiles results, sends consolidated Telegram report with early-termination pattern.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, orchestration, checkin, automation]
    related_skills: [heartbeat-protocol, checkin-orchestrator, hermes-mesh-protocol]
---

# Check-in Agent Orchestrator

## Overview
Orchestrates delegated check-ins to specialized domain agents, compiles results into one consolidated Telegram message. **Does NOT do domain work itself.** Role is dispatch → collect → report.

## When to Use
- Running a full multi-domain check-in cycle
- Determining which agents to dispatch and in what order
- Compiling a single consolidated report from multiple domain agents

## Core Workflow
1. **Read** family-profile/constitution first
2. **Compute CT time** → quiet hours check (10 PM–6 AM CT)
3. **Read** recovery state → early termination check
4. **Discover** active domain agents
5. **Filter exclusions** → parallel dispatch
6. **Collect** results → compile → notify Hector if anything actionable

## Agent Exclusion List (Do NOT dispatch these from check-in)
- `checkin` (self-reference)
- `daily-briefing` (has its own schedule)
- `budget-review` (monthly, 1st-of-month)
- `weekly-planner` (Sunday evening only)
- `meal-planner` (Saturday only)
- `heartbeat` (separate cycle)

## Early-Termination / Recovery Mode
Prevents wasted cycles when everything is quiet.

### Recovery State Schema
```json
{
  "consecutive_all_clear": 0,
  "recovery_active": false,
  "last_cycle_time": "ISO-8601-CT",
  "last_cycle_had_updates": false
}
```

### Logic
```
1. Read recovery state
2. Compute time since last_cycle_time
3. If (time_gap < 90 min) AND (consecutive_all_clear >= 3):
   → SKIP dispatch, return early, update state
4. Otherwise: proceed with normal dispatch
5. After collection: count results, update state file
```

- **Threshold**: 3 consecutive all-clear cycles → skip dispatch
- **Reset**: Any actionable update resets counter to `0`
- **Purpose**: Prevents ~12 wasted rapid cycles per recovery window

## Error Handling
- Agent failure → note as `"⚠️ {Agent}: check-in failed — will retry next cycle"`
- One failure never blocks others
- 3+ failures → send diagnostic alert to Hector
- Auth expired → notify parent immediately

## Performance Targets
- All agents launched **in parallel** (batch all dispatches in one response)
- Per-agent: 2–3 min
- Full orchestration: ≤5 min

## Output Standards
- **Silence if**: ALL agents report nothing / only routine confirmations
- **Telegram**: 2–5 lines max unless detail requested
- Result-first, no internal process narration
- Warm, professional tone

## Common Pitfalls
- Dispatching excluded agents (budget-review, weekly-planner outside schedule)
- Running sequentially instead of in parallel
- Sending a Telegram message when nothing is actionable
- Not updating recovery state after cycle completes

## Verification Checklist
- [ ] Quiet hours checked before dispatch
- [ ] Recovery state read before dispatch
- [ ] Excluded agents filtered out
- [ ] Agents dispatched in parallel
- [ ] Recovery state updated after cycle
- [ ] Telegram only sent if actionable content exists
