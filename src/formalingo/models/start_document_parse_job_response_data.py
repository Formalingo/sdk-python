from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .start_document_parse_job_response_data_status import StartDocumentParseJobResponse_data_status

@dataclass
class StartDocumentParseJobResponse_data(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The documentId property
    document_id: Optional[UUID] = None
    # The parseJobId property
    parse_job_id: Optional[UUID] = None
    # The pollAfterMs property
    poll_after_ms: Optional[int] = None
    # The status property
    status: Optional[StartDocumentParseJobResponse_data_status] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StartDocumentParseJobResponse_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StartDocumentParseJobResponse_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StartDocumentParseJobResponse_data()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .start_document_parse_job_response_data_status import StartDocumentParseJobResponse_data_status

        from .start_document_parse_job_response_data_status import StartDocumentParseJobResponse_data_status

        fields: dict[str, Callable[[Any], None]] = {
            "documentId": lambda n : setattr(self, 'document_id', n.get_uuid_value()),
            "parseJobId": lambda n : setattr(self, 'parse_job_id', n.get_uuid_value()),
            "pollAfterMs": lambda n : setattr(self, 'poll_after_ms', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(StartDocumentParseJobResponse_data_status)),
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
        writer.write_uuid_value("documentId", self.document_id)
        writer.write_uuid_value("parseJobId", self.parse_job_id)
        writer.write_int_value("pollAfterMs", self.poll_after_ms)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

