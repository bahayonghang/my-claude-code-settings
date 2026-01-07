# git-commit

Analyze Git changes and automatically generate Conventional Commits style commit messages.

## Overview

The `git-commit` command uses only Git (no package managers or build tools) to:

- Read staged/unstaged changes
- Suggest splitting into multiple commits when appropriate
- Generate Conventional Commits formatted messages (with optional emoji)
- Execute `git add` and `git commit` as needed

## Usage

```bash
/git-commit                           # Analyze current changes
/git-commit --all                     # Stage all changes and commit
/git-commit --no-verify               # Skip Git hooks
/git-commit --emoji                   # Include emoji in commit message
/git-commit --scope ui --type feat    # Specify scope and type
/git-commit --amend --signoff         # Amend last commit with sign-off
```

## Options

| Option | Description |
|--------|-------------|
| `--no-verify` | Skip local Git hooks (`pre-commit`/`commit-msg`) |
| `--all` | Auto `git add -A` when staging area is empty |
| `--amend` | Amend the previous commit |
| `--signoff` | Add `Signed-off-by` line (DCO compliance) |
| `--emoji` | Include emoji prefix in commit message |
| `--scope <scope>` | Specify commit scope (e.g., `ui`, `docs`, `api`) |
| `--type <type>` | Force commit type (e.g., `feat`, `fix`, `docs`) |

## How It Works

1. **Repository Validation** - Checks if inside a Git repository and current branch status
2. **Change Detection** - Uses `git status --porcelain` and `git diff` to analyze changes
3. **Split Suggestions** - Recommends splitting commits based on:
   - Different concerns (unrelated features/modules)
   - Different types (don't mix `feat`, `fix`, `refactor`)
   - File patterns (source vs docs/tests/config)
   - Size threshold (>300 lines or multiple top-level directories)
4. **Message Generation** - Creates Conventional Commits format:
   - Header: `[<emoji>] <type>(<scope>)?: <subject>` (≤72 chars)
   - Body: Bullet points explaining motivation and changes
   - Footer: Breaking changes, issue references
5. **Commit Execution** - Runs `git commit` with generated message

## Commit Types

| Emoji | Type | Description |
|-------|------|-------------|
| ✨ | `feat` | New feature |
| 🐛 | `fix` | Bug fix |
| 📝 | `docs` | Documentation |
| 🎨 | `style` | Code style/formatting |
| ♻️ | `refactor` | Code refactoring |
| ⚡️ | `perf` | Performance improvement |
| ✅ | `test` | Tests |
| 🔧 | `chore` | Build/tooling |
| 👷 | `ci` | CI/CD |
| ⏪️ | `revert` | Revert commit |

## Examples

**With emoji:**
```
✨ feat(ui): add user authentication flow
🐛 fix(api): handle token refresh race condition
📝 docs: update API usage examples
```

**Without emoji:**
```
feat(ui): add user authentication flow
fix(api): handle token refresh race condition
docs: update API usage examples
```

**With body:**
```
feat(auth): add OAuth2 login flow

- implement Google and GitHub third-party login
- add user authorization callback handling
- improve login state persistence logic

Closes #42
```

**Breaking change:**
```
feat(api)!: redesign authentication API

- migrate from session-based to JWT authentication
- update all endpoint signatures
- remove deprecated login methods

BREAKING CHANGE: authentication API has been completely redesigned
```

## Important Notes

- **Git-only**: No package managers or build commands are used
- **Respects hooks**: Local Git hooks run by default; use `--no-verify` to skip
- **Non-destructive**: Only writes to `.git/COMMIT_EDITMSG` and staging area
- **Safe**: Prompts for confirmation in rebase/merge conflict or detached HEAD states
