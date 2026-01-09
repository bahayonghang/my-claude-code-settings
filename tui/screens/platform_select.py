"""平台选择屏幕

启动时首先显示，让用户选择目标平台 (Claude, Codex, Gemini)。
支持键盘导航和选择。

Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 2.1, 2.2, 2.3, 2.4, 2.5
"""

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static, OptionList
from textual.widgets.option_list import Option
from textual.binding import Binding
from textual.containers import Center, Vertical

from ..core import PlatformConfig, format_platform_option


class PlatformSelectScreen(Screen):
    """平台选择屏幕
    
    显示三个平台选项，支持键盘导航和选择。
    美化后的界面包含:
    - 居中卡片容器，圆角边框和微妙阴影效果
    - 带 emoji 的应用标题
    - 清晰的平台选项列表，显示名称和目标路径
    - Unicode 符号美化的键盘提示
    
    Bindings:
        - Enter: 选择当前高亮的平台
        - Escape: 退出应用
        - Up/Down: 导航选项 (由 OptionList 处理)
    """
    
    BINDINGS = [
        Binding("escape", "quit", "Quit", show=True),
    ]
    
    DEFAULT_CSS = """
    PlatformSelectScreen {
        align: center middle;
        background: $background;
        width: 100%;
        height: 100%;
    }
    
    /* 卡片容器 - 圆角边框、背景色、微妙边框，放大尺寸 */
    PlatformSelectScreen #container {
        width: 70;
        height: auto;
        padding: 4 6;
        border: round $primary;
        background: $surface;
    }
    
    /* 标题 - emoji + 主品牌色 */
    PlatformSelectScreen #title {
        text-align: center;
        text-style: bold;
        padding: 2 0;
        color: $primary;
    }
    
    /* 分隔线 */
    PlatformSelectScreen #separator {
        text-align: center;
        color: $primary-darken-2;
        padding: 1 0 2 0;
    }
    
    /* 副标题 - 放大字体 */
    PlatformSelectScreen #subtitle {
        text-align: center;
        color: $text-muted;
        padding: 1 0 3 0;
    }
    
    /* 平台选项列表 - 放大尺寸 */
    PlatformSelectScreen #platform-list {
        width: 100%;
        height: auto;
        border: round $panel;
        padding: 2 3;
        background: $surface-darken-1;
    }
    
    /* 聚焦时高亮边框 */
    PlatformSelectScreen #platform-list:focus {
        border: round $accent;
    }
    
    /* 高亮选项样式 */
    PlatformSelectScreen #platform-list > .option-list--option-highlighted {
        background: $primary;
        color: $text;
        text-style: bold;
    }
    
    /* 键盘提示 - Unicode 符号美化 */
    PlatformSelectScreen #hint {
        text-align: center;
        color: $text-muted;
        padding: 3 0 1 0;
    }
    """
    
    # 平台配置: (id, 显示名称, 目标路径)
    PLATFORMS = [
        PlatformConfig("claude", "Claude", "~/.claude/"),
        PlatformConfig("codex", "Codex", "~/.codex/"),
        PlatformConfig("gemini", "Gemini", "~/.gemini/"),
    ]
    
    def compose(self) -> ComposeResult:
        """构建屏幕组件
        
        Requirements: 2.1, 2.2, 2.3, 2.4, 2.5
        """
        with Center():
            with Vertical(id="container"):
                # 标题带 emoji 和主品牌色
                yield Static("🚀 MyClaude Skills Manager", id="title")
                # 分隔线
                yield Static("─" * 30, id="separator")
                # 副标题
                yield Static("Select your target platform", id="subtitle")
                # 平台选项列表 - 使用格式化函数显示名称和路径
                yield OptionList(
                    *[Option(format_platform_option(platform), id=platform.id) 
                      for platform in self.PLATFORMS],
                    id="platform-list"
                )
                # 键盘提示 - Unicode 符号美化
                yield Static("↑↓ Navigate  ⏎ Select  ⎋ Quit", id="hint")
    
    def on_mount(self) -> None:
        """屏幕挂载时聚焦到选项列表"""
        option_list = self.query_one("#platform-list", OptionList)
        option_list.focus()
    
    def on_option_list_option_selected(self, event: OptionList.OptionSelected) -> None:
        """处理平台选择事件
        
        当用户按 Enter 选择平台时触发。
        """
        platform_id = event.option.id
        if platform_id:
            self.app.set_platform(str(platform_id))
    
    def action_quit(self) -> None:
        """退出应用"""
        self.app.exit()
