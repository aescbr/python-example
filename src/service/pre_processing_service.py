from model.request import Request
from strategy.handler.auth_verification_handler import AuthVerificationhandler
from strategy.handler.source_validation_handler import SourceValidationHandler
from strategy.handler.file_extension_validation_handler import FileExtensionValidation

class PreProcessingService:

    def __init__(self, 
                 sourceValidationHandler: SourceValidationHandler, 
                 fileExtensionValidation: FileExtensionValidation, 
                 authVerificationhandler: AuthVerificationhandler):
        self.authVerificationhandler = authVerificationhandler
        self.sourceValidationHandler = sourceValidationHandler
        self.fileExtensionValidation = fileExtensionValidation

    def process(self, request: Request)-> Request:
        """
        A service to start the chain
        """

        self.authVerificationhandler.set_next(self.sourceValidationHandler).set_next(self.fileExtensionValidation)

        result = self.authVerificationhandler.handle(request)
        print(result)
        return result
    
    