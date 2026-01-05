# codex

Execute Codex CLI for code generation, analysis, and web search.

## Capabilities

### 1. Code Generation

Deep code analysis and generation with maximum reasoning power.

**When to Use**:
- Complex code analysis requiring deep understanding
- Large-scale refactoring across multiple files
- Automated code generation with safety controls

**Default Configuration**:
- Model: `gpt-5.2-codex`
- Reasoning: `xhigh` (maximum thinking depth)

**Command**:
```bash
codex e -m gpt-5.2-codex -c model_reasoning_effort=xhigh \
  --dangerously-bypass-approvals-and-sandbox \
  --skip-git-repo-check \
  "<task>"
```

**Examples**:
```bash
# Explain code
codex e ... "explain @src/main.ts"

# Refactor
codex e ... "refactor @src/utils for performance"

# Multi-file analysis
codex e ... -C /path/to/project "analyze @. and find security issues"
```

### 2. Web Search & Fetch

Online research with web search and page content fetching.

**When to Use**:
- Documentation lookup
- Fetch and summarize web pages
- Current information retrieval
- Technology comparison

**Default Configuration**:
- Model: `gpt-5.1-codex`
- Reasoning: `high`
- Web search: enabled

**Command**:
```bash
codex e -m gpt-5.1-codex -c model_reasoning_effort=high \
  --enable web_search_request \
  --dangerously-bypass-approvals-and-sandbox \
  --skip-git-repo-check \
  "<task>"
```

**Examples**:
```bash
# Fetch GitHub repo
codex e ... "Fetch and summarize https://github.com/user/repo"

# Documentation search
codex e ... "find the latest React 19 hooks documentation"

# Technology research
codex e ... "compare Vite vs Webpack for React projects in 2024"
```

## Session Resume

Continue previous conversations:

```bash
codex e resume <session_id> "<follow-up task>"
```

## File References

- `@file` - Reference specific file
- `@.` - Reference entire working directory
- `-C <dir>` - Set working directory

## Prerequisites

- Codex CLI installed and authenticated
- API access configured
