---
name: cost-optimizer
description: Use when auditing platform costs, optimizing AI token usage, or reviewing cloud infrastructure expenses. Covers model selection rules and AWS cost cleanup patterns for Rocha family systems.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, cost, cloud, aws, optimization, platform]
    related_skills: [platform-manager, finance-manager, hermes-cron-schedule]
---

# Cost Optimizer Skill

## Overview

Two-layer cost management: (1) platform AI token costs via model selection, and (2) cloud infrastructure waste via AWS audits. Runs automatically on schedule but can be triggered on-demand.

## When to Use

- Reviewing token spend patterns
- Auditing AWS resources for waste
- Recommending model downgrades to cheaper tiers
- Weekly infrastructure cost check-in

## Layer 1: Platform Token Optimization

### Model Selection Hierarchy

| Use Case | Preferred Model | Fallback |
|----------|----------------|---------|
| Simple task nudges, status checks | `claude-haiku-4.5` | — |
| Standard agents, briefings | `claude-sonnet-4.6` | haiku |
| Complex reasoning, medical, NICU | `claude-sonnet-4.6` | never downgrade |
| Code generation, PR review | `claude-sonnet-4.6` | — |

### Auto-Downgrade Rules

When token analysis shows a cron job consistently using <20% of model capacity:
1. Flag for haiku override
2. Add override to cron config (never touch original)
3. Report to Hector: model, job, estimated savings

### Protected Agents — NEVER downgrade:
- `nicu-care` — baby health is non-negotiable
- `wellness-coach` — postpartum medical context
- `health-coach` — medical decisions
- `finance-manager` — money decisions
- Any agent where wrong output = real-world harm

## Layer 2: AWS Infrastructure Audit

Run weekly (Monday 8:35 AM):

### Audit Checklist

```
EC2: Stopped instances >7 days → flag for termination
EBS: Unattached volumes >7 days → snapshot + delete
EIPs: Unassociated Elastic IPs → release (cost: ~$3.60/mo each)
RDS: Dev/staging instances running nights/weekends → schedule stop
S3: Buckets with versioning on but no lifecycle policy → add 30-day cleanup
Lambda: Functions with 0 invocations in 30 days → flag for review
```

### Auto-Actions (no approval needed):
- Release unassociated EIPs
- Add lifecycle policies to S3 buckets
- Tag untagged resources with `owner: hermes-audit`

### Escalate to Hector (approval required):
- Terminate any EC2 instance
- Delete any RDS instance or snapshot
- Changes to security groups or IAM

## Reporting Format

```
☁️ Cloud Cost Audit — [Date]
💰 Current monthly: ~$XX
🔴 Waste found: $XX/mo (X items)
  • [Item]: $X/mo — [action taken or recommended]
✅ Auto-cleaned: $X/mo
📋 Action needed: [items requiring approval]
```

## Common Pitfalls

- ❌ Downgrading NICU/medical/finance agents for cost savings — never
- ❌ Terminating instances without approval
- ❌ Acting on stale data (always pull fresh usage before recommending)
- ❌ Over-reporting — only surface items with $5+/mo impact

## Verification Checklist

- [ ] Protected agents list checked before any model downgrades
- [ ] AWS actions requiring approval routed to Telegram first
- [ ] Cost report leads with total impact, not list of findings
- [ ] Auto-actions logged to working memory for audit trail
