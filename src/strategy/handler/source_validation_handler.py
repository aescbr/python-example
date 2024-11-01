from model.request import Request
from strategy.handler.parent_handler import ParentHandler

class SourceValidationHandler(ParentHandler):
    def handle(self, request: Request):
        print(f"processing: {self.__class__.__name__}" )
        """
        source validation here
        """
        
        request.steps.append(f"{self.__class__.__name__} success")
        return super().handle(request)