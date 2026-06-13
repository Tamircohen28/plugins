# CLAUDE.md — tamirs-plugins

Claude Code guidance for contributors working on this plugin catalog.

## What this repo is

A **catalog only** — it holds a single `.claude-plugin/marketplace.json` that points to each plugin's own repository. No plugin source lives here.

## Key file locations

| Path | Purpose |
|------|---------|
| `.claude-plugin/marketplace.json` | Marketplace manifest — lists all plugins with their repo pointers |
| `README.md` | User-facing install instructions |
| `CHANGELOG.md` | Version history |

## Adding a plugin

1. Edit `.claude-plugin/marketplace.json` — add an entry to the `plugins` array:
   ```json
   {
     "name": "my-plugin",
     "source": { "source": "github", "repo": "Tamircohen28/my-plugin", "ref": "main" },
     "description": "One-line description."
   }
   ```
2. Add a row to the table in `README.md`
3. Add a `CHANGELOG.md` entry under `[Unreleased]`
4. Validate JSON: `python3 -m json.tool .claude-plugin/marketplace.json`

## Updating a plugin description

Edit `.claude-plugin/marketplace.json` directly — descriptions are informational only; they don't affect install behavior.

## Commit convention

```
<type>: <description>

Co-Authored-By: Claude <noreply@anthropic.com>
```

Types: `feat` (new plugin), `fix` (correction), `chore` (description update), `docs`

## Hard constraints

- **Never add plugin source code here** — plugins live in their own repos
- **Never change `"source": "github"`** — this is the only supported source type
- **Always validate JSON** before committing — CI will reject invalid JSON
- **Never commit secrets or tokens**
