"""Footer 组件 - 底部状态栏

显示状态消息、快捷键提示和选中项目数量。
Requirements: 5.1, 5.2, 5.3, 5.4, 9.2, 9.3
"""

from enum import Enum
from textual.widgets import Static
from textual.containers import Horizontal, Vertical

from tui.core.formatters import (
    get_message_icon,
    get_message_css_class,
    format_selection_count,
    format_loading_message,
    format_progress_message,
)


class MessageLevel(Enum):
    """消息级别枚举"""
    INFO = "info"
    SUCCESS = "success"
    WARNING = "warning"
    ERROR = "error"


# 快捷键定义
KEYBINDINGS = [
    ("Tab", "切换"),
    ("Space", "选择"),
    ("i", "安装"),
    ("s", "安装选中"),
    ("a", "全部安装"),
    ("/", "搜索"),
    ("t", "平台"),
    ("q", "退出"),
]


class Footer(Static):
    """底部状态栏组件
    
    显示状态消息、快捷键提示和选中项目数量。
    美化特性:
    - 语义图标 (✓/⚠/✗/ℹ) 前缀状态消息
    - 快捷键提示栏
    - 主题背景色
    - 高亮选中计数
    """
    
    DEFAULT_CSS = """
    Footer {
        dock: bottom;
        height: 4;
        background: $background;
        padding: 0;
    }
    
    Footer #footer-main {
        width: 100%;
        height: 100%;
    }
    
    Footer #keybindings-row {
        width: 100%;
        height: 1;
        background: $panel;
        padding: 0 1;
    }
    
    Footer .keybinding {
        width: auto;
        padding: 0 1;
    }
    
    Footer .key {
        color: $accent;
        text-style: bold;
    }
    
    Footer .key-desc {
        color: $foreground;
    }
    
    Footer #status-row {
        width: 100%;
        height: 3;
        padding: 0 2;
        border-top: solid $primary;
    }
    
    Footer #status-message {
        content-align: left middle;
        width: 1fr;
        padding-left: 1;
    }
    
    Footer #selection-count {
        content-align: right middle;
        width: auto;
        padding: 0 2;
        color: $accent;
        text-style: bold;
    }
    
    Footer .status-info {
        color: $foreground;
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
        self._is_loading = False
    
    def _format_keybindings(self) -> str:
        """格式化快捷键提示"""
        parts = []
        for key, desc in KEYBINDINGS:
            parts.append(f"[bold $accent]{key}[/] {desc}")
        return "  ".join(parts)
    
    def compose(self):
        """构建组件结构"""
        with Vertical(id="footer-main"):
            # 快捷键提示行
            yield Static(self._format_keybindings(), id="keybindings-row", markup=True)
            # 状态行
            with Horizontal(id="status-row"):
                yield Static(self._format_status(), id="status-message", classes="status-info")
                yield Static(self._format_selection(), id="selection-count")

    def _format_status(self) -> str:
        """格式化状态消息，添加语义图标前缀
        
        Returns:
            带有语义图标的状态消息
        """
        if not self._message:
            return "Ready"
        
        # 添加语义图标前缀
        icon = get_message_icon(self._message_level.value)
        return f"{icon} {self._message}"
    
    def _format_selection(self) -> str:
        """格式化选中数量
        
        使用 formatters 模块的 format_selection_count 函数
        """
        return format_selection_count(self._selected_count)
    
    def _get_level_class(self) -> str:
        """获取消息级别对应的 CSS 类名"""
        return get_message_css_class(self._message_level.value)
    
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
        self._selected_count = max(0, count)  # 确保非负
        selection_widget = self.query_one("#selection-count", Static)
        selection_widget.update(self._format_selection())
    
    def clear_message(self) -> None:
        """清除状态消息"""
        self.show_message("", "info")
    
    def show_loading(self, item_type: str = "") -> None:
        """显示加载状态
        
        Args:
            item_type: 正在加载的项目类型 (可选)
        
        Requirements: 9.2 - 操作进行中时显示加载指示器
        """
        message = format_loading_message(item_type)
        self._message = message
        self._message_level = MessageLevel.INFO
        self._is_loading = True
        
        status_widget = self.query_one("#status-message", Static)
        # 移除旧的样式类
        for lvl in MessageLevel:
            status_widget.remove_class(f"status-{lvl.value}")
        status_widget.remove_class("progress-indicator")
        # 添加加载样式
        status_widget.add_class("status-info")
        status_widget.update(message)
    
    def show_progress(self, action: str, current: int, total: int) -> None:
        """显示进度状态
        
        Args:
            action: 操作名称 (如 "Installing")
            current: 当前进度
            total: 总数
        
        Requirements: 9.2, 9.3 - 显示进度指示
        """
        message = format_progress_message(action, current, total)
        self._message = message
        self._message_level = MessageLevel.INFO
        self._is_loading = True
        
        status_widget = self.query_one("#status-message", Static)
        # 移除旧的样式类
        for lvl in MessageLevel:
            status_widget.remove_class(f"status-{lvl.value}")
        # 添加进度样式
        status_widget.add_class("progress-indicator")
        status_widget.update(message)
    
    def hide_loading(self) -> None:
        """隐藏加载状态，恢复为 Ready"""
        self._is_loading = False
        status_widget = self.query_one("#status-message", Static)
        status_widget.remove_class("progress-indicator")
        self.show_message("Ready", "info")
