"""MyClaude Skills TUI 自定义主题

定义 MyClaude 专属的深色主题，灵感来自现代 IDE 和终端应用。

Requirements: 1.1, 1.4
"""

from textual.theme import Theme


# 主题颜色常量 - 便于测试和复用
THEME_COLORS = {
    "primary": "#7C3AED",      # 紫色 - 主品牌色
    "secondary": "#06B6D4",    # 青色 - 次要强调
    "accent": "#F59E0B",       # 琥珀色 - 高亮/警告
    "foreground": "#F1F5F9",   # 更亮的浅灰 - 主文本 (提升对比度)
    "background": "#0F172A",   # 深蓝黑 - 背景
    "success": "#10B981",      # 绿色 - 成功状态
    "warning": "#F59E0B",      # 琥珀色 - 警告状态
    "error": "#EF4444",        # 红色 - 错误状态
    "surface": "#1E293B",      # 深灰蓝 - 表面/卡片
    "panel": "#475569",        # 更亮的灰蓝 - 面板 (增强与 surface 对比)
}

# 必需的主题属性列表
REQUIRED_THEME_PROPERTIES = [
    "primary",
    "secondary", 
    "accent",
    "foreground",
    "background",
    "success",
    "warning",
    "error",
    "surface",
    "panel",
]


def create_myclaude_theme() -> Theme:
    """创建 MyClaude 自定义主题
    
    Returns:
        配置好的 Theme 对象
    """
    return Theme(
        name="myclaude",
        primary=THEME_COLORS["primary"],
        secondary=THEME_COLORS["secondary"],
        accent=THEME_COLORS["accent"],
        foreground=THEME_COLORS["foreground"],
        background=THEME_COLORS["background"],
        success=THEME_COLORS["success"],
        warning=THEME_COLORS["warning"],
        error=THEME_COLORS["error"],
        surface=THEME_COLORS["surface"],
        panel=THEME_COLORS["panel"],
        dark=True,
        variables={
            "block-cursor-text-style": "bold",
            "footer-key-foreground": THEME_COLORS["primary"],
            "input-selection-background": f"{THEME_COLORS['primary']} 40%",
            "input-cursor-foreground": THEME_COLORS["primary"],
        },
    )


# 预创建的主题实例
myclaudeTheme = create_myclaude_theme()
