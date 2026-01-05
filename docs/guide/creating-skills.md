# Creating Skills

## Skill Structure

A minimal skill requires only a `SKILL.md` file:

```
skills/
└── my-skill/
    └── SKILL.md
```

Complex skills can include additional directories:

```
skills/
└── my-skill/
    ├── SKILL.md        # Required
    ├── config/         # Configuration templates
    ├── tips/           # Usage tips
    ├── references/     # Technical references
    ├── scripts/        # Helper scripts
    └── cookbook/       # Code examples
```

## SKILL.md Format

Every `SKILL.md` must include YAML frontmatter:

```yaml
---
name: my-skill
description: Brief description for listing
license: MIT  # optional
---

# My Skill

Detailed instructions and documentation...
```

## Writing Effective Skills

### Be Specific

Provide clear, actionable instructions:

```markdown
## Workflow

1. Analyze the user's requirements
2. Generate initial design
3. Iterate based on feedback
4. Output final result
```

### Include Examples

Show expected inputs and outputs:

```markdown
## Example

**Input:** "Create a login form"

**Output:** A responsive login form with email/password fields,
validation, and submit button.
```

### Define Constraints

Set clear boundaries:

```markdown
## Constraints

- Output must be valid HTML5
- Use semantic elements
- Ensure WCAG 2.1 AA compliance
```

## Testing Your Skill

1. Install the skill:
   ```bash
   ./install.sh install my-skill
   ```

2. Test in Claude Code by invoking the skill

3. Iterate on the `SKILL.md` based on results

## Best Practices

- Keep skills focused on a single domain
- Use clear, concise language
- Include practical examples
- Document any prerequisites
- Follow existing skill patterns for consistency
