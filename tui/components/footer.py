"""Footer 组件 - 底部状态栏

显示状态消息和选中项目数量。
Requirements: 2.5, 9.3, 13.1, 13.2, 13.3
"""

from enum import Enum
from textual.widgets import Static
from textual.containers import Horizontal


class MessageLevel(Enum):
    """消息级别枚举"""
    INFO = "info"
    SUCCESS = "success"
    WARNING = "warning"
    ERROR = "error"


class Footer(Static):
    """底部状态栏组件
    
    显示状态消息和选中项目数量，支持不同级别的消息样式。
    """
    
    DEFAULT_CSS = """
    Footer {
        dock: bottom;
        height: 3;
        background: $surface-darken-1;
        padding: 0 2;
    }
    
    Footer #footer-container {
        width: 100%;
        height: 100%;
    }
    
    Footer #status-message {
        content-align: left middle;
        width: 1fr;
    }
    
    Footer #selection-count {
        content-align: right middle;
        width: auto;
        padding: 0 2;
    }
    
    Footer .status-info {
        color: $text;
    }
    
    Footer .status-success {
        color: $success;
    }
    
    Footer .status-warning {
        color: $warning;
    }
    
    Footer .status-error {
        color: $error;
    }
    """
    
    def __init__(self) -> None:
        """初始化 Footer 组件"""
        super().__init__()
        self._message = ""
        self._message_level = MessageLevel.INFO
        self._selected_count = 0
    
    def compose(self):
        """构建组件结构"""
        with Horizontal(id="footer-container"):
            yield Static(self._format_status(), id="status-message")
            yield Static(self._format_selection(), id="selection-count")
    
    def _format_status(self) -> str:
        """格式化状态消息"""
        return self._message if self._message else "Ready"
    
    def _format_selection(self) -> str:
        """格式化选中数量"""
        if self._selected_count > 0:
            return f"Selected: {self._selected_count}"
        return ""
    
    def _get_level_class(self) -> str:
        """获取消息级别对应的 CSS 类名"""
        return f"status-{self._message_level.value}"
    
    def show_message(self, message: str, level: str = "info") -> None:
        """显示状态消息
        
        Args:
            message: 消息内容
            level: 消息级别 (info/success/warning/error)
        """
        self._message = message
        try:
            self._message_level = MessageLevel(level)
        except ValueError:
            self._message_level = MessageLevel.INFO
        
        status_widget = self.query_one("#status-message", Static)
        # 移除旧的样式类
        for lvl in MessageLevel:
            status_widget.remove_class(f"status-{lvl.value}")
        # 添加新的样式类
        status_widget.add_class(self._get_level_class())
        status_widget.update(self._format_status())
    
    def update_selection_count(self, count: int) -> None:
        """更新选中项目数量
        
        Args:
            count: 选中的项目数量
        """
        self._selected_count = count
        selection_widget = self.query_one("#selection-count", Static)
        selection_widget.update(self._format_selection())
    
    def clear_message(self) -> None:
        """清除状态消息"""
        self.show_message("", "info")
