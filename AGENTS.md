# Repository Guidelines

## Project Structure & Module Organization
- `prompts/` contains repository-wide workflow and translation configs: `CLAUDE.md` and `TRANSLATE.md`. Updates here affect all skills.
- `skills/<skill-name>/SKILL.md` defines one standalone Claude/Codex skill. Each skill lives in its own kebab-case folder.
- `install.sh` manages installing skills to `~/.claude/skills` and syncing the global `CLAUDE.md`.

## Build, Test, and Development Commands
There is no build system; changes are Markdown and Bash only.

- `./install.sh list` - list skills in this repo.
- `./install.sh install <skill>...` / `./install.sh install-all` - copy skills into `~/.claude/skills`.
- `./install.sh prompt-diff` - show differences between local and global `CLAUDE.md`.
- `./install.sh prompt-update` - update `~/.claude/CLAUDE.md` from `prompts/CLAUDE.md`.

## Coding Style & Naming Conventions
- Skill directories and YAML `name` fields use kebab-case (e.g., `skills/git-squash-commits/`, `name: git-squash-commits`).
- Every `SKILL.md` starts with YAML frontmatter:
  ```yaml
  ---
  name: my-skill
  description: One-line purpose.
  ---
  ```
- Keep instructions concise and structured with Markdown headings. Prompts are written in English unless the file is explicitly a translation target.
- For shell scripts, keep Bash style consistent with `install.sh` (2-space indentation, `set -euo pipefail`, avoid silent destructive ops).

## Testing Guidelines
No automated tests are currently tracked. Validate changes by:
- running `bash -n install.sh` after script edits;
- installing the skill locally (`./install.sh install <skill>`) and verifying behavior in Claude/Codex.

## Commit & Pull Request Guidelines
- Prefer conventional commits when possible (`feat:`, `fix:`, `docs:`, `chore:`), imperative mood, and <=50-character subjects.
- PRs should explain the intent and usage of the change, note any breaking behavior in prompts, and include a README update when adding or renaming skills.
