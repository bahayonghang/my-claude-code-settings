"""列表组件 - SelectableItem 和 ItemListView

提供可选择的列表项和通用列表视图组件。
Requirements: 3.1, 3.3-3.9, 4.1-4.8, 9.1, 9.2, 11.2
"""

from typing import Optional
from textual.widgets import Static, ListView, ListItem
from textual.containers import Horizontal, Center
from textual.message import Message

from ..core.models import ItemInfo, InstallStatus
from ..core.formatters import format_checkbox, format_status_icon, format_empty_state_message


class SelectableItem(ListItem):
    """可选择的列表项组件
    
    显示复选框、状态图标、名称和描述。
    支持选择状态切换。
    使用 Unicode 符号美化显示：
    - 复选框: ☐ (未选中) / ☑ (选中)
    - 状态图标: ✓ (已安装/绿色) / ○ (未安装/灰色)
    
    Requirements: 4.1, 4.2, 4.3, 4.4, 4.5, 4.6
    """
    
    DEFAULT_CSS = """
    SelectableItem {
        height: 5;
        padding: 1 2;
        margin: 0 0 1 0;
        background: $panel;
    }

    SelectableItem:hover {
        background: $surface;
        border-left: thick $secondary;
    }

    SelectableItem.-selected {
        background: $primary 30%;
        border-left: thick $accent;
    }

    SelectableItem:focus {
        background: $primary;
        border: wide $accent;
    }

    SelectableItem.-selected:focus {
        background: $accent;
        border: wide $primary;
    }

    /* 聚焦时左侧边框指示器 */
    SelectableItem:focus-within {
        border-left: thick $accent;
    }

    SelectableItem #item-row {
        width: 100%;
        height: 100%;
    }

    SelectableItem #checkbox {
        width: 6;
        content-align: center middle;
        color: $primary;
        text-style: bold;
    }

    SelectableItem.-selected #checkbox {
        color: $accent;
    }

    SelectableItem:focus #checkbox {
        color: $accent;
        text-style: bold;
    }

    SelectableItem.-selected:focus #checkbox {
        color: $background;
        text-style: bold;
    }

    SelectableItem #status {
        width: 5;
        content-align: center middle;
    }

    SelectableItem .status-installed {
        color: $success;
    }

    SelectableItem .status-not-installed {
        color: $text-muted;
    }

    SelectableItem #name {
        width: 30%;
        text-style: bold;
        content-align: left middle;
        padding: 0 2;
    }

    SelectableItem.-selected #name {
        color: $foreground;
        text-style: bold;
    }

    SelectableItem:focus #name {
        color: $foreground;
        text-style: bold;
    }

    SelectableItem.-selected:focus #name {
        color: $background;
        text-style: bold;
    }

    SelectableItem #desc {
        width: 1fr;
        color: $text-muted;
        content-align: left middle;
        padding: 0 2;
    }

    SelectableItem.-selected #desc {
        color: $foreground;
    }

    SelectableItem:focus #desc {
        color: $foreground;
    }

    SelectableItem.-selected:focus #desc {
        color: $background;
    }
    """
    
    class SelectionChanged(Message):
        """选择状态变更消息"""
        def __init__(self, item: "SelectableItem", selected: bool) -> None:
            super().__init__()
            self.item = item
            self.selected = selected
    
    def __init__(
        self,
        item_info: ItemInfo,
        selected: bool = False,
    ) -> None:
        """初始化 SelectableItem
        
        Args:
            item_info: 项目信息
            selected: 初始选择状态
        """
        super().__init__()
        self.item_info = item_info
        self._selected = selected
    
    @property
    def item_name(self) -> str:
        """获取项目名称"""
        return self.item_info.name
    
    @property
    def description(self) -> Optional[str]:
        """获取项目描述"""
        return self.item_info.description
    
    @property
    def installed(self) -> bool:
        """检查是否已安装"""
        return self.item_info.is_installed
    
    @property
    def selected(self) -> bool:
        """获取选择状态"""
        return self._selected
    
    @selected.setter
    def selected(self, value: bool) -> None:
        """设置选择状态"""
        if self._selected != value:
            self._selected = value
            self._update_display()
            self.post_message(self.SelectionChanged(self, value))
    
    def compose(self):
        """构建组件结构"""
        with Horizontal(id="item-row"):
            yield Static(self._format_checkbox(), id="checkbox")
            yield Static(self._format_status(), id="status", classes=self._get_status_class())
            yield Static(self.item_name, id="name")
            yield Static(self.description or "", id="desc")
    
    def _format_checkbox(self) -> str:
        """格式化复选框显示
        
        使用 Unicode 符号: ☐ (未选中) / ☑ (选中)
        Requirements: 4.1
        """
        return format_checkbox(self._selected)
    
    def _format_status(self) -> str:
        """格式化状态图标
        
        使用 Unicode 符号: ✓ (已安装) / ○ (未安装)
        Requirements: 4.2
        """
        return format_status_icon(self.installed)
    
    def _get_status_class(self) -> str:
        """获取状态对应的 CSS 类名"""
        return "status-installed" if self.installed else "status-not-installed"
    
    def _update_display(self) -> None:
        """更新显示状态"""
        try:
            checkbox = self.query_one("#checkbox", Static)
            checkbox.update(self._format_checkbox())
            if self._selected:
                self.add_class("-selected")
            else:
                self.remove_class("-selected")
        except Exception:
            pass  # 组件可能尚未挂载
    
    def toggle_selection(self) -> None:
        """切换选择状态"""
        self.selected = not self._selected
    
    def update_install_status(self, status: InstallStatus) -> None:
        """更新安装状态
        
        Args:
            status: 新的安装状态
        """
        self.item_info.status = status
        try:
            status_widget = self.query_one("#status", Static)
            status_widget.update(self._format_status())
            status_widget.remove_class("status-installed")
            status_widget.remove_class("status-not-installed")
            status_widget.add_class(self._get_status_class())
        except Exception:
            pass  # 组件可能尚未挂载



