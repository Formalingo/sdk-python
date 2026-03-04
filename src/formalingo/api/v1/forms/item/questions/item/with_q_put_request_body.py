from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .with_q_put_request_body_priority import WithQPutRequestBody_priority
    from .with_q_put_request_body_type import WithQPutRequestBody_type

@dataclass
class WithQPutRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    from .with_q_put_request_body_priority import WithQPutRequestBody_priority

    # The priority property
    priority: Optional[WithQPutRequestBody_priority] = WithQPutRequestBody_priority("low")
    # The context property
    context: Optional[str] = None
    # The is_pii property
    is_pii: Optional[bool] = None
    # The is_required property
    is_required: Optional[bool] = None
    # The order property
    order: Optional[int] = None
    # The question_text property
    question_text: Optional[str] = None
    # Assign to a section (optional)
    section_id: Optional[UUID] = None
    # The type property
    type: Optional[WithQPutRequestBody_type] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WithQPutRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WithQPutRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WithQPutRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .with_q_put_request_body_priority import WithQPutRequestBody_priority
        from .with_q_put_request_body_type import WithQPutRequestBody_type

        from .with_q_put_request_body_priority import WithQPutRequestBody_priority
        from .with_q_put_request_body_type import WithQPutRequestBody_type

        fields: dict[str, Callable[[Any], None]] = {
            "context": lambda n : setattr(self, 'context', n.get_str_value()),
            "is_pii": lambda n : setattr(self, 'is_pii', n.get_bool_value()),
            "is_required": lambda n : setattr(self, 'is_required', n.get_bool_value()),
            "order": lambda n : setattr(self, 'order', n.get_int_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_enum_value(WithQPutRequestBody_priority)),
            "question_text": lambda n : setattr(self, 'question_text', n.get_str_value()),
            "section_id": lambda n : setattr(self, 'section_id', n.get_uuid_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(WithQPutRequestBody_type)),
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
        writer.write_str_value("context", self.context)
        writer.write_bool_value("is_pii", self.is_pii)
        writer.write_bool_value("is_required", self.is_required)
        writer.write_int_value("order", self.order)
        writer.write_enum_value("priority", self.priority)
        writer.write_str_value("question_text", self.question_text)
        writer.write_uuid_value("section_id", self.section_id)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

