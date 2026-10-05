from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .expire_post_response_data_outcome import ExpirePostResponse_data_outcome

@dataclass
class ExpirePostResponse_data(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The expiredAt property
    expired_at: Optional[datetime.datetime] = None
    # The linksExpired property
    links_expired: Optional[int] = None
    # The outcome property
    outcome: Optional[ExpirePostResponse_data_outcome] = None
    # The retained property
    retained: Optional[bool] = None
    # The submissionId property
    submission_id: Optional[UUID] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExpirePostResponse_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExpirePostResponse_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExpirePostResponse_data()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .expire_post_response_data_outcome import ExpirePostResponse_data_outcome

        from .expire_post_response_data_outcome import ExpirePostResponse_data_outcome

        fields: dict[str, Callable[[Any], None]] = {
            "expiredAt": lambda n : setattr(self, 'expired_at', n.get_datetime_value()),
            "linksExpired": lambda n : setattr(self, 'links_expired', n.get_int_value()),
            "outcome": lambda n : setattr(self, 'outcome', n.get_enum_value(ExpirePostResponse_data_outcome)),
            "retained": lambda n : setattr(self, 'retained', n.get_bool_value()),
            "submissionId": lambda n : setattr(self, 'submission_id', n.get_uuid_value()),
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
        writer.write_datetime_value("expiredAt", self.expired_at)
        writer.write_int_value("linksExpired", self.links_expired)
        writer.write_enum_value("outcome", self.outcome)
        writer.write_bool_value("retained", self.retained)
        writer.write_uuid_value("submissionId", self.submission_id)
        writer.write_additional_data_value(self.additional_data)
    

