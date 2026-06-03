---
name: telegram-bridge
description: Use when sending Telegram messages to Hector or Paula. Defines TTS rules, message length limits, allowlist, per-person communication standards, and quiet hours.
version: 1.1.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, telegram, communication, hector, paula]
    related_skills: [family-profile, standing-orders, luna-awareness, wellness-coach]
---

# Telegram Bridge — Communication Standards

## Overview

Hermes communicates with the Rocha family exclusively via Telegram. Two channels: Hector (primary, TTS-enabled) and Paula (secondary, strict limits). This skill defines the rules, format, and delivery patterns for all Telegram messages.

## When to Use

- Any time Hermes sends a message to the family
- Before deciding TTS vs text
- When deciding message length or timing
- When considering whether to message at all

## Per-Person Rules

### Hector (Chat ID: 7729308746)
- **TTS:** ✅ Always include `speak: true` for short messages — Hector uses voice
- **Length:** 2–5 lines preferred; longer OK for briefings
- **Tone:** Direct, result-first. Bottom line up front.
- **Tasks:** One task at a time (ADD pattern) — never stack multiple asks
- **Format:** Bold key info, avoid walls of text

### Paula
- **TTS:** ❌ NEVER use `speak: true` — not configured, unwanted
- **Length:** 2–3 lines MAX per message
- **Drip-feed:** Space messages hours apart — never rapid-fire
- **Questions:** One question at a time, maximum
- **Tone:** Warm, low-pressure, never urgent unless clinical emergency
- **Quiet hours:** No messages 10 PM – 8 AM (she needs sleep)

## Quiet Hours (all family)
- **Night:** 10:00 PM – 7:00 AM — no non-emergency messages
- **Emergency override:** BP >160/110, baby distress, safety issue
- **Houston timezone:** All times CST/CDT

## Message Priority Levels

| Priority | When | Behavior |
|----------|------|----------|
| CRITICAL | Safety, medical emergency, baby distress | Send immediately, any hour |
| HIGH | Time-sensitive family action needed | Send during waking hours |
| NORMAL | Updates, reminders, briefings | Follow schedule |
| LOW | Nice-to-know, non-actionable | Batch or skip |

## Message Format Patterns

### Standard update (Hector, TTS):
```
✅ [Result/status in one line]
📌 [Key detail if needed]
→ [Single next action if any]
```

### Task Serve (Hector):
```
🎯 [Task Title]
📋 [1-line instruction]
⏱️ ~X min
📋 X pending | Y due today
```

### Task Completion + Next (Hector):
```
✅ [Done task] — nice! 🎉
→ 🎯 Next: [Next task] (~X min)
📋 X pending
```

### Alert / Urgent (Hector):
```
🔴 [URGENT THING]
📝 [What to do RIGHT NOW]
📞 [Contact/link if applicable]
```

### Daily Briefing (Hector):
```
☀️ Good morning!
📅 Today: [X events]
• [Event 1] at [time]
✅ Tasks: X pending (Y high priority)
💰 Bills: [any due today/tomorrow]
🍽️ Dinner: [tonight's meal]
```

### Status Report (Hector):
```
📊 [Report Title]
• [Finding 1]
• [Finding 2]
[Action taken or recommendation]
```

### Wellness check-in (Paula):
```
Hey — quick check-in. [One observation or question].
```
*Never: "Your data shows...", "According to your metrics...", "I noticed you..."*

### Morning briefing header (Hector):
```
☀️ Good morning, Hector — [Day, Date]
[2–4 bullets max for preview]
```

## What NOT to Send

- **Don't send** if there's nothing actionable or time-sensitive
- **Don't send** "FYI" messages that require no response and add no value
- **Don't send** duplicate information OG already sent
- **Don't send** to Paula: task lists, finance updates, technical system info
- **Don't send** to either: raw data dumps, long tables, code

## Extension Architecture (for reference)

The Telegram bridge extension (`telegram_send_message`) accepts:
```json
{
  "chat_id": "string",      // recipient chat ID
  "text": "string",         // message body (Markdown ok)
  "speak": true/false       // TTS voice note — Hector only
}
```

Allowlist enforced in extension — only whitelisted chat IDs accepted.

The `telegram_ask_human` tool enables ask-and-wait patterns (up to 5 min response window) — use sparingly, only for time-sensitive decisions.

## Common Pitfalls

- **TTS to Paula** — never, breaks her experience
- **Multiple questions** to Paula — overwhelming, she'll disengage
- **Stacking tasks** to Hector — ADD means one at a time
- **Messaging during quiet hours** unless critical
- **Over-messaging** — each message should earn its send

## Verification Checklist

- [ ] Hector messages include `speak: true` where appropriate
- [ ] Paula messages are ≤3 lines
- [ ] No more than 1 question per Paula message
- [ ] Quiet hours respected (10 PM – 7 AM)
- [ ] Message has clear purpose before sending
- [ ] Not duplicating what OG already sent
