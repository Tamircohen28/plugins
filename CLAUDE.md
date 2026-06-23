# CLAUDE.md — tamirs-plugins

Claude Code guidance for contributors working on this plugin catalog.

## What this repo is

A **catalog only** — it holds marketplace manifests that point to each plugin's own repository. No plugin source lives here.

## Key file locations

| Path | Purpose |
|------|---------|
| `.claude-plugin/marketplace.json` | Canonical Claude Code marketplace manifest (edit this) |
| `.agents/plugins/marketplace.json` | Codex marketplace manifest (generated) |
| `.cursor-plugin/marketplace.json` | Cursor team marketplace manifest (generated) |
| `scripts/generate-marketplaces.py` | Generator: Claude → Codex + Cursor |
| `scripts/validate-marketplaces.py` | Cross-platform manifest validation |
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
2. Run `make generate` to refresh Codex and Cursor manifests
3. Add a row to the table in `README.md`
4. Add a `CHANGELOG.md` entry under `[Unreleased]`
5. Validate: `make validate`

## Updating a plugin description

Edit `.claude-plugin/marketplace.json` directly, then run `make generate`. Descriptions are informational only; they don't affect install behavior.

## Commit convention

```
<type>: <description>

Co-Authored-By: Claude <noreply@anthropic.com>
```

Types: `feat` (new plugin), `fix` (correction), `chore` (description update), `docs`

## Hard constraints

- **Never add plugin source code here** — plugins live in their own repos
- **Never change `"source": "github"`** in the Claude manifest — this is the only supported source type
- **Always run `make validate`** before committing — CI will reject out-of-sync manifests
- **Never commit secrets or tokens**
