# Platform Manager — Hermes Self-Improvement Skill

## Core Philosophy
**Detect → Fix → Report** (not Detect → Report → Wait → Fix)

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
- Every skill must have: purpose, behaviors, output format, integration points
- Every cron job must have: schedule, description, expected output
- Memory files must not exceed 5KB (trim working memory proactively)
