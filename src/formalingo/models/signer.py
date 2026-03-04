from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .signer_status import Signer_status

@dataclass
class Signer(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The color property
    color: Optional[str] = None
    # The completedAt property
    completed_at: Optional[datetime.datetime] = None
    # The createdAt property
    created_at: Optional[datetime.datetime] = None
    # The documentId property
    document_id: Optional[UUID] = None
    # The email property
    email: Optional[str] = None
    # The id property
    id: Optional[UUID] = None
    # The label property
    label: Optional[str] = None
    # The link property
    link: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The order property
    order: Optional[float] = None
    # The role property
    role: Optional[str] = None
    # The status property
    status: Optional[Signer_status] = None
    # The submissionId property
    submission_id: Optional[UUID] = None
    # The token property
    token: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Signer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Signer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Signer()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .signer_status import Signer_status

        from .signer_status import Signer_status

        fields: dict[str, Callable[[Any], None]] = {
            "color": lambda n : setattr(self, 'color', n.get_str_value()),
            "completedAt": lambda n : setattr(self, 'completed_at', n.get_datetime_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "documentId": lambda n : setattr(self, 'document_id', n.get_uuid_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "link": lambda n : setattr(self, 'link', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "order": lambda n : setattr(self, 'order', n.get_float_value()),
            "role": lambda n : setattr(self, 'role', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(Signer_status)),
            "submissionId": lambda n : setattr(self, 'submission_id', n.get_uuid_value()),
            "token": lambda n : setattr(self, 'token', n.get_str_value()),
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
        writer.write_datetime_value("completedAt", self.completed_at)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_uuid_value("documentId", self.document_id)
        writer.write_str_value("email", self.email)
        writer.write_uuid_value("id", self.id)
        writer.write_str_value("label", self.label)
        writer.write_str_value("link", self.link)
        writer.write_str_value("name", self.name)
        writer.write_float_value("order", self.order)
        writer.write_str_value("role", self.role)
        writer.write_enum_value("status", self.status)
        writer.write_uuid_value("submissionId", self.submission_id)
        writer.write_str_value("token", self.token)
        writer.write_additional_data_value(self.additional_data)
    

