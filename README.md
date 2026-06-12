<p align="center">
  <img src="assets/banner.png" alt="tamirs-plugins banner" width="600" />
</p>

<h1 align="center">tamirs-plugins</h1>

<p align="center">
  <a href="https://github.com/Tamircohen28/plugins-catalog/actions/workflows/ci.yml">
    <img src="https://github.com/Tamircohen28/plugins-catalog/actions/workflows/ci.yml/badge.svg" alt="CI" />
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT" />
  </a>
  <img src="https://img.shields.io/badge/Claude%20Code-Plugin%20Catalog-blueviolet" alt="Claude Code Plugin Catalog" />
</p>

<p align="center">
  A unified <a href="https://docs.anthropic.com/en/docs/claude-code">Claude Code</a> plugin marketplace for <a href="https://github.com/Tamircohen28">@Tamircohen28</a> — one <code>marketplace add</code> command installs everything.
</p>

---

## Features

- **Single install point** — add one marketplace to get all plugins, no per-repo configuration
- **Catalog only** — this repo holds only `marketplace.json`; plugin source lives in each plugin's own repo
- **Auto-updated** — each plugin entry pins a branch so you always get the latest compatible version
- **Schema-validated** — CI validates the manifest on every push against the official Claude Code marketplace schema
- **Three production plugins** — superpowers, fantasy football AI, and a job-search CRM ready to install

## Plugins

| Plugin | Repo | Description |
|--------|------|-------------|
| `tamirs-superpowers` | [Tamircohen28/tamirs-superpowers](https://github.com/Tamircohen28/tamirs-superpowers) | Skills, smart worktree hooks, statusline, and MCP stubs for a full dev workflow. |
| `jose-claudinho` | [Tamircohen28/jose-claudinho](https://github.com/Tamircohen28/jose-claudinho) | AI manager for Sport5 Fantasy World Cup 2026. |
| `headhunter` | [Tamircohen28/headhunter](https://github.com/Tamircohen28/headhunter) | Job-search CRM with Gmail/Calendar/Notion/Todoist integrations. |

## Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed and authenticated
- `claude` CLI accessible in your terminal

## Quick Start

```bash
# 1. Add this marketplace to Claude Code
/plugin marketplace add Tamircohen28/plugins-catalog

# 2. Install the plugins you want
/plugin install tamirs-superpowers@tamirs-plugins
/plugin install jose-claudinho@tamirs-plugins
/plugin install headhunter@tamirs-plugins

# 3. Verify installation
/doctor
```

## Documentation

Full user guide, concepts, and troubleshooting are in [`docs/`](docs/README.md).

## Contributing

See [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md) — adding a new plugin is a one-file change.

## License

MIT © [Tamir Cohen](https://github.com/Tamircohen28)
