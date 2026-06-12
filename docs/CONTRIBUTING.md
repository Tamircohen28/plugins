# Contributing

## Adding a plugin to the catalog

This repo is a catalog — all you need to do is add one entry to `.claude-plugin/marketplace.json`.

### Steps

1. Fork this repo and create a branch: `git checkout -b feat/add-<plugin-name>`

2. Open `.claude-plugin/marketplace.json` and add your plugin entry inside the `"plugins"` array:

```json
{
  "name": "your-plugin-name",
  "source": {
    "source": "github",
    "repo": "YourGitHubHandle/your-plugin-repo",
    "ref": "main"
  },
  "description": "One sentence describing what the plugin does."
}
```

3. Validate the JSON locally:

```bash
python3 -c "import json; json.load(open('.claude-plugin/marketplace.json')); print('OK')"
```

4. Open a pull request. CI will validate the schema automatically.

## Requirements for listed plugins

- Plugin must have a public GitHub repo
- Plugin must contain a `.claude-plugin/` directory with a valid `plugin.json`
- Plugin must not contain Wix-internal references, credentials, or proprietary IP
- Description must be one sentence, 10–100 characters

## Code of Conduct

Be respectful. This is a personal catalog — the maintainer reserves the right to decline additions that don't fit the project's scope.
