# Skill Optimizer Skill
*Adapted from htekdev/copilot-home-assistant — skill-optimizer pattern*

## Purpose
Keep Hermes skills lean, non-redundant, and well-organized. Prevent knowledge drift and bloat.

## Quality Signals to Monitor

### Orphaned References
- Skills that reference other skills that no longer exist
- Cron entries pointing to removed skills
- Memory references to outdated family facts

### Bloated Skills
- Single skill file >15KB → split by domain
- Repeated content across 3+ skills → extract to shared base skill

### Outdated Skills
- Skills referencing past events as future (dates passed)
- Skills with placeholder values never filled in
- Skills imported from source repo but not adapted to Rocha family context

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
| Placeholder text | Flag for Hector to fill in |
| Missing domain | Create skeleton skill |

## Scheduled Review
- Weekly: scan all skills in ~/.hermes/skills/home-assistant/
- Log findings to progress.md
- Auto-fix safe issues (stale dates, typos, dead paths)
- Report summary to Hector on Telegram

## Never Touch
- constitution.md or standing-orders.md content (propose only)
- Family medical or financial data
- Skill files mid-session (defer until idle)
