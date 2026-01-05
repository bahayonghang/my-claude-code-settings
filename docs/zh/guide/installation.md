# 安装

## 前置要求

- Git
- Bash (Linux/macOS) 或 PowerShell (Windows)
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) 或 [Codex CLI](https://github.com/openai/codex)

## 克隆仓库

```bash
git clone https://github.com/anthropics/my-claude-skills.git
cd my-claude-skills
```

## Linux/macOS

### 安装所有技能

```bash
./install.sh install-all
```

### 安装到 Codex

```bash
./install.sh --target=codex install-all
```

### 更新全局提示词

```bash
./install.sh prompt-update
```

## Windows (PowerShell)

### 安装所有技能

```powershell
.\install.ps1 install-all
```

### 安装到 Codex

```powershell
.\install.ps1 -Target codex install-all
```

### 更新全局提示词

```powershell
.\install.ps1 prompt-update
```

## 验证安装

检查已安装的技能：

::: code-group
```bash [Linux/macOS]
./install.sh installed
```
```powershell [Windows]
.\install.ps1 installed
```
:::

## 安装路径

| 目标 | 路径 |
|------|------|
| Claude | `~/.claude/skills/` |
| Codex | `~/.codex/skills/` |
