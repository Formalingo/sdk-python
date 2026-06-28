from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .detected_document_field_rect import DetectedDocumentField_rect
    from .detected_document_field_type import DetectedDocumentField_type

@dataclass
class DetectedDocumentField(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The confidence property
    confidence: Optional[float] = None
    # The label property
    label: Optional[str] = None
    # The pageNumber property
    page_number: Optional[int] = None
    # The rect property
    rect: Optional[DetectedDocumentField_rect] = None
    # The type property
    type: Optional[DetectedDocumentField_type] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DetectedDocumentField:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DetectedDocumentField
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DetectedDocumentField()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .detected_document_field_rect import DetectedDocumentField_rect
        from .detected_document_field_type import DetectedDocumentField_type

        from .detected_document_field_rect import DetectedDocumentField_rect
        from .detected_document_field_type import DetectedDocumentField_type

        fields: dict[str, Callable[[Any], None]] = {
            "confidence": lambda n : setattr(self, 'confidence', n.get_float_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "pageNumber": lambda n : setattr(self, 'page_number', n.get_int_value()),
            "rect": lambda n : setattr(self, 'rect', n.get_object_value(DetectedDocumentField_rect)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(DetectedDocumentField_type)),
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
        writer.write_float_value("confidence", self.confidence)
        writer.write_str_value("label", self.label)
        writer.write_int_value("pageNumber", self.page_number)
        writer.write_object_value("rect", self.rect)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

