from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .bulk_post_request_body_recipients_prefill import BulkPostRequestBody_recipients_prefill

@dataclass
class BulkPostRequestBody_recipients(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The email property
    email: Optional[str] = None
    # The expires_at property
    expires_at: Optional[datetime.datetime] = None
    # The label property
    label: Optional[str] = None
    # The password property
    password: Optional[str] = None
    # The phone property
    phone: Optional[str] = None
    # The prefill property
    prefill: Optional[BulkPostRequestBody_recipients_prefill] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BulkPostRequestBody_recipients:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BulkPostRequestBody_recipients
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BulkPostRequestBody_recipients()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .bulk_post_request_body_recipients_prefill import BulkPostRequestBody_recipients_prefill

        from .bulk_post_request_body_recipients_prefill import BulkPostRequestBody_recipients_prefill

        fields: dict[str, Callable[[Any], None]] = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "expires_at": lambda n : setattr(self, 'expires_at', n.get_datetime_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "prefill": lambda n : setattr(self, 'prefill', n.get_object_value(BulkPostRequestBody_recipients_prefill)),
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
        writer.write_additional_data_value(self.additional_data)
    

