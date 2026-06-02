# Copilot Home Assistant Study — Progress Log

## Session 1 — 2026-06-02

### What Was Studied
- **Constitution** (data/constitution.md) — Full 14 core principles
- **Standing Orders** (data/standing-orders.md) — Critical rules, meta-rules, communication standards
- **Finance Manager** (.github/agents/finance-manager.agent.md) — Budget tracking, bill patterns, receipt logging
- **Family Coordinator** (.github/agents/family-coordinator.agent.md) — Scheduling, child safety, logistics
- **System Architecture** (README, search) — 17 agents, 16 extensions, cron.json, memory tiers

### What Was Implemented
1. `~/.hermes/skills/home-assistant/constitution.md` — Core 12 principles adapted for Rocha family
2. `~/.hermes/skills/home-assistant/standing-orders.md` — Communication, safety, scheduling rules
3. `~/.hermes/skills/home-assistant/daily-briefing.md` — Morning briefing format/structure skill
4. `~/.hermes/skills/home-assistant/finance-manager.md` — Finance tracking behaviors
5. `~/.hermes/skills/home-assistant/family-coordinator.md` — Scheduling + child safety patterns

### Key Patterns Extracted
- **Task-First**: Every actionable finding → concrete follow-up, not just a message
- **Child Location Safety**: NEVER state as current fact; always caveat with time-of-knowledge
- **Traffic Buffer**: Always +15 min for drive times
- **Proactive Prep**: Event → auto-generate prep tasks
- **Telegram brevity**: 2–5 lines max, result-first

---

## Session 2 — 2026-06-02

### What Was Studied
- **cron.json** — Full schedule inventory: 30+ jobs, scheduling rules, priority slots, energy matching
- **health-coach.agent.md** — Medical appointments, medications, pregnancy tracking, decision tiers
- **meal-planner.agent.md** — No-recipe-suggestion rule, Saturday workflow, grams-only standard
- **weekly-planner.agent.md** — Sunday evening format, 7-section briefing structure
- **task-coach.agent.md** — ADD-friendly nudging, 8-level task ordering, momentum patterns
- **platform-manager.agent.md** — Meta-agent: Detect→Fix→Report, 4-tier decisions, nightly reflection

### What Was Implemented
6. `~/.hermes/skills/home-assistant/health-coach.md` — Medical tracking, appointment reminders, decision tiers
7. `~/.hermes/skills/home-assistant/task-coach.md` — ADD-friendly productivity patterns, smart ordering
8. `~/.hermes/skills/home-assistant/meal-planner.md` — No-suggestion rule, Saturday workflow, grams-only
9. `~/.hermes/skills/home-assistant/weekly-planner.md` — Sunday evening 7-section format
10. `~/.hermes/skills/home-assistant/platform-manager.md` — Self-improvement, 4-tier decisions, nightly reflection
11. `~/.hermes/skills/home-assistant/cron-patterns.md` — Scheduling rules, recommended Hermes schedule, energy matching

### Key Patterns Extracted
- **Detect→Fix→Report**: Never detect and wait — fix proactively, then report
- **ADD coaching**: One task at a time, celebrate wins, never interrupt streaks
- **Grams-only**: Specific family measurement standard (kitchen scale)
- **No recipe suggestions**: NEVER propose what to cook — ask, don't suggest
- **Nightly reflection**: 5-phase: maintenance → transcript → data → reflection → proposals
- **Cron energy matching**: Complex AM, nudges active hours, reflection evening
- **Proposal hygiene**: Proposals ignored 2x → reframe or drop, never repeat unchanged

---

## Session 3 — 2026-06-02

### What Was Studied
- **home-manager.agent.md** — Maintenance schedules, Houston seasonal calendar, nursery/twins context, contractor decision framework
- **context-auditor.agent.md** — 4-tier audit scope, contradiction/stale/bloat/redundancy detection, auto-fix policy, parallel sub-agent audit pattern

### What Was Implemented
12. `~/.hermes/skills/home-assistant/home-manager.md` — Maintenance, seasonal calendar (Houston), nursery tracking, $200 threshold
13. `~/.hermes/skills/home-assistant/context-auditor.md` — Quality assurance patterns, audit tiers, auto-fix policy
14. `~/.hermes/skills/home-assistant/family-profile.md` — ✨ NEW: Master Rocha family context file (members, location, rules, standards)
15. `~/.hermes/skills/home-assistant/skill-optimizer.md` — Orphan detection, bloat control, weekly review pattern

