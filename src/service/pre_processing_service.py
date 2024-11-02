from model.request import Request
from strategy.handler.auth_verification_handler import AuthVerificationhandler
from strategy.handler.source_validation_handler import SourceValidationHandler
from strategy.handler.file_extension_validation_handler import FileExtensionValidation
from injector import inject 

class PreProcessingService:

    @inject
    def __init__(self, authValidationHandler: AuthVerificationhandler, 
                 sourceValidationHandler: SourceValidationHandler, 
                 fileExtensionValidation: FileExtensionValidation):
        self.authValidationHandler = authValidationHandler
        self.sourceValidationHandler = sourceValidationHandler
        self.fileExtensionValidation = fileExtensionValidation

    def process(self, request: Request):
        """
        A service to start the chain
        """
        self.authValidationHandler.set_next(self.sourceValidationHandler).set_next(self.fileExtensionValidation)

        result = self.authValidationHandler.handle(request)
        print(result)
    
    