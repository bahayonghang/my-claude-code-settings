# MyClaude Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A curated collection of Claude Code skills and prompts for enhanced AI-assisted development workflows.

## Features

- 🎯 Reusable AI skill modules covering frontend design, research, documentation, and more
- 📦 Unified skill format (`SKILL.md`) for easy extension and maintenance
- 🔄 Cross-platform Python installation script (`install.py`)
- 🎛️ Multi-target support: Claude Code (`~/.claude/`), Codex CLI (`~/.codex/`), and Gemini CLI (`~/.gemini/`)
- ⚡ Slash commands for common workflows (git commit, etc.)

## Prerequisites

- Git
- Python 3.6+
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Codex CLI](https://github.com/openai/codex), or [Gemini CLI](https://geminicli.com)

## Quick Start

```bash
# Clone the repository
git clone https://github.com/anthropics/my-claude-skills.git
cd my-claude-skills

# Install all skills
python3 install.py install-all

# Update global prompt configuration
python3 install.py prompt-update

# Or use the TUI for interactive management
python3 install_tui.py
```

Run `python3 install.py --help` for more options.

## Skills

| Skill | Description |
|-------|-------------|
| [article-cover](skills/article-cover/) | Generate professional SVG cover images for blog posts and articles |
| [codex](skills/codex/) | Codex CLI integration for deep code analysis and web search |
| [excalidraw](skills/excalidraw/) | Create hand-drawn style diagrams as Excalidraw JSON files |
| [frontend-design](skills/frontend-design/) | Build distinctive, production-grade frontend interfaces |
| [gemini-image](skills/gemini-image/) | AI image generation via Gemini API (text-to-image, image-to-image) |
| [research](skills/research/) | Technical research with web search and citation support |
| [spec-interview](skills/spec-interview/) | Deep interview to refine technical specs through systematic questioning |
| [paper-replication](skills/paper-replication/) | Replicate deep learning papers into industrial-grade PyTorch code with detailed module documentation |
| [tech-blog](skills/tech-blog/) | Write technical blog posts with source code analysis |
| [tech-design-doc](skills/tech-design-doc/) | Generate structured technical design documents |

## Commands

Slash commands provide quick access to common workflows. Install them to `~/.claude/commands/`.

| Command | Description |
|---------|-------------|
| [git-commit](commands/git-commit.md) | Analyze changes and generate Conventional Commits messages (optional emoji) |

### OMO Agents (Multi-Agent System)

Inspired by [oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode), these skills enable multi-agent collaboration where specialized agents work together on complex tasks.

| Skill | Description |
|-------|-------------|
| [omo-agents](skills/omo-agents/) | Multi-agent orchestration system overview and usage guide |
| [sisyphus](skills/sisyphus/) | Main orchestrator for complex task planning and parallel execution |
| [oracle](skills/oracle/) | Expert architect for design decisions, code review, and debugging |
| [explore](skills/explore/) | Fast code search agent for locating code and tracing dependencies |
| [librarian](skills/librarian/) | Documentation researcher for external docs and best practices |
| [frontend-engineer](skills/frontend-engineer/) | UI/UX expert for creating beautiful, polished interfaces |
| [document-writer](skills/document-writer/) | Technical writer for README, API docs, and architecture docs |
| [multimodal-looker](skills/multimodal-looker/) | Visual analyst for images, PDFs, charts, and diagrams |

## Installation

### Basic Installation

```bash
git clone https://github.com/anthropics/my-claude-skills.git
cd my-claude-skills

# Install all skills to Claude (default)
python3 install.py install-all

# Install to Gemini
python3 install.py --target gemini install-all

# Install to Codex
python3 install.py --target codex install-all

# Update global CLAUDE.md
python3 install.py prompt-update
```

## Commands

| Command | Description |
|---------|-------------|
| `python3 install.py list` | List all available skills |
| `python3 install.py installed` | List currently installed skills |
| `python3 install.py install <skill> [skill2...]` | Install specific skill(s) |
| `python3 install.py install-all` | Install all skills |
| `python3 install.py interactive` | Interactive skill selection |
| `python3 install.py prompt-diff` | Show diff between local and global CLAUDE.md |
| `python3 install.py prompt-update` | Sync CLAUDE.md to ~/.claude/ |
| `python3 install.py --target gemini <command>` | Run command targeting Gemini |

### TUI Mode (Recommended)

For a more user-friendly experience, use the TUI (Terminal User Interface):

```bash
python3 install_tui.py
```

The TUI provides:
- 🎯 Visual platform selection (Claude/Codex/Gemini)
- 📋 Tabbed interface for Skills and Commands
- ⌨️ Keyboard shortcuts for quick operations
- 🔍 Real-time search filtering
- ✅ Multi-select batch installation

**TUI Keyboard Shortcuts:**

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

**Requirements:** Python 3.10+ and [Textual](https://textual.textualize.io/) library (`pip install textual`)

## Project Structure

```
.
├── install.py              # Unified Python installer
├── prompts/
│   ├── CLAUDE.md           # Global workflow configuration
│   └── TRANSLATE.md        # Translation guidelines
├── commands/               # Slash commands
│   └── git-commit.md       # Git commit command
└── skills/
    └── <skill-name>/
        ├── SKILL.md        # Skill definition (required)
        ├── config/         # Configuration templates (optional)
        ├── tips/           # Usage tips (optional)
        ├── references/     # Reference documents (optional)
        ├── scripts/        # Helper scripts (optional)
        └── cookbook/       # Code examples (optional)
```

## Prompts

### CLAUDE.md

Global workflow configuration based on Linus Torvalds-style engineering principles:
- KISS/YAGNI enforcement
- Structured workflow (intake → context → exploration → planning → execution → verification → handoff)
- Online search integration via Codex
- Self-reflection checklist before handoff

### TRANSLATE.md

Technical content translation guidelines:
- Natural phrasing over literal translation
- Preserve code, brands, and established technical terms
- Handle ambiguous terms with annotations

## Contributing

### Adding a New Skill

1. Create a new directory under `skills/`:
   ```bash
   mkdir skills/my-new-skill
   ```

2. Create `SKILL.md` with YAML frontmatter:
   ```yaml
   ---
   name: my-new-skill
   description: Brief description for listing
   license: MIT  # optional
   ---

   # My New Skill

   Detailed instructions and documentation...
   ```

3. (Optional) Add supporting directories:
   - `config/` - Configuration templates
   - `tips/` - Usage tips
   - `references/` - Technical references
   - `scripts/` - Helper scripts
   - `cookbook/` - Code examples

4. Test installation:
   ```bash
   ./install.sh install my-new-skill
   ```

### Guidelines

- Keep `SKILL.md` focused and actionable
- Use clear, concise language
- Include examples where helpful
- Follow existing skill patterns for consistency

## FAQ

**Q: What's the difference between Claude, Codex, and Gemini targets?**

A: The target determines the installation directory:
- Claude: `~/.claude/skills/` (default)
- Codex: `~/.codex/skills/`
- Gemini: `~/.gemini/skills/`

**Q: How do I update an existing skill?**

A: Simply run the install command again. It will overwrite the existing skill with the latest version.

**Q: Can I use skills from multiple sources?**

A: Yes. The `installed` command shows which skills come from this repository vs external sources.

**Q: Where is the backup stored when updating CLAUDE.md?**

A: Backups are created in `~/.claude/` with timestamp suffix, e.g., `CLAUDE.md.backup.20240115_143022`.

## License

MIT
