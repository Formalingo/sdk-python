from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .status_get_response_data_profiles import StatusGetResponse_data_profiles

@dataclass
class StatusGetResponse_data(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The active property
    active: Optional[int] = None
    # The profiles property
    profiles: Optional[list[StatusGetResponse_data_profiles]] = None
    # The total property
    total: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StatusGetResponse_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StatusGetResponse_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StatusGetResponse_data()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .status_get_response_data_profiles import StatusGetResponse_data_profiles

        from .status_get_response_data_profiles import StatusGetResponse_data_profiles

        fields: dict[str, Callable[[Any], None]] = {
            "active": lambda n : setattr(self, 'active', n.get_int_value()),
            "profiles": lambda n : setattr(self, 'profiles', n.get_collection_of_object_values(StatusGetResponse_data_profiles)),
            "total": lambda n : setattr(self, 'total', n.get_int_value()),
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
        writer.write_int_value("active", self.active)
        writer.write_collection_of_object_values("profiles", self.profiles)
        writer.write_int_value("total", self.total)
        writer.write_additional_data_value(self.additional_data)
    

