from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .form_branding import Form_branding
    from .form_settings import Form_settings
    from .form_status import Form_status

@dataclass
class Form(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The branding property
    branding: Optional[Form_branding] = None
    # The createdAt property
    created_at: Optional[datetime.datetime] = None
    # The creatorId property
    creator_id: Optional[UUID] = None
    # The description property
    description: Optional[str] = None
    # The id property
    id: Optional[UUID] = None
    # The publicToken property
    public_token: Optional[str] = None
    # The question_count property
    question_count: Optional[float] = None
    # The settings property
    settings: Optional[Form_settings] = None
    # The status property
    status: Optional[Form_status] = None
    # The title property
    title: Optional[str] = None
    # The updatedAt property
    updated_at: Optional[datetime.datetime] = None
    # The workspaceId property
    workspace_id: Optional[UUID] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Form:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Form
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Form()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .form_branding import Form_branding
        from .form_settings import Form_settings
        from .form_status import Form_status

        from .form_branding import Form_branding
        from .form_settings import Form_settings
        from .form_status import Form_status

        fields: dict[str, Callable[[Any], None]] = {
            "branding": lambda n : setattr(self, 'branding', n.get_object_value(Form_branding)),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "creatorId": lambda n : setattr(self, 'creator_id', n.get_uuid_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "publicToken": lambda n : setattr(self, 'public_token', n.get_str_value()),
            "question_count": lambda n : setattr(self, 'question_count', n.get_float_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(Form_settings)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(Form_status)),
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
        writer.write_object_value("branding", self.branding)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_uuid_value("creatorId", self.creator_id)
        writer.write_str_value("description", self.description)
        writer.write_uuid_value("id", self.id)
        writer.write_str_value("publicToken", self.public_token)
        writer.write_float_value("question_count", self.question_count)
        writer.write_object_value("settings", self.settings)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("title", self.title)
        writer.write_datetime_value("updatedAt", self.updated_at)
        writer.write_uuid_value("workspaceId", self.workspace_id)
        writer.write_additional_data_value(self.additional_data)
    

