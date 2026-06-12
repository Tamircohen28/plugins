# Concepts

## What is a Claude Code plugin?

A Claude Code plugin is a directory published to GitHub that Claude Code can install at session start. A plugin can bundle:

- **Skills** — slash commands that give Claude a workflow (e.g. `/repo-polish`, `/debug`)
- **Hooks** — shell scripts that run automatically on events like session start or file save
- **MCP servers** — Model Context Protocol servers that give Claude access to external tools
- **Settings** — default keybindings, status line config, and permissions

## What is a marketplace?

A **marketplace** is a catalog file (`marketplace.json`) that lists multiple plugins by name and their source repos. Instead of installing each plugin directly from its GitHub URL, you add the marketplace once:

```bash
/plugin marketplace add Tamircohen28/plugins-catalog
```

Then install any listed plugin by name:

```bash
/plugin install tamirs-superpowers@tamirs-plugins
```

The `@tamirs-plugins` suffix tells Claude Code which marketplace to resolve the name from.

## How this catalog works

`tamirs-plugins` is a **catalog-only** repo. It contains nothing but a `marketplace.json` that points at each plugin's real repo. The actual plugin source (skills, hooks, MCP config) lives in those repos — this catalog just gives them a friendly name and keeps them discoverable in one place.

```
plugins-catalog/
  .claude-plugin/
    marketplace.json    ← the only file that matters
```

When you install a plugin from this catalog, Claude Code fetches it directly from the source repo listed in `marketplace.json`. Updates to plugin source repos are automatically picked up on the next install.

## Plugin inventory

| Plugin | What it does |
|--------|-------------|
| `tamirs-superpowers` | Core dev workflow — skills for planning, debugging, code review, and git worktrees |
| `jose-claudinho` | Fantasy World Cup AI — lineup/transfer/captain recommendations via Sport5 API |
| `headhunter` | Job search CRM — pipeline, interview prep, Gmail/Notion/Todoist integrations |
