# Nightly Reflection — Hermes Protocol

> Hermes self-improvement cycle. Runs nightly ~9 PM CT after heartbeat. 5 phases.

---

## Trigger
- Scheduled: `10 21 * * *` (after 9 PM heartbeat)
- Can also run on-demand via Hector request

---

## Phase 0 — Platform Health (FIX FIRST, before any reflection)

Before reflecting, auto-fix anything broken:

| Check | Auto-Fix Action |
|-------|----------------|
| Stale working.md files (>5KB) | Trim, archive to long-term.md |
| Missing memory tier files | Create from template |
| Skills with broken references | Flag for repair |
| Cron schedule inconsistencies | Note for human approval (Hermes doesn't auto-edit cron) |

> If Tier 4 issue found (data loss, exposed creds, child safety risk) → Telegram Hector immediately, skip remaining phases.

---

## Phase 1 — Session Transcript Review

Review what happened today:
- What corrections did Hector or Paula make? → Persist any new rules to hermes-governance.md
- What worked well? → Reinforce in skills
- What was repeated from prior mistakes? → Add hookflow-style permanent rule
- Any frustrations surfaced? → Acknowledge + fix root cause

**Output:** List of corrections applied (or "no corrections today")

---

## Phase 2 — Family State Snapshot

Gather current state across domains:

| Domain | What to Check |
|--------|--------------|
| NICU/Twins | Leo/Mia status, any discharge updates, adjusted age progression |
| Paula | Pump output trends, postpartum recovery notes |
| HJ | School/daycare schedule, any pickup confirmations outstanding |
| Bella | Last feeding, vet appointment status, any baby-intro progress |
| Home | Maintenance tasks due, seasonal flags, nursery readiness |
| Health | Any upcoming appointments, medication reminders pending |

---

## Phase 3 — Pattern Recognition

Look for patterns across the week:
- Recurring reminders that aren't being acted on → reframe or escalate
- Proposals sent to Hector 2x without response → drop or reframe (never repeat unchanged)
- Working memory files that have grown bloated → trim
- Domain overlaps with OG agent or Pi → clarify boundaries if confusion arose

---

## Phase 4 — Improvement Proposals

Generate 2–4 proposals for Hector, rated by effort/impact:

Format:
```
📋 PROPOSAL: [Title]
Impact: High/Medium/Low | Effort: Low/Medium/High
[1-2 sentence description]
[Concrete next step]
```

**Rules:**
- Never propose something already declined or ignored twice
- Proposals must be actionable, not abstract
- Include at least one "quick win" (Low effort, Medium+ impact)

---

## Phase 5 — Nightly Report to Hector

Send via Telegram (with speak param):

```
🌙 Hermes nightly — [date]

✅ [Top win or observation today]
⚠️ [One flag or heads-up if any]
📋 [1-2 proposals if any]

Tomorrow: [One proactive note — appointment, reminder, etc.]
```

**Rules:**
- Max 5 lines unless Hector asked for detail
- Result-first, no narration
- Skip if genuinely nothing notable ("quiet day" is fine to say in 1 line)

---

## Memory Update After Reflection

After completing all phases:
1. Update relevant working.md files with state changes
2. Append significant events to events.log
3. Write any new permanent rules to hermes-governance.md
4. Commit to git: `fix: nightly reflection — [date] corrections applied`

---

## Quiet Hours Guard
- Never run reflection messaging during 10 PM – 6 AM CT unless Phase 0 escalation
- Reflection computation can run anytime; only messaging respects quiet hours
