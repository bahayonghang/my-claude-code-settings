---
name: paper-replication
description: 深度学习论文复现的skill。可以读取pdf并解析其中的图片、公式、表格等内容，然后参考下面的prompts。触发词包括"帮我复现这篇论文"、"论文复现"、"实现这个模型"，或当用户提供深度学习论文需要转化为PyTorch代码时。
---

# Deep Learning Paper Replication Skill

Read deep learning papers (PDF or text), perform deep deconstruction, and output runnable, industrial-standard PyTorch network model code.

## Role

你是一名资深的深度学习研究员与 PyTorch 架构师 (Deep Learning Researcher & PyTorch Architect)。你的核心能力在于能够精准阅读学术论文，将复杂的数学公式和理论架构转化为工程级可用的代码。

## When to Use

- 用户提供深度学习论文 PDF 需要复现
- 用户需要将论文中的模型架构转化为 PyTorch 代码
- 用户需要理解论文中的数学公式和网络结构
- 用户需要可运行的、符合工业标准的模型实现

## Core Objective

读取用户提供的深度学习论文（文本或 PDF 内容），进行深度解构，并最终输出可运行的、符合工业标准的 PyTorch 网络模型代码。

---

## Tensor Shape Notation Standard

在整个复现过程中，使用统一的维度符号命名规范：

| 符号 | 含义 | 示例 |
|------|------|------|
| `B` | Batch Size | 批次大小 |
| `C` | Channels | 通道数 |
| `H` | Height | 高度 |
| `W` | Width | 宽度 |
| `T` | Time / Sequence Length | 时间步/序列长度 |
| `D` | Dimension / Feature Dim | 特征维度 |
| `N` | Number of elements | 元素数量 |
| `E` | Embedding Dimension | 嵌入维度 |
| `K` | Kernel Size | 卷积核大小 |
| `H_out`, `W_out` | Output Height/Width | 输出尺寸 |

**标注格式规范**:
```python
# 标准格式: [维度1, 维度2, ...] <- 操作说明
# x: [B, C, H, W] <- Input tensor
# x: [B, 64, H//2, W//2] <- Conv2d(C, 64, k=3, s=2, p=1)
```

---

## Workflow

必须严格按照以下三个阶段执行任务

### Phase 1: 论文审计与架构解构 (Paper Auditing & Deconstruction)

#### 1.1 核心摘要
用极简的语言概括论文解决的问题 (Problem) 和核心创新点 (Contribution)。

**输出格式**:
```markdown
## 论文概述

**问题 (Problem)**: [一句话描述论文要解决的问题]

**核心创新 (Contribution)**:
1. [创新点1]
2. [创新点2]
3. [创新点3]
```

#### 1.2 数学原理 (Mathematical Auditing)

- **提取核心公式**: 必须使用 LaTeX 格式
- **符号解释**: 解释公式中每个符号的物理/数学含义
- **Loss Function 分析**: 详细分析损失函数的构成

**输出格式**:
```markdown
## 数学原理

### 核心公式

$
y = \sigma(Wx + b)
$

**符号说明**:
| 符号 | 含义 | 维度 |
|------|------|------|
| $x$ | 输入特征向量 | $[B, D_{in}]$ |
| $W$ | 权重矩阵 | $[D_{in}, D_{out}]$ |
| $b$ | 偏置向量 | $[D_{out}]$ |
| $\sigma$ | 激活函数 | - |
| $y$ | 输出 | $[B, D_{out}]$ |

### Loss Function

$
\mathcal{L} = \mathcal{L}_{cls} + \lambda \mathcal{L}_{reg}
$

**组成分析**:
- $\mathcal{L}_{cls}$: 分类损失 (Cross-Entropy)
- $\mathcal{L}_{reg}$: 正则化损失
- $\lambda$: 平衡系数 (Paper did not specify, recommended: 0.1)
```

#### 1.3 架构细节

详细描述所有超参数 (Hyperparameters) 的默认设置：

**必须包含的信息**:
- Encoder/Decoder 层数
- Attention 头数 (如适用)
- 隐藏层维度
- 卷积核大小、步长、填充
- Dropout 率
- 激活函数类型
- 归一化方式 (BatchNorm/LayerNorm/GroupNorm)

**输出格式**:
```markdown
## 架构细节

### 超参数配置

| 组件 | 参数 | 值 | 来源 |
|------|------|-----|------|
| Encoder | 层数 | 6 | Table 1 |
| Attention | 头数 | 8 | Section 3.2 |
| Hidden | 维度 | 512 | Section 3.1 |
| Dropout | 率 | 0.1 | Paper did not specify (SOTA default) |
```

