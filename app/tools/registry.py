from typing import Any, Type

from .base import BaseTool

class ToolRegistry:

    def __init__(self) -> None:

        self._tools: dict[str, Type[BaseTool]] = {}

        def register(
                self,
                
        )