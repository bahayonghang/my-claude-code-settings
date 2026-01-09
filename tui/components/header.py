"""Header 组件 - 顶部标题栏

显示应用标题和当前平台标识。
Requirements: 3.1, 3.2, 3.3, 3.4
"""

from textual.widgets import Static
from textual.containers import Horizontal

from tui.core.formatters import format_platform_badge


class Header(Static):
    """顶部标题栏组件
    
    显示应用标题 "MyClaude Skills Manager" 和当前平台标识。
    
    设计规范:
    - 使用 $primary 颜色作为背景 (Requirements 3.3)
    - 平台徽章使用 $secondary 背景色和圆角 (Requirements 3.2)
    - 标题文字加粗并使用高对比度颜色 (Requirements 3.1)
    - 保持一致的高度和内边距 (Requirements 3.4)
    """
    
    DEFAULT_CSS = """
    Header {
        dock: top;
        height: 3;
        background: $primary;
        padding: 0 2;
    }
    
    Header #header-container {
        width: 100%;
        height: 100%;
        align: left middle;
    }
    
    Header #app-title {
        content-align: left middle;
        width: 1fr;
        text-style: bold;
        color: $text;
    }
    
    Header #platform-badge {
        content-align: center middle;
        width: auto;
        min-width: 12;
        background: $secondary;
        padding: 0 2;
        margin: 0 0 0 1;
        color: $text;
        text-style: bold;
    }
    """
    
    # 应用图标
    APP_ICON = "🚀"
    APP_TITLE = "MyClaude Skills Manager"
    
    def __init__(self, platform: str = "") -> None:
        """初始化 Header 组件
        
        Args:
            platform: 当前平台名称
        """
        super().__init__()
        self._platform = platform
    
    def compose(self):
        """构建组件结构"""
        with Horizontal(id="header-container"):
            yield Static(f"{self.APP_ICON} {self.APP_TITLE}", id="app-title")
            yield Static(self._format_badge(), id="platform-badge")
    
    def _format_badge(self) -> str:
        """格式化平台徽章显示文本
        
        Returns:
            格式化后的徽章文本，包含大写平台名称
            
        Requirements: 3.2 - 平台徽章应显示大写格式
        """
        if self._platform:
            return format_platform_badge(self._platform)
        return "—"
    
    def set_platform(self, platform: str) -> None:
        """设置当前平台
        
        Args:
            platform: 平台名称 (claude/codex/gemini)
        """
        self._platform = platform
        badge = self.query_one("#platform-badge", Static)
        badge.update(self._format_badge())
