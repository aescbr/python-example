from model.request import Request
from strategy.handler.auth_verification_handler import AuthVerificationhandler
from strategy.handler.source_validation_handler import SourceValidationHandler
from strategy.handler.file_extension_validation_handler import FileExtensionValidation

class PreProcessingService():

    def process(self, request: Request):
        """
        A service to start the chain
        """
        authHandler = AuthVerificationhandler();
        sourceValidation = SourceValidationHandler();
        fileExtensionValidation = FileExtensionValidation();

        authHandler.set_next(sourceValidation).set_next(fileExtensionValidation)

        result = authHandler.handle(request)
        print(result)
    
    