class ItemListView(ListView):
    """通用列表视图组件
    
    用于显示 Skills 或 Commands 列表，支持选择、过滤等操作。
    当列表为空时显示居中的空状态消息。
    
    Requirements: 3.1, 3.6, 3.7, 9.1, 9.2, 11.2
    """
    
    DEFAULT_CSS = """
    ItemListView {
        height: 1fr;
        border: round $primary;
        padding: 0 1;
    }
    
    ItemListView:focus {
        border: round $accent;
    }
    
    ItemListView .empty-state {
        width: 100%;
        height: 100%;
        align: center middle;
    }
    
    ItemListView .empty-state-message {
        text-align: center;
        color: $text-muted;
        padding: 4;
    }
    """
    
    class SelectionCountChanged(Message):
        """选中数量变更消息"""
        def __init__(self, count: int) -> None:
            super().__init__()
            self.count = count
    
    def __init__(self, item_type: str = "skills", id: str | None = None) -> None:
        """初始化 ItemListView
        
        Args:
            item_type: 项目类型 ("skills" 或 "commands")
            id: 组件 ID
        """
        super().__init__(id=id)
        self.item_type = item_type
        self._all_items: list[SelectableItem] = []
        self._filter_text: str = ""
        self._empty_state_widget: Optional[Static] = None
    
    @property
    def items(self) -> list[SelectableItem]:
        """获取所有项目列表"""
        return self._all_items
    
    def compose(self):
        """构建组件结构，包含空状态占位"""
        # 空状态消息会在需要时动态添加
        yield from super().compose()
    
    def load_items(self, item_infos: list[ItemInfo]) -> None:
        """从 ItemInfo 列表加载项目
        
        Args:
            item_infos: 项目信息列表
        """
        self.clear()
        self._all_items = []
        self._remove_empty_state()
        
        if not item_infos:
            self._show_empty_state()
            return
        
        for info in item_infos:
            item = SelectableItem(item_info=info)
            self._all_items.append(item)
            self.append(item)
    
    def _show_empty_state(self) -> None:
        """显示空状态消息
        
        Requirements: 9.1 - 空列表应显示居中消息和图标
        """
        if self._empty_state_widget is None:
            message = format_empty_state_message(self.item_type)
            self._empty_state_widget = Static(
                message,
                classes="empty-state-message"
            )
            # 使用 ListItem 包装以便在 ListView 中显示
            empty_item = ListItem(Center(self._empty_state_widget, classes="empty-state"))
            empty_item.can_focus = False  # 空状态不可聚焦
            self.append(empty_item)
    
    def _remove_empty_state(self) -> None:
        """移除空状态消息"""
        if self._empty_state_widget is not None:
            try:
                # 清除列表会移除空状态
                self._empty_state_widget = None
            except Exception:
                pass
    
    def get_selected_items(self) -> list[SelectableItem]:
        """获取所有选中的项目
        
        Returns:
            选中的 SelectableItem 列表
        """
        return [item for item in self._all_items if item.selected]
    
    def get_selected_names(self) -> list[str]:
        """获取所有选中项目的名称
        
        Returns:
            选中项目名称列表
        """
        return [item.item_name for item in self._all_items if item.selected]
    
    def select_all(self) -> None:
        """全选所有可见项目"""
        for item in self._get_visible_items():
            item.selected = True
        self._notify_selection_changed()
    
    def deselect_all(self) -> None:
        """取消全选"""
        for item in self._all_items:
            item.selected = False
        self._notify_selection_changed()
    
    def filter_items(self, text: str) -> None:
        """过滤列表项目
        
        根据名称进行大小写不敏感的过滤。
        
        Args:
            text: 过滤文本
        """
        self._filter_text = text.lower()
        self._apply_filter()
    
    def clear_filter(self) -> None:
        """清除过滤"""
        self._filter_text = ""
        self._apply_filter()
    
    def _apply_filter(self) -> None:
        """应用过滤条件
        
        如果过滤后没有匹配项，显示空状态消息。
        Requirements: 9.1
        """
        self.clear()
        self._remove_empty_state()
        
        visible_items = [item for item in self._all_items if self._matches_filter(item)]
        
        if not visible_items:
            # 显示过滤后的空状态
            self._show_empty_state()
            return
        
        for item in visible_items:
            self.append(item)
    
    def _matches_filter(self, item: SelectableItem) -> bool:
        """检查项目是否匹配过滤条件
        
        Args:
            item: 要检查的项目
            
        Returns:
            是否匹配
        """
        if not self._filter_text:
            return True
        return self._filter_text in item.item_name.lower()
    
    def _get_visible_items(self) -> list[SelectableItem]:
        """获取当前可见的项目列表"""
        if not self._filter_text:
            return self._all_items
        return [item for item in self._all_items if self._matches_filter(item)]
    
    def _notify_selection_changed(self) -> None:
        """通知选中数量变更"""
        count = len(self.get_selected_items())
        self.post_message(self.SelectionCountChanged(count))
    
    def on_selectable_item_selection_changed(self, event: SelectableItem.SelectionChanged) -> None:
        """处理项目选择状态变更"""
        self._notify_selection_changed()
    
    def get_focused_item(self) -> Optional[SelectableItem]:
        """获取当前聚焦的项目
        
        Returns:
            当前聚焦的 SelectableItem，如果没有则返回 None
        """
        if self.highlighted_child is not None:
            child = self.highlighted_child
            if isinstance(child, SelectableItem):
                return child
        return None
    
    def toggle_focused_selection(self) -> None:
        """切换当前聚焦项目的选择状态"""
        focused = self.get_focused_item()
        if focused:
            focused.toggle_selection()
