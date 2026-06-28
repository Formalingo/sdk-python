from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .detected_document_field import DetectedDocumentField
    from .document_parse_job_result_stats import DocumentParseJobResult_stats
    from .parse_job_applied_result import ParseJobAppliedResult

@dataclass
class DocumentParseJobResult(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The applied property
    applied: Optional[ParseJobAppliedResult] = None
    # The detectedLanguage property
    detected_language: Optional[str] = None
    # The fields property
    fields: Optional[list[DetectedDocumentField]] = None
    # The stats property
    stats: Optional[DocumentParseJobResult_stats] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DocumentParseJobResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DocumentParseJobResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DocumentParseJobResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .detected_document_field import DetectedDocumentField
        from .document_parse_job_result_stats import DocumentParseJobResult_stats
        from .parse_job_applied_result import ParseJobAppliedResult

        from .detected_document_field import DetectedDocumentField
        from .document_parse_job_result_stats import DocumentParseJobResult_stats
        from .parse_job_applied_result import ParseJobAppliedResult

        fields: dict[str, Callable[[Any], None]] = {
            "applied": lambda n : setattr(self, 'applied', n.get_object_value(ParseJobAppliedResult)),
            "detectedLanguage": lambda n : setattr(self, 'detected_language', n.get_str_value()),
            "fields": lambda n : setattr(self, 'fields', n.get_collection_of_object_values(DetectedDocumentField)),
            "stats": lambda n : setattr(self, 'stats', n.get_object_value(DocumentParseJobResult_stats)),
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
        writer.write_object_value("applied", self.applied)
        writer.write_str_value("detectedLanguage", self.detected_language)
        writer.write_collection_of_object_values("fields", self.fields)
        writer.write_object_value("stats", self.stats)
        writer.write_additional_data_value(self.additional_data)
    

