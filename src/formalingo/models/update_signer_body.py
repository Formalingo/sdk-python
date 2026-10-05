from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class UpdateSignerBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Set true to clear the stored phone. Omit to leave it unchanged; cannot be combined with a non-null phone.
    clear_phone: Optional[bool] = None
    # The color property
    color: Optional[str] = None
    # The email property
    email: Optional[str] = None
    # ISO 8601 expiry; null clears it.
    expires_at: Optional[datetime.datetime] = None
    # The label property
    label: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The order property
    order: Optional[int] = None
    # Write-only password; null removes it and it is never returned.
    password: Optional[str] = None
    # Accepted formatted phone input. International input may include spaces, parentheses, and hyphens, but must include `+`. National input uses the workspace default phone country.
    phone: Optional[str] = None
    # The role property
    role: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UpdateSignerBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdateSignerBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UpdateSignerBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "clearPhone": lambda n : setattr(self, 'clear_phone', n.get_bool_value()),
            "color": lambda n : setattr(self, 'color', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "expiresAt": lambda n : setattr(self, 'expires_at', n.get_datetime_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "order": lambda n : setattr(self, 'order', n.get_int_value()),
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
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
        writer.write_bool_value("clearPhone", self.clear_phone)
        writer.write_str_value("color", self.color)
        writer.write_str_value("email", self.email)
        writer.write_datetime_value("expiresAt", self.expires_at)
        writer.write_str_value("label", self.label)
        writer.write_str_value("name", self.name)
        writer.write_int_value("order", self.order)
        writer.write_str_value("password", self.password)
        writer.write_str_value("phone", self.phone)
        writer.write_str_value("role", self.role)
        writer.write_additional_data_value(self.additional_data)
    

