# 命令

## 概览

`install.sh` (Bash) 和 `install.ps1` (PowerShell) 支持相同的命令。

## 技能管理

### 列出可用技能

显示仓库中所有技能及其安装状态。

::: code-group
```bash [Linux/macOS]
./install.sh list
```
```powershell [Windows]
.\install.ps1 list
```
:::

### 列出已安装技能

显示当前已安装的技能及其来源。

::: code-group
```bash [Linux/macOS]
./install.sh installed
```
```powershell [Windows]
.\install.ps1 installed
```
:::

### 安装指定技能

按名称安装一个或多个技能。

::: code-group
```bash [Linux/macOS]
./install.sh install codex frontend-design
```
```powershell [Windows]
.\install.ps1 install codex frontend-design
```
:::

### 安装所有技能

一次性安装所有可用技能。

::: code-group
```bash [Linux/macOS]
./install.sh install-all
```
```powershell [Windows]
.\install.ps1 install-all
```
:::

### 交互模式

从编号列表中交互式选择技能。

::: code-group
```bash [Linux/macOS]
./install.sh interactive
```
```powershell [Windows]
.\install.ps1 interactive
```
:::

## 提示词管理

### 显示提示词差异

比较本地 `CLAUDE.md` 与全局版本。

::: code-group
```bash [Linux/macOS]
./install.sh prompt-diff
```
```powershell [Windows]
.\install.ps1 prompt-diff
```
:::

### 更新全局提示词

同步本地 `CLAUDE.md` 到 `~/.claude/CLAUDE.md`。会创建带时间戳的备份。

::: code-group
```bash [Linux/macOS]
./install.sh prompt-update
```
```powershell [Windows]
.\install.ps1 prompt-update
```
:::

## 目标选择

使用 `--target` (Bash) 或 `-Target` (PowerShell) 在 Claude 和 Codex 之间切换。

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

## 帮助

::: code-group
```bash [Linux/macOS]
./install.sh help
```
```powershell [Windows]
.\install.ps1 help
```
:::
