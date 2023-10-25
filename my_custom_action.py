# from great_expectations.validation_operators import ValidationAction
from great_expectations.checkpoint.actions import ValidationAction

from great_expectations.compatibility.typing_extensions import override
from great_expectations.core.expectation_validation_result import ExpectationSuiteValidationResult
from great_expectations.data_context.types.resource_identifiers import (
    GXCloudIdentifier,
    ValidationResultIdentifier
)
from typing import Union


class MyCustomAction(ValidationAction):
    def __init__(
        self,
        data_context,
    ) -> None:
        super().__init__(data_context)

    @override
    def _run(  # noqa: PLR0913
        self,
        validation_result_suite: ExpectationSuiteValidationResult,
        validation_result_suite_identifier: Union[
            ValidationResultIdentifier, GXCloudIdentifier
        ],
        data_asset,
        expectation_suite_identifier=None,
        checkpoint_identifier=None,
        **kwargs
    ) -> None:
        print("Happily doing nothing")
