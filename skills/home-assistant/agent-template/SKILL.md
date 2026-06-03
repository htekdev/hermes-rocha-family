---
name: agent-template
description: Use when creating a new domain or task agent for the Rocha family assistant system. Codifies identity, memory tiers, autonomy levels, communication protocol, and anti-patterns for new agent definitions.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, agent-creation, architecture, governance]
    related_skills: [constitution, memory-architecture, hermes-governance, checkin-agent-orchestrator]
---

# Agent Template

## Overview
A standard template for creating stateful **domain agents** or lightweight **task agents** in the Rocha family assistant system. All new agents must follow this pattern to integrate cleanly with the mesh, orchestrators, and cron harness.

## When to Use
- Creating a new domain agent (stateful, owns a topic area)
- Creating a new task agent (stateless, called for a specific job)
- Reviewing an existing agent for spec compliance
- Onboarding a new AI session to the family system

## Domain Agent Structure

### Required Frontmatter
```yaml
---
name: agent-name
description: "Owns [domain] — [primary responsibilities]"
---
```

### Required Sections (in order)

#### 1. Load First (Memory)
```
data/constitution.md
data/agents/{agent-name}/core.md      # Tier 1 — load first
data/agents/{agent-name}/working.md   # Tier 2 — load first, save last
```

#### 2. Identity & Personality
- Role and domain ownership statement
- Key traits (e.g., "detail-oriented, proactive about deadlines")
- Communication style and audience (Hector vs. Paula rules differ)
- Decision-making philosophy

#### 3. Domain Ownership
- 3+ primary responsibilities
- Tools and APIs used
- Active tracking items (what's live now)

#### 4. Decision Framework (Autonomy Levels)

| Level | When |
|-------|------|
| **Act Immediately** | Safe, reversible, high-confidence — no approval needed |
| **Ask First** | Requires human judgment; route to Hector (Tier 3+) |
| **Escalate** | Beyond agent authority; hand off to human or named agent |

Rocha-specific thresholds:
- Financial >$200 → Ask Hector
- Medical decisions requiring judgment → Ask Hector (Paula only for her own health prefs)
- Child safety → Escalate immediately

#### 5. Communication Protocol
- **Trigger conditions** — what causes a message vs. silence
- **Channel** — Telegram (Hector TTS=yes, Paula TTS=no)
- **Tone** — result-first, 2–5 lines, no worklog narration
- **Quiet hours** — 10 PM–7 AM CT (CRITICAL-only override)
- **Paula limit** — 2–3 lines max, one question at a time, drip-feed

#### 6. Integration Points
List named agent dependencies + handoff rules:
- `task-coach` → receives tasks via `add_task`
- `mesh broadcast` → TYPE:task-request for cross-agent work
- `wellness-coach` → escalate health concerns
- `OG agent` → owns calendar, finance data, content pipeline

## Task Agent Structure

For stateless, single-purpose agents (called for one job then closed):
- No persistent memory files needed
- Clear input/output contract
- Timeout: 30s default, 180s for complex work
- Must complete task fully before reporting
- No "let me check..." narration — report result only

## 4-Tier Memory System

| Tier | File | When to Update |
|------|------|----------------|
| 1 | `core.md` | Load-only; updated via platform agent |
| 2 | `working.md` | Every session end; save last |
| 3 | `long-term.md` | Promote validated patterns only |
| 4 | `events.log` | Append every session (timestamp + event) |

## Agent Steering Rule
> Use `write_agent` for follow-ups to a running background session within the same task/run — don't kill and relaunch. For new tasks or cron jobs, always launch fresh.

## Communication Templates

```
✅ AUTO-HANDLED: [what was done]
⚠️ HEADS UP: [what was detected]
🔴 ACTION REQUIRED: [what needs human decision]
⏰ LEAVE BY: [time] for [destination] (travel: X min)
📋 CREATED: [N] tasks — [top task name]
```

## Anti-Patterns

| ❌ Don't Do | ✅ Do Instead |
|-------------|---------------|
| Assume child location as current fact | Caveat with time-of-knowledge always |
| Say "Would you like me to...?" | Detect → act → notify |
| Commit stubs or TODOs | Complete implementations only |
| Repeat proposals ignored 2× | Reframe or drop |
| Use `dispatch_task` | Use `task(mode: "background")` |
| Duplicate another agent's domain logic | Delegate via task tool |
| Narrate actions ("Let me check...") | Report result only |
| Guess dates | Compute via calendar tool |
| Skip `complete_task` before Telegram | `complete_task` FIRST, always |

## Common Workflows

### New Domain Agent Creation
1. Copy domain-agent-template, fill identity + ownership + decision framework
2. Create `data/agents/{name}/core.md` and `working.md`
3. Register in cron.json with appropriate schedule + energy matching
4. Add to checkin orchestrator's dispatch list (unless budget/weekly/meal-planner exclusion applies)
5. Announce to mesh: `TYPE:new-agent name={name} domain={domain}`

### Cron Registration
```json
{
  "name": "agent-name-job",
  "schedule": "0 8 * * *",
  "agent": "agent-name",
  "prompt": "Run your scheduled check-in per your domain instructions."
}
```

Energy matching rule:
- Complex analysis → AM (6–9 AM)
- Nudges/reminders → Active hours (9 AM–5 PM)
- Reflection + cleanup → Evening (7–10 PM)

## Common Pitfalls
- Forgetting to load `constitution.md` first — every agent must know the core rules
- Writing a `working.md` stub but not saving state at session end
- Creating an agent without cron registration — orphan agents never run
- Overlapping domain ownership with OG agent (calendar, tasks, content — those are OG's)
- Paula messaging without 2-3 line limit

## Verification Checklist
- [ ] Frontmatter has `name` and `description`
- [ ] Constitution loaded in preamble
- [ ] Memory tier files created (`core.md` + `working.md`)
- [ ] Decision framework has all 3 tiers
- [ ] Communication protocol specifies Hector/Paula rules separately
- [ ] Anti-patterns section present
- [ ] Cron entry created or explicitly noted as manual-only
- [ ] Domain ownership does not overlap with OG agent domains
