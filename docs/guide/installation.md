# Installation

## Prerequisites

- Git
- Bash (Linux/macOS) or PowerShell (Windows)
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) or [Codex CLI](https://github.com/openai/codex)

## Clone Repository

```bash
git clone https://github.com/anthropics/my-claude-skills.git
cd my-claude-skills
```

## Linux/macOS

### Install All Skills

```bash
./install.sh install-all
```

### Install to Codex

```bash
./install.sh --target=codex install-all
```

### Update Global Prompt

```bash
./install.sh prompt-update
```

## Windows (PowerShell)

### Install All Skills

```powershell
.\install.ps1 install-all
```

### Install to Codex

```powershell
.\install.ps1 -Target codex install-all
```

### Update Global Prompt

```powershell
.\install.ps1 prompt-update
```

## Verify Installation

Check installed skills:

::: code-group
```bash [Linux/macOS]
./install.sh installed
```
```powershell [Windows]
.\install.ps1 installed
```
:::

## Installation Paths

| Target | Path |
|--------|------|
| Claude | `~/.claude/skills/` |
| Codex | `~/.codex/skills/` |
