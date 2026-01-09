# latex-paper-en

LaTeX academic paper assistant for English conference/journal papers. Provides format checking (chktex), compilation, grammar analysis, complex sentence decomposition, and expression restructuring.

## Critical Rules

1. NEVER modify content inside `\cite{}`, `\ref{}`, `\label{}`, math environments
2. NEVER fabricate bibliography entries
3. NEVER change domain-specific terminology without permission
4. NEVER apply changes directly - always output diff-comment format first
5. ALWAYS run format check before analyzing text content

## Quick Start

### Compile Document
```bash
# Auto-detect and compile (recommended)
python scripts/compile.py main.tex

# Explicit compiler selection
python scripts/compile.py main.tex --compiler pdflatex
python scripts/compile.py main.tex --compiler xelatex

# Using recipes
python scripts/compile.py main.tex --recipe pdflatex-bibtex
python scripts/compile.py main.tex --recipe xelatex-biber
```

### Format Check
```bash
python scripts/check_format.py main.tex
python scripts/check_format.py main.tex --strict
```

## 4-Layer Workflow

### Layer 0: Pre-flight Check (MANDATORY)
```bash
python scripts/check_format.py main.tex
python scripts/verify_bib.py references.bib
```

### Layer 1: Grammar & Style Analysis
- Subject-verb agreement, article usage
- Tense consistency (past for methods, present for results)
- Chinglish detection
- Weak verb replacement: make→construct, do→perform, get→obtain

### Layer 2: Complex Sentence Decomposition
Trigger: Sentences >50 words or >3 subordinate clauses

```latex
% LONG SENTENCE DETECTED (Line 45, 67 words)
% Core Clause: [main subject + verb + object]
% Suggested Rewrite: [simplified version]
```

### Layer 3: Expression Restructuring
```latex
% SUGGESTION (Line 23): Improve academic tone
% Before: We use machine learning to get better results.
% After: We employ machine learning techniques to achieve superior performance.
```

## Venue-Specific Rules

| Venue | Key Rules |
|-------|-----------|
| IEEE | Active voice for contributions, past tense for methods |
| ACM | Present tense for general truths, structured abstract |
| Springer | Figure captions below, table captions above |
| NeurIPS/ICML | Concise (8 pages), specific formatting |
