---
name: content-analytics
description: Use when monitoring Hector's creator brand performance, managing social comments, reporting engagement trends, or feeding strategy insights to content agents. Covers analytics workflow, auto-reply decision tree, quality gates, and inter-agent data flow.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, content, analytics, social-media]
    related_skills: [content-pipeline, morning-briefing, telegram-bridge]
---

# Content Analytics Skill

## Overview
Hermes's role in the content analytics domain: **observe, flag, route**. Analytics output flows from Hector's creator brand (GitHub/LinkedIn/YouTube) through this skill to daily briefing and content pipeline agents. Hermes does not post content — it monitors signals and flags exceptions.

## When to Use
- Reporting engagement spikes or drops to Hector
- Deciding whether to auto-reply to a comment or escalate
- Feeding performance data into morning briefings
- Routing content insights to OG / content agents via mesh

## Analytics Check Workflow
1. **Load** content working memory
2. **Pull data** — top posts, 7-day window, per-platform
3. **Compute deltas** — follower growth, engagement spikes/drops, top/bottom 3 posts
4. **Comment management** (8 AM–9 PM CT only) — classify → draft → quality gate → post
5. **Report** — Telegram only if notable; full weekly report Sundays 6 PM CT

## Notification Thresholds
| **Always Notify** | **Silent** |
|---|---|
| >10× normal engagement (viral) | Routine checks with normal results |
| >100 new followers/day | Individual comment replies |
| Sunday weekly report | Minor follower fluctuations (<2%) |
| >50% engagement drop WoW | Expected low engagement (first 2 hrs) |
| Notable account comment | |

Silent by default. Quiet hours: 10 PM–6 AM CT.

## Auto-Reply Decision Tree
| Comment Type | Action |
|---|---|
| ✅ Positive | Thank + engage ("What topic next?") |
| ✅ Question | Answer with source links |
| ✅ Constructive | Acknowledge + address |
| ✅ Feature request | Acknowledge + log as content idea |
| 🚩 Negative/controversial | Flag → task for Hector |
| 🚩 Competitor mentions | Flag → task for Hector |
| 🚩 Brand safety issues | Flag → task for Hector |
| 🗑️ Spam/abusive | Hide comment |

**Max 20 auto-replies per cycle.**

## Reply Quality Gate (5 Checks)
1. **Tone** — helpful, human, sounds like Hector
2. **Accuracy** — grounded in source/docs
3. **Brand safety** — no unreleased feature claims
4. **Specificity** — no generic canned responses
5. **URL validation** — all links return HTTP 200

### URL Validation Flow
```
Draft reply → Extract URLs → Validate (HEAD request) → All 200? → Post
                                                          ↓ FAIL
                                        Fix/remove URL → Re-validate → Post
                                                          ↓ STILL FAIL
                                          Skip reply → create task for Hector
```

## Duplicate Reply Check (MANDATORY)
Always verify via API that Hector's account hasn't already replied — **never trust working memory alone** for this check.

## Performance Metrics Reference
| Metric | Formula | Benchmark |
|---|---|---|
| Engagement Rate | (likes+comments+shares)/impressions×100 | >3% short, >5% long |
| Reach Rate | unique reach/followers×100 | >30% |
| CTR | link clicks/impressions×100 | >2% |
| Save Rate (IG) | saves/impressions×100 | >1% |
| Comment Rate | comments/views×100 | >0.5% |
| Follower Growth | new/total×100 weekly | >1%/week |
| View Completion | full views/total×100 | >40% shorts, >25% medium |

## Content Pillars (Track Performance By)
1. AI & Copilot Ecosystem
2. Developer Productivity
3. Creator Economy
4. Career & Leadership
5. Employer Platform (Azure/M365)

## Sibling Agent Integration
- **→ content-manager**: Best/worst pillars, audience questions, engagement spike topics
- **→ content-scheduler**: Best time slots, day-of-week patterns, frequency sweet spots
- **→ content-creative**: Hook performance, image style patterns, pillar data

## Hermes Domain Boundary
- Hermes **observes and flags** — does not post, comment, or create content
- All actionable analytics flags route to Hector via Telegram or task
- OG/content agents own content creation and scheduling

## Common Pitfalls
- ❌ Replying without API duplicate check (silently double-post)
- ❌ Posting a reply with an unvalidated URL (404 links hurt brand)
- ❌ Pinging Hector for routine/expected low engagement
- ❌ Treating first 2 hours of a post as underperforming (normal low engagement window)

## Verification Checklist
- [ ] Duplicate reply checked via API (not memory)
- [ ] All URLs in replies validated (HTTP 200)
- [ ] Reply passed all 5 quality gate checks
- [ ] Notification threshold met before sending Telegram
- [ ] Task created before any actionable Telegram message
