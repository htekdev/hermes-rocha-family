---
name: checkin-orchestrator
description: Use when running the hourly mesh check-in cycle. Orchestrates heartbeat, message polling, domain status checks, and broadcast in correct sequence.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, mesh, orchestration, cron]
    related_skills: [hermes-mesh-protocol, hermes-governance, stasis-detection]
---

# Check-In Orchestrator Skill

## Overview

Every scheduled Hermes run begins with this orchestration sequence. It ensures heartbeat, message handling, domain health, and broadcast happen in the correct order with no step skipped.

## When to Use

- Every hourly cron run (before any domain work)
- Every study session run
- Any autonomous Hermes invocation

## Orchestration Sequence

### Phase 0: Heartbeat (ALWAYS FIRST)
```bash
BASE="http://AgentM-MeshS-C9BTpnBG6o3j-892354001.us-east-1.elb.amazonaws.com/mesh/Q71OPXGenFuk"
HERMES_ID="zvV2q_LzJNua"
curl -s -X POST "$BASE/agents/$HERMES_ID/heartbeat"
```
- Must succeed before any other work
- If heartbeat fails: log failure, continue anyway (don't block domain work)

### Phase 1: Message Poll
```bash
OFFSET=$(cat ~/.hermes/mesh_offset.txt 2>/dev/null || echo 0)
curl -s "$BASE/messages?recipient=$HERMES_ID&timeout=10&offset=$OFFSET"
```
- Save highest `message_id` seen to `~/.hermes/mesh_offset.txt`
- If `count == 0`: note "no new messages" and continue
- If messages present: process each (see Reply Protocol below)

### Phase 2: Reply Protocol
For each incoming message:
1. **Identify sender** — check `hermes-mesh-protocol/SKILL.md` agent table
2. **Domain check** — is this in Hermes's domain? Route or own it
3. **Reply** — use `TYPE:` prefix convention:
   - `TYPE:ack` — received, noted
   - `TYPE:task-request` — creating task in OG's system
   - `TYPE:status` — domain status update
   - `TYPE:question` — clarification needed
4. **Send reply:**
   ```bash
   curl -s -X POST "$BASE/messages" \
     -H "Content-Type: application/json" \
     -d '{"sender_id":"zvV2q_LzJNua","recipient_id":"<target>","content":"<message>"}'
   ```

### Phase 3: Domain Health Scan (Quick, Silent)
Check each active domain for obvious issues:
- `family-coordinator/working.md` — any CRITICAL items needing action?
- `wellness-coach/working.md` — pump trend alert?
- `home-manager/working.md` — any overdue maintenance?
- `dog-parent/working.md` — Bella phase advancement ready?
- Stasis check: any working.md not updated in 7+ days? → flag

Quiet unless CRITICAL. Don't generate noise.

### Phase 4: Execute Domain Work
Run the actual scheduled task (briefing, study session, etc.)

### Phase 5: Broadcast to Mesh
After completing domain work:
```bash
curl -s -X POST "$BASE/messages" \
  -H "Content-Type: application/json" \
  -d '{"sender_id":"zvV2q_LzJNua","recipient_id":"*","content":"<broadcast>"}'
```
Broadcast format:
```
TYPE:status | Hermes session complete | [what was done] | Next: [what's next]
```

### Phase 6: Update Offset
Save the latest mesh `message_id` to `~/.hermes/mesh_offset.txt`.

## Domain Priority Matrix (for Phase 3)

| Domain | Check Frequency | CRITICAL Threshold |
|--------|-----------------|-------------------|
| Wellness (Paula) | Every run | Pump drop 3+ days, BP alert |
| Twins (Leo/Mia) | Every run | Leo health issue, Mia discharge date |
| Family Coordinator | Every run | HJ acute distress, car seat, safety |
| Home Manager | Daily | Nursery temp out of range (68-72°F) |
| Dog Parent | Daily | Bella unsupervised near twins |
| Finance | Weekly | Overdraft, unusual charge |

## Quiet Hours Rule

- 10 PM – 7 AM CT: suppress all non-CRITICAL Telegram messages
- CRITICAL = safety issue, medical emergency, security breach
- Mesh broadcasts: OK any time (no user-facing output)

## Common Pitfalls

- ❌ Don't skip heartbeat — do it before ANYTHING else
- ❌ Don't process messages without updating offset — causes duplicate processing
- ❌ Don't broadcast before completing domain work — sequence matters
- ❌ Don't wake Paula outside quiet hours for non-CRITICAL items
- ❌ Don't reply to mesh messages using Paula's Telegram — route to Hector or mesh only

## Verification Checklist

- [ ] Heartbeat sent and returned `{"status":"ok"}`
- [ ] Mesh offset read from file before polling
- [ ] All incoming messages read and replied to
- [ ] Mesh offset file updated with highest seen ID
- [ ] Domain health scan ran silently (no noise unless CRITICAL)
- [ ] Broadcast sent after work is complete
