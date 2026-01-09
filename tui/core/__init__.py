"""
TUI 核心业务逻辑模块

包含:
- models: 数据模型 (ItemType, InstallStatus, ItemInfo, InstallResult)
- manager: TUIManager 封装 SkillManager
- theme: MyClaude 自定义主题
- formatters: 格式化工具函数
"""

from .models import ItemType, InstallStatus, ItemInfo, InstallResult
from .manager import TUIManager
from .theme import myclaudeTheme, THEME_COLORS, REQUIRED_THEME_PROPERTIES
from .formatters import (
    PlatformConfig,
    format_platform_option,
    format_platform_badge,
    format_checkbox,
    format_status_icon,
    format_selection_count,
    get_message_icon,
    get_message_css_class,
    format_empty_state_message,
    format_loading_message,
    format_progress_message,
    CHECKBOX_CHECKED,
    CHECKBOX_UNCHECKED,
    STATUS_INSTALLED,
    STATUS_NOT_INSTALLED,
    ARROW_INDICATOR,
    ICON_EMPTY,
    ICON_LOADING,
    ICON_PROGRESS,
)

__all__ = [
    "ItemType",
    "InstallStatus",
    "ItemInfo",
    "InstallResult",
    "TUIManager",
    "myclaudeTheme",
    "THEME_COLORS",
    "REQUIRED_THEME_PROPERTIES",
    # Formatters
    "PlatformConfig",
    "format_platform_option",
    "format_platform_badge",
    "format_checkbox",
    "format_status_icon",
    "format_selection_count",
    "get_message_icon",
    "get_message_css_class",
    "format_empty_state_message",
    "format_loading_message",
    "format_progress_message",
    "CHECKBOX_CHECKED",
    "CHECKBOX_UNCHECKED",
    "STATUS_INSTALLED",
    "STATUS_NOT_INSTALLED",
    "ARROW_INDICATOR",
    "ICON_EMPTY",
    "ICON_LOADING",
    "ICON_PROGRESS",
]
