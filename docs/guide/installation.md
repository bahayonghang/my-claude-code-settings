# Installation

## Prerequisites

- Git
- Python 3.6+
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Codex CLI](https://github.com/openai/codex), [Gemini CLI](https://geminicli.com), or [Qwen Code](https://qwenlm.github.io/qwen-code-docs/)

## Clone Repository

```bash
git clone https://github.com/anthropics/my-claude-skills.git
cd my-claude-skills
```

## Basic Usage

### Install All Skills

```bash
# Default target is Claude
python3 install.py install-all
```

### Install to Specific Target

```bash
# Install to Gemini
python3 install.py --target gemini install-all

# Install to Codex
python3 install.py --target codex install-all

# Install to Qwen
python3 install.py --target qwen install-all
```

### Update Global Prompt

```bash
python3 install.py prompt-update
```

### Interactive Mode

```bash
python3 install.py interactive
```

## TUI Mode (Recommended)

For a modern, visual experience, use the TUI (Terminal User Interface):

```bash
python3 install_tui.py
```

### Features

- 🎯 Visual platform selection (Claude/Codex/Gemini/Qwen)
- 📋 Tabbed interface for Skills and Commands
- ⌨️ Keyboard shortcuts for quick operations
- 🔍 Real-time search filtering
- ✅ Multi-select batch installation

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Tab` | Switch between Skills/Commands tabs |
| `i` / `Enter` | Install focused item |
| `Space` | Toggle selection |
| `s` | Install selected items |
| `a` | Install all items |
| `Ctrl+A` | Select all |
| `Ctrl+D` | Deselect all |
| `/` | Search |
| `t` | Switch platform |
| `q` | Quit |

### Requirements

- Python 3.10+
- [Textual](https://textual.textualize.io/) library

```bash
pip install textual
```

## Verify Installation

Check installed skills:

```bash
python3 install.py installed
```

## Installation Paths

| Target | Path |
|--------|------|
| Claude | `~/.claude/skills/` |
| Codex | `~/.codex/skills/` |
| Gemini | `~/.gemini/skills/` |
| Qwen | `~/.qwen/skills/` |
