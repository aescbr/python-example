from strategy.pre_processing_handler import PreProcesingHandler
from typing import Any

class AbstractHandler(PreProcesingHandler): 
    """
    default chaining behaivor 
    """
    _next_handler: PreProcesingHandler = None

    def set_next(self, handler) -> PreProcesingHandler:
        self._next_handler = handler
        """
        to chain next step like firstHandler.set_next(secnondHandler).set_next(thirdHandler)
        """
        return handler

    def handle(self, request: Any) ->Any:
        if self._next_handler:
            return self._next_handler.handle(request)
        
        return request