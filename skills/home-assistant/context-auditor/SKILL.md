---
name: context-auditor
description: Use when auditing skills, memories, or working files for contradictions, staleness, bloat, or redundancy. QA agent for all Hermes knowledge files.
version: 2.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, quality, audit, maintenance]
    related_skills: [platform-manager, skill-optimizer, memory-architecture]
---

# Context Auditor Skill

## Overview
Quality assurance for all Hermes context and knowledge files. Detects contradictions, staleness, bloat, redundancy, and skill extraction opportunities.

## When to Use
- Daily quick scan cron (6 AM CT — silent unless critical)
- Weekly full audit (Sunday 8 PM CT)
- After a major update or working.md age exceeds 7 days
- After any family event that changes key facts

## Audit Scope (4 Tiers)
| Tier | Priority | Files |
|------|----------|-------|
| 1 | Highest | constitution/SKILL.md, standing-orders/SKILL.md |
| 2 | High | skills/home-assistant/*/SKILL.md |
| 3 | Medium | */working.md |
| 4 | Medium | cron schedules, family data files |

## What to Look For

### 🔴 Contradictions (Critical)
- Cross-document rule conflicts
- Quiet hours discrepancies
- Domain ownership conflicts between agents/skills

### 🟡 Stale Info (High)
- Passed dates still referenced as future
- Working memory not updated in 7+ days
- References to deleted agents or files

### 🟡 Redundancy (Medium)
- Same rule/fact in 3+ places → single source of truth
- Duplicate procedures across skills

### 🟡 Bloat (Medium)
- Skill files >15KB → split or trim
- Working memory >5KB → promote validated patterns

### 🟢 Format Issues (Low-Med)
- Flat `.md` skills that should be `subdirectory/SKILL.md`
- Skills missing required frontmatter or sections

## Auto-Fix Policy

**Fix immediately:**
- Stale dates with unambiguous correct value
- Typos in names/paths
- Exact-duplicate paragraphs
- Broken file path references
- Flat .md skills → migrate to SKILL.md format

**Create task (needs approval):**
- Constitution ↔ skill rule contradictions
- Proposed skill extractions
- Removing large context sections
- Cron schedule changes

**Never touch:**
- constitution/SKILL.md, standing-orders/SKILL.md (propose only)
- Family medical/financial data
- Production configs without approval

## Report Format
- 🔴 Critical | 🟡 Warning | 🟢 Info | ✅ Auto-fixed
- Full audit: weekly (Sunday)
- Quick scan: daily (quiet unless critical)

## Common Pitfalls
- Auditing constitution.md directly (propose only)
- Missing working.md staleness (7+ day threshold)
- Not checking for flat .md skills that need migration

## Verification Checklist
- [ ] Contradictions checked across tiers?
- [ ] Working.md files <7 days old?
- [ ] All skills in subdirectory/SKILL.md format?
- [ ] Flat .md skills identified for migration?
- [ ] Auto-fixes applied only to safe items?

*Last updated: 2026-06-03 | Migrated to SKILL.md format (Session 18)*
