from __future__ import annotations
from service.pre_processing_service import PreProcessingService
from model.request import Request



def main() -> int:
    service = PreProcessingService();

    request = Request("request1", ["path1", "path2"])
    service.process(request)
    return 0


if __name__ == "__main__":
   main()
