# git-commit

分析 Git 改动并自动生成 Conventional Commits 风格的提交信息。

## 概述

`git-commit` 命令仅使用 Git（不依赖包管理器或构建工具）来：

- 读取已暂存/未暂存的改动
- 在适当时建议拆分为多次提交
- 生成 Conventional Commits 格式的信息（可选 emoji）
- 按需执行 `git add` 和 `git commit`

## 使用方法

```bash
/git-commit                           # 分析当前改动
/git-commit --all                     # 暂存所有改动并提交
/git-commit --no-verify               # 跳过 Git 钩子
/git-commit --emoji                   # 在提交信息中包含 emoji
/git-commit --scope ui --type feat    # 指定作用域和类型
/git-commit --amend --signoff         # 修补上次提交并签名
```

## 选项

| 选项 | 描述 |
|------|------|
| `--no-verify` | 跳过本地 Git 钩子（`pre-commit`/`commit-msg`） |
| `--all` | 暂存区为空时自动 `git add -A` |
| `--amend` | 修补上一次提交 |
| `--signoff` | 添加 `Signed-off-by` 行（DCO 合规） |
| `--emoji` | 在提交信息中包含 emoji 前缀 |
| `--scope <scope>` | 指定提交作用域（如 `ui`、`docs`、`api`） |
| `--type <type>` | 强制提交类型（如 `feat`、`fix`、`docs`） |

## 工作原理

1. **仓库校验** - 检查是否在 Git 仓库内及当前分支状态
2. **改动检测** - 使用 `git status --porcelain` 和 `git diff` 分析改动
3. **拆分建议** - 基于以下因素建议拆分提交：
   - 不同关注点（不相关的功能/模块）
   - 不同类型（不要混合 `feat`、`fix`、`refactor`）
   - 文件模式（源代码 vs 文档/测试/配置）
   - 规模阈值（>300 行或跨多个顶级目录）
4. **信息生成** - 创建 Conventional Commits 格式：
   - 标题：`[<emoji>] <type>(<scope>)?: <subject>`（≤72 字符）
   - 正文：解释动机和改动的要点列表
   - 脚注：破坏性变更、issue 引用
5. **执行提交** - 使用生成的信息运行 `git commit`

## 提交类型

| Emoji | 类型 | 描述 |
|-------|------|------|
| ✨ | `feat` | 新功能 |
| 🐛 | `fix` | 缺陷修复 |
| 📝 | `docs` | 文档 |
| 🎨 | `style` | 代码风格/格式 |
| ♻️ | `refactor` | 代码重构 |
| ⚡️ | `perf` | 性能优化 |
| ✅ | `test` | 测试 |
| 🔧 | `chore` | 构建/工具 |
| 👷 | `ci` | CI/CD |
| ⏪️ | `revert` | 回滚提交 |

## 示例

**使用 emoji：**
```
✨ feat(ui): add user authentication flow
🐛 fix(api): handle token refresh race condition
📝 docs: update API usage examples
```

**不使用 emoji：**
```
feat(ui): add user authentication flow
fix(api): handle token refresh race condition
docs: update API usage examples
```

**包含正文：**
```
feat(auth): add OAuth2 login flow

- implement Google and GitHub third-party login
- add user authorization callback handling
- improve login state persistence logic

Closes #42
```

**破坏性变更：**
```
feat(api)!: redesign authentication API

- migrate from session-based to JWT authentication
- update all endpoint signatures
- remove deprecated login methods

BREAKING CHANGE: authentication API has been completely redesigned
```

## 重要说明

- **仅使用 Git**：不使用包管理器或构建命令
- **尊重钩子**：默认运行本地 Git 钩子；使用 `--no-verify` 跳过
- **非破坏性**：只写入 `.git/COMMIT_EDITMSG` 和暂存区
- **安全**：在 rebase/merge 冲突或 detached HEAD 状态下会提示确认
