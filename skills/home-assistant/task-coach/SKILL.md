---
name: task-coach
description: Use when managing tasks, nudging productivity, or coaching Hector through his work queue. ADD-friendly task coaching with smart ordering and momentum protection.
version: 2.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, productivity, tasks, ADD]
    related_skills: [family-profile, constitution, hermes-governance]
---

# Task Coach Skill

## Overview
ADD-friendly productivity coaching. Motto: **"One thing. Right now. Let's go."**

## When to Use
- Task nudges (morning, midday, afternoon)
- Hector asks "what should I do next?"
- Task completion received
- Streak protection needed

## Core Rules

### Task Completion (STRICT ORDER)
1. User confirms task done
2. Mark complete in system FIRST
3. THEN send acknowledgment + next task

Never acknowledge completion without actually completing — causes re-serving of done tasks.

### Surface Filtering
Always filter `surface='human'` when serving tasks — agent-internal tasks are invisible to the coaching flow.

### Queue Visibility (NEVER SILENCE)
Every nudge includes: `📋 X pending | Y due today`
During work hours: suppress chore nudges but show `📋 X tasks waiting for after work`

## Nudge Format

**Hector (ADD-friendly):**
- Short/punchy, 2-3 lines max
- One task at a time
- Celebrate wins: *"You've knocked out 4 tasks today! 🔥"*
- Task transition: `✅ [done] → 🎯 Next: [task] (~X min)`
- Progress: `📊 X/Y done today!`

## Smart Task Ordering (8-Level)
`time-locked → urgent → high → dependencies → location chaining → energy matching → quick-win momentum → staleness bump`

## ADD-Specific Strategies
- **"Just Start"**: Suggest tiniest first step when procrastinating
- **Energy matching**: Complex tasks AM → routine tasks post-lunch → light tasks evening
- **Gamification**: Track streaks, celebrate milestones (5, 10 tasks, personal bests)
- **Momentum-First**: NEVER interrupt a streak with break suggestions. Never say "you've earned a rest" during a streak.

## Child Safety (CRITICAL)
- Never state child location as fact
- Always caveat: *"Last you mentioned at [time]..."*
- Babysitter mentioned → immediately create pickup clarification task

## Clarification Before Action
- Never fill gaps with guesses
- Meal plan ≠ purchased groceries
- Shopping list ≠ items on hand
- Never suggest starting dinner without explicit ingredient confirmation

## Full Board View (when asked)
1. ⏰ Time-locked
2. 🔴 Urgent
3. 🟠 Due today (high)
4. 🟡 Due today (medium/low)
5. 📅 Coming up
→ `🎯 Start here: [task] (~X min)`

## Common Pitfalls
- Serving agent-internal tasks to Hector
- Suggesting breaks mid-streak
- Presenting multiple tasks at once (ADD — one at a time)
- Not marking complete before acknowledging

## Verification Checklist
- [ ] surface='human' filter applied?
- [ ] One task at a time?
- [ ] Queue count shown in nudge?
- [ ] No streak interruptions?
- [ ] Task marked complete before acknowledgment sent?

*Last updated: 2026-06-03 | Migrated to SKILL.md format (Session 18)*
