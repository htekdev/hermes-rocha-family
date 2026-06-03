# Hermes Cron Schedule — Rocha Family

## Schedule Philosophy
- Energy matching: Complex tasks AM, nudges active hours, reflection PM
- Minimum 3-min gap between jobs in same hour
- Quiet hours: 10 PM – 7 AM CT (non-urgent silence) — **extended 1h for overnight feeds**
- **POST-DISCHARGE MODE ACTIVE (Leo home June 3, 2026)**: Assume 2–4 AM overnight feeds for household. Morning jobs shifted 1h later to respect disrupted sleep.

## Recommended Hermes Cron Jobs

### Daily Briefing
- **morning-briefing** | `0 7 * * 1-5` | Weekday morning — weather, tasks, calendar
- **weekend-briefing** | `0 8 * * 0,6` | Weekend morning — lighter format
- ⚠️ POST-DISCHARGE: Keep weekday briefing at 7 AM for Hector; Paula messages NOT before 9 AM unless critical

### Family Pulse
- **wellness-coach-morning** | `3 9 * * *` | Paula BP/sleep/pump check-in — 9 AM (not 8; overnight feeds)
- **wellness-coach-midday** | `10 13 * * *` | Pump session trend check
- **wellness-coach-evening** | `0 18 * * *` | Daily summary + bedtime suggestions
- **nicu-care-checkin** | `6 9,11,13,15,17,19 * * *` | Mia NICU monitoring; pumping reminders 15 min before session
- **parenting-coach-morning** | `6 9 * * *` | HJ sibling adjustment check-in
- **dinner-reminder** | `0 15 * * *` | 3 PM dinner check + grocery needs
- **luna-checkin** | `10 10,14,18 * * *` | Paula emotional check-ins (3x/day, not 4 during discharge week)

### Weekly Events
- **weekly-planner** | `10 19 * * 0` | Sunday evening — 7-section weekly brief
- **budget-review** | `0 10 1 * *` | 1st of month deep-dive budget report

### Maintenance
- **nightly-reflection** | `0 21 * * *` | Detect→Fix→Report cycle; update working memories
- **context-audit** | `5 6 * * *` | Daily quick scan — contradictions, stale data (silent if clean)
- **context-audit-weekly** | `0 20 * * 0` | Full audit Sundays

### Mesh
- **mesh-heartbeat** | Every cron run | Send heartbeat first, check messages, broadcast at end

## Scheduling Rules
1. No two jobs share the same minute+hour
2. Always send mesh heartbeat at job start
3. Check mesh messages; respond to direct messages before primary task
4. Broadcast progress summary after each run
5. **POST-DISCHARGE RULE**: No Paula messages before 9 AM; no non-critical messages after 9 PM

## Energy Matching (Post-Discharge Adjusted)
| Time | Cognitive Load | Job Type | Post-Discharge Note |
|------|---------------|---------|-------------------|
| 6–7 AM | High | Context audit (silent), Hector briefing | Paula likely sleep-deprived; Hector-only msgs ok |
| 7–9 AM | Medium-High | Hector morning briefing, Mia NICU check | No Paula msgs before 9 AM |
| 9 AM–12 PM | Medium | Paula wellness, parenting coach, NICU | Paula messages start here |
| 12–5 PM | Medium | Routine NICU, wellness midday, grocery | Keep Paula msgs ≤2-3 lines |
| 5–9 PM | Low | Dinner, wellness evening, family time | Drip-feed, no rapid-fire |
| 9–10 PM | Low | Nightly reflection, memory updates | Wind-down tone |
| 10 PM–7 AM | Silent | No non-urgent messages | Overnight feeds in progress |
