from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .bulk_post_request_body_recipients import BulkPostRequestBody_recipients

@dataclass
class BulkPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The confirmBulk property
    confirm_bulk: Optional[bool] = None
    # The recipients property
    recipients: Optional[list[BulkPostRequestBody_recipients]] = None
    # The sendNotifications property
    send_notifications: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BulkPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BulkPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BulkPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .bulk_post_request_body_recipients import BulkPostRequestBody_recipients

        from .bulk_post_request_body_recipients import BulkPostRequestBody_recipients

        fields: dict[str, Callable[[Any], None]] = {
            "confirmBulk": lambda n : setattr(self, 'confirm_bulk', n.get_bool_value()),
            "recipients": lambda n : setattr(self, 'recipients', n.get_collection_of_object_values(BulkPostRequestBody_recipients)),
            "sendNotifications": lambda n : setattr(self, 'send_notifications', n.get_bool_value()),
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
        writer.write_bool_value("confirmBulk", self.confirm_bulk)
        writer.write_collection_of_object_values("recipients", self.recipients)
        writer.write_bool_value("sendNotifications", self.send_notifications)
        writer.write_additional_data_value(self.additional_data)
    

