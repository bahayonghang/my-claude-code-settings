# research

Technical research with web search and citation support using Codex CLI.

## Core Principles

1. **Codex retrieves, you analyze** - Get raw sources, organize yourself
2. **Focus on key results** - Only keep what users care about
3. **Complete citations** - All claims need clickable sources
4. **Verify links** - Validate URLs before finalizing

## Workflow

### 1. Clarify Goals
- What's the core question?
- What needs comparison?
- Which aspects matter?

### 2. Batch Retrieval

```bash
codex e -m gpt-5.1-codex -c model_reasoning_effort=high \
  --enable web_search_request \
  --dangerously-bypass-approvals-and-sandbox \
  --skip-git-repo-check \
  "Return RAW search results with URLs. Search: <query>"
```

**Query Tips**:
- Add year constraints: `2024 2025`
- Include exact product names
- Focus each query on single topic

### 3. Extract & Organize
- Filter valuable information
- Organize structure
- Add analysis and insights
- Unify citation format

### 4. Validate Links

```bash
codex e ... "Verify if these URLs are valid: 1. <url1> 2. <url2>"
```

## Output Format

### Inline Citations
```markdown
OpenSearch forked from Elasticsearch 7.10 in 2021 ([AWS Blog]).

[AWS Blog]: https://aws.amazon.com/blogs/...
```

### Report Structure
```markdown
# [Topic] Research Report

## 1. Overview
## 2. Core Features
## 3. Comparison
## 4. Recommendations

## References
[Link 1]: URL1
[Link 2]: URL2
```

## Source Priority

1. Official documentation
2. Official blogs/announcements
3. Third-party tech blogs (verify quality)
4. Independent benchmarks (note bias)

## Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| Wrong product searched | Include exact name in query |
| 404 links | Validate before finalizing |
| Vendor bias | Note source in report |
| Broad queries | Focus on single topic |
