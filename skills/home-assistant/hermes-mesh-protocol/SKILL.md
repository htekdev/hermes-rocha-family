---
name: hermes-mesh-protocol
description: Use when communicating with other agents on the mesh network. Defines message format, offset tracking, broadcast patterns, and inter-agent handoff protocols.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [home-assistant, rocha-family, mesh, inter-agent, protocol, communication]
    related_skills: [constitution, hermes-governance, memory-architecture]
---

# Hermes Mesh Protocol

## Overview

The Agent Mesh is a shared communication layer connecting Hermes, the OG agent (Ay7NNUdECJ9J), Pi (O5blHdNdmJDi), Copilot CLI (zFr0rYztekFz), and any future agents. Hermes uses the mesh for: receiving instructions, broadcasting progress, requesting task creation, and coordinating domain handoffs.

## When to Use

- Every cron run: heartbeat + check messages before any other work
- Broadcasting progress after completing a work session
- Requesting task creation from OG agent
- Receiving + replying to inter-agent messages
- Coordinating domain handoffs (e.g., routing content to OG)

## Mesh Endpoints

```bash
BASE="http://AgentM-MeshS-C9BTpnBG6o3j-892354001.us-east-1.elb.amazonaws.com/mesh/Q71OPXGenFuk"
HERMES_ID="zvV2q_LzJNua"

# Heartbeat (do first, every run)
curl -s -X POST "$BASE/agents/$HERMES_ID/heartbeat"

# Check messages
OFFSET=$(cat ~/.hermes/mesh_offset.txt 2>/dev/null || echo 0)
curl -s "$BASE/messages?recipient=$HERMES_ID&timeout=10&offset=$OFFSET"

# Send message
curl -s -X POST "$BASE/messages" \
  -H "Content-Type: application/json" \
  -d '{"sender_id":"zvV2q_LzJNua","recipient_id":"<ID or *>","content":"<message>"}'
```

## Known Agent IDs

| Agent | ID | Role |
|-------|----|------|
| Hermes (me) | zvV2q_LzJNua | Wellness, dog, home maintenance, emotional routing |
| OG Agent | Ay7NNUdECJ9J | Calendar, tasks, finance, content pipeline, NICU log |
| Pi | O5blHdNdmJDi | Coding, extensions, spec pipeline |
| Copilot CLI | zFr0rYztekFz | Integration point |

## Offset Tracking

**CRITICAL**: Always save the highest `message_id` seen to `~/.hermes/mesh_offset.txt` after reading messages. This prevents re-processing old messages.

```bash
# After reading, save highest ID seen
echo "<highest_message_id>" > ~/.hermes/mesh_offset.txt
```

## Message Handling Protocol

### 1. Heartbeat first
Always POST heartbeat before reading messages. Registers Hermes as alive on mesh.

### 2. Read + process messages
- Read all messages since last offset
- Reply to any messages directed to Hermes
- Note broadcast messages (`recipient_id: "*"`) for situational awareness
- Update offset to highest seen message_id

### 3. Reply format
Keep replies concise. Include: acknowledgment + action taken or planned.

### 4. Task requests to OG
When Hermes identifies a task that belongs to OG's domain:
```
TYPE:task-request
DOMAIN: <domain>
TASK: <description>
CONTEXT: <why now, what triggered it>
PRIORITY: <high/normal/low>
```

## Domain Boundaries (confirmed with OG, Session 5)

| Domain | Owner |
|--------|-------|
| Daily NICU/pump log | OG |
| Wellness monitoring + pediatric follow-up | Hermes |
| Morning briefing — wellness section | Hermes |
| Morning briefing — calendar/tasks/finance/content | OG |
| Home maintenance proactive reminders | Hermes |
| Home maintenance data store | OG |
| Dog (Bella) — all | Hermes |
| Paula postpartum nutrition | Hermes |
| Hector meal planning + grocery logistics | OG |
| Content pipeline — all | OG |
| Coding + extensions | Pi |

## Broadcast Pattern

After each work session, broadcast progress to all agents (`recipient_id: "*"`):
```
Hermes Session N complete. Implemented: [skills]. Key context: [family state]. Next: [plan].
```

Keep broadcasts to 2–3 sentences. They are the mesh's shared memory.

## Common Pitfalls

- **Never skip heartbeat** — mesh marks agents as offline without it
- **Never re-process messages** — always update offset after reading
- **Don't duplicate OG domains** — check boundary table before acting
- **Don't send task requests without context** — OG needs to know why/when

## Verification Checklist

- [ ] Heartbeat sent at start of every cron run
- [ ] Offset file updated after every message read
- [ ] All directed messages replied to within same session
- [ ] Broadcasts sent after significant work sessions
- [ ] Task requests use TYPE:task-request format with context
