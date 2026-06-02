# Context Auditor Skill
*Adapted from htekdev/copilot-home-assistant — context-auditor.agent.md*

## Purpose
Quality assurance for all Hermes context and knowledge files. Detects contradictions, staleness, bloat, redundancy, and skill extraction opportunities.

## Audit Scope (4 Tiers)
| Tier | Priority | Files |
|------|----------|-------|
| 1 | Highest | constitution.md, standing-orders.md |
| 2 | High | skills/home-assistant/*.md |
| 3 | Medium | memories/, working context |
| 4 | Medium | cron schedules, family data files |

## What to Look For

### 🔴 Contradictions (Critical)
- Cross-document rule conflicts
- Quiet hours discrepancies
- Cron violations
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
- Working memory >5KB → promote validated patterns to long-term

### 🟡 Skill Extraction (Medium)
- Procedures >500 tokens used by 2+ agents → extract to shared skill

### 🟢 Missing Context (Low-Med)
- No escalation policy defined
- No quiet hours specified for notification agents

## Auto-Fix Policy

**Fix immediately:**
- Stale dates with unambiguous correct value
- Typos in names/paths
- Exact-duplicate paragraphs
- Broken file path references

**Create task (needs approval):**
- Constitution ↔ skill rule contradictions
- Proposed skill extractions
- Removing large context sections
- Cron schedule changes
- Any edit to constitution.md or standing-orders.md

**Never touch:**
- constitution.md, standing-orders.md (propose only)
- Family medical/financial data
- Production configs without approval

## Report Format
- 🔴 Critical | 🟡 Warning | 🟢 Info | ✅ Auto-fixed
- Full audit: weekly (Sunday)
- Quick scan: daily (quiet unless critical)
- Quiet hours 10 PM–6 AM CT

## Trigger Schedule (Recommended)
- Daily quick scan: 6 AM CT
- Weekly full audit: Sunday 11 PM CT
