from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .import_document_bundle_response_data import ImportDocumentBundleResponse_data
    from .import_document_bundle_response_meta import ImportDocumentBundleResponse_meta

@dataclass
class ImportDocumentBundleResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The actions_omitted property
    actions_omitted: Optional[int] = None
    # The conditions_omitted property
    conditions_omitted: Optional[int] = None
    # The data property
    data: Optional[ImportDocumentBundleResponse_data] = None
    # The meta property
    meta: Optional[ImportDocumentBundleResponse_meta] = None
    # The success property
    success: Optional[bool] = None
    # The warnings property
    warnings: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ImportDocumentBundleResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ImportDocumentBundleResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ImportDocumentBundleResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .import_document_bundle_response_data import ImportDocumentBundleResponse_data
        from .import_document_bundle_response_meta import ImportDocumentBundleResponse_meta

        from .import_document_bundle_response_data import ImportDocumentBundleResponse_data
        from .import_document_bundle_response_meta import ImportDocumentBundleResponse_meta

        fields: dict[str, Callable[[Any], None]] = {
            "actions_omitted": lambda n : setattr(self, 'actions_omitted', n.get_int_value()),
            "conditions_omitted": lambda n : setattr(self, 'conditions_omitted', n.get_int_value()),
            "data": lambda n : setattr(self, 'data', n.get_object_value(ImportDocumentBundleResponse_data)),
            "meta": lambda n : setattr(self, 'meta', n.get_object_value(ImportDocumentBundleResponse_meta)),
            "success": lambda n : setattr(self, 'success', n.get_bool_value()),
            "warnings": lambda n : setattr(self, 'warnings', n.get_collection_of_primitive_values(str)),
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
        writer.write_int_value("actions_omitted", self.actions_omitted)
        writer.write_int_value("conditions_omitted", self.conditions_omitted)
        writer.write_object_value("data", self.data)
        writer.write_object_value("meta", self.meta)
        writer.write_bool_value("success", self.success)
        writer.write_collection_of_primitive_values("warnings", self.warnings)
        writer.write_additional_data_value(self.additional_data)
    

