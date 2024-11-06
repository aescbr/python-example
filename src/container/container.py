from dependency_injector import containers, providers

from strategy.handler.auth_verification_handler import AuthVerificationhandler
from strategy.handler.file_extension_validation_handler import FileExtensionValidation
from strategy.handler.source_validation_handler import SourceValidationHandler
from service.pre_processing_service import PreProcessingService

class Container(containers.DeclarativeContainer):
    
    #services
    pre_processing_service = providers.Factory(
        PreProcessingService,
        sourceValidationHandler = SourceValidationHandler(),
        fileExtensionValidation = FileExtensionValidation(),
        authVerificationhandler = AuthVerificationhandler()
    )
