from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SignerInput_prefill(AdditionalDataHolder, Parsable):
    """
    Map of field identifier → pre-filled value. Keys can be field UUIDs or field labels. Label-based keys are resolved against fields assigned to this signer's role. If a label matches multiple fields for the same role, the request is rejected with disambiguation details. Creates DocumentResponse records immediately.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SignerInput_prefill:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SignerInput_prefill
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SignerInput_prefill()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
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
        writer.write_additional_data_value(self.additional_data)
    

