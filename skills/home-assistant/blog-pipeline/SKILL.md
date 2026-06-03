---
name: blog-pipeline
description: Use when Hermes needs to understand the content blog pipeline structure, spot content opportunities for Hector's site, or route blog-related requests to the correct agents.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, content, blog, pipeline]
    related_skills: [content-awareness, content-pipeline, project-manager, hermes-mesh-protocol]
---

# Blog Pipeline

## Overview
Hector's personal developer site (htek-dev-site) uses a 3-agent blog pipeline: blog-planner → blog-writer → blog-reviewer. Hermes's role is strictly observer + opportunity spotter. Hermes does NOT write, review, or publish.

## When to Use
- Hector asks about a blog post status
- A family experience could be content-worthy (route to blog-planner via OG)
- Understanding which agent owns which part of the pipeline

## Pipeline Architecture

```
blog-idea → [blog-planner] → blog-ready → [blog-writer] → blog-draft → [blog-reviewer] → blog-published
```

### blog-planner
- **Owns**: intake, interview, brief synthesis
- **Does NOT write** — produces a brief only
- Asks Hector 3–5 high-signal questions before brief is complete
- Moves issue: `blog-idea → blog-interviewing → blog-ready`

### blog-writer
- **Owns**: research → write → parallel review → PR creation
- Dispatches `content-illustrator` MANDATORY (hero image, dev.to cover, 2-4 inline)
- Quality gate (hallucination detection) before every PR — no bypass
- Moves issue: `blog-ready → blog-draft`

### blog-reviewer
- **Owns**: independent quality check before publication
- Verifies: illustrations exist, quality gate passed, brief fidelity, voice, SEO, cross-links
- Approve → `blog-published` | Reject → `blog-draft` with specific revision note
- Moves issue: `blog-draft → blog-review → blog-published`

## Quality Gate (Non-Negotiable)
Every article must pass before PR:
1. URL verification (all links resolve with HTTP 200)
2. Claim grounding (all facts sourced)
3. Tool/package validation
4. Statistic & version number verification
5. No TODO/TBD/placeholder/lorem ipsum

Failure → remediation loop (max 2 cycles) → escalate to Hector. **No bypass.**

## Issue Labels
| Stage | Label |
|-------|-------|
| Intake | `blog-idea` |
| In interview | `blog-interviewing` |
| Brief complete | `blog-ready` |
| Draft created | `blog-draft` |
| In review | `blog-review` |
| Live | `blog-published` |
| Priority | `priority:hot-trend` / `priority:timely` / `priority:evergreen` |

## Hermes Opportunity Routing
If Hermes spots a blog opportunity:
1. Check family stress gate (wellness-coach/working.md) — HIGH stress → hold
2. Send mesh task-request to OG with:
   - Event/topic description
   - Why it's content-worthy for Hector's audience
   - Priority estimate (hot-trend/timely/evergreen)
3. Do NOT contact blog-planner directly — route via OG

## Common Pitfalls
- **Writing any content yourself**: Not Hermes's domain — route only
- **Routing timely content during HIGH family stress**: Stress gate always runs first
- **Conflating blog-planner and blog-writer**: Planner never writes; writer never plans
- **Bypassing quality gate**: No publication without gate pass — reviewer enforces

## Verification Checklist
- [ ] Blog opportunity identified (if applicable)
- [ ] Stress gate checked before routing
- [ ] Routed via OG mesh task-request (not directly to blog agents)
- [ ] No content produced by Hermes
- [ ] If asked for status: read-only check via OG, no direct pipeline tool calls
