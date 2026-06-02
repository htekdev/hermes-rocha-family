# Hermes Cron Schedule — Rocha Family

## Schedule Philosophy
- Energy matching: Complex tasks AM, nudges active hours, reflection PM
- Minimum 3-min gap between jobs in same hour
- Quiet hours: 10 PM – 6 AM CT (non-urgent silence)

## Recommended Hermes Cron Jobs

### Daily Briefing
- **morning-briefing** | `0 7 * * 1-5` | Weekday morning — weather, tasks, calendar
- **weekend-briefing** | `0 8 * * 0,6` | Weekend morning — lighter format

### Family Pulse
- **health-checkin** | `0 9 * * *` | Daily health prompt reminder (meds, BP if needed)
- **dinner-reminder** | `0 15 * * *` | 3 PM dinner check + grocery needs

### Weekly Events
- **weekly-planner** | `10 19 * * 0` | Sunday evening — 7-section weekly brief
- **monday-handoff** | `25 7 * * 1` | Monday morning context summary

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

## Energy Matching
| Time | Cognitive Load | Job Type |
|------|---------------|---------|
| 6–9 AM | High | Complex briefings, audits, planning |
| 9 AM–12 PM | Medium-High | Health, task coach, proactive reminders |
| 12–5 PM | Medium | Routine reminders, grocery, family |
| 5–9 PM | Low | Light nudges, dinner, family time |
| 9–10 PM | Low | Reflection, memory updates |
| 10 PM–6 AM | Silent | No non-urgent messages |
