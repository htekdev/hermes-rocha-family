# Finance Manager — Working Memory

> Updated: 2026-06-02 (Session 5)
> Last updated by: Hermes cron job

---

## Current State

### Hermes Role in Finance
- **Monitor only** — Hermes does NOT own finance execution
- Execution domain: OG Copilot agent (Ay7NNUdECJ9J)
- Hermes surfaces wellness-related financial concerns (e.g., NICU costs, baby supplies runout)

### Known Financial Context
- NICU stay: Extended premature birth — significant insurance/billing complexity expected
- Medical bills: Multiple (twins born April 16, ~10 weeks preterm)
- Auto-pay bills: Do NOT create reminder tasks for auto-pay items
- Baby supply burn rate: Elevated post-discharge (formula, diapers, medical supplies)

### Finance-Related Wellness Flags
- Postpartum/NICU stress is financially driven in part
- When Hector mentions financial stress → acknowledge + offer to surface specific actionable data (not advice)

---

## Pending Flags
- [ ] Leo discharge will trigger increased baby supply spending — flag to OG agent
- [ ] NICU billing reconciliation (insurance EOBs) — flag when home

---

## Do Not Duplicate
- Bill tracking → OG agent
- Grocery costs → OG agent (meal-planner)
- Task creation for financial actions → always use TYPE:task-request to OG agent
