from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .document_submission_signed_pdf_authorization import DocumentSubmission_signedPdf_authorization
    from .document_submission_signed_pdf_download_method import DocumentSubmission_signedPdf_downloadMethod

@dataclass
class DocumentSubmission_signedPdf(AdditionalDataHolder, Parsable):
    """
    Stable API-key-gated file descriptor for the completed signed PDF.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The authorization property
    authorization: Optional[DocumentSubmission_signedPdf_authorization] = None
    # The contentType property
    content_type: Optional[str] = None
    # The downloadMethod property
    download_method: Optional[DocumentSubmission_signedPdf_downloadMethod] = None
    # Formalingo API endpoint that requires Authorization: Bearer <api-key>
    download_url: Optional[str] = None
    # The fileId property
    file_id: Optional[UUID] = None
    # The name property
    name: Optional[str] = None
    # The sizeBytes property
    size_bytes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DocumentSubmission_signedPdf:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DocumentSubmission_signedPdf
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DocumentSubmission_signedPdf()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .document_submission_signed_pdf_authorization import DocumentSubmission_signedPdf_authorization
        from .document_submission_signed_pdf_download_method import DocumentSubmission_signedPdf_downloadMethod

        from .document_submission_signed_pdf_authorization import DocumentSubmission_signedPdf_authorization
        from .document_submission_signed_pdf_download_method import DocumentSubmission_signedPdf_downloadMethod

        fields: dict[str, Callable[[Any], None]] = {
            "authorization": lambda n : setattr(self, 'authorization', n.get_enum_value(DocumentSubmission_signedPdf_authorization)),
            "contentType": lambda n : setattr(self, 'content_type', n.get_str_value()),
            "downloadMethod": lambda n : setattr(self, 'download_method', n.get_enum_value(DocumentSubmission_signedPdf_downloadMethod)),
            "downloadUrl": lambda n : setattr(self, 'download_url', n.get_str_value()),
            "fileId": lambda n : setattr(self, 'file_id', n.get_uuid_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "sizeBytes": lambda n : setattr(self, 'size_bytes', n.get_int_value()),
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
        writer.write_enum_value("authorization", self.authorization)
        writer.write_str_value("contentType", self.content_type)
        writer.write_enum_value("downloadMethod", self.download_method)
        writer.write_str_value("downloadUrl", self.download_url)
        writer.write_uuid_value("fileId", self.file_id)
        writer.write_str_value("name", self.name)
        writer.write_int_value("sizeBytes", self.size_bytes)
        writer.write_additional_data_value(self.additional_data)
    

