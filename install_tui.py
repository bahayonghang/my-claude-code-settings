#!/usr/bin/env python3
"""MyClaude Skills TUI 安装管理器入口文件

使用 Textual 库构建的现代化终端用户界面，用于管理 Skills 和 Commands 的安装。

Usage:
    python install_tui.py

Requirements: 12.1, 12.2
"""

import sys


def main() -> int:
    """运行 TUI 应用
    
    Returns:
        退出码 (0 表示正常退出)
    """
    from tui.app import SkillInstallerApp
    
    app = SkillInstallerApp()
    app.run()
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        # 优雅处理 Ctrl+C 中断
        print("\nAborted by user.")
        sys.exit(0)
