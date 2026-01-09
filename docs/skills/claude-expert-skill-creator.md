# claude-expert-skill-creator

Create production-ready skills from expert knowledge. Extracts domain expertise and system ontologies, uses scripts for deterministic work, loads knowledge progressively.

## Why Skills Fail

AI assistants fail not because they lack intelligence, but because they lack:

1. **Domain Expertise** — Industry-specific rules, edge cases, unwritten conventions
2. **Ontology Understanding** — How YOUR systems, data structures, and workflows actually work

## Workflow

```
Assess → Discover (Expertise + Ontology) → Design → Create → Refine → Ship
```

## Quick Assessment

**Create a skill when:**
- Used 3+ times (or will be)
- Follows consistent procedure
- Saves >300 tokens per use
- Requires specialized knowledge not in Claude's training

**Don't create for:** one-time tasks, basic knowledge Claude already has, rapidly changing content.

## Skill Architecture

```
skill-name/
├── SKILL.md              # Layer 1: Core (300-500 tokens)
├── scripts/              # Layer 0: Automation (0 tokens to run)
│   └── validate.py
└── resources/            # Layer 2: Details (loaded selectively)
    └── ADVANCED.md
```

| Layer | Purpose | Token Cost |
|-------|---------|------------|
| Layer 0 (Scripts) | Free execution, structured JSON output | 0 tokens |
| Layer 1 (SKILL.md) | Loaded when triggered - keep lean | 300-500 tokens |
| Layer 2 (Resources) | Fetched only when needed | On-demand |

## Token Optimization

| Technique | Instead of | Do this | Savings |
|-----------|-----------|---------|---------|
| Scripts | 500 tokens explaining validation | `python scripts/validate.py` | ~450 tokens |
| Reference | Inline schema (200 tokens) | Link to `resources/schema.json` | ~185 tokens |
| Layer 2 | Everything in SKILL.md | Link to `resources/ADVANCED.md` | ~750 tokens |

## Description Formula

```
<Action> <Object> for <Purpose>. Use when <Trigger>.
```

Example: "Validate billing data for system migration. Use before importing invoices."

## Quality Checklist

Before shipping:
- [ ] Description <30 tokens
- [ ] SKILL.md <500 tokens (Layer 1)
- [ ] Scripts for deterministic operations
- [ ] Advanced content in resources/ (Layer 2)
- [ ] Version in frontmatter
- [ ] All referenced files exist
