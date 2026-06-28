from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .document_parse_job_result import DocumentParseJobResult
    from .get_document_parse_job_response_data_apply_mode import GetDocumentParseJobResponse_data_applyMode
    from .get_document_parse_job_response_data_status import GetDocumentParseJobResponse_data_status

@dataclass
class GetDocumentParseJobResponse_data(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The applyMode property
    apply_mode: Optional[GetDocumentParseJobResponse_data_applyMode] = None
    # The documentId property
    document_id: Optional[UUID] = None
    # The error property
    error: Optional[str] = None
    # The parseJobId property
    parse_job_id: Optional[UUID] = None
    # The pollAfterMs property
    poll_after_ms: Optional[int] = None
    # The result property
    result: Optional[DocumentParseJobResult] = None
    # The status property
    status: Optional[GetDocumentParseJobResponse_data_status] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GetDocumentParseJobResponse_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GetDocumentParseJobResponse_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GetDocumentParseJobResponse_data()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .document_parse_job_result import DocumentParseJobResult
        from .get_document_parse_job_response_data_apply_mode import GetDocumentParseJobResponse_data_applyMode
        from .get_document_parse_job_response_data_status import GetDocumentParseJobResponse_data_status

        from .document_parse_job_result import DocumentParseJobResult
        from .get_document_parse_job_response_data_apply_mode import GetDocumentParseJobResponse_data_applyMode
        from .get_document_parse_job_response_data_status import GetDocumentParseJobResponse_data_status

        fields: dict[str, Callable[[Any], None]] = {
            "applyMode": lambda n : setattr(self, 'apply_mode', n.get_enum_value(GetDocumentParseJobResponse_data_applyMode)),
            "documentId": lambda n : setattr(self, 'document_id', n.get_uuid_value()),
            "error": lambda n : setattr(self, 'error', n.get_str_value()),
            "parseJobId": lambda n : setattr(self, 'parse_job_id', n.get_uuid_value()),
            "pollAfterMs": lambda n : setattr(self, 'poll_after_ms', n.get_int_value()),
            "result": lambda n : setattr(self, 'result', n.get_object_value(DocumentParseJobResult)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(GetDocumentParseJobResponse_data_status)),
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
        writer.write_enum_value("applyMode", self.apply_mode)
        writer.write_uuid_value("documentId", self.document_id)
        writer.write_str_value("error", self.error)
        writer.write_uuid_value("parseJobId", self.parse_job_id)
        writer.write_int_value("pollAfterMs", self.poll_after_ms)
        writer.write_object_value("result", self.result)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