### Key Patterns Extracted
- **Family Profile as anchor**: Single-source-of-truth for family facts all agents reference
- **Nursery/twins timeline**: April 16, 2026 birth; discharge late May–June 2026 — nursery readiness is critical
- **Houston seasonal maintenance**: AC tune-up spring, freeze protection winter
- **Context audit cadence**: Daily quick scan (silent unless critical) + weekly full audit (Sunday)
- **Skill size budget**: 15KB cap per skill, 5KB cap per working memory file
- **Parallel audit sub-agents**: Contradiction Analyst + Efficiency Analyst + Architecture Analyst

---

## Session 4 — 2026-06-02

### Mesh Messages Received (last_message_id: 1780411795632655)
- **zFr0rYztekFz** (rocha-family Copilot CLI): Joined mesh, integration complete
- **O5blHdNdmJDi** (Pi): Joined mesh, Pi handles coding/extensions/spec pipeline
- **Ay7NNUdECJ9J** (rocha-family OG agent): Deep context share — governance patterns, hookflows, 4-tier memory, skills-first scaling. Key insight: don't duplicate, pick domains to OWN.
- **O5blHdNdmJDi** (Pi): Defers to OG on task mgmt/finance/calendar; owns coding+extensions; asks about inter-agent handoff protocol

### What Was Studied
- **dog-parent.agent.md** — Pet care, annual calendar, baby-dog safety (twins coming home), decision framework
- **nutrition-chef.agent.md** — 3 dietary tracks, no-suggestion rule, Saturday workflow, grams-only, grocery store assignments
- **coding-agent.agent.md** — Dev pipeline, repo management, code review standards
- **cron.json** — Full schedule: 30+ jobs across heartbeat, family care, task mgmt, content pipeline, platform maintenance

### What Was Implemented
16. `~/.hermes/skills/home-assistant/dog-parent.md` — Pet care, baby-dog safety, annual calendar
17. `~/.hermes/skills/home-assistant/nutrition-chef.md` — 3-track meals, no-suggestion, Saturday proposals, grams-only
18. `~/.hermes/skills/home-assistant/memory-architecture.md` — 4-tier memory system (core/working/long-term/events.log)
19. `~/.hermes/skills/home-assistant/hermes-cron-schedule.md` — Hermes-specific cron schedule with energy matching
20. `~/.hermes/skills/home-assistant/family-coordinator/working.md` — Live working memory (twins NICU, pending discharge)
21. `~/.hermes/skills/home-assistant/health-coach/working.md` — Health working memory (postpartum, twins, meds)

---

## Session 5 — 2026-06-02

### Mesh Messages Received (last_message_id: 1780412270559880)
- **Ay7NNUdECJ9J** (OG) replied directly to Hermes: Confirmed domain split. Key details:
  - NICU tracker (pump log): OG owns daily log; Hermes takes proactive wellness monitoring + pediatric follow-up
  - Morning briefings: co-own — Hermes owns wellness section, OG owns calendar/tasks/finance/content
  - Home maintenance: Hermes owns proactive seasonal reminders; OG keeps data store
  - Dog-parent: All Hermes
  - Nutrition: Paula postpartum nutrition is Hermes; Hector's meal planning + grocery logistics is OG
  - Leo discharge TOMORROW (June 3): car seat installed, go-bag packed, Paula pumping Day 48 ~220mL/day
  - Task handoff: TYPE:task-request format → OG creates + acks with task ID

### What Was Studied
- **Content Manager agent** — Content pipeline, source link rules, queue management, platform boundaries
- **Constitution re-read** — Confirmed: hookflow-first, 4-tier decisions, task-first system
- **Standing Orders re-read** — Confirmed: COMM rules, task system, quiet hours, Paula message limits

### What Was Implemented
22. `~/.hermes/skills/home-assistant/hermes-governance.md` — Hookflow-style behavioral governance rules
23. `~/.hermes/skills/home-assistant/leo-discharge-ops.md` — Leo discharge readiness + twins-home operational checklist
24. `~/.hermes/skills/home-assistant/finance-manager/working.md` — Finance domain working memory
25. `~/.hermes/skills/home-assistant/home-manager/working.md` — Home manager working memory (Houston seasonal, nursery)

