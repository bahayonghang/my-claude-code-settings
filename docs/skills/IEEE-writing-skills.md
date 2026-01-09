# IEEE-writing-skills

Translate, polish, restructure, and validate academic papers for IEEE publications. Strict adherence to IEEE style, academic tone, and formatting rules.

## Capabilities

| Function | Description |
|----------|-------------|
| Translation | CN ↔ EN academic translation preserving LaTeX/Typst syntax |
| Polishing | Grammar, flow, and academic tone enhancement |
| Restructuring | Logical flow and paragraph organization optimization |
| Validation | Automated checks for structure, abstract length, forbidden words |

## Core Guidelines

### Academic Tone Guard
Aggressively replace informal language:
- ❌ "very", "amazing", "I think"
- ✅ "significant", "demonstrates", "it is observed that"

### Voice Preference
- Prefer impersonal active voice: "The system performs..."
- Or passive voice over first-person: "The experiment was conducted..."

## Workflow

### 1. Identify Task
Determine if user wants to **Translate**, **Polish**, **Restructure**, or **Validate**.

### 2. Apply Guidelines
For ALL tasks:
- Enforce tone guard rules
- Maintain terminology consistency
- Preserve LaTeX commands (`\cite{}`, `\ref{}`)

### 3. Execute

#### Translation
- Strict terminology consistency
- Preserve all LaTeX commands
- Output pure text/code block

#### Polishing
- Focus on clarity and conciseness
- Do NOT change technical meaning
- Provide diff summary if requested

#### Restructuring
- Analyze logical flow
- Suggest splitting long paragraphs
- Ensure Introduction covers contributions clearly

#### Validation
```bash
python skills/IEEE-writing-skills/scripts/check_structure.py "path/to/paper.txt"
```

## Example Usage

**User:** "Polish this abstract."

**Action:** Check word count, rewrite removing "very" and "good", ensure 150-250 words.

**User:** "Check my paper format."

**Action:** Run `check_structure.py`, report issues, offer to fix forbidden words.
