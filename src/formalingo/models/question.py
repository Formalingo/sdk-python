from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .question_priority import Question_priority
    from .question_type import Question_type

@dataclass
class Question(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The context property
    context: Optional[str] = None
    # The createdAt property
    created_at: Optional[datetime.datetime] = None
    # The formId property
    form_id: Optional[UUID] = None
    # The id property
    id: Optional[UUID] = None
    # The isPii property
    is_pii: Optional[bool] = None
    # The isRequired property
    is_required: Optional[bool] = None
    # The order property
    order: Optional[float] = None
    # The priority property
    priority: Optional[Question_priority] = None
    # The questionText property
    question_text: Optional[str] = None
    # The sectionId property
    section_id: Optional[UUID] = None
    # The type property
    type: Optional[Question_type] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Question:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Question
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Question()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .question_priority import Question_priority
        from .question_type import Question_type

        from .question_priority import Question_priority
        from .question_type import Question_type

        fields: dict[str, Callable[[Any], None]] = {
            "context": lambda n : setattr(self, 'context', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "formId": lambda n : setattr(self, 'form_id', n.get_uuid_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "isPii": lambda n : setattr(self, 'is_pii', n.get_bool_value()),
            "isRequired": lambda n : setattr(self, 'is_required', n.get_bool_value()),
            "order": lambda n : setattr(self, 'order', n.get_float_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_enum_value(Question_priority)),
            "questionText": lambda n : setattr(self, 'question_text', n.get_str_value()),
            "sectionId": lambda n : setattr(self, 'section_id', n.get_uuid_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(Question_type)),
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
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_uuid_value("formId", self.form_id)
        writer.write_uuid_value("id", self.id)
        writer.write_bool_value("isPii", self.is_pii)
        writer.write_bool_value("isRequired", self.is_required)
        writer.write_float_value("order", self.order)
        writer.write_enum_value("priority", self.priority)
        writer.write_str_value("questionText", self.question_text)
        writer.write_uuid_value("sectionId", self.section_id)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

