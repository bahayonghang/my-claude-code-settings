# latex-thesis-zh

Chinese doctoral/master thesis LaTeX assistant. Provides structure integrity checking, GB/T 7714 format validation, compilation (xelatex/lualatex), Chinese academic expression standards, and terminology consistency analysis.

## Critical Rules / 核心原则

1. 绝不修改 `\cite{}`、`\ref{}`、`\label{}`、公式环境内的内容
2. 绝不凭空捏造参考文献条目
3. 绝不在未经许可的情况下修改专业术语
4. 绝不直接应用修改 - 始终先以注释形式输出 diff
5. 必须先运行结构映射，再开始分析
6. 中文文档必须使用 XeLaTeX 或 LuaLaTeX 编译

## Quick Start / 快速开始

### Compile Document / 编译文档
```bash
# Auto-detect (XeLaTeX for Chinese)
python scripts/compile.py main.tex

# Explicit compiler
python scripts/compile.py main.tex --compiler xelatex

# Using recipes
python scripts/compile.py main.tex --recipe xelatex-biber  # 推荐
```

### Structure Mapping / 结构映射
```bash
python scripts/map_structure.py main.tex  # MUST run first
```

## 5-Layer Workflow / 工作流程

### Layer 0: Structure Mapping (MANDATORY)
Map thesis structure, detect template type, determine processing order.

### Layer 1: Structure Integrity Check
- Front Matter: Cover, Declaration, Abstract (CN+EN), TOC
- Main Body: Introduction → Related Work → Core Content → Conclusions
- Back Matter: References, Acknowledgments, Publication list

### Layer 2: GB/T 7714 Format Check
- Bibliography format (biblatex-gb7714-2015)
- Figure/table captions (宋体五号)
- Equation numbering (e.g., (3.1))

### Layer 3: Chinese Academic Expression
| Oral | Academic |
|------|----------|
| 很多研究表明 | 大量研究表明 |
| 效果很好 | 具有显著优势 |
| 显然、毫无疑问 | 研究表明、实验结果显示 |

### Layer 4: Long Sentence Decomposition
Trigger: >60 characters or >3 clauses

### Layer 5: Expression Restructuring
```latex
% 修改建议（第23行）
% 原文：我们使用了ResNet模型。
% 修改后：本文采用ResNet模型作为特征提取器。
```

## Supported Templates / 支持的模板

| Template | University |
|----------|------------|
| thuthesis | Tsinghua University |
| pkuthss | Peking University |
| ustcthesis | USTC |
| fduthesis | Fudan University |
| generic | General GB/T compliant |
