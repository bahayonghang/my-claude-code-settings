# Commands

## Overview

Both `install.sh` (Bash) and `install.ps1` (PowerShell) support the same commands.

## Skill Management

### List Available Skills

Shows all skills in the repository with installation status.

::: code-group
```bash [Linux/macOS]
./install.sh list
```
```powershell [Windows]
.\install.ps1 list
```
:::

### List Installed Skills

Shows currently installed skills and their source.

::: code-group
```bash [Linux/macOS]
./install.sh installed
```
```powershell [Windows]
.\install.ps1 installed
```
:::

### Install Specific Skills

Install one or more skills by name.

::: code-group
```bash [Linux/macOS]
./install.sh install codex frontend-design
```
```powershell [Windows]
.\install.ps1 install codex frontend-design
```
:::

### Install All Skills

Install all available skills at once.

::: code-group
```bash [Linux/macOS]
./install.sh install-all
```
```powershell [Windows]
.\install.ps1 install-all
```
:::

### Interactive Mode

Select skills interactively from a numbered list.

::: code-group
```bash [Linux/macOS]
./install.sh interactive
```
```powershell [Windows]
.\install.ps1 interactive
```
:::

## Prompt Management

### Show Prompt Diff

Compare local `CLAUDE.md` with the global version.

::: code-group
```bash [Linux/macOS]
./install.sh prompt-diff
```
```powershell [Windows]
.\install.ps1 prompt-diff
```
:::

### Update Global Prompt

Sync local `CLAUDE.md` to `~/.claude/CLAUDE.md`. Creates a timestamped backup.

::: code-group
```bash [Linux/macOS]
./install.sh prompt-update
```
```powershell [Windows]
.\install.ps1 prompt-update
```
:::

## Target Selection

Use `--target` (Bash) or `-Target` (PowerShell) to switch between Claude and Codex.

::: code-group
```bash [Linux/macOS]
./install.sh --target=codex list
./install.sh --target=codex install-all
```
```powershell [Windows]
.\install.ps1 -Target codex list
.\install.ps1 -Target codex install-all
```
:::

## Help

::: code-group
```bash [Linux/macOS]
./install.sh help
```
```powershell [Windows]
.\install.ps1 help
```
:::
