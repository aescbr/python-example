from __future__ import annotations
from service.pre_processing_service import PreProcessingService
from model.request import Request
from container.container import Container
from dependency_injector.wiring import Provide, inject

@inject
def main(service: PreProcessingService = Provide[Container.pre_processing_service]) -> int:
     
    request = Request("request1", ["path1", "path2"])
    service.process(request)
    return 0



if __name__ == "__main__":
    container = Container()
    container.init_resources()
    container.wire(modules=[__name__])
    main()
