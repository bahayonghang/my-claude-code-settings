# Export Session Context

The `/export` command analyzes the current session history and generates a structured summary for context inheritance.

## Usage

```bash
/export
```

## Description

This command performs a comprehensive review of the current conversation and codebase state to generate a **Handoff Summary**. This summary is saved as a Markdown file (e.g., `session_context.md`), which can be fed into a new session to restore context seamlessly.

The summary includes:
- 🎯 **Session Goal**: What was the main objective?
- ✅ **Accomplishments**: Completed tasks and implemented features.
- 🧠 **Key Decisions**: Architectural choices and important discoveries.
- 🚧 **Next Steps**: Actionable items for the next session.
- 📂 **Key Files**: List of relevant files modified or analyzed.

## Platform Support

| Platform | Support | File Format |
|----------|---------|-------------|
| Claude Code | ✅ | Markdown (`.md`) |
| Gemini CLI | ✅ | TOML (`.toml`) |
| Codex CLI | ❌ | Not yet supported |

## Example Output

```markdown
# Session Handoff: [Date]

## 🎯 Goal
Implement the user login flow using OAuth2.

## ✅ Accomplishments
- Created `auth_service.py` with `login` function.
- Updated `requirements.txt` to include `python-jose`.

## 🚧 Next Steps
- Implement token refresh logic.
- Add unit tests for `auth_service.py`.
```
