from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SummaryGetResponse_data(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The completedRecipients property
    completed_recipients: Optional[int] = None
    # The completedSigners property
    completed_signers: Optional[int] = None
    # The documents property
    documents: Optional[int] = None
    # The forms property
    forms: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SummaryGetResponse_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SummaryGetResponse_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SummaryGetResponse_data()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "completedRecipients": lambda n : setattr(self, 'completed_recipients', n.get_int_value()),
            "completedSigners": lambda n : setattr(self, 'completed_signers', n.get_int_value()),
            "documents": lambda n : setattr(self, 'documents', n.get_int_value()),
            "forms": lambda n : setattr(self, 'forms', n.get_int_value()),
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
        writer.write_int_value("completedRecipients", self.completed_recipients)
        writer.write_int_value("completedSigners", self.completed_signers)
        writer.write_int_value("documents", self.documents)
        writer.write_int_value("forms", self.forms)
        writer.write_additional_data_value(self.additional_data)
    

