from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class WithFPutRequestBody_options(AdditionalDataHolder, Parsable):
    """
    Type-specific options, including additional options supported by the field type. For calculation fields, use formula and result_type (text or number).
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Set true for a supporting upload request excluded from the document and signed PDF. Only file_upload supports this flag; false and changing the field purpose after creation are rejected.
    supporting_attachment: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WithFPutRequestBody_options:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WithFPutRequestBody_options
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WithFPutRequestBody_options()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "supporting_attachment": lambda n : setattr(self, 'supporting_attachment', n.get_bool_value()),
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
        writer.write_bool_value("supporting_attachment", self.supporting_attachment)
        writer.write_additional_data_value(self.additional_data)
    

