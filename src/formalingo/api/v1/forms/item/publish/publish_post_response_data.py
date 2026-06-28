from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.form import Form
    from ......models.form_revision import FormRevision

@dataclass
class PublishPostResponse_data(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The form property
    form: Optional[Form] = None
    # The revision property
    revision: Optional[FormRevision] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PublishPostResponse_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PublishPostResponse_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PublishPostResponse_data()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ......models.form import Form
        from ......models.form_revision import FormRevision

        from ......models.form import Form
        from ......models.form_revision import FormRevision

        fields: dict[str, Callable[[Any], None]] = {
            "form": lambda n : setattr(self, 'form', n.get_object_value(Form)),
            "revision": lambda n : setattr(self, 'revision', n.get_object_value(FormRevision)),
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
        writer.write_object_value("form", self.form)
        writer.write_object_value("revision", self.revision)
        writer.write_additional_data_value(self.additional_data)
    