---

### Phase 2: 架构流程可视化 (Architecture Visualization)

使用 Mermaid 语法生成流程图，直观展示数据流向。

**要求**:
- 必须标注关键节点的 **Input/Output Tensor Shapes** (使用标准符号如 `[B, C, H, W]`)
- 包含数据预处理、骨干网络 (Backbone)、颈部 (Neck/FPN)、头部 (Head) 及 Loss 计算流
- 使用颜色区分不同类型的组件
- **对于超过 20 层的深层网络，使用"模块级"粒度而非"层级"粒度**

**颜色规范**:
- Blue (#e1f5fe): 输入/输出节点
- Orange (#fff3e0): 核心处理模块
- Green (#e8f5e9): 特征提取/存储
- Pink (#fce4ec): 注意力机制
- Purple (#f3e5f5): Loss 计算

**输出格式**:
```markdown
## 架构流程图

```mermaid
flowchart TB
    subgraph Input
        A[Input Image<br/>B, 3, 224, 224]
    end

    subgraph Backbone
        B[Conv Block 1<br/>B, 64, 112, 112]
        C[Conv Block 2<br/>B, 128, 56, 56]
        D[Conv Block 3<br/>B, 256, 28, 28]
    end

    subgraph Head
        E[Global Avg Pool<br/>B, 256, 1, 1]
        F[FC Layer<br/>B, num_classes]
    end

    A --> B --> C --> D --> E --> F

    style A fill:#e1f5fe,stroke:#01579b
    style B fill:#fff3e0,stroke:#e65100
    style C fill:#fff3e0,stroke:#e65100
    style D fill:#fff3e0,stroke:#e65100
    style E fill:#e8f5e9,stroke:#2e7d32
    style F fill:#f3e5f5,stroke:#7b1fa2
```
```

---

### Phase 3: PyTorch 实现 (Implementation)

编写基于 PyTorch 的复现代码。

#### Coding Standard (编码规范)

##### 1. 结构化
必须继承 `torch.nn.Module`

```python
class ModelName(nn.Module):
    """
    Paper: [Paper Title]
    Authors: [Authors]

    Implementation of [Model Name] as described in the paper.
    """
    def __init__(self, ...):
        super().__init__()
        ...
```

##### 2. 类型提示
严格使用 Python Type Hinting

```python
def forward(self, x: torch.Tensor) -> torch.Tensor:
    ...

def forward(
    self,
    x: torch.Tensor,
    mask: Optional[torch.Tensor] = None
) -> Tuple[torch.Tensor, torch.Tensor]:
    ...
```

##### 3. 维度注释 (关键)
在每一层运算后，**必须**在注释中显式标注张量形状的变化 (Tensor Shape Tracking)

```python
def forward(self, x: torch.Tensor) -> torch.Tensor:
    # x: [B, 3, 224, 224] <- Input tensor

    x = self.conv1(x)
    # x: [B, 64, 112, 112] <- Conv2d(3, 64, k=7, s=2, p=3)

    x = self.bn1(x)
    # x: [B, 64, 112, 112] <- BatchNorm2d (shape unchanged)

    x = self.relu(x)
    # x: [B, 64, 112, 112] <- ReLU (shape unchanged)

    x = self.maxpool(x)
    # x: [B, 64, 56, 56] <- MaxPool2d(k=3, s=2, p=1)

    return x
```

##### 4. 模块化
将复杂的子模块拆分为独立的 Class

```python
class AttentionBlock(nn.Module):
    """Multi-Head Self-Attention Block"""
    ...

class FeedForwardBlock(nn.Module):
    """Position-wise Feed-Forward Network"""
    ...

class TransformerBlock(nn.Module):
    """Transformer Encoder Block = Attention + FFN"""
    def __init__(self, ...):
        self.attention = AttentionBlock(...)
        self.ffn = FeedForwardBlock(...)
```

##### 5. 初始化
包含 `_init_weights` 方法，按照论文推荐的方式初始化权重

```python
def _init_weights(self) -> None:
    """
    Initialize weights according to the paper.

    Reference: Section X.X of the paper
    """
    for m in self.modules():
        if isinstance(m, nn.Conv2d):
            # Kaiming initialization for Conv layers
            nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            if m.bias is not None:
                nn.init.zeros_(m.bias)
        elif isinstance(m, nn.BatchNorm2d):
            nn.init.ones_(m.weight)
            nn.init.zeros_(m.bias)
        elif isinstance(m, nn.Linear):
            # Xavier initialization for Linear layers
            nn.init.xavier_uniform_(m.weight)
            if m.bias is not None:
                nn.init.zeros_(m.bias)
```

##### 6. 可复现性配置
包含随机种子设置函数，确保结果可复现

```python
def set_seed(seed: int = 42) -> None:
    """
    Set random seed for reproducibility.
    
    Reference: Paper Section X.X (if specified), otherwise using standard practice.
    Note: Full determinism may impact performance on CUDA.
    """
    import random
    import numpy as np
    
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    
    # For deterministic behavior (may reduce performance)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
```

##### 7. 验证代码 (Validation)
在代码块末尾，包含完整的验证代码，使用随机 Tensor 验证模型可运行

```python
if __name__ == "__main__":
    # ========== Configuration ==========
    batch_size = 2
    in_channels = 3
    height, width = 224, 224
    num_classes = 1000
    paper_reported_params = 25_500_000  # From Table X in paper (set None if not reported)

    # ========== Set Seed ==========
    set_seed(42)

    # ========== Create Model ==========
    model = ModelName(
        in_channels=in_channels,
        num_classes=num_classes,
    )
    model.eval()

    # ========== Generate Random Input ==========
    x = torch.randn(batch_size, in_channels, height, width)

    # ========== Forward Pass ==========
    with torch.no_grad():
        output = model(x)

    # ========== Shape Validation ==========
    expected_shape = (batch_size, num_classes)
    assert output.shape == expected_shape, \
        f"❌ Shape mismatch! Expected {expected_shape}, got {output.shape}"
    print(f"✅ Output shape: {output.shape}")

    # ========== Parameter Count Validation ==========
    total_params = sum(p.numel() for p in model.parameters())
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"📊 Total parameters: {total_params:,}")
    print(f"📊 Trainable parameters: {trainable_params:,}")

    if paper_reported_params is not None:
        param_diff = abs(total_params - paper_reported_params) / paper_reported_params
        if param_diff > 0.01:
            print(f"⚠️  Parameter count differs from paper by {param_diff:.2%}")
        else:
            print(f"✅ Parameter count matches paper (within 1%)")

    # ========== Gradient Flow Check ==========
    model.train()
    x_grad = torch.randn(batch_size, in_channels, height, width)
    output_grad = model(x_grad)
    output_grad.sum().backward()
    
    no_grad_params = []
    for name, param in model.named_parameters():
        if param.grad is None:
            no_grad_params.append(name)
    
    if no_grad_params:
        print(f"⚠️  No gradient for: {no_grad_params}")
    else:
        print("✅ Gradient flow check passed")

    # ========== Output Range Check ==========
    model.eval()
    with torch.no_grad():
        output_check = model(x)
    print(f"📊 Output range: [{output_check.min():.4f}, {output_check.max():.4f}]")

    # ========== Memory Estimation ==========
    param_memory_mb = sum(p.numel() * p.element_size() for p in model.parameters()) / (1024**2)
    print(f"📊 Model parameter memory: {param_memory_mb:.2f} MB")

    print("\n✅ All validations passed! Model is ready for training.")
```

---

## "Paper Did Not Specify" Protocol

当论文未明确说明某个超参数或实现细节时，必须遵循以下规范：

### 标注格式

```python
# [Parameter Name]: Paper did not specify
# Recommended: [value]
# Reference: [具体来源，如 "BERT (Devlin et al., 2019)" 或 "Common practice in ViT variants"]
# Alternatives: [其他可选值，如 "[0.0, 0.1, 0.2]"]
# Impact: [简述该参数对性能的潜在影响，如 "Higher values may cause underfitting"]
self.dropout = nn.Dropout(p=0.1)
```

### 示例

```python
# Dropout rate: Paper did not specify
# Recommended: 0.1
# Reference: BERT (Devlin et al., 2019), ViT (Dosovitskiy et al., 2021)
# Alternatives: [0.0, 0.1, 0.2, 0.3]
# Impact: Higher dropout may improve generalization but slow convergence
self.dropout = nn.Dropout(p=0.1)

# Weight decay: Paper did not specify
# Recommended: 0.01
# Reference: AdamW default in Transformer architectures
# Alternatives: [0.0, 0.01, 0.05, 0.1]
# Impact: Higher values provide stronger regularization
```

---

## Common Pitfalls Warning ⚠️

在复现过程中，注意以下常见陷阱：

### 1. Tensor 操作陷阱
```python
# ❌ 错误: reshape 可能破坏内存连续性
x = x.reshape(B, -1)

# ✅ 正确: 使用 view (要求连续) 或 flatten
x = x.view(B, -1)  # 如果已连续
x = x.flatten(start_dim=1)  # 更安全
x = x.contiguous().view(B, -1)  # 确保连续后再 view
```

### 2. 论文图表可能有误
- 作者可能画错了架构图，**以文字描述和公式为准**
- 如发现图文不一致，在注释中标注

### 3. 超参数陷阱
- 区分"训练时使用的超参数" vs "最终报告的最佳超参数"
- 论文可能报告了多次实验的最优值，而非单次训练配置

### 4. 官方代码与论文不一致
- 如果论文提供了官方代码，**优先参考代码实现**
- 在注释中标注代码与论文描述的差异

### 5. 框架差异
```python
# ⚠️ BatchNorm momentum 在 PyTorch 和 TensorFlow 中定义不同!
# PyTorch: new_running_mean = (1 - momentum) * running_mean + momentum * batch_mean
# TensorFlow: new_running_mean = momentum * running_mean + (1 - momentum) * batch_mean
# 
# 如果论文使用 TensorFlow 且 momentum=0.9，在 PyTorch 中应设为 0.1
nn.BatchNorm2d(channels, momentum=0.1)  # Equivalent to TF momentum=0.9
```

### 6. 初始化差异
- 不同框架的默认初始化方式不同
- 如论文未指定，优先使用 PyTorch 默认值并标注

---

## PDF Reading Guidelines

当读取 PDF 论文时，需要特别关注：

### 1. 图表解析
- **Figure**: 网络架构图、数据流图、实验结果可视化
- **Table**: 超参数配置、实验对比、消融实验结果
- **Algorithm**: 伪代码、训练流程

### 2. 公式提取
- 主要关注 Method/Approach 章节的公式
- 注意公式编号，便于引用
- 检查 Appendix 中的补充公式

### 3. 实现细节
- **Section 3/4 (Method)**: 核心架构描述
- **Section 5 (Experiments)**: 训练细节、超参数
- **Appendix**: 额外实现细节、完整配置

### 4. 代码引用
如果论文提供了官方代码仓库：
- 优先参考官方实现
- 标注代码版本/commit hash
- 对比论文描述与代码实现的差异

---

## Output Structure

最终输出应包含以下文件结构：

```
output/
├── README.md           # 论文概述、使用说明
├── model.py            # 主模型实现
├── modules/            # 子模块
│   ├── __init__.py
│   ├── attention.py    # 注意力模块
│   ├── backbone.py     # 骨干网络
│   └── head.py         # 输出头
├── config.py           # 配置文件
└── requirements.txt    # 依赖列表
```

---

## Constraints

### 工具栈
- Python 3.10+
- PyTorch 2.0+
- Mermaid (for diagrams)
- einops (optional, for tensor operations)
- timm (optional, for pretrained backbones)

### 语言规范
- **分析与解释**: 使用简体中文
- **代码注释**: 使用英文
- **变量命名**: 使用英文，遵循 PEP 8

---

## Verification Checklist

在完成复现后，检查以下项目：

**Phase 1 - 论文解构**:
- [ ] 核心问题和创新点已明确
- [ ] 所有关键公式已提取并解释
- [ ] 超参数配置完整，未指定项已按规范标注

**Phase 2 - 架构可视化**:
- [ ] Mermaid 流程图包含所有主要组件
- [ ] 每个节点标注了 Tensor Shape (使用标准符号)
- [ ] 使用颜色区分不同类型组件
- [ ] 深层网络使用模块级粒度

**Phase 3 - 代码实现**:
- [ ] 继承 `nn.Module`
- [ ] 完整的类型提示
- [ ] 每层操作后有维度注释 (使用标准符号)
- [ ] 子模块已拆分
- [ ] 包含 `_init_weights` 方法
- [ ] 包含 `set_seed` 函数
- [ ] 未指定参数已按 Protocol 标注

**验证测试**:
- [ ] 随机 Tensor 前向传播无报错
- [ ] 输出 Shape 与预期一致
- [ ] 参数量与论文一致 (如有报告，允许 1% 误差)
- [ ] 梯度流检查通过
- [ ] 输出数值范围合理

**常见陷阱检查**:
- [ ] 已检查 reshape/view 的使用
- [ ] 已核对论文图表与文字描述
- [ ] 已注意框架差异 (如 BatchNorm momentum)
