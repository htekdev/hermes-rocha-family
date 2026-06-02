# Cron Scheduling Patterns — Hermes Skill

## Source
Adapted from htekdev/copilot-home-assistant cron.json

## Key Principles
- No two jobs share the same minute+hour
- Minimum 3-minute gap between jobs in the same hour
- Lightweight/haiku model jobs for frequent polling
- Sonnet/full model for complex daily tasks
- Early-exit pattern: jobs check if there's anything to do before running

## Recommended Hermes Schedule

### Backbone (multi-hour recurring)
| Job | Schedule | Purpose |
|-----|----------|---------|
| morning-checkin | `0 7 * * 1-5` | Weekday morning briefing |
| weekend-checkin | `0 8 * * 0,6` | Weekend morning briefing |
| task-nudge | `3 9,12,15,18 * * *` | One clear next action |
| evening-wrap | `0 20 * * *` | Day wrap-up, tomorrow prep |

### Daily One-Shot
| Job | Schedule | Purpose |
|-----|----------|---------|
| finance-review | `20 6 * * *` | Unusual charges, budget alerts |
| weekly-planner | `0 18 * * 0` | Sunday evening week preview |
| meal-planner | `0 10 * * 6` | Saturday meal planning session |
| health-reminders | `0 8 * * *` | Appointment + medication reminders |

## Schedule Hygiene
- Priority slots: backbone (`:00-:03`), family care (`:06-:10`), daily tasks (`:15-:30`)
- Don't schedule more than 3 jobs within the same 15-minute window
- Disable jobs immediately when their purpose is met (no zombie crons)
- Silent-if-nothing pattern: lightweight jobs return `[SILENT]` if no action needed

## Energy Matching
- Complex analysis → morning (6-9 AM)
- Nudges and reminders → active hours (9 AM - 7 PM)
- Reflection and wrap-up → evening (8-10 PM)
- Never schedule non-urgent jobs during family quiet hours (10 PM - 6 AM)
