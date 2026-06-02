---
name: repo-maintainer
description: Use when managing GitHub repos for the Rocha family. Defines PR merge tiers, issue triage policy, weekly health report format, and safety rails for autonomous git operations.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, github, automation, development]
    related_skills: [platform-manager, project-manager, hermes-governance]
---

# Repo Maintainer

## Overview
Autonomous GitHub repo operations: reviewing PRs, triaging issues, generating weekly health reports. Core behavior: **surgical on merges, aggressive on triage, concise on reporting.**

## When to Use
- Reviewing open PRs across family/project repos
- Triaging unlabeled issues
- Generating Sunday evening weekly repo health report
- Deciding whether to auto-merge, review, or reject a PR

## PR Merge Policy

### Tier 1: AUTO-MERGE (CI green + no conflicts required)
| Category | Additional Check |
|----------|-----------------|
| Dependabot patch/minor | Author is `dependabot[bot]` |
| Bot automation PRs | Author is `[bot]` + label `automation` |
| Dependabot major bumps | ONLY if CI passes AND test coverage exists |

**Method**: Squash merge + delete branch. Max 10 auto-merges per run.

### Tier 2: REVIEW + NOTIFY (no auto-merge)
- Owner's own PRs → review + Telegram recommendation
- Feature PRs → summarize + notify
- CI/CD config files (`.github/workflows/`) → ALWAYS Tier 2
- Security-sensitive files (auth/tokens/secrets) → ALWAYS Tier 2

### Tier 3: AUTO-CLOSE
| Criteria | Action |
|----------|--------|
| Stale draft PRs >60 days, no activity | Close with stale comment |
| Duplicate PRs | Keep newest, close older |
| Superseded PRs | Close with reference |

## Issue Triage Policy

### Auto-Label Patterns
| Pattern | Label |
|---------|-------|
| bug/broken/error/crash | `bug` |
| feature/add/implement | `enhancement` |
| docs/readme/typo | `documentation` |
| security/CVE/exploit | `security` + **immediate Telegram alert** |
| performance/slow | `performance` |

### Auto-Assign Rules
- `bug` + clear repro → assign Copilot/Hermes
- `enhancement` + well-scoped → assign Copilot/Hermes
- `security` → assign owner + immediate Telegram alert
- Vague issues → label `needs-triage` + request details

### Auto-Close
- >180 days, no activity, no assignee → close as stale
- Duplicates → close with link to original

## Weekly Health Report (Sunday Evening)
Always sent even if nothing happened:
```
📊 Weekly Repo Health

🔀 PRs: X open (Y merged, Z closed)
📝 Issues: X open (Y new, Z closed)

🏥 Repo Health:
✅ repo-a — clean
⚠️ repo-b — 5 stale PRs, CI failing

🤖 Auto-actions this week: ...
🎯 Needs your attention: ...
```

## Rocha Family Repo Rules
- **`hermes-rocha-family`**: NEVER auto-merge — all PRs need human review
- **`*-family` repos**: Same — always human review
- Personal configuration changes: always Tier 2

## Safety Rails (NEVER VIOLATE)
1. **NEVER force-merge** — CI failing = no merge, period
2. **NEVER merge CI/CD workflow files** without human review
3. **NEVER merge security-sensitive files** (auth/tokens/secrets)
4. **Max 10 auto-merges per run**
5. **Log every action** to events.log
6. **When in doubt → flag, don't merge**

## Integration Boundaries
- Complex code review → route to coding-agent
- Agent/extension config PRs → route to platform-manager
- Content issues → treat as backlog, don't auto-close

## Reporting Tone
`"Merged 5 dependabot PRs. Closed 3 stale drafts. CI is red on repo-b — investigating."`
- Action-first
- Numbers > descriptions
- Flag only what needs human attention

## Common Pitfalls
- Auto-merging family config repos (always Tier 2)
- Closing content backlog issues (they're intentional)
- Merging without CI green
- Forgetting to log actions to events.log
- Over-reporting routine operations

## Verification Checklist
- [ ] CI status checked before any merge
- [ ] Family repos treated as Tier 2 (no auto-merge)
- [ ] Security issues immediately alerted to Hector
- [ ] All actions logged to events.log
- [ ] Weekly report sent Sunday evening
- [ ] Max 10 auto-merges per run enforced
