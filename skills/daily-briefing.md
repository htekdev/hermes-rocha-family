# Hermes Skill: Daily Briefing

> Adapted from htekdev/copilot-home-assistant daily-briefing agent pattern

## Purpose
Deliver a concise daily morning briefing to Hector covering what matters for the day.

## Trigger
- Morning cron (configurable, suggested 7:30 AM)
- On-demand: "Give me today's briefing" / "What's on today?"

## Briefing Structure
Deliver in this order — skip sections if nothing relevant:

1. **Weather** — Current conditions + today's high/low (if weather tool available)
2. **Today's calendar** — Events in chronological order with leave-by times (+15 min traffic buffer)
3. **Upcoming deadlines** — Anything due in the next 48 hours
4. **Bills/Finance** — Any bills due this week
5. **Action items** — Top 1–3 things Hector should do today (specific, not vague)

## Format Rules
- Total message: **10 lines max** for Telegram
- Each section: 1–2 lines
- Omit empty sections entirely
- Result-first: no "Good morning! I've checked your calendar and..."
- Acceptable opener: "📋 Today, [Date]:" then items

## Example Output
```
📋 Today, Tuesday Jun 3:
• 10 AM dentist — leave by 9:40 (traffic)
• 3 PM call with contractor
Bills: Internet bill due Fri ($89)
Action: Confirm dentist insurance before 9 AM
```

## Implementation Notes
- Always compute current date — never assume
- For appointments, calculate leave-by = appointment time minus (drive time + 15 min)
- If calendar is unavailable, say "calendar unavailable" rather than guessing

---

*Source: htekdev/copilot-home-assistant — daily-briefing.agent.md pattern*
*Adapted: 2026-06-02*
