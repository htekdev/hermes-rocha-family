---
name: parallel-coordination
description: Use when orchestrating multiple independent agents simultaneously to reduce latency and token cost. Codifies launch-wait-collect-report pattern with graceful failure handling.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, orchestration, performance, agents]
    related_skills: [checkin-agent-orchestrator, checkin-orchestrator, heartbeat-protocol, stasis-detection]
---

# Parallel Agent Coordination

## Overview
When multiple independent domain agents need to run — e.g., during hourly check-ins — launching them in parallel dramatically reduces total latency vs. sequential dispatch. This skill codifies the canonical pattern used by the checkin orchestrator.

**Speedup example:** 3 agents × 2min each = **2min parallel** vs **6min sequential** (3× faster; scales linearly)

## When to Use
- Hourly check-in dispatching multiple domain agents
- System audits requiring input from several domains at once
- Any multi-agent work where tasks are independent (no dependency chain)
- Batch processing across family domains

## Core Pattern

```
Launch All (1 response) → Wait for All → Collect Results → Handle Failures → Compile ONE Report
```

## Implementation

### Step 1 — Launch All in Parallel (single response)
All `task` calls must be issued in **one response** to execute in parallel:

```
task(agent_type: "finance-manager", mode: "background", name: "finance-check", prompt: "Run daily check-in...")
task(agent_type: "home-manager", mode: "background", name: "home-check", prompt: "Run daily check-in...")
task(agent_type: "wellness-coach", mode: "background", name: "wellness-check", prompt: "Run daily check-in...")
```

### Step 2 — Wait for Completion
```
read_agent(agent_id: "finance-check", wait: true, timeout: 180)
read_agent(agent_id: "home-check", wait: true, timeout: 180)
read_agent(agent_id: "wellness-check", wait: true, timeout: 180)
```

Default timeout: **30s**. Use **180s** for agents with external API calls.

### Step 3 — Handle Failures Gracefully
For each agent:
- `status == "completed"` → include result in report
- `status != "completed"` → log as `[agent-name]: [status]`
- `TimeoutError` → log as `[agent-name]: timeout after 180s — will retry next cycle`

> Never block the full report on a single agent failure. Partial results are acceptable.

### Step 4 — Compile ONE Report
Send one consolidated Telegram message (or mesh broadcast):
```
✅ 3/3 agents reported.
[Key findings from each]
```
or:
```
✅ 2/3 agents reported. 1 timeout.
⚠️ home-check: timeout after 180s — retry next cycle
[Results from completed agents]
```

## Performance Targets

| Metric | Target |
|--------|--------|
| Agent startup | <30s each |
| Agent completion | <3 min each |
| Total orchestration | <5 min |
| Default timeout | 3 min (180s) |

## Early Termination / Recovery Mode

From `checkin-agent-orchestrator`:
- After **3 consecutive all-clear cycles** → skip dispatch, save ~12 wasted agent cycles
- Reset counter on ANY finding (task created, alert sent, anomaly detected)
- Excluded from parallel dispatch: `budget-review`, `weekly-planner`, `meal-planner` — these run on their own cron schedule

## Hermes-Specific Agent List

Agents eligible for parallel dispatch in hourly check-in:

| Agent | Domain | Notes |
|-------|--------|-------|
| `wellness-coach` | Paula postpartum health | High priority — never skip |
| `home-manager` | Maintenance, nursery | Active during NICU period |
| `dog-parent` | Bella intro protocol | Phase 1 active since June 3 |
| `nicu-care` | Mia NICU monitoring | Only trend/follow-up; OG logs sessions |
| `task-coach` | ADD-friendly task nudges | Skip outside 9 AM–5 PM CT |

**NOT dispatched from checkin:**
- `budget-review` (1st of month cron)
- `weekly-planner` (Sunday evening cron)
- `meal-planner` (Saturday cron)
- `morning-briefing` (6 AM weekday / 8 AM weekend cron)

## Dynamic Agent Discovery (Advanced)
```
all_agents = glob(".github/agents/*.agent.md")
domain_agents = filter(all_agents, exclude=["orchestrator", "task-agent-*", "team-*"])
for agent in domain_agents:
    task(agent_type=agent.name, mode="background", ...)
```

## Error Escalation

| Failure Rate | Action |
|---|---|
| 1 agent timeout | Log, retry next cycle, no alert |
| >30% agents fail | ⚠️ Alert Hector — systemic issue (network/load) |
| Critical agent fails (wellness-coach, nicu-care) | Retry immediately with `timeout=300` |

## Common Pitfalls
- Issuing `task` calls across multiple responses (sequential, not parallel — wastes 3–5min)
- No timeouts on `read_agent` calls (infinite wait blocks the orchestrator)
- Reporting partial failures without noting retry plan
- Dispatching excluded agents (budget-review etc.) from the check-in loop
- Blocking the full report because one non-critical agent timed out

## Verification Checklist
- [ ] All `task` calls issued in single response
- [ ] `read_agent` called with `wait: true` and explicit `timeout`
- [ ] Failure handling: partial results accepted, failures logged
- [ ] ONE consolidated report (not one Telegram per agent)
- [ ] Excluded agents (`budget-review`, `weekly-planner`, `meal-planner`) not in dispatch list
- [ ] Early-termination counter incremented on all-clear, reset on finding
