from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class CreateSubmissionSignerResult(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The color property
    color: Optional[str] = None
    # The id property
    id: Optional[UUID] = None
    # The label property
    label: Optional[str] = None
    # Authorized live signing link. This bearer link is returned to the caller but is not stored in dispatch evidence.
    link: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The order property
    order: Optional[int] = None
    # The role property
    role: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateSubmissionSignerResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateSubmissionSignerResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateSubmissionSignerResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "color": lambda n : setattr(self, 'color', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "link": lambda n : setattr(self, 'link', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "order": lambda n : setattr(self, 'order', n.get_int_value()),
            "role": lambda n : setattr(self, 'role', n.get_str_value()),
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
        writer.write_str_value("color", self.color)
        writer.write_uuid_value("id", self.id)
        writer.write_str_value("label", self.label)
        writer.write_str_value("link", self.link)
        writer.write_str_value("name", self.name)
        writer.write_int_value("order", self.order)
        writer.write_str_value("role", self.role)
        writer.write_additional_data_value(self.additional_data)
    

