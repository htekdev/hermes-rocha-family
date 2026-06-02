# Memory Architecture — Rocha Family Hermes

## Overview
4-tier memory system adapted from copilot-home-assistant for Hermes.

## Tier Structure

### Tier 1: Core Identity (`core.md`)
- Agent's permanent identity, values, domain ownership
- Rarely changes — only when fundamental role shifts
- Location: `~/.hermes/skills/home-assistant/{agent}/core.md`

### Tier 2: Working Memory (`working.md`)
- Current state: active tasks, in-progress items, recent decisions
- Updated every session
- Max 5KB — trim aggressively, promote patterns to long-term.md
- Location: `~/.hermes/skills/home-assistant/{agent}/working.md`

### Tier 3: Long-term Patterns (`long-term.md`)
- Validated patterns, repeated behaviors, learned preferences
- Promoted from working.md when confirmed 2+ times
- Location: `~/.hermes/skills/home-assistant/{agent}/long-term.md`

### Tier 4: Event Stream (`events.log`)
- Chronological append-only log of significant events
- Format: `[YYYY-MM-DD HH:MM CT] EVENT_TYPE: description`
- Location: `~/.hermes/skills/home-assistant/{agent}/events.log`

## Read/Write Protocol

### Session Start (Read Order):
1. Constitution → standing-orders → relevant domain skill
2. core.md (Tier 1) → working.md (Tier 2) for current context
3. Relevant long-term.md patterns

### Session End (Write Order):
1. Update working.md with new state
2. Append to events.log
3. Promote any confirmed patterns → long-term.md
4. If working.md > 5KB → trim oldest items, promote or archive

## Memory Promotion Rules
- Pattern seen once → working.md note
- Pattern confirmed 2x → promote to long-term.md
- Pattern critical/safety → promote immediately to constitution.md or standing-orders.md

## Hermes Agent Memory Files (Implement Progressively)
```
~/.hermes/skills/home-assistant/
  ├── family-coordinator/
  │   ├── core.md
  │   ├── working.md
  │   ├── long-term.md
  │   └── events.log
  ├── health-coach/
  │   └── [same structure]
  ├── finance-manager/
  │   └── [same structure]
  └── [other agents]/
```

## Working Memory Template
```markdown
# [Agent] Working Memory — Updated [DATE]

## Active Context
- [Current priorities, pending items]

## Recent Decisions
- [YYYY-MM-DD] Decision made + rationale

## Pending Clarifications
- [Items waiting on family input]

## Watchlist
- [Items to monitor next session]
```

## Cross-Agent Context Sharing
- Agents share via mesh messages (broadcast or direct)
- Critical context (safety, medical, child location) → share immediately
- Routine context → share in session-end broadcast
- Never duplicate full datasets — reference by pointer (e.g., "see finance-manager working.md")
