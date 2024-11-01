from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

class PreProcesingHandler(ABC):
    """
    handler interface
    """
    @abstractmethod
    def set_next(self, handler: PreProcesingHandler) -> PreProcesingHandler:
        pass

    @abstractmethod
    def handle(slef, request) -> Optional[Any]:
        pass