from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .apply_document_parse_job_response_meta import ApplyDocumentParseJobResponse_meta
    from .parse_job_applied_result import ParseJobAppliedResult

@dataclass
class ApplyDocumentParseJobResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The data property
    data: Optional[ParseJobAppliedResult] = None
    # The meta property
    meta: Optional[ApplyDocumentParseJobResponse_meta] = None
    # The success property
    success: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApplyDocumentParseJobResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApplyDocumentParseJobResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApplyDocumentParseJobResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .apply_document_parse_job_response_meta import ApplyDocumentParseJobResponse_meta
        from .parse_job_applied_result import ParseJobAppliedResult

        from .apply_document_parse_job_response_meta import ApplyDocumentParseJobResponse_meta
        from .parse_job_applied_result import ParseJobAppliedResult

        fields: dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_object_value(ParseJobAppliedResult)),
            "meta": lambda n : setattr(self, 'meta', n.get_object_value(ApplyDocumentParseJobResponse_meta)),
            "success": lambda n : setattr(self, 'success', n.get_bool_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("data", self.data)
        writer.write_object_value("meta", self.meta)
        writer.write_bool_value("success", self.success)
        writer.write_additional_data_value(self.additional_data)
    

