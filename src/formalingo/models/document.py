from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .document_page_dimensions import Document_pageDimensions
    from .document_status import Document_status

@dataclass
class Document(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The completedPdfUrl property
    completed_pdf_url: Optional[str] = None
    # The createdAt property
    created_at: Optional[datetime.datetime] = None
    # The creatorId property
    creator_id: Optional[UUID] = None
    # The deletedAt property
    deleted_at: Optional[datetime.datetime] = None
    # The fileType property
    file_type: Optional[str] = None
    # The id property
    id: Optional[UUID] = None
    # The originalFilename property
    original_filename: Optional[str] = None
    # The originalUrl property
    original_url: Optional[str] = None
    # The pageCount property
    page_count: Optional[float] = None
    # The pageDimensions property
    page_dimensions: Optional[list[Document_pageDimensions]] = None
    # The status property
    status: Optional[Document_status] = None
    # The title property
    title: Optional[str] = None
    # The updatedAt property
    updated_at: Optional[datetime.datetime] = None
    # The workspaceId property
    workspace_id: Optional[UUID] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Document:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Document
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Document()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .document_page_dimensions import Document_pageDimensions
        from .document_status import Document_status

        from .document_page_dimensions import Document_pageDimensions
        from .document_status import Document_status

        fields: dict[str, Callable[[Any], None]] = {
            "completedPdfUrl": lambda n : setattr(self, 'completed_pdf_url', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "creatorId": lambda n : setattr(self, 'creator_id', n.get_uuid_value()),
            "deletedAt": lambda n : setattr(self, 'deleted_at', n.get_datetime_value()),
            "fileType": lambda n : setattr(self, 'file_type', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "originalFilename": lambda n : setattr(self, 'original_filename', n.get_str_value()),
            "originalUrl": lambda n : setattr(self, 'original_url', n.get_str_value()),
            "pageCount": lambda n : setattr(self, 'page_count', n.get_float_value()),
            "pageDimensions": lambda n : setattr(self, 'page_dimensions', n.get_collection_of_object_values(Document_pageDimensions)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(Document_status)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "updatedAt": lambda n : setattr(self, 'updated_at', n.get_datetime_value()),
            "workspaceId": lambda n : setattr(self, 'workspace_id', n.get_uuid_value()),
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
        writer.write_str_value("completedPdfUrl", self.completed_pdf_url)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_uuid_value("creatorId", self.creator_id)
        writer.write_datetime_value("deletedAt", self.deleted_at)
        writer.write_str_value("fileType", self.file_type)
        writer.write_uuid_value("id", self.id)
        writer.write_str_value("originalFilename", self.original_filename)
        writer.write_str_value("originalUrl", self.original_url)
        writer.write_float_value("pageCount", self.page_count)
        writer.write_collection_of_object_values("pageDimensions", self.page_dimensions)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("title", self.title)
        writer.write_datetime_value("updatedAt", self.updated_at)
        writer.write_uuid_value("workspaceId", self.workspace_id)
        writer.write_additional_data_value(self.additional_data)
    

