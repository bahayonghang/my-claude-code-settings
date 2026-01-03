# MyClaude Skills

A curated collection of Claude Code skills and prompts for enhanced AI-assisted development workflows.

## Quick Start

```bash
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
| [github-wrapped](skills/github-wrapped/) | Generate verifiable GitHub year-in-review as single-file HTML |
| [research](skills/research/) | Technical research with web search and citation support |
| [spec-interview](skills/spec-interview/) | Deep interview to refine technical specs through systematic questioning |
| [tech-blog](skills/tech-blog/) | Write technical blog posts with source code analysis |
| [tech-design-doc](skills/tech-design-doc/) | Generate structured technical design documents |

## Project Structure

```
.
├── install.sh              # Skill installer and prompt sync tool
├── install.ps1             # PowerShell installer for Windows
├── prompts/
│   ├── CLAUDE.md           # Global workflow configuration
│   └── TRANSLATE.md        # Translation guidelines
└── skills/
    └── <skill-name>/
        └── SKILL.md        # Skill definition and instructions
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

## Installation

### Linux/macOS

```bash
git clone https://github.com/user/my-claude-code-settings.git
cd my-claude-code-settings
./install.sh install-all
./install.sh prompt-update
```

### Windows

```powershell
git clone https://github.com/user/my-claude-code-settings.git
cd my-claude-code-settings
.\install.ps1
```

## Commands

```bash
./install.sh list           # List available skills
./install.sh install <skill> # Install specific skill(s)
./install.sh install-all    # Install all skills
./install.sh prompt-diff    # Show diff between local and global CLAUDE.md
./install.sh prompt-update  # Sync CLAUDE.md to ~/.claude/
```

## License

MIT
