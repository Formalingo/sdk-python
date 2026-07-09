from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .import_document_bundle_response_data_generation_type import ImportDocumentBundleResponse_data_generationType
    from .import_document_bundle_response_data_status import ImportDocumentBundleResponse_data_status

@dataclass
class ImportDocumentBundleResponse_data(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The generationType property
    generation_type: Optional[ImportDocumentBundleResponse_data_generationType] = None
    # The id property
    id: Optional[UUID] = None
    # The originalFilename property
    original_filename: Optional[str] = None
    # The originalUrl property
    original_url: Optional[str] = None
    # The status property
    status: Optional[ImportDocumentBundleResponse_data_status] = None
    # The title property
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ImportDocumentBundleResponse_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ImportDocumentBundleResponse_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ImportDocumentBundleResponse_data()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .import_document_bundle_response_data_generation_type import ImportDocumentBundleResponse_data_generationType
        from .import_document_bundle_response_data_status import ImportDocumentBundleResponse_data_status

        from .import_document_bundle_response_data_generation_type import ImportDocumentBundleResponse_data_generationType
        from .import_document_bundle_response_data_status import ImportDocumentBundleResponse_data_status

        fields: dict[str, Callable[[Any], None]] = {
            "generationType": lambda n : setattr(self, 'generation_type', n.get_enum_value(ImportDocumentBundleResponse_data_generationType)),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "originalFilename": lambda n : setattr(self, 'original_filename', n.get_str_value()),
            "originalUrl": lambda n : setattr(self, 'original_url', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ImportDocumentBundleResponse_data_status)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_enum_value("generationType", self.generation_type)
        writer.write_uuid_value("id", self.id)
        writer.write_str_value("originalFilename", self.original_filename)
        writer.write_str_value("originalUrl", self.original_url)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

