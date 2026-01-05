# 创建技能

## 技能结构

最简单的技能只需要一个 `SKILL.md` 文件：

```
skills/
└── my-skill/
    └── SKILL.md
```

复杂技能可以包含额外目录：

```
skills/
└── my-skill/
    ├── SKILL.md        # 必需
    ├── config/         # 配置模板
    ├── tips/           # 使用提示
    ├── references/     # 技术参考
    ├── scripts/        # 辅助脚本
    └── cookbook/       # 代码示例
```

## SKILL.md 格式

每个 `SKILL.md` 必须包含 YAML frontmatter：

```yaml
---
name: my-skill
description: 用于列表展示的简短描述
license: MIT  # 可选
---

# My Skill

详细说明和文档...
```

## 编写有效的技能

### 具体明确

提供清晰、可操作的指令：

```markdown
## 工作流程

1. 分析用户需求
2. 生成初始设计
3. 根据反馈迭代
4. 输出最终结果
```

### 包含示例

展示预期的输入和输出：

```markdown
## 示例

**输入：** "创建一个登录表单"

**输出：** 一个响应式登录表单，包含邮箱/密码字段、
验证和提交按钮。
```

### 定义约束

设置清晰的边界：

```markdown
## 约束

- 输出必须是有效的 HTML5
- 使用语义化元素
- 确保 WCAG 2.1 AA 合规
```

## 测试技能

1. 安装技能：
   ```bash
   ./install.sh install my-skill
   ```

2. 在 Claude Code 中调用技能进行测试

3. 根据结果迭代 `SKILL.md`

## 最佳实践

- 保持技能专注于单一领域
- 使用清晰简洁的语言
- 包含实用示例
- 记录任何前置要求
- 遵循现有技能的模式以保持一致性