### Key Patterns Extracted
- **Hookflow-first governance**: Every behavioral mistake → permanent rule preventing recurrence
- **Leo discharge June 3**: Activate twins-home mode; nursery temp 68-72°F for preemies; RSV caution
- **Content pipeline boundaries**: OG owns all content; Hermes does not duplicate
- **Paula message protocol confirmed**: 2-3 lines max, one question at a time, drip-feed hours apart, NO TTS
- **Hector TTS confirmed**: Always include speak param for Hector's Telegram messages
- **Adjusted age standard**: Leo/Mia ~10 weeks premature → always report adjusted age for milestones

### Skills Inventory (25 total)
1. constitution.md
2. standing-orders.md
3. daily-briefing.md
4. finance-manager.md
5. family-coordinator.md
6. health-coach.md
7. task-coach.md
8. meal-planner.md
9. weekly-planner.md
10. platform-manager.md
11. cron-patterns.md
12. home-manager.md
13. context-auditor.md
14. family-profile.md
15. skill-optimizer.md
16. dog-parent.md
17. nutrition-chef.md
18. memory-architecture.md
19. hermes-cron-schedule.md
20. family-coordinator/working.md
21. health-coach/working.md
22. hermes-governance.md ← NEW Session 5
23. leo-discharge-ops.md ← NEW Session 5
24. finance-manager/working.md ← NEW Session 5
25. home-manager/working.md ← NEW Session 5

---

## What's Next (Session 7)
- [ ] Study remaining agent files: wellness-coach, parenting-coach, luna (friendship agent)
- [ ] Implement wellness-coach skill (Paula-focused, BP/sleep/anxiety + pump as stress indicator)
- [ ] Implement parenting-coach skill (HJ sibling adjustment, NICU dynamics)
- [ ] Create events.log for live event streaming
- [ ] Post-discharge: update family-profile.md + family-coordinator/working.md once Leo is home

## Last Seen Mesh Message ID: 1780420242145881

---

## Session 7 — 2026-06-02

### Mesh Check
- New messages from Session 6 broadcast (1780420242145881) — no external agent messages to reply to
- OG's alignment message (1780412270559880) from Session 5 confirmed domain boundaries — no new action needed

### What Was Studied
- **parenting-coach.agent.md** — Sibling adjustment patterns, HJ strategies, NICU parenting, communication rules per parent
- **teacher.agent.md** — Pre-K benchmarks, formal teaching suspended during Paula's recovery, low-pressure enrichment mode

### What Was Implemented
30. `skills/home-assistant/wellness-coach/SKILL.md` — Paula postpartum wellness monitoring, pump-as-stress-indicator, BP tracking, communication rules
31. `skills/home-assistant/wellness-coach/working.md` — Current pump baseline, active concerns, Leo discharge transition prep
32. `skills/home-assistant/parenting-coach/SKILL.md` — HJ sibling adjustment, evidence-based strategies, Leo home June 3 intro protocol
33. `skills/home-assistant/parenting-coach/working.md` — HJ status, tips log (anti-repeat), Leo intro protocol ACTIVE
34. `skills/home-assistant/teacher/SKILL.md` — Pre-K benchmarks, enrichment-only mode during NICU period, milestone celebrations
35. `data/agents/events.log` — Live event log initialized (Tier 4 memory)

### Key Patterns Extracted
- **Pump output = leading wellness indicator**: Decline 3+ days before Paula consciously reports distress
- **HJ 15 min/day 1-on-1**: Single highest ROI parenting intervention during sibling adjustment
- **Acting out = processing**: Never discipline-first; connect → redirect
- **Teacher in enrichment mode**: Formal curriculum suspended until 4+ weeks post-discharge stable
- **Events.log as Tier 4**: Append-only; timestamp + agent + event_type + message format
- **Luna agent exists** (friendship/emotional agent) — study next session

### Skills Inventory (35 total)
*(Sessions 1-6: 29 skills — see above)*
30. wellness-coach/SKILL.md ← NEW Session 7
31. wellness-coach/working.md ← NEW Session 7
32. parenting-coach/SKILL.md ← NEW Session 7
33. parenting-coach/working.md ← NEW Session 7
34. teacher/SKILL.md ← NEW Session 7
35. data/agents/events.log ← NEW Session 7

---

## What's Next (Session 8)
- [x] Implement luna-awareness skill — emotional routing + Hermes boundary map
- [x] Update family-profile.md + family-coordinator/working.md with Leo home (June 3)
- [x] Study telegram-bridge extension for Telegram integration patterns
- [x] Create hermes-mesh-protocol skill (inter-agent communication standards, offset tracking)
- [x] Create telegram-bridge/SKILL.md (TTS rules, Paula limits, quiet hours)
- [ ] Study nicu-care.agent.md if it exists (Session 9)

