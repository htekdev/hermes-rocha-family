---
name: skill-optimizer
description: Use when auditing skills for orphaned references, bloat, duplication, or outdated content. Keeps the Hermes skill library lean and well-organized.
version: 2.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, skills, optimization, maintenance]
    related_skills: [context-auditor, platform-manager, memory-architecture]
---

# Skill Optimizer Skill

## Overview
Keep Hermes skills lean, non-redundant, and well-organized. Prevent knowledge drift and bloat.

## When to Use
- Weekly scan (Sunday alongside context audit)
- After adding multiple new skills
- When context auditor flags redundancy/bloat
- Post-migration cleanup (flat .md → SKILL.md)

## Quality Signals to Monitor

### Orphaned References
- Skills that reference other skills that no longer exist
- Cron entries pointing to removed skills
- Memory references to outdated family facts

### Bloated Skills
- Single SKILL.md file >15KB → split by domain
- Repeated content across 3+ skills → extract to shared base skill

### Outdated Skills
- Skills referencing past events as future (dates passed)
- Skills with placeholder values never filled in
- Skills imported from source repo but not adapted to Rocha family context

### Format Issues
- Flat `.md` skills not yet migrated to `subdirectory/SKILL.md` format
- Skills missing required frontmatter fields
- Skills where description doesn't start with "Use when"

### Missing Skills
- Domains with no skill coverage
- Agents with no corresponding Hermes skill

## Optimization Actions
| Finding | Action |
|---------|--------|
| Orphaned ref | Fix reference or remove dead link |
| Bloat >15KB | Propose split, await approval |
| Duplication in 3+ files | Extract to shared skill, update refs |
| Stale dates | Auto-fix unambiguous cases |
| Flat .md skill | Migrate to subdirectory/SKILL.md |
| Missing frontmatter | Add frontmatter inline |
| Missing domain | Create skeleton skill |

## Skill Count Tracking (as of Session 18)
- Total SKILL.md files: 58+ (Sessions 1-17) + 19 migrations (Session 18) = 77+
- Flat .md files: Being migrated this session

## Scheduled Review
- Weekly: scan all skills in `skills/home-assistant/`
- Log findings to progress.md
- Auto-fix safe issues (stale dates, typos, dead paths, format fixes)
- Report summary in Telegram after Sunday audit

## Never Touch
- constitution/SKILL.md or standing-orders/SKILL.md content (propose only)
- Family medical or financial data
- Skill files mid-session (defer until idle)

## Common Pitfalls
- Deleting a flat .md before migrating its content to SKILL.md
- Editing constitution directly (must propose)
- Auto-fixing ambiguous stale dates

## Verification Checklist
- [ ] All flat .md skills have SKILL.md counterpart before deletion?
- [ ] No auto-fixes applied to constitution or standing-orders?
- [ ] Findings reported in progress.md?
- [ ] SKILL.md format validated (frontmatter + sections)?

*Last updated: 2026-06-03 | Migrated to SKILL.md format (Session 18)*
