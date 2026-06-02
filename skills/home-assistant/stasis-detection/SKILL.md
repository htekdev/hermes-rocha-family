---
name: stasis-detection
description: Use when deciding whether an agent or cron job should exit early due to inactivity. Governs the stasis detection pattern — cost-saving mechanism for idle agents/projects that suppresses cron runs when no progress has been made for 5+ consecutive days.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, platform, cost-optimization, cron, governance]
    related_skills: [platform-manager, cron-patterns, hermes-governance, context-auditor]
---

# Stasis Detection

## Overview
The stasis detection pattern prevents idle agents from consuming tokens unnecessarily. When a project, agent, or task domain has no new inputs, no progress, and no open work items for 5+ consecutive days, the agent logs the stasis event, increments a counter, and exits within ≤2 turns without doing work.

## When to Use
- Any cron-driven agent that checks a project or domain
- Evaluating whether to skip a heartbeat run
- Platform manager nightly reflection — filter out stale agents
- Cost review — identify agents accumulating idle runs

## Stasis Trigger Conditions
All of the following must be true:
1. `stasis_consecutive_days >= 5`
2. No new user input for the domain
3. No open tasks with approaching deadlines
4. No external events (API changes, alerts, calendar triggers)

If ANY condition is false → run normally.

## Stasis Protocol (When Triggered)

```
1. Log: "Stasis day N — no new input. Skipping."
2. Append to events.log: {timestamp, agent, event_type: "stasis", stasis_day: N}
3. Increment stasis_consecutive_days in working.md
4. EXIT (≤2 turns total)
5. Do NOT send Telegram notification (silent skip)
```

## Working Memory Format

Add this section to any domain's `working.md`:

```markdown
## Stasis Tracking
- stasis_consecutive_days: 0
- last_active: YYYY-MM-DD
- stasis_triggered: false
- last_reset_reason: [brief description]
```

## Reset Conditions
Reset `stasis_consecutive_days = 0` when:
- New user message received for this domain
- External event triggers (bill due, appointment, etc.)
- Manual override from Hector
- Scheduled forced-run day (e.g., monthly reviews always run)

## Agent File Format

Add this section to any agent's definition file:

```markdown
## Stasis Detection
- Trigger: stasis_consecutive_days >= 5 AND no new input
- Action: log → increment → EXIT (≤2 turns)
- Reset: any new input or external event
- Never: send Telegram on stasis skip (silent)
```

## Known Stasis Agents (Source Reference)
From htekdev/copilot-home-assistant standing-orders:
- `carplay` — 21+ days stasis
- `milk-mama` — 14+ days stasis

## Hermes Application
Hermes should apply stasis detection to:
- `teacher` domain — formal curriculum suspended during Paula's recovery
- `content-awareness` — only active when OG flags content opportunity
- Any working.md with no updates in 7+ days → flag in context-auditor scan

## Common Pitfalls
- ❌ Triggering stasis on family-critical domains (health, twins, Bella) — these always run
- ❌ Resetting counter without logging the reset reason
- ❌ Sending Telegram on stasis skip — it should be completely silent
- ❌ Applying stasis to heartbeat/mesh check-in — these always run regardless
- ❌ Counting weekends as stasis days for work-calendar agents

## Verification Checklist
- [ ] Stasis counter in working.md for applicable agents
- [ ] Exit happens in ≤2 turns when triggered
- [ ] No Telegram sent on stasis skip
- [ ] Reset reason logged when stasis_consecutive_days resets to 0
- [ ] Critical-domain agents (health, NICU, dogs) excluded from stasis eligibility
