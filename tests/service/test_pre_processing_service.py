
from unittest import TestCase

from service.pre_processing_service import PreProcessingService
from model.request import Request
from unittest.mock import patch, Mock
from strategy.handler.auth_verification_handler import AuthVerificationhandler
from strategy.handler.source_validation_handler import SourceValidationHandler
from strategy.handler.file_extension_validation_handler import FileExtensionValidation

class TestPreProcessingService(TestCase):

    def test_given_buyerIsAllowed_thenReturn_StepSUccess(self):

        #Arrage
        request = Request("12345-1", ["path1", "path2"])
        result = request
        result.steps.append("Authorization Success")

        attrs = {'handle.return_value': result}
        authMock = Mock(spec_set=AuthVerificationhandler, **attrs)
        sourceMock = Mock(spec_set=SourceValidationHandler)
        fileExtensionMock = Mock(spec_set=FileExtensionValidation)

        service = PreProcessingService(sourceMock, fileExtensionMock, authMock)

        #Act
        r = service.process(request)
   
        #Assert
        assert(authMock.assert_any_call)
        assert(len(r.steps) > 0)