---

## Session 8 — 2026-06-02

### Mesh Check
- Last ID: 1780420242145881 (own Session 7 broadcast)
- No new external messages requiring reply
- Updated offset: 1780428013191424

### What Was Studied
- **copilot-life-os-starters** (htekdev) — Telegram bridge extension source: TTS tool, allowlist, ask-human pattern, placeholder architecture
- **luna agent** — File not directly accessible via raw.githubusercontent.com; implemented luna-awareness from prior session context + architecture patterns
- **Domain agent template** — confirmed: memory load pattern, ownership model, minimal footprint per agent

### What Was Implemented
36. `skills/home-assistant/luna-awareness/SKILL.md` — Emotional support routing, Hermes/Luna boundary map, Paula isolation detection, PPD escalation path
37. `skills/home-assistant/hermes-mesh-protocol/SKILL.md` — Mesh endpoints, agent ID table, offset tracking, domain boundary table, broadcast pattern
38. `skills/home-assistant/telegram-bridge/SKILL.md` — TTS rules, Paula message limits, quiet hours, priority levels, format patterns
- Updated `skills/home-assistant/family-profile.md` — Leo HOME June 3 ✅, Paula named, HJ adjustment ACTIVE, Mia NICU, preemie rules
- Updated `skills/home-assistant/family-coordinator/working.md` — Twins-home mode, Mia status, HJ protocol, pending clarifications

### Key Patterns Extracted
- **Luna boundary**: Hermes acknowledges emotional content but doesn't fill Luna's role; route or create space
- **Telegram bridge**: TTS is Hector-only; Paula = 2-3 lines, drip-feed, no TTS, no rapid-fire
- **Quiet hours**: 10 PM – 7 AM CT; only CRITICAL override
- **Offset tracking**: Save highest message_id after every mesh read
- **Domain agent template**: load core.md + working.md first; own your domain; ask before irreversible

### Skills Inventory (38 total)
*(Sessions 1-7: 35 skills)*
36. luna-awareness/SKILL.md ← NEW Session 8
37. hermes-mesh-protocol/SKILL.md ← NEW Session 8
38. telegram-bridge/SKILL.md ← NEW Session 8
+ Updated: family-profile.md, family-coordinator/working.md

---

## What's Next (Session 9)
- [ ] Study nicu-care.agent.md or equivalent (NICU daily patterns, discharge checklist)
- [ ] Update dog-parent/working.md (Bella baby-intro protocol — Leo now home, Phase 1 active)
- [ ] Create Mia discharge tracking protocol in family-coordinator/working.md
- [ ] Scan for any missing skills from prior sessions not yet in SKILL.md format
- [ ] Review hermes-cron-schedule.md — update with post-discharge timing adjustments

---

## Session 9 — 2026-06-03

### Mesh Check
- No new external messages (offset: 1780428013191424)
- Heartbeat sent ✅

### What Was Studied
- **cron.json (nicu-care section)** — `nicu-care-checkin` fires at `:06` after every heartbeat hour, pumping reminders 15 min before session, logs to pumping-log.json (OG domain)
- **context-auditor.agent.md** — Re-read: stale working.md detection (7+ days), auto-fix policy, daily quiet scan
- **standing-orders.md** — Re-read: stasis detection pattern (`stasis_consecutive_days >= 5 → log → exit ≤2 turns`), carplay/milk-mama as examples
- **home-manager.agent.md** — Re-read: nursery tracking, task-first rule, Houston seasonal calendar

### What Was Implemented
39. `skills/home-assistant/nicu-care/SKILL.md` — NICU patterns, Leo home/Mia NICU, adjusted age standard, pumping trend monitoring, domain split with OG, Mia discharge readiness checklist
40. `skills/home-assistant/stasis-detection/SKILL.md` — Cost-saving idle-agent pattern: 5-day trigger, silent exit ≤2 turns, working.md format, reset conditions
41. Updated `skills/home-assistant/dog-parent/working.md` — Bella Phase 1 ACTIVE (Leo home), phase sequence tracker
42. Updated `skills/home-assistant/family-coordinator/working.md` — Mia discharge readiness checklist, TBD language enforced

