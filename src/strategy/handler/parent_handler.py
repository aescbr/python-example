from model.request import Request
from strategy.handler.abstract_handler import AbstractHandler

class ParentHandler(AbstractHandler): 
    def handle(self, request: Request):
        return super().handle(request)