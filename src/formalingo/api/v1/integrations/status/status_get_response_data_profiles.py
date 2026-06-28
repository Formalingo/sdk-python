from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class StatusGetResponse_data_profiles(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The active property
    active: Optional[bool] = None
    # The createdAt property
    created_at: Optional[datetime.datetime] = None
    # The id property
    id: Optional[UUID] = None
    # The label property
    label: Optional[str] = None
    # The typeSlug property
    type_slug: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StatusGetResponse_data_profiles:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StatusGetResponse_data_profiles
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StatusGetResponse_data_profiles()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_bool_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "typeSlug": lambda n : setattr(self, 'type_slug', n.get_str_value()),
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
        writer.write_bool_value("active", self.active)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_uuid_value("id", self.id)
        writer.write_str_value("label", self.label)
        writer.write_str_value("typeSlug", self.type_slug)
        writer.write_additional_data_value(self.additional_data)
    