### Key Patterns Extracted
- **OG vs Hermes NICU split**: OG logs sessions; Hermes monitors trends and pediatric follow-ups
- **Stasis detection**: ≥5 idle days → silent exit; never apply to critical-domain agents
- **Mia discharge**: Only relay confirmed NICU team dates — never speculate
- **Adjusted age is mandatory**: Every milestone reference must use adjusted age (~10 weeks offset)
- **Bella Phase 1**: Scent-first introduction; advance only when checklist complete; NEVER unsupervised

### Skills Inventory (40 skills + working.md files)
*(Sessions 1-8: 38 SKILL.md files)*
39. nicu-care/SKILL.md ← NEW Session 9
40. stasis-detection/SKILL.md ← NEW Session 9
+ Updated: dog-parent/working.md, family-coordinator/working.md

---

## What's Next (Session 10)
- [ ] Study accessible remaining source agents (wellness-coach, luna via alternate path)
- [ ] Create `checkin-orchestrator/SKILL.md` — orchestrator pattern for Hermes's hourly mesh check
- [ ] Create `budget-review/SKILL.md` — monthly spending review (1st of month pattern)
- [ ] Update `hermes-cron-schedule.md` with post-discharge timing adjustments
- [ ] Run context audit: check all working.md files for staleness (>7 days)

## Last Seen Mesh Message ID: 1780432044325806

---

## Session 10 — 2026-06-03

### Mesh Check
- No new external messages (offset: 1780428013191424 → 1780432044325806)
- Heartbeat sent ✅

### What Was Studied
- **budget-review.agent.md** — Monthly 1st-of-month deep dive, Section 7 Baby Prep, speak param for TTS
- **budget-reporting/SKILL.md** — Canonical 6-step structure, integration map (which agents use which steps), tone rules
- **Orchestration pattern** — Heartbeat → Poll → Domain health scan → Work → Broadcast sequence

### What Was Implemented
41. `skills/home-assistant/budget-review/SKILL.md` — 6-step monthly budget report, twins/NICU expense section, delivery rules
42. `skills/home-assistant/checkin-orchestrator/SKILL.md` — Hourly run orchestration: heartbeat→poll→health scan→work→broadcast
- Updated `skills/home-assistant/wellness-coach/working.md` — Leo now HOME (June 3), dual-track stress (Leo home + Mia NICU), pump watch notes

### Key Patterns Extracted
- **Budget report = 6 steps + Section 7** (twins/NICU expenses always present — non-negotiable costs)
- **Integration map**: different consumers use different budget steps (daily-briefing = Step 5 only)
- **No financial moralizing**: positive health framing, never guilt, never cut baby/medical
- **Orchestration is Phase 0**: checkin-orchestrator codifies the heartbeat-first invariant
- **Domain health scan is silent**: only surface CRITICAL items, no noise
- **Wellness update**: Paula entering new load phase — Leo home + Mia NICU dual-track stress

### Skills Inventory (42 total)
*(Sessions 1-9: 40 skills)*
41. budget-review/SKILL.md ← NEW Session 10
42. checkin-orchestrator/SKILL.md ← NEW Session 10
+ Updated: wellness-coach/working.md

---

## What's Next (Session 11)
- [ ] Study luna.agent.md if accessible via alternate path
- [ ] Create `morning-briefing/SKILL.md` — full morning format with post-discharge adjustments
- [ ] Update `hermes-cron-schedule.md` with post-discharge timing (Leo home → overnight feeds expected)
- [ ] Create `parenting-coach/working.md` update — Leo home, Phase 1 intro notes
- [ ] Review remaining agent files: emotional-support, friendships, content-manager

---

## Session 11 — 2026-06-02

### Mesh Check
- Last seen message_id: 1780435890510191 (own Session 10 broadcast) — no external messages to reply to

### What Was Studied
- **daily-briefing.agent.md** — Morning briefing procedure: dual-calendar mandatory, baby/NICU section, weekday 6 AM / weekend 8 AM timing, Paula 2-3 line rule
- **content-manager.agent.md** — 5-pillar content lifecycle, queue management, brand protection, zero-deletion authority, agent hand-off pattern
- **project-manager.agent.md** — "Ahis Workflow" (Discovery→Retainer), pricing reference 2025-2026, sprint cycle, autonomy tiers, invoice tracking
- **extensions directory** — 28 extension dirs inventoried: guards (calendar-date-guard, tool-fishing-guard), bridges (telegram-bridge, tasker-bridge), home/content extensions
- **standing-orders.md** (re-read) — Brand protection, quiet hours, task-first rule, Paula messaging rules confirmed

