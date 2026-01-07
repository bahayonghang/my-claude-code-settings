"""平台选择屏幕

启动时首先显示，让用户选择目标平台 (Claude, Codex, Gemini)。
支持键盘导航和选择。

Requirements: 1.1, 1.2, 1.3, 1.4, 1.5
"""

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static, OptionList
from textual.widgets.option_list import Option
from textual.binding import Binding
from textual.containers import Center, Vertical


class PlatformSelectScreen(Screen):
    """平台选择屏幕
    
    显示三个平台选项，支持键盘导航和选择。
    
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
        background: $surface;
    }
    
    PlatformSelectScreen #container {
        width: 60;
        height: auto;
        padding: 2 4;
    }
    
    PlatformSelectScreen #title {
        text-align: center;
        text-style: bold;
        padding: 1 0;
        color: $text;
    }
    
    PlatformSelectScreen #subtitle {
        text-align: center;
        color: $text-muted;
        padding: 0 0 2 0;
    }
    
    PlatformSelectScreen #platform-list {
        width: 100%;
        height: auto;
        border: round $primary;
        padding: 1 2;
    }
    
    PlatformSelectScreen #platform-list:focus {
        border: round $accent;
    }
    
    PlatformSelectScreen #hint {
        text-align: center;
        color: $text-muted;
        padding: 2 0 0 0;
    }
    """
    
    # 平台配置: (id, 显示名称, 目标路径)
    PLATFORMS = [
        ("claude", "Claude", "~/.claude/"),
        ("codex", "Codex", "~/.codex/"),
        ("gemini", "Gemini", "~/.gemini/"),
    ]
    
    def compose(self) -> ComposeResult:
        """构建屏幕组件"""
        with Center():
            with Vertical(id="container"):
                yield Static("🚀 MyClaude Skills Manager", id="title")
                yield Static("Select your target platform", id="subtitle")
                yield OptionList(
                    *[Option(f"{name}  ({path})", id=key) 
                      for key, name, path in self.PLATFORMS],
                    id="platform-list"
                )
                yield Static("↑↓ Navigate  Enter Select  Esc Quit", id="hint")
    
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
