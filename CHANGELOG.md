# Changelog

All notable changes to the tamirs-plugins catalog are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [Unreleased]

### Added
- Codex marketplace manifest at `.agents/plugins/marketplace.json`
- Cursor team marketplace manifest at `.cursor-plugin/marketplace.json`
- `scripts/generate-marketplaces.py` and `scripts/validate-marketplaces.py`
- `make generate` and `make validate` targets
- Multi-platform install instructions for Claude Code, Codex, and Cursor

### Changed
- CI validates all three marketplace manifests and fails on generator drift
- Release workflow regenerates Codex and Cursor manifests when bumping version

---

## [1.0.0] — 2025-06-01

### Added
- Initial catalog with three plugins: `tamirs-superpowers`, `jose-claudinho`, `headhunter`
- `allowCrossMarketplaceDependenciesOn` for `superpowers-dev` marketplace (enables `tamirs-superpowers` dependency auto-install)
