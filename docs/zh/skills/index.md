# 技能概览

MyClaude Skills 提供一系列专门的 AI 技能，用于不同的开发任务。

## 可用技能

| 技能 | 分类 | 描述 |
|------|------|------|
| [article-cover](./article-cover) | 设计 | 生成专业的 SVG 封面图 |
| [codex](./codex) | 开发 | 通过 Codex CLI 进行代码分析和网络搜索 |
| [excalidraw](./excalidraw) | 设计 | 创建手绘风格图表 |
| [frontend-design](./frontend-design) | 设计 | 构建独特的前端界面 |
| [gemini-image](./gemini-image) | 设计 | 通过 Gemini API 生成图像 |
| [paper-replication](./paper-replication) | 开发 | 将深度学习论文复现为 PyTorch 代码 |
| [research](./research) | 研究 | 技术研究，支持引用 |
| [spec-interview](./spec-interview) | 规划 | 通过系统性提问完善规格说明 |
| [tech-blog](./tech-blog) | 文档 | 撰写技术博客 |
| [tech-design-doc](./tech-design-doc) | 文档 | 生成技术设计文档 |

## 技能分类

### 设计类技能
用于创建视觉资产和界面：
- **article-cover** - 文章 SVG 封面图
- **excalidraw** - 手绘风格图表
- **frontend-design** - 生产级 UI
- **gemini-image** - AI 生成图像

### 开发类技能
用于代码分析和生成：
- **codex** - 使用 Codex CLI 进行深度代码分析
- **paper-replication** - 深度学习论文复现为 PyTorch 代码

### 研究类技能
用于收集和组织信息：
- **research** - 带引用的网络研究

### 文档类技能
用于创建技术文档：
- **tech-blog** - 技术博客文章
- **tech-design-doc** - 设计文档
- **spec-interview** - 规格说明完善

## 安装

安装所有技能：

::: code-group
```bash [Linux/macOS]
./install.sh install-all
```
```powershell [Windows]
.\install.ps1 install-all
```
:::

安装指定技能：

::: code-group
```bash [Linux/macOS]
./install.sh install frontend-design excalidraw
```
```powershell [Windows]
.\install.ps1 install frontend-design excalidraw
```
:::
