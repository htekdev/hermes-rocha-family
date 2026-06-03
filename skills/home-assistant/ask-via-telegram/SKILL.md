---
name: ask-via-telegram
description: Use when an agent needs human confirmation before taking a high-stakes, irreversible, or ambiguous action. Routes confirmation prompts to Telegram instead of blocking or silently proceeding. Implements the 4-tier decision framework.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, telegram, confirmation, governance, safety]
    related_skills: [telegram-bridge, hermes-governance, extensions-architecture, constitution]
---

# Ask Via Telegram

## Overview

The `ask-via-telegram` pattern routes high-stakes decisions to a human via Telegram instead of either blocking silently or proceeding autonomously. It is the core human-in-the-loop mechanism for Tier 3 and Tier 4 actions.

## When to Use

Apply the ask-via-telegram pattern whenever an action:
- Is **irreversible** (deleting data, canceling appointments, financial transactions)
- Has **ambiguous parameters** (could mean two different things)
- Exceeds the agent's **autonomous authority tier**
- Has **cascading effects** on family wellbeing (medical, child safety, financial)

---

## 4-Tier Decision Framework

| Tier | Type | Action | Example |
|------|------|--------|---------|
| **1** | Routine, reversible, low-stakes | ACT silently | Logging a pump session time |
| **2** | Medium stakes, reversible | ACT + notify | Creating a calendar event, sending a reminder |
| **3** | High stakes OR irreversible | **ASK FIRST** via Telegram → wait | Canceling a doctor appointment, ordering supplies |
| **4** | Destructive / financial / medical | **ALWAYS ASK**, never assume | Medication changes, budget reallocation, ER threshold decisions |

---

## Trigger Conditions

### Always Ask (Tier 3+)
- Any action involving **financial transactions** > $20
- **Medical decisions**: medication dosage, appointment cancellations, escalation to ER
- **Calendar deletions** or modifications to events within 24 hours
- **Child-affecting decisions**: HJ routine changes, Leo/Mia medical updates to external parties
- **Data deletion**: removing working memory, clearing task lists, archiving events

### Never Ask (Tier 1)
- Sending a scheduled daily briefing
- Logging data that was explicitly provided by user
- Reading/checking status (non-mutating operations)
- Heartbeat + mesh operations

---

## Message Format

When routing to Telegram for confirmation:

```
⚠️ CONFIRMATION NEEDED

[1-line description of proposed action]

Details:
• [key parameter 1]
• [key parameter 2]

Reply YES to confirm or NO to cancel.
```

**Rules:**
- Keep the prompt to ≤5 lines
- Include enough detail to decide without follow-up questions
- ONE decision per message — never bundle multiple asks
- Add context only if essential (don't pad)
- For Hector: include `speak` param (TTS) for voice confirmation
- For Paula: plain text only, no TTS, ≤3 lines

---

## Fallback Behavior

If no reply within:
- **Time-sensitive** (appointment in 2h): default to SAFE action (don't cancel, don't send)
- **Non-time-sensitive**: wait up to 4 hours, then log as "pending human confirmation"
- **Critical** (ER-level): escalate regardless — send message + take safe action

---

## Anti-Patterns

1. **Asking for everything** — decision fatigue kills trust; tier 1/2 must stay silent/notify-only
2. **Bundling asks** — "Should I do A and B?" — split into separate prompts
3. **Vague asks** — "Should I do the thing?" — always specify exactly what action
4. **Asking after acting** — never act first then ask for retroactive approval
5. **Repeating unanswered asks** — if 2x unanswered, escalate to Hector only, log, and drop

---

## Rocha Family Specific Routing

| User | Message limit | TTS | Quiet hours |
|------|-------------|-----|-------------|
| Hector (7729308746) | No limit | ✅ Always | 10 PM – 7 AM CT |
| Paula | 2-3 lines max | ❌ Never | 10 PM – 9 AM CT (post-discharge) |

**Route to Hector first** for all Tier 3+ decisions unless the question directly involves Paula's own health preferences.

---

## Common Pitfalls

1. Using ask-via-telegram for Tier 1/2 actions — creates noise, erodes trust
2. Not specifying the fallback behavior before sending the ask
3. Asking Paula urgent questions before 9 AM post-discharge
4. Missing the speak param for Hector (he uses TTS)

## Verification Checklist

- [ ] Action tier assessed (1/2/3/4)
- [ ] Prompt is ≤5 lines with clear YES/NO framing
- [ ] Correct recipient (Hector vs Paula) selected
- [ ] Fallback behavior defined if no reply
- [ ] Not bundling multiple asks in one message
- [ ] TTS included for Hector; omitted for Paula
