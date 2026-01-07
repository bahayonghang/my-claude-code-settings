# OMO Agents 教程

受 [oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) 启发的多代理编排系统完整使用指南。

## 什么是 OMO Agents？

OMO Agents 是一个多代理协作系统，让专业的 AI 代理协同工作。不再是单个 AI 处理所有事情，而是让不同代理专注于各自擅长的领域：

- **Sisyphus** 编排复杂任务
- **Oracle** 提供架构指导
- **Explore** 搜索代码库
- **Librarian** 研究外部文档
- **Frontend Engineer** 创建精美 UI
- **Document Writer** 撰写技术文档
- **Multimodal Looker** 分析视觉内容

## 核心理念

oh-my-opencode 项目展示了关键原则：

1. **专业化**: 每个代理在自己的领域表现出色
2. **委派**: 将工作路由给正确的专家
3. **并行化**: 同时运行独立任务
4. **上下文效率**: 通过委派探索任务保持主代理上下文精简

## 安装

安装所有 OMO Agents 技能：

::: code-group
```bash [Linux/macOS]
./install.sh install sisyphus oracle explore librarian frontend-engineer document-writer multimodal-looker omo-agents
```
```powershell [Windows]
.\install.ps1 install sisyphus oracle explore librarian frontend-engineer document-writer multimodal-looker omo-agents
```
:::

或安装全部：

::: code-group
```bash [Linux/macOS]
./install.sh install-all
```
```powershell [Windows]
.\install.ps1 install-all
```
:::

## 快速开始

### 方法 1: 让 Sisyphus 编排

对于复杂任务，直接告诉 Sisyphus 你需要什么：

```
@sisyphus 给这个电商项目添加用户评价系统
```

Sisyphus 会：
1. 分析任务并创建 TODO 列表
2. 启动 @explore 查找现有相关代码
3. 咨询 @oracle 进行架构决策
4. 派遣 @librarian 研究最佳实践
5. 并行执行实现任务
6. 将 UI 工作委派给 @frontend-engineer
7. 让 @document-writer 更新文档

### 方法 2: 直接调用代理

对于特定需求，直接调用代理：

```
@oracle 状态管理应该用 Redux 还是 Zustand？

@explore 找到这个项目中所有认证相关的代码

@librarian Next.js 14 的 Server Actions 怎么用？

@frontend-engineer 创建一个带流畅动画的订阅表单

@document-writer 为用户服务编写 API 文档

@multimodal-looker 分析这个错误截图
```

## 代理参考

### Sisyphus - 编排者

**适用于**: 复杂多步骤任务、功能开发、重构项目

**工作流程**:
1. **Phase 0**: 分类意图（简单问答 vs 复杂任务）
2. **Phase 1**: 评估代码库结构和模式
3. **Phase 2A**: 探索和研究（委派给其他代理）
4. **Phase 2B**: 执行并追踪 TODO

**示例**:
```
@sisyphus 实现带 JWT token 的用户认证
```

### Oracle - 架构师

**适用于**: 设计决策、代码审查、调试指导、技术选型

**响应风格**: 直接的建议配合权衡分析

**示例**:
```
@oracle 审查这个认证流程的安全问题

@oracle 这个规模应该用微服务还是单体架构？
```

### Explore - 侦察兵

**适用于**: 查找代码、追踪依赖、理解结构

**使用工具**: grep、glob、LSP、ast-grep、git log/blame

**示例**:
```
@explore 找到支付处理在哪里

@explore 追踪 UserService 类的所有使用
```

### Librarian - 研究员

**适用于**: 外部文档、开源实现、最佳实践

**三种模式**:
- TYPE A: 概念性问题（"X 是什么？"）
- TYPE B: 实现参考（"怎么实现 X？"）
- TYPE C: 上下文和历史（"X 为什么这样设计？"）

**示例**:
```
@librarian 其他项目怎么实现限流？

@librarian React 19 推荐怎么处理表单验证？
```

### Frontend Engineer - UI 专家

**适用于**: 创建精美界面、动画、响应式设计

