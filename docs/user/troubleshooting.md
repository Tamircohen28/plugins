# Troubleshooting

## Claude Code

### `/plugin marketplace add` fails

**Symptom**: `Error: could not fetch marketplace from Tamircohen28/plugins`

**Fixes**:
1. Confirm you are authenticated: run `/status` and check your GitHub connection
2. Confirm network access to `github.com`
3. Try again — transient GitHub API rate limits can cause this

### Plugin installs but skills don't appear

**Symptom**: `/plugin install` succeeds but skills are not found

**Fix**: Open a **new** Claude Code session. Plugins are loaded at session start, not mid-session.

### `@tamirs-plugins` not recognized

**Symptom**: `/plugin install headhunter@tamirs-plugins` returns `unknown marketplace`

**Fix**: Add the marketplace first:

```bash
claude plugin marketplace add Tamircohen28/plugins
```

---

## Codex

### Marketplace add succeeds but no plugins listed

**Symptom**: `codex plugin list --source plugins` is empty

**Fixes**:
1. Confirm you used `--sparse .agents/plugins` when adding the marketplace
2. Confirm each plugin repo has `.codex-plugin/plugin.json`
3. Upgrade the marketplace snapshot: `codex plugin marketplace upgrade plugins`

### Plugin install fails with manifest error

**Symptom**: Codex cannot resolve the plugin from the marketplace entry

**Fix**: Open an issue in the plugin's own repo — the catalog only points at it; the plugin manifest must be valid Codex format.

---

## Cursor

### Team marketplace import finds no plugins

**Symptom**: Import parses zero plugins from this repo

**Fixes**:
1. Confirm `.cursor-plugin/marketplace.json` exists on the `main` branch
2. Confirm each plugin repo has `.cursor-plugin/plugin.json`
3. Click **Refresh** in Dashboard → Settings → Plugins after pushing catalog changes

### Local plugin does not load

**Symptom**: Symlinked plugin under `~/.cursor/plugins/local/` has no skills or rules

**Fixes**:
1. Confirm `.cursor-plugin/plugin.json` exists at the plugin root
2. Run **Developer: Reload Window**
3. Check **Settings → Rules** and **Settings → MCP** for loaded components

---

## General

### `/doctor` or health check shows a plugin as unhealthy

**Fix**: Update the plugin to get the latest manifest:

```bash
claude plugin update tamirs-superpowers
```

If the error persists, open an issue in the plugin's own repo (not this catalog).

### Getting more help

- Open an issue in [this repo](https://github.com/Tamircohen28/plugins/issues) for catalog-level problems (wrong repo URL, missing plugin entry)
- Open an issue in the plugin's own repo for plugin-level bugs
