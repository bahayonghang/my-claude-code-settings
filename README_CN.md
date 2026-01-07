# MyClaude Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Claude Code 技能和提示词集合，用于增强 AI 辅助开发工作流。

## 特性

- 🎯 可复用的 AI 技能模块，覆盖前端设计、技术研究、文档生成等场景
- 📦 统一的技能定义格式（`SKILL.md`），便于扩展和维护
- 🔄 跨平台安装脚本（Bash + PowerShell）
- 🎛️ 双目标支持：Claude Code (`~/.claude/`) 和 Codex CLI (`~/.codex/`)
- ⚡ 斜杠命令，用于常见工作流（git commit 等）

## 前置要求

- Git
- Bash (Linux/macOS) 或 PowerShell (Windows)
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) 或 [Codex CLI](https://github.com/openai/codex)

## 快速开始

```bash
# 克隆仓库
git clone https://github.com/anthropics/my-claude-skills.git
cd my-claude-skills

# 安装所有技能
./install.sh install-all

# 更新全局提示词配置
./install.sh prompt-update
```

运行 `./install.sh help` 查看更多选项。

## 技能列表

| 技能 | 描述 |
|------|------|
| [article-cover](skills/article-cover/) | 为博客文章生成专业的 SVG 封面图 |
| [codex](skills/codex/) | Codex CLI 集成，支持深度代码分析和网络搜索 |
| [excalidraw](skills/excalidraw/) | 创建手绘风格的 Excalidraw JSON 图表 |
| [frontend-design](skills/frontend-design/) | 构建独特的生产级前端界面 |
| [gemini-image](skills/gemini-image/) | 通过 Gemini API 生成图像（文生图、图生图） |
| [research](skills/research/) | 技术研究，支持网络搜索和引用 |
| [spec-interview](skills/spec-interview/) | 通过系统性提问深度访谈，完善技术规格说明 |
| [paper-replication](skills/paper-replication/) | 将深度学习论文复现为工业级 PyTorch 代码 |
| [tech-blog](skills/tech-blog/) | 撰写带源码分析的技术博客 |
| [tech-design-doc](skills/tech-design-doc/) | 生成结构化的技术设计文档 |

## 命令

斜杠命令提供常见工作流的快捷访问。安装到 `~/.claude/commands/`。

| 命令 | 描述 |
|------|------|
| [git-commit](commands/git-commit.md) | 分析改动并生成 Conventional Commits 风格的提交信息（可选 emoji） |

### OMO Agents (多代理系统)

受 [oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) 启发，这些技能实现多代理协作，让专业代理协同处理复杂任务。

| 技能 | 描述 |
|------|------|
| [omo-agents](skills/omo-agents/) | 多代理编排系统概览和使用指南 |
| [sisyphus](skills/sisyphus/) | 主编排代理，用于复杂任务规划和并行执行 |
| [oracle](skills/oracle/) | 专家架构师，负责设计决策、代码审查和调试指导 |
| [explore](skills/explore/) | 快速代码搜索代理，定位代码和追踪依赖 |
| [librarian](skills/librarian/) | 文档研究员，查找外部文档和最佳实践 |
| [frontend-engineer](skills/frontend-engineer/) | UI/UX 专家，创建精美、精致的界面 |
| [document-writer](skills/document-writer/) | 技术写手，撰写 README、API 文档和架构文档 |
| [multimodal-looker](skills/multimodal-looker/) | 视觉分析师，分析图片、PDF、图表和图表 |

## 安装方法

### Linux/macOS

```bash
git clone https://github.com/anthropics/my-claude-skills.git
cd my-claude-skills

# 安装所有技能到 Claude
./install.sh install-all

# 或安装到 Codex
./install.sh --target=codex install-all

# 更新全局 CLAUDE.md
./install.sh prompt-update
```

### Windows (PowerShell)

```powershell
git clone https://github.com/anthropics/my-claude-skills.git
cd my-claude-skills

# 安装所有技能到 Claude
.\install.ps1 install-all

# 或安装到 Codex
.\install.ps1 -Target codex install-all

# 更新全局 CLAUDE.md
.\install.ps1 prompt-update
```

## 命令说明

### Linux/macOS (Bash)

| 命令 | 描述 |
|------|------|
| `./install.sh list` | 列出所有可用技能 |
| `./install.sh installed` | 列出已安装的技能 |
| `./install.sh install <skill> [skill2...]` | 安装指定技能 |
| `./install.sh install-all` | 安装所有技能 |
| `./install.sh interactive` | 交互式技能选择 |
| `./install.sh prompt-diff` | 显示本地与全局 CLAUDE.md 的差异 |
| `./install.sh prompt-update` | 同步 CLAUDE.md 到 ~/.claude/ |
| `./install.sh --target=codex <command>` | 以 Codex 为目标执行命令 |

### Windows (PowerShell)

| 命令 | 描述 |
|------|------|
| `.\install.ps1 list` | 列出所有可用技能 |
| `.\install.ps1 installed` | 列出已安装的技能 |
| `.\install.ps1 install <skill> [skill2...]` | 安装指定技能 |
| `.\install.ps1 install-all` | 安装所有技能 |
| `.\install.ps1 interactive` | 交互式技能选择 |
| `.\install.ps1 prompt-diff` | 显示本地与全局 CLAUDE.md 的差异 |
| `.\install.ps1 prompt-update` | 同步 CLAUDE.md 到 ~/.claude/ |
| `.\install.ps1 -Target codex <command>` | 以 Codex 为目标执行命令 |

## 项目结构

```
.
├── install.sh              # Bash 安装脚本 (Linux/macOS)
├── install.ps1             # PowerShell 安装脚本 (Windows)
├── prompts/
│   ├── CLAUDE.md           # 全局工作流配置
│   └── TRANSLATE.md        # 翻译指南
├── commands/               # 斜杠命令
│   └── git-commit.md       # Git 提交命令
└── skills/
    └── <skill-name>/
        ├── SKILL.md        # 技能定义（必需）
        ├── config/         # 配置模板（可选）
        ├── tips/           # 使用提示（可选）
        ├── references/     # 参考文档（可选）
        ├── scripts/        # 辅助脚本（可选）
        └── cookbook/       # 代码示例（可选）
```

## 提示词说明

### CLAUDE.md

基于 Linus Torvalds 风格工程原则的全局工作流配置：
- 强制 KISS/YAGNI 原则
- 结构化工作流（接收 → 上下文收集 → 探索 → 规划 → 执行 → 验证 → 交付）
- 通过 Codex 集成在线搜索
- 交付前自检清单

### TRANSLATE.md

技术内容翻译指南：
- 自然表达优先于逐字翻译
- 保留代码、品牌名和通用技术术语
- 对歧义术语添加标注

## 贡献指南

### 添加新技能

1. 在 `skills/` 下创建新目录：
   ```bash
   mkdir skills/my-new-skill
   ```

2. 创建包含 YAML frontmatter 的 `SKILL.md`：
   ```yaml
   ---
   name: my-new-skill
   description: 用于列表展示的简短描述
   license: MIT  # 可选
   ---

   # My New Skill

   详细说明和文档...
   ```

3. （可选）添加辅助目录：
   - `config/` - 配置模板
   - `tips/` - 使用提示
   - `references/` - 技术参考
   - `scripts/` - 辅助脚本
   - `cookbook/` - 代码示例

4. 测试安装：
   ```bash
   ./install.sh install my-new-skill
   ```

### 贡献规范

- 保持 `SKILL.md` 聚焦且可操作
- 使用清晰简洁的语言
- 适当添加示例
- 遵循现有技能的模式以保持一致性

## 常见问题

**Q: Claude 和 Codex 目标有什么区别？**

A: Claude 目标安装到 `~/.claude/skills/` 供 Claude Code 使用，Codex 目标安装到 `~/.codex/skills/` 供 OpenAI Codex CLI 使用。技能格式兼容两者。

**Q: 如何更新已安装的技能？**

A: 重新运行安装命令即可，会用最新版本覆盖现有技能。

**Q: 可以使用多个来源的技能吗？**

A: 可以。`installed` 命令会显示哪些技能来自本仓库，哪些来自外部。

**Q: 更新 CLAUDE.md 时备份存储在哪里？**

A: 备份创建在 `~/.claude/` 目录下，带有时间戳后缀，如 `CLAUDE.md.backup.20240115_143022`。

## 许可证

MIT
