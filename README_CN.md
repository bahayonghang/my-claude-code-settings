# MyClaude Skills

Claude Code 技能和提示词集合，用于增强 AI 辅助开发工作流。

## 快速开始

```bash
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
| [github-wrapped](skills/github-wrapped/) | 生成可验证的 GitHub 年度回顾单文件 HTML |
| [research](skills/research/) | 技术研究，支持网络搜索和引用 |
| [tech-blog](skills/tech-blog/) | 撰写带源码分析的技术博客 |
| [tech-design-doc](skills/tech-design-doc/) | 生成结构化的技术设计文档 |

## 项目结构

```
.
├── install.sh              # 技能安装和提示词同步工具
├── install.ps1             # Windows PowerShell 安装脚本
├── prompts/
│   ├── CLAUDE.md           # 全局工作流配置
│   └── TRANSLATE.md        # 翻译指南
└── skills/
    └── <skill-name>/
        └── SKILL.md        # 技能定义和说明
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

## 安装方法

### Linux/macOS

```bash
git clone https://github.com/user/my-claude-code-settings.git
cd my-claude-code-settings
./install.sh install-all
./install.sh prompt-update
```

### Windows

```powershell
git clone https://github.com/user/my-claude-code-settings.git
cd my-claude-code-settings
.\install.ps1
```

## 命令说明

```bash
./install.sh list           # 列出可用技能
./install.sh install <skill> # 安装指定技能
./install.sh install-all    # 安装所有技能
./install.sh prompt-diff    # 显示本地与全局 CLAUDE.md 的差异
./install.sh prompt-update  # 同步 CLAUDE.md 到 ~/.claude/
```

## 许可证

MIT
