# 插件

Claude Code 支持插件系统，通过社区贡献的技能和工具扩展其功能。

## 插件市场

插件市场是托管插件集合的仓库。你可以添加多个市场来发现和安装插件。

| 市场 | 仓库 | 可用数量 | 描述 |
|------|------|----------|------|
| claude-code-workflows | [wshobson/agents](https://github.com/wshobson/agents) | 67 | 工作流集合 |
| claude-hud | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | 1 | HUD 显示增强 |
| claude-plugins-official ⭐ | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | 40 | Anthropic 官方插件集 |
| daymade-skills | [daymade/claude-code-skills](https://github.com/daymade/claude-code-skills) | 26 | 技能集合 |

## 推荐插件

### 官方插件 (claude-plugins-official)

| 插件 | 描述 |
|------|------|
| code-review | 代码审查助手 |
| context7 | 上下文管理 |
| feature-dev | 功能开发辅助 |
| frontend-design | 前端设计助手 |
| pyright-lsp | Python 语言服务器支持 |
| rust-analyzer-lsp | Rust 语言服务器支持 |
| serena | Serena 助手 |
| typescript-lsp | TypeScript 语言服务器支持 |

### 社区插件

| 插件 | 来源 | 描述 |
|------|------|------|
| claude-hud | claude-hud | Claude Code HUD 显示增强 |
| skill-creator | daymade-skills | 技能创建工具 |

## 使用方法

在 Claude Code 中使用 `/plugin` 命令管理插件：

```
> /plugin
```

### 导航

- `Discover` - 浏览可用插件
- `Installed` - 查看已安装插件
- `Marketplaces` - 管理插件市场
- `Errors` - 查看错误日志

### 快捷键

| 按键 | 操作 |
|------|------|
| `Tab` | 切换标签页 |
| `Space` | 切换选中 |
| `Enter` | 查看详情 |
| `Delete` | 卸载插件 |
| `Esc` | 返回 |

## 添加插件市场

1. 使用 `/plugin` 打开插件管理器
2. 切换到 `Marketplaces` 标签页
3. 选择 `+ Add Marketplace`
4. 输入仓库地址，格式为 `owner/repo`