**原则**: 像素级完美、动效是灵魂、直觉优先

**示例**:
```
@frontend-engineer 创建一个带悬浮效果的仪表盘卡片组件

@frontend-engineer 构建一个带平滑进入/退出动画的模态框
```

### Document Writer - 技术写手

**适用于**: README、API 文档、架构文档、JSDoc 注释

**文档类型**: README.md、API 参考、架构文档、用户指南

**示例**:
```
@document-writer 为认证模块编写完整的 API 文档

@document-writer 给这个服务类添加 JSDoc 注释
```

### Multimodal Looker - 视觉分析师

**适用于**: 截图、PDF、图表、架构图、设计稿

**输出**: 相关信息的结构化提取

**示例**:
```
@multimodal-looker 这个错误截图显示什么？

@multimodal-looker 从这个图表提取数据
```

## 最佳实践

### 1. 选择正确的代理

| 需求 | 代理 |
|------|------|
| 复杂功能开发 | @sisyphus |
| 架构建议 | @oracle |
| 在项目中找代码 | @explore |
| 研究外部文档 | @librarian |
| 构建 UI 组件 | @frontend-engineer |
| 编写文档 | @document-writer |
| 分析图片/PDF | @multimodal-looker |

### 2. 提供良好的上下文

**不好**:
```
@explore 找那个函数
```

**好**:
```
@explore 找支付处理函数，可能在 src/services/ 或 src/api/ 目录
```

### 3. 不确定时用 Sisyphus

当不确定用哪个代理时，从 Sisyphus 开始：
```
@sisyphus 我需要改进用户列表页的性能
```

Sisyphus 会分析并路由到合适的代理。

### 4. 组合代理处理复杂任务

对于"添加用户评价"这样的功能：

1. `@sisyphus 添加用户评价系统`（编排一切）

或手动：
1. `@explore 查找现有评价或评分代码`
2. `@oracle 设计评价数据模型`
3. `@librarian 研究评价系统模式`
4. `@frontend-engineer 构建评价 UI`
5. `@document-writer 更新 API 文档`

## 示例工作流

### 功能开发

```
用户: @sisyphus 给应用添加暗色模式支持

Sisyphus:
├── @explore → 查找现有主题/样式代码
├── @oracle → 推荐暗色模式实现方案
├── @librarian → 研究 CSS 自定义属性最佳实践
├── 执行: 创建主题上下文和 CSS 变量
├── @frontend-engineer → 更新组件支持暗色模式
└── @document-writer → 记录主题配置
```

### Bug 调查

```
用户: @sisyphus 用户反馈登录偶尔失败

Sisyphus:
├── @explore → 查找认证/登录代码路径
├── @oracle → 分析潜在故障点
├── @librarian → 检查认证库的已知问题
└── 执行: 实现修复并添加错误处理
```

### 代码重构

```
用户: @sisyphus 重构用户模块使用仓储模式

Sisyphus:
├── @explore → 映射所有用户相关文件和依赖
├── @oracle → 设计仓储接口
├── @librarian → 研究仓储模式实现
├── 执行: 重构并追踪 TODO
└── @document-writer → 更新架构文档
```

## 技巧和窍门

1. **并行执行**: Sisyphus 同时运行独立任务——不用担心顺序

2. **TODO 追踪**: Sisyphus 为复杂任务维护 TODO 列表——随时检查进度

3. **上下文效率**: 代理委派探索以保持上下文精简——相信这个过程

4. **挑战请求**: Sisyphus 可能质疑次优方案——考虑反馈

5. **直接调用更快**: 对于简单、特定的需求，直接调用代理而不是通过 Sisyphus

## 故障排除

**代理响应不符合预期？**
- 提供更多项目上下文
- 具体说明你需要什么
- 如果任务不匹配，尝试其他代理

**Sisyphus 创建太多子任务？**
- 将请求拆分为更小、更聚焦的任务
- 对简单需求使用直接代理调用

**结果不准确？**
- 验证代理可以访问相关文件
- 提供文件路径或代码片段作为上下文
