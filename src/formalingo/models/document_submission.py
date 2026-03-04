from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .document_submission_status import DocumentSubmission_status
    from .signer import Signer

@dataclass
class DocumentSubmission(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The completedAt property
    completed_at: Optional[datetime.datetime] = None
    # The completedPdfUrl property
    completed_pdf_url: Optional[str] = None
    # The createdAt property
    created_at: Optional[datetime.datetime] = None
    # The documentId property
    document_id: Optional[UUID] = None
    # The id property
    id: Optional[UUID] = None
    # The signers property
    signers: Optional[list[Signer]] = None
    # The status property
    status: Optional[DocumentSubmission_status] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DocumentSubmission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DocumentSubmission
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DocumentSubmission()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .document_submission_status import DocumentSubmission_status
        from .signer import Signer

        from .document_submission_status import DocumentSubmission_status
        from .signer import Signer

        fields: dict[str, Callable[[Any], None]] = {
            "completedAt": lambda n : setattr(self, 'completed_at', n.get_datetime_value()),
            "completedPdfUrl": lambda n : setattr(self, 'completed_pdf_url', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "documentId": lambda n : setattr(self, 'document_id', n.get_uuid_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "signers": lambda n : setattr(self, 'signers', n.get_collection_of_object_values(Signer)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(DocumentSubmission_status)),
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
        writer.write_datetime_value("completedAt", self.completed_at)
        writer.write_str_value("completedPdfUrl", self.completed_pdf_url)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_uuid_value("documentId", self.document_id)
        writer.write_uuid_value("id", self.id)
        writer.write_collection_of_object_values("signers", self.signers)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

