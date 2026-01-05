# MyClaude Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A curated collection of Claude Code skills and prompts for enhanced AI-assisted development workflows.

## Features

- 🎯 Reusable AI skill modules covering frontend design, research, documentation, and more
- 📦 Unified skill format (`SKILL.md`) for easy extension and maintenance
- 🔄 Cross-platform installation scripts (Bash + PowerShell)
- 🎛️ Dual target support: Claude Code (`~/.claude/`) and Codex CLI (`~/.codex/`)

## Prerequisites

- Git
- Bash (Linux/macOS) or PowerShell (Windows)
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) or [Codex CLI](https://github.com/openai/codex)

## Quick Start

```bash
# Clone the repository
git clone https://github.com/anthropics/my-claude-skills.git
cd my-claude-skills

# Install all skills
./install.sh install-all

# Update global prompt configuration
./install.sh prompt-update
```

Run `./install.sh help` for more options.

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
| [tech-blog](skills/tech-blog/) | Write technical blog posts with source code analysis |
| [tech-design-doc](skills/tech-design-doc/) | Generate structured technical design documents |

## Installation

### Linux/macOS

```bash
git clone https://github.com/anthropics/my-claude-skills.git
cd my-claude-skills

# Install all skills to Claude
./install.sh install-all

# Or install to Codex
./install.sh --target=codex install-all

# Update global CLAUDE.md
./install.sh prompt-update
```

### Windows (PowerShell)

```powershell
git clone https://github.com/anthropics/my-claude-skills.git
cd my-claude-skills

# Install all skills to Claude
.\install.ps1 install-all

# Or install to Codex
.\install.ps1 -Target codex install-all

# Update global CLAUDE.md
.\install.ps1 prompt-update
```

## Commands

### Linux/macOS (Bash)

| Command | Description |
|---------|-------------|
| `./install.sh list` | List all available skills |
| `./install.sh installed` | List currently installed skills |
| `./install.sh install <skill> [skill2...]` | Install specific skill(s) |
| `./install.sh install-all` | Install all skills |
| `./install.sh interactive` | Interactive skill selection |
| `./install.sh prompt-diff` | Show diff between local and global CLAUDE.md |
| `./install.sh prompt-update` | Sync CLAUDE.md to ~/.claude/ |
| `./install.sh --target=codex <command>` | Run command targeting Codex |

### Windows (PowerShell)

| Command | Description |
|---------|-------------|
| `.\install.ps1 list` | List all available skills |
| `.\install.ps1 installed` | List currently installed skills |
| `.\install.ps1 install <skill> [skill2...]` | Install specific skill(s) |
| `.\install.ps1 install-all` | Install all skills |
| `.\install.ps1 interactive` | Interactive skill selection |
| `.\install.ps1 prompt-diff` | Show diff between local and global CLAUDE.md |
| `.\install.ps1 prompt-update` | Sync CLAUDE.md to ~/.claude/ |
| `.\install.ps1 -Target codex <command>` | Run command targeting Codex |

## Project Structure

```
.
├── install.sh              # Bash installer (Linux/macOS)
├── install.ps1             # PowerShell installer (Windows)
├── prompts/
│   ├── CLAUDE.md           # Global workflow configuration
│   └── TRANSLATE.md        # Translation guidelines
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

**Q: What's the difference between Claude and Codex targets?**

A: Claude target installs to `~/.claude/skills/` for Claude Code, while Codex target installs to `~/.codex/skills/` for OpenAI Codex CLI. The skill format is compatible with both.

**Q: How do I update an existing skill?**

A: Simply run the install command again. It will overwrite the existing skill with the latest version.

**Q: Can I use skills from multiple sources?**

A: Yes. The `installed` command shows which skills come from this repository vs external sources.

**Q: Where is the backup stored when updating CLAUDE.md?**

A: Backups are created in `~/.claude/` with timestamp suffix, e.g., `CLAUDE.md.backup.20240115_143022`.

## License

MIT
