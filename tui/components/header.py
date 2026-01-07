"""Header 组件 - 顶部标题栏

显示应用标题和当前平台标识。
Requirements: 2.1
"""

from textual.widgets import Static
from textual.containers import Horizontal


class Header(Static):
    """顶部标题栏组件
    
    显示应用标题 "MyClaude Skills Manager" 和当前平台标识。
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
    }
    
    Header #app-title {
        content-align: left middle;
        width: 1fr;
        text-style: bold;
    }
    
    Header #platform-badge {
        content-align: right middle;
        width: auto;
        background: $secondary;
        padding: 0 2;
    }
    """
    
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
            yield Static("🚀 MyClaude Skills Manager", id="app-title")
            yield Static(self._format_platform(), id="platform-badge")
    
    def _format_platform(self) -> str:
        """格式化平台显示文本"""
        if self._platform:
            return f"Platform: {self._platform.upper()}"
        return "Platform: -"
    
    def set_platform(self, platform: str) -> None:
        """设置当前平台
        
        Args:
            platform: 平台名称 (claude/codex/gemini)
        """
        self._platform = platform
        badge = self.query_one("#platform-badge", Static)
        badge.update(self._format_platform())
