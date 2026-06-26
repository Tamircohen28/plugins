# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2026-06-26

### Added
- Codex and Cursor marketplace manifests generated from the canonical Claude manifest
- Generator and validation scripts with `make generate` and `make validate` targets

### Changed
- Banner SVG: corrected repo name (`plugins-catalog` → `plugins`) and replaced hardcoded plugin list with platform description (`Claude Code · Cursor · Codex`)

## [1.0.0] - 2026-06-13

### Added
- Initial marketplace catalog with three plugins: `tamirs-superpowers`, `jose-claudinho`, `headhunter`
- `marketplace.json` validated against the official Claude Code schema
- CI workflow for JSON validation on every push
