from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .start_document_parse_job_body_apply_mode import StartDocumentParseJobBody_applyMode

@dataclass
class StartDocumentParseJobBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    from .start_document_parse_job_body_apply_mode import StartDocumentParseJobBody_applyMode

    # The applyMode property
    apply_mode: Optional[StartDocumentParseJobBody_applyMode] = StartDocumentParseJobBody_applyMode("draft")
    # The confirmAiParse property
    confirm_ai_parse: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StartDocumentParseJobBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StartDocumentParseJobBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StartDocumentParseJobBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .start_document_parse_job_body_apply_mode import StartDocumentParseJobBody_applyMode

        from .start_document_parse_job_body_apply_mode import StartDocumentParseJobBody_applyMode

        fields: dict[str, Callable[[Any], None]] = {
            "applyMode": lambda n : setattr(self, 'apply_mode', n.get_enum_value(StartDocumentParseJobBody_applyMode)),
            "confirmAiParse": lambda n : setattr(self, 'confirm_ai_parse', n.get_bool_value()),
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
        writer.write_enum_value("applyMode", self.apply_mode)
        writer.write_bool_value("confirmAiParse", self.confirm_ai_parse)
        writer.write_additional_data_value(self.additional_data)
    

