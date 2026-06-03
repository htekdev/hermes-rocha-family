---
name: platform-manager
description: Use when performing self-improvement, nightly reflection, cron health checks, or skill maintenance. Detect→Fix→Report cycle with 4-tier decision framework.
version: 2.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, platform, self-improvement, maintenance]
    related_skills: [context-auditor, skill-optimizer, constitution, hermes-governance]
---

# Platform Manager Skill

## Overview
Self-improvement, system health, and nightly reflection for Hermes. Core philosophy: **Detect → Fix → Report** (never Detect → Report → Wait → Fix).

## When to Use
- Nightly reflection cron (9 PM CT)
- Finding a cron/skill/memory issue
- Receiving a correction from Hector
- Platform health scan

## Decision Tiers

### Tier 1 — Auto-Fix Immediately (no confirmation needed)
- Broken or misconfigured cron entries
- Stale memory files
- Duplicate tasks
- JSON syntax errors
- Orphaned skill references

### Tier 2 — Act Then Report (medium confidence)
- Bloated skill/memory refactors
- New cron prompts
- Fixing deprecated references in skills
- Creating missing memory files

### Tier 3 — Propose First (requires Hector's approval)
- New domain agents/skills
- Significant skill instruction refactors
- Core standards changes (constitution, standing-orders)
- Removing or disabling skills or cron jobs
- Architectural changes

### Tier 4 — Escalate Immediately
- Exposed secrets / broken auth
- Data loss risk
- Multiple systems failing simultaneously

## Nightly Reflection Pattern (5 Phases)
1. **Active Maintenance** — cron health, task hygiene, memory health
2. **Transcript Review** — frustrations, decisions, corrections from the day
3. **Data Gathering** — tasks, calendar, bills, budget
4. **Reflection** — what went well/poorly, patterns
5. **Improvement Proposals** — 3-5 specific proposals with effort/impact rating → send to Hector

> Proposals ignored twice → reframe or drop. Never repeat same proposal unchanged.

## Implementation Rules
1. Read before writing — always read current file first
2. No stubs or TODOs — every change must be complete
3. Respect domain boundaries — don't inline another domain's logic
4. Use conventional commits: `feat:`, `fix:`, `refactor:`, `docs:`
5. Every correction is permanent — save learnings to memory

## Quality Gates
- Every skill must have: proper SKILL.md format with frontmatter
- Every cron job must have: schedule, description, expected output
- Memory files must not exceed 5KB (trim working memory proactively)
- Skills must be in `subdirectory/SKILL.md` format (not flat `.md`)

## Common Pitfalls
- Waiting for Hector to fix something Hermes can fix autonomously
- Repeating the same proposal without reframing
- Editing constitution.md or standing-orders.md directly (propose only)

## Verification Checklist
- [ ] Fix applied before reporting?
- [ ] Tier evaluated before acting?
- [ ] Proposals rated by effort/impact?
- [ ] Corrections persisted to memory/skills?

*Last updated: 2026-06-03 | Migrated to SKILL.md format (Session 18)*
