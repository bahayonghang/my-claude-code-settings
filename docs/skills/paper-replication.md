# Paper Replication

Deep learning paper replication skill that transforms academic papers into industrial-grade PyTorch code.

## Overview

This skill enables Claude to read deep learning papers (PDF or text), perform deep deconstruction, and output runnable, industrial-standard PyTorch network model code.

## Trigger Phrases

- "帮我复现这篇论文" (Help me replicate this paper)
- "论文复现" (Paper replication)
- "实现这个模型" (Implement this model)
- When providing a deep learning paper that needs to be converted to PyTorch code

## Workflow

The skill follows a strict three-phase workflow:

### Phase 1: Paper Auditing & Deconstruction

1. **Core Summary** - Problem statement and key contributions
2. **Mathematical Auditing** - Extract formulas in LaTeX, explain symbols, analyze loss functions
3. **Architecture Details** - Document all hyperparameters with sources

### Phase 2: Architecture Visualization

Generate Mermaid flowcharts with:
- Input/Output tensor shapes using standard notation (`[B, C, H, W]`)
- Color-coded components (Input, Backbone, Attention, Loss, etc.)
- Module-level granularity for deep networks (20+ layers)

### Phase 3: PyTorch Implementation

Generate production-ready code following strict standards:
- Type hints throughout
- Tensor shape comments after every operation
- Modular architecture with separate classes
- Weight initialization methods
- Reproducibility configuration
- Comprehensive validation code

## Tensor Shape Notation

| Symbol | Meaning | Example |
|--------|---------|---------|
| `B` | Batch Size | - |
| `C` | Channels | - |
| `H` | Height | - |
| `W` | Width | - |
| `T` | Time / Sequence Length | - |
| `D` | Dimension / Feature Dim | - |
| `N` | Number of elements | - |
| `E` | Embedding Dimension | - |

## "Paper Did Not Specify" Protocol

When papers don't specify certain parameters, the skill uses a standardized annotation format:

```python
# Dropout rate: Paper did not specify
# Recommended: 0.1
# Reference: BERT (Devlin et al., 2019)
# Alternatives: [0.0, 0.1, 0.2, 0.3]
# Impact: Higher dropout may improve generalization
self.dropout = nn.Dropout(p=0.1)
```

## Output Structure

```
output/
├── README.md           # Paper overview, usage instructions
├── model.py            # Main model implementation
├── modules/            # Sub-modules
│   ├── __init__.py
│   ├── attention.py    # Attention modules
│   ├── backbone.py     # Backbone network
│   └── head.py         # Output head
├── config.py           # Configuration file
└── requirements.txt    # Dependencies
```

## Common Pitfalls Handled

- Tensor reshape vs view operations
- Paper figure/text inconsistencies
- Framework differences (PyTorch vs TensorFlow BatchNorm momentum)
- Initialization differences across frameworks

## Requirements

- Python 3.10+
- PyTorch 2.0+
- Optional: einops, timm

## Example Usage

```
Please replicate this paper: [attach PDF or paste paper content]
```

The skill will:
1. Extract and explain core formulas
2. Generate architecture diagram
3. Produce validated PyTorch code with shape annotations
