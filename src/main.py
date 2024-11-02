from __future__ import annotations
from service.pre_processing_service import PreProcessingService
from model.request import Request
from strategy.handler.auth_verification_handler import AuthVerificationhandler
from strategy.handler.source_validation_handler import SourceValidationHandler
from strategy.handler.file_extension_validation_handler import FileExtensionValidation


def main() -> int:
    authVerificationHandler = AuthVerificationhandler()
    sourceValidationHandler = SourceValidationHandler()
    fileExtensionValidation = FileExtensionValidation()

    service = PreProcessingService(authVerificationHandler, sourceValidationHandler, fileExtensionValidation);

    request = Request("request1", ["path1", "path2"])
    service.process(request)
    return 0


if __name__ == "__main__":
   main()
