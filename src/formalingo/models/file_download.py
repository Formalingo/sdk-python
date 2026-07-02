from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class FileDownload(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The contentType property
    content_type: Optional[str] = None
    # Temporary Supabase signed URL
    download_url: Optional[str] = None
    # The expiresIn property
    expires_in: Optional[int] = None
    # The fileId property
    file_id: Optional[UUID] = None
    # The name property
    name: Optional[str] = None
    # The sizeBytes property
    size_bytes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FileDownload:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FileDownload
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FileDownload()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "contentType": lambda n : setattr(self, 'content_type', n.get_str_value()),
            "downloadUrl": lambda n : setattr(self, 'download_url', n.get_str_value()),
            "expiresIn": lambda n : setattr(self, 'expires_in', n.get_int_value()),
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
        writer.write_str_value("contentType", self.content_type)
        writer.write_str_value("downloadUrl", self.download_url)
        writer.write_int_value("expiresIn", self.expires_in)
        writer.write_uuid_value("fileId", self.file_id)
        writer.write_str_value("name", self.name)
        writer.write_int_value("sizeBytes", self.size_bytes)
        writer.write_additional_data_value(self.additional_data)
    

