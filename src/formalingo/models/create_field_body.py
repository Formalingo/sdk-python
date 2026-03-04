from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .create_field_body_direction import CreateFieldBody_direction
    from .create_field_body_options import CreateFieldBody_options
    from .create_field_body_type import CreateFieldBody_type

@dataclass
class CreateFieldBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    from .create_field_body_direction import CreateFieldBody_direction

    # The direction property
    direction: Optional[CreateFieldBody_direction] = CreateFieldBody_direction("auto")
    # The assigneeRole property
    assignee_role: Optional[str] = None
    # The defaultValue property
    default_value: Optional[str] = None
    # The height property
    height: Optional[float] = None
    # The isReadOnly property
    is_read_only: Optional[bool] = None
    # The isRequired property
    is_required: Optional[bool] = None
    # The label property
    label: Optional[str] = None
    # The options property
    options: Optional[CreateFieldBody_options] = None
    # The order property
    order: Optional[int] = None
    # The pageNumber property
    page_number: Optional[int] = None
    # The type property
    type: Optional[CreateFieldBody_type] = None
    # The width property
    width: Optional[float] = None
    # The x property
    x: Optional[float] = None
    # The y property
    y: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateFieldBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateFieldBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateFieldBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .create_field_body_direction import CreateFieldBody_direction
        from .create_field_body_options import CreateFieldBody_options
        from .create_field_body_type import CreateFieldBody_type

        from .create_field_body_direction import CreateFieldBody_direction
        from .create_field_body_options import CreateFieldBody_options
        from .create_field_body_type import CreateFieldBody_type

        fields: dict[str, Callable[[Any], None]] = {
            "assigneeRole": lambda n : setattr(self, 'assignee_role', n.get_str_value()),
            "defaultValue": lambda n : setattr(self, 'default_value', n.get_str_value()),
            "direction": lambda n : setattr(self, 'direction', n.get_enum_value(CreateFieldBody_direction)),
            "height": lambda n : setattr(self, 'height', n.get_float_value()),
            "isReadOnly": lambda n : setattr(self, 'is_read_only', n.get_bool_value()),
            "isRequired": lambda n : setattr(self, 'is_required', n.get_bool_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "options": lambda n : setattr(self, 'options', n.get_object_value(CreateFieldBody_options)),
            "order": lambda n : setattr(self, 'order', n.get_int_value()),
            "pageNumber": lambda n : setattr(self, 'page_number', n.get_int_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(CreateFieldBody_type)),
            "width": lambda n : setattr(self, 'width', n.get_float_value()),
            "x": lambda n : setattr(self, 'x', n.get_float_value()),
            "y": lambda n : setattr(self, 'y', n.get_float_value()),
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
        writer.write_str_value("assigneeRole", self.assignee_role)
        writer.write_str_value("defaultValue", self.default_value)
        writer.write_enum_value("direction", self.direction)
        writer.write_float_value("height", self.height)
        writer.write_bool_value("isReadOnly", self.is_read_only)
        writer.write_bool_value("isRequired", self.is_required)
        writer.write_str_value("label", self.label)
        writer.write_object_value("options", self.options)
        writer.write_int_value("order", self.order)
        writer.write_int_value("pageNumber", self.page_number)
        writer.write_enum_value("type", self.type)
        writer.write_float_value("width", self.width)
        writer.write_float_value("x", self.x)
        writer.write_float_value("y", self.y)
        writer.write_additional_data_value(self.additional_data)
    

