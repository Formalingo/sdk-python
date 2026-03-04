from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .recipient_status import Recipient_status

@dataclass
class Recipient(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The created_at property
    created_at: Optional[datetime.datetime] = None
    # The email property
    email: Optional[str] = None
    # The expires_at property
    expires_at: Optional[datetime.datetime] = None
    # The form_id property
    form_id: Optional[UUID] = None
    # The has_password property
    has_password: Optional[bool] = None
    # The id property
    id: Optional[UUID] = None
    # The is_active property
    is_active: Optional[bool] = None
    # The is_anonymous property
    is_anonymous: Optional[bool] = None
    # The label property
    label: Optional[str] = None
    # The last_activity_at property
    last_activity_at: Optional[datetime.datetime] = None
    # The link property
    link: Optional[str] = None
    # The phone property
    phone: Optional[str] = None
    # The response_count property
    response_count: Optional[float] = None
    # The status property
    status: Optional[Recipient_status] = None
    # The token property
    token: Optional[str] = None
    # The total_questions property
    total_questions: Optional[float] = None
    # The visit_count property
    visit_count: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Recipient:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Recipient
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Recipient()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .recipient_status import Recipient_status

        from .recipient_status import Recipient_status

        fields: dict[str, Callable[[Any], None]] = {
            "created_at": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "expires_at": lambda n : setattr(self, 'expires_at', n.get_datetime_value()),
            "form_id": lambda n : setattr(self, 'form_id', n.get_uuid_value()),
            "has_password": lambda n : setattr(self, 'has_password', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "is_active": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "is_anonymous": lambda n : setattr(self, 'is_anonymous', n.get_bool_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "last_activity_at": lambda n : setattr(self, 'last_activity_at', n.get_datetime_value()),
            "link": lambda n : setattr(self, 'link', n.get_str_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "response_count": lambda n : setattr(self, 'response_count', n.get_float_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(Recipient_status)),
            "token": lambda n : setattr(self, 'token', n.get_str_value()),
            "total_questions": lambda n : setattr(self, 'total_questions', n.get_float_value()),
            "visit_count": lambda n : setattr(self, 'visit_count', n.get_float_value()),
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
        writer.write_datetime_value("created_at", self.created_at)
        writer.write_str_value("email", self.email)
        writer.write_datetime_value("expires_at", self.expires_at)
        writer.write_uuid_value("form_id", self.form_id)
        writer.write_bool_value("has_password", self.has_password)
        writer.write_uuid_value("id", self.id)
        writer.write_bool_value("is_active", self.is_active)
        writer.write_bool_value("is_anonymous", self.is_anonymous)
        writer.write_str_value("label", self.label)
        writer.write_datetime_value("last_activity_at", self.last_activity_at)
        writer.write_str_value("link", self.link)
        writer.write_str_value("phone", self.phone)
        writer.write_float_value("response_count", self.response_count)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("token", self.token)
        writer.write_float_value("total_questions", self.total_questions)
        writer.write_float_value("visit_count", self.visit_count)
        writer.write_additional_data_value(self.additional_data)
    

