---
name: memory-architecture
description: Use when designing, reading, or writing to Hermes memory tiers. Defines the 4-tier memory system, read/write protocol, and working memory limits.
version: 2.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, memory, architecture, context]
    related_skills: [platform-manager, context-auditor, skill-optimizer]
---

# Memory Architecture Skill

## Overview
4-tier memory system for Hermes. Adapted from htekdev/copilot-home-assistant architecture.

## When to Use
- Starting any domain session (read order)
- Ending any domain session (write order)
- Working.md exceeds 5KB (trim time)
- Pattern confirmed twice (promotion time)

## Tier Structure

### Tier 1: Core Identity (`SKILL.md`)
- Agent's permanent rules, domain ownership, behavioral standards
- Rarely changes — only when fundamental role shifts
- Location: `skills/home-assistant/{agent}/SKILL.md`

### Tier 2: Working Memory (`working.md`)
- Current state: active tasks, in-progress items, recent decisions
- Updated every session
- **Max 5KB** — trim aggressively; promote patterns to long-term
- Location: `skills/home-assistant/{agent}/working.md`

### Tier 3: Long-term Patterns (`long-term.md`)
- Validated patterns, repeated behaviors, learned preferences
- Promoted from working.md when confirmed 2+ times
- Location: `skills/home-assistant/{agent}/long-term.md`

### Tier 4: Event Stream (`events.log`)
- Chronological append-only log of significant events
- Format: `[YYYY-MM-DD HH:MM CT] EVENT_TYPE: description`
- Location: `data/agents/events.log`

## Read/Write Protocol

### Session Start (Read Order)
1. Constitution → standing-orders → family-profile
2. SKILL.md (Tier 1) → working.md (Tier 2)
3. Relevant long-term.md patterns if needed

### Session End (Write Order)
1. Update working.md with new state
2. Append to events.log
3. Promote confirmed patterns → long-term.md
4. If working.md >5KB → trim oldest, promote or archive

## Memory Promotion Rules
- Pattern seen once → working.md note
- Pattern confirmed 2x → promote to long-term.md
- Pattern critical/safety → promote immediately to constitution/standing-orders (propose only)

## Current Active Memory Files
```
skills/home-assistant/
  ├── family-coordinator/working.md ✅
  ├── health-coach/working.md ✅
  ├── wellness-coach/working.md ✅
  ├── dog-parent/working.md ✅
  ├── parenting-coach/working.md ✅
  ├── finance-manager/working.md ✅
  └── home-manager/working.md ✅
data/agents/events.log ✅
```

## Cross-Agent Context Sharing
- Share via mesh (broadcast or direct)
- Critical context (safety, medical, child location) → share immediately
- Routine context → session-end broadcast
- Never duplicate full datasets — reference by pointer

## Common Pitfalls
- Working.md exceeding 5KB without trimming
- Promoting a pattern seen only once to long-term
- Duplicating full datasets across agents instead of using pointers

## Verification Checklist
- [ ] Working.md under 5KB?
- [ ] Session-start read order followed?
- [ ] New patterns noted in working.md?
- [ ] Events.log appended with significant events?

*Last updated: 2026-06-03 | Migrated to SKILL.md format (Session 18)*
