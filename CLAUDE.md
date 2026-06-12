# Claude Code — plugins-catalog

## Overview

This is a **catalog-only** repo. It holds a single `.claude-plugin/marketplace.json` that lists Tamir's Claude Code plugins, each sourced from its own GitHub repository. There is no runnable code here — the only "build" is JSON validation.

## Key files

| Path | Purpose |
|------|---------|
| `.claude-plugin/marketplace.json` | The marketplace manifest — the only file that matters |
| `docs/user/concepts.md` | Explains the marketplace model |
| `.github/workflows/ci.yml` | Validates the JSON on every push |

## Commands

| Action | Command |
|--------|---------|
| Validate manifest | `python3 -c "import json; json.load(open('.claude-plugin/marketplace.json')); print('OK')"` |
| Install all plugins | `/plugin marketplace add Tamircohen28/plugins-catalog` |

## Commit convention

```
feat: add <plugin-name> to catalog
fix: correct <plugin-name> source ref
chore: bump <plugin-name> ref to <branch>
```

## Hard constraints

- Never add runnable code to this repo — it is a catalog only
- Never change `owner.github` away from `Tamircohen28`
- Never add Wix-internal URLs, registries, or credentials
- The `$schema` field in `marketplace.json` must always point to the official Claude Code schema
