# Troubleshooting

## `/plugin marketplace add` fails

**Symptom**: `Error: could not fetch marketplace from Tamircohen28/plugins-catalog`

**Fixes**:
1. Confirm you are authenticated: run `/status` and check your GitHub connection
2. Confirm network access to `github.com`
3. Try again — transient GitHub API rate limits can cause this

---

## Plugin installs but skills don't appear

**Symptom**: `/plugin install` succeeds but `/tamirs-superpowers:start-dev` is not found

**Fix**: Open a **new** Claude Code session. Plugins are loaded at session start, not mid-session.

---

## `/doctor` shows a plugin as unhealthy

**Symptom**: `[WARN] tamirs-superpowers: missing required field 'version'` or similar

**Fix**: Update the plugin to get the latest manifest:
```bash
/plugin update tamirs-superpowers
```

If the error persists, open an issue in the plugin's own repo (not this catalog).

---

## `@tamirs-plugins` not recognized

**Symptom**: `/plugin install headhunter@tamirs-plugins` returns `unknown marketplace`

**Fix**: You skipped Step 1. Add the marketplace first:
```bash
/plugin marketplace add Tamircohen28/plugins-catalog
```

---

## Getting more help

- Open an issue in [this repo](https://github.com/Tamircohen28/plugins-catalog/issues) for catalog-level problems (wrong repo URL, missing plugin entry)
- Open an issue in the plugin's own repo for plugin-level bugs