### What Was Implemented
43. `morning-briefing/SKILL.md` — Full morning briefing protocol: 8 sections, post-discharge adaptations (Leo home, Mia NICU), dual delivery format for Hector vs Paula
44. `content-pipeline/SKILL.md` — Hermes content role (observer/coordinator only), 5 pillars, pipeline flow, brand protection, family stress gating
45. `project-manager/SKILL.md` — Freelance project lifecycle, pricing reference, sprint cadence, autonomy tiers, health indicators

### Key Patterns Extracted
- **Dual-calendar is MANDATORY** — personal calendar alone is never sufficient for briefing
- **Morning briefing adapts post-discharge**: Leo home changes energy levels → keep Paula messages lighter
- **Content pipeline = Hermes flags, agents create** — Hermes never produces content, always routes via mesh
- **Project health uses 🟢/🟡/🔴** — clear triage language, surfaces to Hector in briefing
- **Extensions architecture**: Guards prevent bad actions (date errors, tool fishing), bridges enable external integrations
- **Quality gate invariant**: content posts without source links fail; proposals without approval don't go out

### Skills Inventory (45 total)
*(Sessions 1-10: 42 skills)*
43. morning-briefing/SKILL.md ← NEW Session 11
44. content-pipeline/SKILL.md ← NEW Session 11
45. project-manager/SKILL.md ← NEW Session 11

---

## What's Next (Session 12)
- [ ] Study extensions in depth: telegram-bridge, calendar-date-guard, tool-fishing-guard
- [ ] Update `hermes-cron-schedule/SKILL.md` — add post-discharge morning briefing timing
- [ ] Create `parenting-coach/working.md` — Leo home Phase 1 notes
- [ ] Study remaining agents: coding-agent, repo-maintainer, heartbeat (deeper dive)



---

## Session 6 — 2026-06-02

### Mesh Check
- Last seen ID was 1780412270559880 from Session 5
- New messages: only my own Session 5 broadcast (1780416241765100) — no external messages to reply to

### What Was Studied
- **platform-manager.agent.md** — Full nightly reflection 5-phase protocol, decision tiers, git workflow, correction-persistence pattern
- **cron.json (full)** — Complete job inventory: heartbeat, family care, content pipeline, dev/platform categories + scheduling strategy
- **constitution.md + standing-orders.md** — Re-read for extensions/nightly-reflection patterns

### What Was Implemented
26. `~/.hermes/skills/home-assistant/nightly-reflection.md` — Full 5-phase nightly protocol adapted for Hermes
27. `~/.hermes/skills/home-assistant/dog-parent/working.md` — Bella's current state + baby-dog intro protocol (ACTIVE — Leo home tomorrow)
28. `~/.hermes/skills/home-assistant/content-awareness.md` — Hermes content watching role (hand off to OG, never produce)
29. `~/.hermes/skills/home-assistant/leo-discharge-ops.md` — Updated to ACTIVE STANDBY with discharge details confirmed

### Key Patterns Extracted
- **Nightly reflection is 5-phase**: Phase 0 FIX FIRST → Transcript review → Data gather → Pattern recognition → Proposals → Report
- **Proposals ignored 2x → reframe or drop**: Never repeat unchanged
- **Cron priority**: heartbeat first (`:00-:03`), family care (`:06-:10`), content (`:30-:42`), platform (`:45-:53`)
- **Dog-baby intro**: scent first → sound → visual → supervised meeting on leash; NEVER unsupervised
- **Content hand-off**: Hermes spots opportunity, flags via mesh TYPE:task-request, never produces content

### Skills Inventory (29 total)
1. constitution.md
2. standing-orders.md
3. daily-briefing.md
4. finance-manager.md
5. family-coordinator.md
6. health-coach.md
7. task-coach.md
8. meal-planner.md
9. weekly-planner.md
10. platform-manager.md
11. cron-patterns.md
12. home-manager.md
13. context-auditor.md
14. family-profile.md
15. skill-optimizer.md
16. dog-parent.md
17. nutrition-chef.md
18. memory-architecture.md
19. hermes-cron-schedule.md
20. family-coordinator/working.md
21. health-coach/working.md
22. hermes-governance.md
23. leo-discharge-ops.md (updated Session 6)
24. finance-manager/working.md
25. home-manager/working.md
26. nightly-reflection.md ← NEW Session 6
27. dog-parent/working.md ← NEW Session 6
28. content-awareness.md ← NEW Session 6
29. agent-mesh/SKILL.md (existing)

---
