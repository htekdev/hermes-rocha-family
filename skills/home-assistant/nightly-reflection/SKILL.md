---
name: nightly-reflection
description: Use when performing the end-of-day Hermes reflection cycle. Runs 5-phase protocol to fix issues, review transcripts, gather data, recognize patterns, and submit proposals.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, platform, nightly, reflection]
    related_skills: [platform-manager, context-auditor, standing-orders, hermes-governance]
---

# Nightly Reflection

## Overview
End-of-day 5-phase reflection protocol. Detects behavioral drift, extracts patterns from the day's interactions, and generates proposals for Hermes improvement. Runs nightly ~10 PM CT (before quiet hours) or early morning ~5 AM CT.

## When to Use
- Nightly scheduled cron job
- After significant family events (discharge, medical appointments)
- When proposal backlog exceeds 3 unreviewed items

## 5-Phase Protocol

### Phase 0 — Fix First (MANDATORY)
Before anything else, check for open issues:
- Broken skills or failed mesh messages
- Stale working.md files (7+ days unchanged = flag)
- Failed cron jobs in last 24h
- Any `status:blocked` items

**Rule**: Fix what you can silently. If Tier 3+ fix needed → task for Hector. **Never proceed through phases while a critical issue is open.**

### Phase 1 — Transcript Review
- Review today's Telegram messages sent/received
- Review mesh messages exchanged
- Flag: missed alerts, incorrect information, tone failures, TTS mistakes
- Check Paula message compliance (2-3 lines max, no TTS, no rapid-fire)
- Check Hector message compliance (speak param present)

### Phase 2 — Data Gather
- Refresh working.md files with today's known facts
- Update wellness-coach/working.md if pump/BP data available
- Update parenting-coach/working.md with HJ observations
- Update nicu-care/SKILL.md status if Mia updates received
- Append to events.log: `[timestamp] | hermes | nightly-reflection | Phase 2 complete`

### Phase 3 — Pattern Recognition
Scan today's interactions for:
- **Recurring mistakes** → candidate for new standing order or hookflow
- **Missed proactive actions** → candidate for cron job
- **Stale proposals** (proposed 2x, no action) → reframe or drop, NEVER repeat unchanged
- **Domain overlap** with OG agent → clarify boundary if needed

### Phase 4 — Proposals
Generate improvement proposals if patterns found:
- Format: `## Proposal: [title]` + rationale + specific change
- Save to `~/.hermes/copilot-ha-study/proposals.md`
- Do NOT implement without acknowledgment (Tier 3 decisions)
- Max 3 new proposals per night (avoid proposal flood)

### Phase 5 — Report
If anything meaningful found:
- Single Telegram to Hector: "🌙 Nightly reflection complete. [N issues fixed] | [M proposals queued] | [Notable pattern]"
- If all-clear: **SILENT** (no message)

## Proposal Hygiene
- Track each proposal's submission count in proposals.md
- `count >= 2` AND no response → reframe or drop
- Never submit same wording twice
- Proposals queue is reviewed Sunday during weekly-planner run

## Common Pitfalls
- **Running phases out of order**: Phase 0 must run first — unresolved issues corrupt pattern analysis
- **Generating too many proposals**: Max 3/night; quality over quantity
- **Sending nightly message during quiet hours**: Buffer until 7 AM if reflection runs late
- **Repeating dropped proposals**: Once dropped, start fresh with different framing or different solution

## Verification Checklist
- [ ] Phase 0 complete: no open critical issues
- [ ] All working.md files checked for staleness
- [ ] events.log appended
- [ ] Proposals.md updated (or no new proposals)
- [ ] Telegram message sent only if actionable (silent if all-clear)
- [ ] No repeated proposals from prior nights
