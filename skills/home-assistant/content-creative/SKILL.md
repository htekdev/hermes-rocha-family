---
name: content-creative
description: Use when a content creation pipeline is triggered or social media posts need to be created, scheduled, or coordinated. Codifies Hermes observer/coordinator role in the content-creative agent workflow.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, content, social-media, pipeline]
    related_skills: [content-pipeline, content-analytics, content-scheduler, blog-pipeline, content-awareness]
---

# Content Creative Pipeline Skill

## Overview
Codifies Hermes's role relative to the content-creative agent: **observer and coordinator only**. Hermes never writes posts, generates images, or schedules content. Hermes flags opportunities via mesh and observes quality gates.

Source: `content-creative.agent.md` — voice-to-post pipeline agent for creator brand content.

## When to Use
Use when Hector asks about content status, when content pipeline decisions need routing, or when Hermes needs to understand the 7-phase creation workflow to provide correct coordination.

## Content Creation Workflow (7 Phases)

### Triggers
1. **Daily Cron** — 7 AM CT weekdays → auto-select topic → LinkedIn post
2. **Article Promo Cron** — 12 PM CT weekdays → promote existing blog articles
3. **Voice Command** — "make a post about X" → full pipeline
4. **Blog Companion** — blog-writer publishes → LinkedIn companion post
5. **Trend React** — content-manager flags hot trend

### Phase Summary
| Phase | Action | Hermes Role |
|-------|--------|-------------|
| 1 — Topic Selection | Pull issues with `status:ready/idea`, check pillar balance | None (OG domain) |
| 2 — Post Generation | Strong hook, unique copy per platform | None |
| 3 — AI Image | Dark navy background, infographic style only | None |
| 4 — Upload & Schedule | Late API, best times Tue–Thu 7–8 AM or 12–1 PM CT | None |
| 5 — Update Source Issue | Structured comment, swap label to `status:scheduled` | None |
| 6 — Telegram Preview | 6-field preview message to Hector | Observe for family stress gate |
| 7 — Post-Publish Feedback | Record engagement data in long-term memory | None |

## Quality Gates (Non-Negotiable)
Hermes must know these to avoid flagging false issues:

### Hallucination Detection (before ANY scheduling)
1. Verify all URLs resolve via `web_fetch`
2. Verify all factual claims are sourced
3. Verify all tool/product names actually exist
4. Check for banned patterns: `TODO`, `TBD`, placeholder, lorem ipsum
5. Max 2 remediation cycles → STOP and escalate to Hector

### Source Links Policy (CRITICAL)
Every post MUST include links to source material:
- **LinkedIn:** Source link in **first comment** (not post body)
- **Twitter/X:** Link in post body or first reply
- **YouTube:** Link in video description
- **Instagram:** Caption + "Link in bio"
> A post without source links **FAILS** the quality gate — Hermes flags this to Hector if observed

## Voice & Style Rules
**Never use:** "I'm thrilled to announce", "excited to share", "synergy", "leverage"
**Always use:** Real insights > polished platitudes; Specific > vague

## Image Generation Rules
- Dark navy-charcoal `#0f172a` background, blue-led accents, blue→purple→pink gradient
- **INFOGRAPHIC STYLE ONLY** — summarizes post at a glance
- **NEVER transparent backgrounds**
- **BANNED:** neon, cyberpunk, wireframe-heavy, garish glowing effects
- **Exception:** If post links to article with existing `heroImage` → do NOT generate image

## Platform-Specific Rules
| Platform | Key Rules |
|----------|-----------|
| LinkedIn | No links in body — first comment only; thought leadership tone |
| Twitter/X | Concise, punchy; links in body OK |
| YouTube | Full description with timestamps + links |
| TikTok | Hook-first, casual, trending format |
| Instagram | 23:00 UTC slot for IG Medium queue — NOT 22:30 UTC |

## Hermes Coordination Role

### When to Route via Mesh
- Hector asks "how is content looking?" → check content-scheduler queue status, report summary
- Hector mentions new topic idea → route to OG via TYPE:task-request for content creation
- Family stress event detected → apply family stress gate (see content-awareness/SKILL.md)

### Family Stress Gate
If significant family stress is detected (medical emergency, NICU setback, grief):
1. Do NOT create/schedule content
2. Notify OG agent via mesh: "Family stress gate active — recommend pausing content pipeline"
3. Hermes does NOT override — suggests pause, Hector decides

### Telegram Preview Format (what to expect)
When content-creative completes, Hector receives:
```
🎨 New [Platform] post scheduled!

📝 Preview: [First 200 chars...]
🖼️ Image: [description]
📅 Scheduled: [date + time CT]
🏷️ Pillar: [content pillar]
📊 Source: [issue / trend / voice command]
🔗 Issue: [link]

Want me to adjust anything before it goes live?
```

## Common Pitfalls
- Hermes must NEVER generate social media content or images — always route to OG/content-creative agent
- Don't apply family stress gate overly broadly — normal family life doesn't pause content
- Do not flag source-link violations unless actually observed; don't preemptively police
- LinkedIn link placement (first comment, not body) is by design — don't report as error
- IG Medium queue 23:00 UTC slot is correct — don't suggest "earlier" scheduling

## Verification Checklist
- [ ] Content creation routed to OG agent, not self-executed
- [ ] Family stress gate checked before any content coordination
- [ ] Source link policy known and not flagged as error
- [ ] Platform-specific rules respected when advising Hector
- [ ] Telegram preview format recognized as expected output (not duplicate)
