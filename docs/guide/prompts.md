# Prompts

The `prompts/` directory contains global configuration files that enhance Claude Code's behavior.

## CLAUDE.md

Global workflow configuration based on engineering best practices.

### Key Principles

- **KISS/YAGNI** - Keep it simple, avoid over-engineering
- **Structured Workflow** - Systematic approach to tasks
- **Self-Reflection** - Verification before handoff

### Workflow Stages

1. **Intake** - Understand the request
2. **Context** - Gather relevant information
3. **Exploration** - Investigate options
4. **Planning** - Design the solution
5. **Execution** - Implement the solution
6. **Verification** - Validate the result
7. **Handoff** - Deliver with documentation

### Installation

Sync to global config:

::: code-group
```bash [Linux/macOS]
./install.sh prompt-update
```
```powershell [Windows]
.\install.ps1 prompt-update
```
:::

This copies `prompts/CLAUDE.md` to `~/.claude/CLAUDE.md`.

## TRANSLATE.md

Guidelines for technical content translation.

### Principles

- **Natural Phrasing** - Prioritize readability over literal translation
- **Preserve Technical Terms** - Keep code, brands, and established terms
- **Annotate Ambiguity** - Add notes for unclear terms

### Usage

Reference this file when translating technical documentation to maintain consistency and quality.
