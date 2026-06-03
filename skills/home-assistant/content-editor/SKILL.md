---
name: content-editor
description: Use when video content editing, auto-publish pipeline coordination, or media production orchestration questions arise. Codifies the 8-stage pipeline and Hermes observer role.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, content, video, pipeline, media-production]
    related_skills: [content-creative, blog-pipeline, content-scheduler, content-pipeline]
---

# Content Editor — Media Production Pipeline Skill

## Overview
Codifies Hermes's understanding of the content-editor agent: **Media Production Orchestrator**. Dual function — hands-on video editor + pipeline orchestrator. Philosophy: *"Ship the full bundle fast, iterate on feedback. A publishable release today beats a perfect release never."*

Hermes role: **observer and support coordinator only**. Never edit video, generate transcripts, or publish.

## When to Use
Use when Hector asks about video processing status, when video delivery Telegram messages arrive, or when coordinating around the auto-publish pipeline schedule.

## 8-Stage Auto-Publish Pipeline

| Stage | Owner | Action |
|-------|-------|--------|
| 0 — Initialize | content-editor | Generate `run_id`, create output dir, load config |
| 1 — Inspect & Transcribe | content-editor | ffprobe + faster-whisper → transcript.json + captions.srt |
| 2 — Research | → content-researcher | Pass transcript/topics, receive research package |
| 3 — Production Planning | content-editor | Primary angle, social hooks, bundle deliverables |
| 4A — Edit Lane | content-editor | Silence removal, captions, quality review, intro/outro, variants |
| 4B — Blog Lane | → blog-writer | Context package → PR URL; blog-reviewer owns quality |
| 4C — Social Lane | → content-creative | Unique copy per platform with source links |
| 5 — Quality Check | content-editor | Coherence review, brand safety, source link verification |
| 6 — Publish | content-editor | Late API posts |
| 7 — Schedule | → content-scheduler | Post IDs + bundle metadata |
| 8 — Notify | content-editor | ONE Telegram message to Hector |

## Stage 4C Platform Requirements
- **LinkedIn:** Thought leadership, no external links in body (links in first comment)
- **Twitter/X:** Concise, punchy, can include links
- **YouTube:** Full description with timestamps + links
- **TikTok:** Hook-first, casual, trending format
- **Instagram:** Visual-first caption, relevant hashtags
- **CRITICAL:** Every post MUST include source links — if missing, send back to content-creative

## Decision Framework
| Act Immediately | Ask First | Escalate |
|----------------|-----------|----------|
| Auto-publish pipeline | Custom clip selection (ad-hoc) | QR failures after retries |
| Quality review | Major caption style changes | Unintelligible transcript |
| Research delegation | | Corrupt/unplayable files |
| Publishing | | FFmpeg errors after 2-3 attempts |

**Tool debugging limit:** After 2-3 failures, notify Hector and move on — never burn context debugging inline.

## Caption Defaults
- **FontSize=21, MarginV=25, Arial Bold** — use without asking

## Intro/Outro Rules
- >60 seconds: intro + outro (both)
- 60s–5min: both
- Shorts <60s: outro only

## Video Delivery Note
> `telegram_send_photo` does NOT work for video — always use `curl.exe sendVideo` (50MB limit). This is a known workaround — don't flag as error.

## Output Directory Structure
```
data/content-editor-output/
  {run_id}/                    # Auto-publish runs
    context-package.json
    transcript.json
    captions.srt
    production-plan.json
    edited.mp4 → captioned.mp4 → published-master.mp4
    variants/
    publish-results.json
  {YYYY-MM-DD-HHMMSS}/         # Manual sessions
    analysis.md, silence-gaps.json, edit-plan.md
    tight-edit.mp4, clip-*.mp4, captioned.mp4
```

## Hermes Coordination Role

### When Hector Asks About Video Status
1. Check events.log for recent content-editor run entries
2. Report pipeline stage and run_id if available
3. If stuck or failed at a stage → escalate to Hector with specific error (not generic "there's an issue")

### Pipeline Completion Signal
When Stage 8 fires (ONE Telegram message to Hector), Hermes should:
- Recognize this as expected pipeline completion notification
- Not create a duplicate notification
- Log to events.log if relevant to family content calendar

### Family Content Calendar Integration
- Blog published → LinkedIn companion post auto-triggered (Stage 4C)
- Hermes does not interfere with this automation
- Hermes CAN flag to Hector if family content topic seems sensitive given current family context (e.g., don't promote travel content during NICU crisis)

## Common Pitfalls
- NEVER attempt video editing, ffprobe, or whisper transcription — content-editor agent owns these
- Stage 8 fires ONE message — receiving a Telegram notification is expected, not a duplicate bug
- `curl.exe sendVideo` for video delivery is the correct workaround — not a bug to fix
- Quality review failures (max 2 retries) are designed escalations — Hermes routes to Hector, doesn't retry
- Do not duplicate content-editor's Stage 8 Telegram notification

## Verification Checklist
- [ ] Pipeline stages clearly understood — not attempting to execute any stage
- [ ] Stage 8 Telegram message recognized (not duplicated)
- [ ] Video delivery via curl.exe pattern known (not flagged as error)
- [ ] Family stress gate applied before any content coordination
- [ ] Quality gate failures escalated to Hector with specific error details
