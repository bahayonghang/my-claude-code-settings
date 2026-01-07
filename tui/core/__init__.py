"""
TUI 核心业务逻辑模块

包含:
- models: 数据模型 (ItemType, InstallStatus, ItemInfo, InstallResult)
- manager: TUIManager 封装 SkillManager
"""

from .models import ItemType, InstallStatus, ItemInfo, InstallResult
from .manager import TUIManager

__all__ = ["ItemType", "InstallStatus", "ItemInfo", "InstallResult", "TUIManager"]
