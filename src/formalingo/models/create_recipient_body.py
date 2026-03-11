from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .create_recipient_body_prefill import CreateRecipientBody_prefill

@dataclass
class CreateRecipientBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The email property
    email: Optional[str] = None
    # ISO 8601 expiry date
    expires_at: Optional[datetime.datetime] = None
    # The label property
    label: Optional[str] = None
    # Optional password to protect the form link
    password: Optional[str] = None
    # The phone property
    phone: Optional[str] = None
    # Map of question ID → pre-filled value. The value is saved as a Response.
    prefill: Optional[CreateRecipientBody_prefill] = None
    # If true, suppresses recipient_invite notification for this recipient.
    suppress_notifications: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateRecipientBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateRecipientBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateRecipientBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .create_recipient_body_prefill import CreateRecipientBody_prefill

        from .create_recipient_body_prefill import CreateRecipientBody_prefill

        fields: dict[str, Callable[[Any], None]] = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "expires_at": lambda n : setattr(self, 'expires_at', n.get_datetime_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "prefill": lambda n : setattr(self, 'prefill', n.get_object_value(CreateRecipientBody_prefill)),
            "suppress_notifications": lambda n : setattr(self, 'suppress_notifications', n.get_bool_value()),
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
        writer.write_str_value("email", self.email)
        writer.write_datetime_value("expires_at", self.expires_at)
        writer.write_str_value("label", self.label)
        writer.write_str_value("password", self.password)
        writer.write_str_value("phone", self.phone)
        writer.write_object_value("prefill", self.prefill)
        writer.write_bool_value("suppress_notifications", self.suppress_notifications)
        writer.write_additional_data_value(self.additional_data)
    

