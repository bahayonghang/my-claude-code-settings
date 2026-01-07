# Plugins

Claude Code supports a plugin system that extends its capabilities through community-contributed skills and tools.

## Plugin Marketplaces

Marketplaces are repositories that host collections of plugins. You can add multiple marketplaces to discover and install plugins.

| Marketplace | Repository | Available | Description |
|-------------|------------|-----------|-------------|
| claude-code-workflows | [wshobson/agents](https://github.com/wshobson/agents) | 67 | Workflow collection |
| claude-hud | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | 1 | HUD display enhancement |
| claude-plugins-official ⭐ | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | 40 | Official Anthropic plugins |
| daymade-skills | [daymade/claude-code-skills](https://github.com/daymade/claude-code-skills) | 26 | Skills collection |

## Recommended Plugins

### Official Plugins (claude-plugins-official)

| Plugin | Description |
|--------|-------------|
| code-review | Code review assistant |
| context7 | Context management |
| feature-dev | Feature development helper |
| frontend-design | Frontend design assistant |
| pyright-lsp | Python language server support |
| rust-analyzer-lsp | Rust language server support |
| serena | Serena assistant |
| typescript-lsp | TypeScript language server support |

### Community Plugins

| Plugin | Source | Description |
|--------|--------|-------------|
| claude-hud | claude-hud | HUD display enhancement for Claude Code |
| skill-creator | daymade-skills | Tool for creating new skills |

## Usage

Use the `/plugin` command in Claude Code to manage plugins:

```
> /plugin
```

### Navigation

- `Discover` - Browse available plugins
- `Installed` - View installed plugins
- `Marketplaces` - Manage plugin sources
- `Errors` - View error logs

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Tab` | Cycle through tabs |
| `Space` | Toggle selection |
| `Enter` | View details |
| `Delete` | Uninstall plugin |
| `Esc` | Go back |

## Adding a Marketplace

1. Open the plugin manager with `/plugin`
2. Navigate to `Marketplaces` tab
3. Select `+ Add Marketplace`
4. Enter the repository in format `owner/repo`
