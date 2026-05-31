# Hermes Rocha Family

Third iteration of the Rocha Family home assistant, built on [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent).

## Purpose

This repo holds the Rocha-family-specific project instructions and persona templates used by Hermes on the dedicated AWS VM.

## Repo layout

- `AGENTS.md` — repo-specific behavior, workflows, and operating rules for Hermes when working in this repo
- `templates/SOUL.md` — durable identity/persona template to deploy to `~/.hermes/SOUL.md`

## VM deployment

Current Hermes VM:

- Instance: `i-06bae602c58483eb2`
- Region: `us-east-1`
- Public IP: `98.92.123.91`
- Type: `t4g.micro`
- OS: Ubuntu 24.04 ARM64
- Repo path on VM: `~/hermes-rocha-family`
- Hermes home: `~/.hermes`

## Quick start on the VM

```bash
cd ~/hermes-rocha-family
cp templates/SOUL.md ~/.hermes/SOUL.md
export PATH="$HOME/.local/bin:$HOME/.hermes/node/bin:$PATH"
hermes chat -q "Reply with pong" --provider copilot --model claude-sonnet-4.6 --quiet
```

## Secrets

Secrets are **not committed**. The active runtime reads from:

- `~/.hermes/.env` — Hermes runtime secrets
- `~/hermes-rocha-family/.env` — project-local copy for operational convenience

## Telegram note

Hermes supports Telegram natively, but bot-token cutover must be coordinated with the existing Pi deployment if they share the same token.
