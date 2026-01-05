# tech-blog

Write technical blog posts with source code analysis.

## Use Cases

- Explaining system internals
- Source code analysis and walkthrough
- Comparing implementations
- Architecture deep dives

## Document Structure

```markdown
# [Topic] Deep Dive

> **Code Version**: Based on [project] `vX.Y.Z`

## 1. Introduction
## 2. Background
## 3-N. Core Content (by data flow)
## N+1. Comparison / Trade-offs
## N+2. Code Index
## References
```

## Core Principles

### Progressive Explanation
- Start with the problem, not the solution
- Build concepts layer by layer
- Explain "why" not just "what"

### Concept-First
- Never use undefined terms
- Define before use
- Add navigation hints

### Big Picture First
- Start with visual overview
- Use comparison diagrams for multiple approaches
- Show complete flow in one diagram

### Balanced Comparison
- Analyze both sides
- Use comparison tables
- Identify true differences

## Writing Guidelines

### Code Examples
- Include file path and line numbers
- Explain what it does
- Use flow diagrams + key snippets

### Diagrams (Mermaid)
```mermaid
flowchart LR
    A[Client] --> B[Component]
    style A fill:#e1f5fe,stroke:#01579b
    style B fill:#fff3e0,stroke:#e65100
```

### Callouts
- 💡 **Key Point**: Critical insights
- ⚠️ **Gotcha**: Common mistakes
- 📝 **Terminology**: Definitions

## Data Integrity

**Never fabricate**:
- ❌ "Compression ratio is 16:1" (without source)
- ✅ "Based on [source], ratio is X:Y"

**Requires citation**:
- Performance benchmarks
- Memory usage numbers
- Quantitative comparisons

## Output

- Location: `docs/` or `ai_docs/`
- Filename: `[topic-name].md`
