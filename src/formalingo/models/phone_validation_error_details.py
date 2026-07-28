from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .phone_validation_error_details_code import PhoneValidationError_details_code

@dataclass
class PhoneValidationError_details(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Stable phone-normalization failure code.
    code: Optional[PhoneValidationError_details_code] = None
    # The invalid phone field. Indexed signer paths identify the failing signer.
    field: Optional[str] = None
    # Zero-based signer index when a submission signer phone is invalid.
    index: Optional[int] = None
    # One-based CSV import row when an imported phone is invalid.
    row: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneValidationError_details:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneValidationError_details
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneValidationError_details()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .phone_validation_error_details_code import PhoneValidationError_details_code

        from .phone_validation_error_details_code import PhoneValidationError_details_code

        fields: dict[str, Callable[[Any], None]] = {
            "code": lambda n : setattr(self, 'code', n.get_enum_value(PhoneValidationError_details_code)),
            "field": lambda n : setattr(self, 'field', n.get_str_value()),
            "index": lambda n : setattr(self, 'index', n.get_int_value()),
            "row": lambda n : setattr(self, 'row', n.get_int_value()),
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
        writer.write_enum_value("code", self.code)
        writer.write_str_value("field", self.field)
        writer.write_int_value("index", self.index)
        writer.write_int_value("row", self.row)
        writer.write_additional_data_value(self.additional_data)
    

