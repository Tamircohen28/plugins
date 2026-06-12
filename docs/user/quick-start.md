# Quick Start

Get all plugins installed in under 5 minutes.

## Prerequisites

- Claude Code installed (`npm install -g @anthropic-ai/claude-code` or via the desktop app)
- Authenticated: run `claude` and complete the login flow

## Step 1 — Add the marketplace

```bash
/plugin marketplace add Tamircohen28/plugins-catalog
```

You should see: `Marketplace "tamirs-plugins" added.`

## Step 2 — Install plugins

Install whichever plugins you need:

```bash
# Dev workflow superpowers (recommended for all users)
/plugin install tamirs-superpowers@tamirs-plugins

# Fantasy World Cup AI manager
/plugin install jose-claudinho@tamirs-plugins

# Job-search CRM
/plugin install headhunter@tamirs-plugins
```

## Step 3 — Verify

```bash
/doctor
```

All installed plugins should appear as healthy. If any show errors, see [Troubleshooting](troubleshooting.md).

## Step 4 — Use a skill

Open a new Claude Code session in any project and try:

```bash
/tamirs-superpowers:start-dev
```

or list available skills:

```bash
/help
```

## Updating plugins

Plugins are fetched from their source branch on install. To update:

```bash
/plugin update tamirs-superpowers
```
