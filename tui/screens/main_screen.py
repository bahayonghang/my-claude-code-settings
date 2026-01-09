"""主界面屏幕

包含 Skills 和 Commands 两个标签页，支持安装、选择、搜索等操作。

Requirements: 2.2, 2.3, 2.4, 2.6, 6.1, 6.2, 7.1, 8.1, 8.2, 9.1, 9.2, 11.1
"""

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import TabbedContent, TabPane, Input, Static
from textual.binding import Binding
from textual.containers import Vertical, Container

from ..components.header import Header
from ..components.footer import Footer
from ..components.item_list import ItemListView, SelectableItem
from ..core.manager import TUIManager
from ..core.models import InstallStatus


class MainScreen(Screen):
    """主界面屏幕
    
    集成 Header、TabbedContent (Skills/Commands)、Footer。
    支持安装、选择、搜索等操作。
    
    Bindings:
        - Tab: 切换标签页
        - i/Enter: 安装当前聚焦项
        - s: 安装选中项
        - a: 安装全部
        - Space: 切换选择状态
        - Ctrl+A: 全选
        - Ctrl+D: 取消全选
        - /: 搜索
        - t: 切换平台
        - q: 退出
    """
    
    BINDINGS = [
        Binding("tab", "next_tab", "Switch Tab", show=True),
        Binding("i", "install_focused", "Install", show=True),
        Binding("enter", "install_focused", "Install", show=False),
        Binding("s", "install_selected", "Install Selected", show=True),
        Binding("a", "install_all", "Install All", show=True),
        Binding("space", "toggle_selection", "Select", show=True),
        Binding("ctrl+a", "select_all", "Select All", show=True),
        Binding("ctrl+d", "deselect_all", "Deselect All", show=True),
        Binding("slash", "search", "Search", show=True),
        Binding("t", "toggle_platform", "Switch Platform", show=True),
        Binding("q", "quit", "Quit", show=True),
        Binding("escape", "clear_search", "Clear Search", show=False),
    ]
    
    DEFAULT_CSS = """
    MainScreen {
        background: $surface;
    }
    
    MainScreen #main-container {
        width: 100%;
        height: 100%;
    }
    
    MainScreen #content-area {
        width: 100%;
        height: 1fr;
        padding: 1 2;
    }
    
    MainScreen #search-container {
        width: 100%;
        height: 5;
        padding: 1 2;
    }
    
    MainScreen #search-container.-hidden {
        display: none;
    }
    
    /* 搜索框样式 - Requirements: 7.1, 7.2, 7.3 */
    MainScreen #search-input {
        width: 100%;
        height: 3;
        border: round $panel;
        background: $background;
        padding: 0 2;
    }
    
    MainScreen #search-input:focus {
        border: round $accent;
        background: $surface;
    }
    
    /* TabbedContent 样式 - Requirements: 6.1, 6.2, 6.3, 6.4 */
    MainScreen TabbedContent {
        height: 1fr;
    }
    
    MainScreen TabPane {
        padding: 1;
    }
    """
    
    def __init__(self, platform: str = "claude") -> None:
        """初始化主界面
        
        Args:
            platform: 目标平台
        """
        super().__init__()
        self._platform = platform
        self._manager: TUIManager | None = None
        self._search_visible = False
    
    @property
    def manager(self) -> TUIManager:
        """获取 TUIManager 实例"""
        if self._manager is None:
            self._manager = TUIManager(self._platform)
        return self._manager
    
    def set_platform(self, platform: str) -> None:
        """设置平台并刷新数据
        
        Args:
            platform: 平台名称
        """
        self._platform = platform
        self._manager = TUIManager(platform)
        self._refresh_data()
    
    def compose(self) -> ComposeResult:
        """构建屏幕组件"""
        yield Header(platform=self._platform)
        with Vertical(id="main-container"):
            with Container(id="search-container", classes="-hidden"):
                yield Input(placeholder="Search... (Esc to close)", id="search-input")
            with Container(id="content-area"):
                with TabbedContent(id="tabs"):
                    with TabPane("Skills", id="skills-tab"):
                        yield ItemListView(item_type="skills", id="skills-list")
                    with TabPane("Commands", id="commands-tab"):
                        yield ItemListView(item_type="commands", id="commands-list")
        yield Footer()
    
    def on_mount(self) -> None:
        """屏幕挂载时加载数据"""
        self._refresh_data()
        # 聚焦到 skills 列表
        skills_list = self.query_one("#skills-list", ItemListView)
        skills_list.focus()
    
    def _refresh_data(self) -> None:
        """刷新数据
        
        Requirements: 2.7 - 检测源目录不存在时显示错误
        """
        # 更新 Header 平台显示
        header = self.query_one(Header)
        header.set_platform(self._platform)
        
        # 检查源目录是否存在
        skills_exist = self.manager.check_skills_source_exists()
        commands_exist = self.manager.check_commands_source_exists()
        
        # 加载 Skills
        skills_list = self.query_one("#skills-list", ItemListView)
        if skills_exist:
            skills = self.manager.get_skills()
            skills_list.load_items(skills)
        else:
            skills_list.load_items([])
            self._show_message(
                f"Skills directory not found: {self.manager.get_skills_source_dir()}", 
                "error"
            )
        
        # 加载 Commands
        commands_list = self.query_one("#commands-list", ItemListView)
        if commands_exist:
            commands = self.manager.get_commands()
            commands_list.load_items(commands)
        else:
            commands_list.load_items([])
            # 只有当 skills 目录存在时才显示 commands 错误，避免覆盖
            if skills_exist:
                self._show_message(
                    f"Commands directory not found: {self.manager.get_commands_source_dir()}", 
                    "warning"
                )
        
        # 清除选择计数
        footer = self.query_one(Footer)
        footer.update_selection_count(0)
    
    def _get_active_list(self) -> ItemListView:
        """获取当前活动的列表视图"""
        tabs = self.query_one("#tabs", TabbedContent)
        if tabs.active == "commands-tab":
            return self.query_one("#commands-list", ItemListView)
        return self.query_one("#skills-list", ItemListView)
    
    def _show_message(self, message: str, level: str = "info") -> None:
        """显示状态消息"""
        footer = self.query_one(Footer)
        footer.show_message(message, level)
    
    def _update_selection_count(self) -> None:
        """更新选中计数"""
        active_list = self._get_active_list()
        count = len(active_list.get_selected_items())
        footer = self.query_one(Footer)
        footer.update_selection_count(count)
    
    # === Action Methods ===
    
    def action_next_tab(self) -> None:
        """切换到下一个标签页"""
        tabs = self.query_one("#tabs", TabbedContent)
        if tabs.active == "skills-tab":
            tabs.active = "commands-tab"
            self.query_one("#commands-list", ItemListView).focus()
        else:
            tabs.active = "skills-tab"
            self.query_one("#skills-list", ItemListView).focus()
        self._update_selection_count()
    
    def action_install_focused(self) -> None:
        """安装当前聚焦的项目
        
        Requirements: 6.1, 6.2, 6.3, 6.4, 6.5, 6.6
        """
        active_list = self._get_active_list()
        focused = active_list.get_focused_item()
        
        if focused is None:
            self._show_message("No item focused", "warning")
            return
        
        item_name = focused.item_name
        is_skill = active_list.item_type == "skills"
        
        # 显示安装中状态
        self._show_message(f"Installing {item_name}...", "info")
        
        # 执行安装
        if is_skill:
            result = self.manager.install_skill(item_name)
        else:
            result = self.manager.install_command(item_name)
        
        if result.success:
            # 更新项目状态
            focused.update_install_status(InstallStatus.INSTALLED)
            self._show_message(result.message, "success")
        else:
            # 显示详细错误信息
            error_msg = result.message
            if result.error:
                error_msg = f"{result.message}: {result.error}"
            self._show_message(error_msg, "error")
    
    def action_install_selected(self) -> None:
        """安装所有选中的项目
        
        Requirements: 7.1, 7.2, 7.3, 7.4, 7.5, 7.6
        """
        active_list = self._get_active_list()
        selected = active_list.get_selected_items()
        
        if not selected:
            self._show_message("No items selected", "warning")
            return
        
        is_skill = active_list.item_type == "skills"
        total = len(selected)
        success_count = 0
        fail_count = 0
        failed_items: list[str] = []
        
        # 显示进度指示
        self._show_message(f"Installing 0/{total}...", "info")
        
        for i, item in enumerate(selected, 1):
            # 更新进度
            self._show_message(f"Installing {i}/{total}: {item.item_name}...", "info")
            
            if is_skill:
                result = self.manager.install_skill(item.item_name)
            else:
                result = self.manager.install_command(item.item_name)
            
            if result.success:
                success_count += 1
                item.update_install_status(InstallStatus.INSTALLED)
            else:
                fail_count += 1
                failed_items.append(item.item_name)
        
        # 清除选择状态
        active_list.deselect_all()
        self._update_selection_count()
        
        # 显示结果摘要
        if fail_count == 0:
            self._show_message(f"Installed {success_count} items", "success")
        else:
            # 显示失败的项目名称
            failed_str = ", ".join(failed_items[:3])
            if len(failed_items) > 3:
                failed_str += f" (+{len(failed_items) - 3} more)"
            self._show_message(
                f"Installed {success_count}, failed {fail_count}: {failed_str}", 
                "warning"
            )
    
    def action_install_all(self) -> None:
        """安装当前标签页的所有项目
        
        Requirements: 8.1, 8.2, 8.3, 8.4, 8.5
        """
        active_list = self._get_active_list()
        is_skill = active_list.item_type == "skills"
        
        # 检查源目录是否存在
        if is_skill and not self.manager.check_skills_source_exists():
            self._show_message(
                f"Skills directory not found: {self.manager.get_skills_source_dir()}", 
                "error"
            )
            return
        
        if not is_skill and not self.manager.check_commands_source_exists():
            self._show_message(
                f"Commands directory not found: {self.manager.get_commands_source_dir()}", 
                "error"
            )
            return
        
        # 获取总数用于进度显示
        items = self.manager.get_skills() if is_skill else self.manager.get_commands()
        total = len(items)
        
        if total == 0:
            self._show_message("No items to install", "warning")
            return
        
        # 显示进度指示
        self._show_message(f"Installing all {total} items...", "info")
        
        # 定义进度回调
        current = [0]  # 使用列表以便在闭包中修改
        def progress_callback(name: str, success: bool) -> None:
            current[0] += 1
            self._show_message(f"Installing {current[0]}/{total}: {name}...", "info")
        
        if is_skill:
            success, fail, failures = self.manager.install_all_skills(callback=progress_callback)
        else:
            success, fail, failures = self.manager.install_all_commands(callback=progress_callback)
        
        # 刷新列表以更新状态
        self._refresh_data()
        
        # 显示结果摘要
        if fail == 0:
            self._show_message(f"Installed all {success} items", "success")
        else:
            # 显示失败的项目名称
            failed_str = ", ".join(failures[:3])
            if len(failures) > 3:
                failed_str += f" (+{len(failures) - 3} more)"
            self._show_message(
                f"Installed {success}, failed {fail}: {failed_str}", 
                "warning"
            )
    
    def action_toggle_selection(self) -> None:
        """切换当前聚焦项目的选择状态"""
        active_list = self._get_active_list()
        active_list.toggle_focused_selection()
        self._update_selection_count()
    
    def action_select_all(self) -> None:
        """全选当前列表"""
        active_list = self._get_active_list()
        active_list.select_all()
        self._update_selection_count()
        self._show_message("Selected all items", "info")
    
    def action_deselect_all(self) -> None:
        """取消全选"""
        active_list = self._get_active_list()
        active_list.deselect_all()
        self._update_selection_count()
        self._show_message("Deselected all items", "info")
    
    def action_search(self) -> None:
        """显示搜索框
        
        Requirements: 11.1
        """
        search_container = self.query_one("#search-container")
        search_input = self.query_one("#search-input", Input)
        
        if self._search_visible:
            # 已经显示，直接聚焦
            search_input.focus()
        else:
            # 显示搜索框
            search_container.remove_class("-hidden")
            self._search_visible = True
            search_input.focus()
    
    def action_clear_search(self) -> None:
        """清除搜索
        
        Requirements: 11.3
        """
        if self._search_visible:
            search_container = self.query_one("#search-container")
            search_input = self.query_one("#search-input", Input)
            
            # 隐藏搜索框
            search_container.add_class("-hidden")
            self._search_visible = False
            search_input.value = ""
            
            # 清除过滤
            active_list = self._get_active_list()
            active_list.clear_filter()
            active_list.focus()
    
    def action_toggle_platform(self) -> None:
        """返回平台选择界面"""
        self.app.pop_screen()
    
    def action_quit(self) -> None:
        """退出应用"""
        self.app.exit()
    
    # === Event Handlers ===
    
    def on_input_changed(self, event: Input.Changed) -> None:
        """处理搜索输入变化 - 实时过滤列表
        
        Requirements: 11.2, 11.4
        """
        if event.input.id == "search-input":
            active_list = self._get_active_list()
            active_list.filter_items(event.value)
    
    def on_input_submitted(self, event: Input.Submitted) -> None:
        """处理搜索输入提交"""
        if event.input.id == "search-input":
            # 聚焦回列表
            active_list = self._get_active_list()
            active_list.focus()
    
    def on_item_list_view_selection_count_changed(
        self, 
        event: ItemListView.SelectionCountChanged
    ) -> None:
        """处理选中数量变化"""
        footer = self.query_one(Footer)
        footer.update_selection_count(event.count)
