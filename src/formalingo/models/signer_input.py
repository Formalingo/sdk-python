from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .signer_input_prefill import SignerInput_prefill

@dataclass
class SignerInput(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The email property
    email: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # Optional password to protect the signing link
    password: Optional[str] = None
    # The phone property
    phone: Optional[str] = None
    # Map of field ID → pre-filled value. Creates DocumentResponse records immediately.
    prefill: Optional[SignerInput_prefill] = None
    # If true, prefilled fields are marked read-only on the document
    prefill_readonly: Optional[bool] = None
    # List of field IDs to mark as read-only for this signer, regardless of the document-level isReadOnly setting. Useful for locking specific fields per-signer at submission time.
    readonly_field_ids: Optional[list[UUID]] = None
    # Must match a signer role defined in the document editor
    role: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SignerInput:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SignerInput
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SignerInput()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .signer_input_prefill import SignerInput_prefill

        from .signer_input_prefill import SignerInput_prefill

        fields: dict[str, Callable[[Any], None]] = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "prefill": lambda n : setattr(self, 'prefill', n.get_object_value(SignerInput_prefill)),
            "prefillReadonly": lambda n : setattr(self, 'prefill_readonly', n.get_bool_value()),
            "readonlyFieldIds": lambda n : setattr(self, 'readonly_field_ids', n.get_collection_of_primitive_values(UUID)),
            "role": lambda n : setattr(self, 'role', n.get_str_value()),
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
        writer.write_str_value("email", self.email)
        writer.write_str_value("name", self.name)
        writer.write_str_value("password", self.password)
        writer.write_str_value("phone", self.phone)
        writer.write_object_value("prefill", self.prefill)
        writer.write_bool_value("prefillReadonly", self.prefill_readonly)
        writer.write_collection_of_primitive_values("readonlyFieldIds", self.readonly_field_ids)
        writer.write_str_value("role", self.role)
        writer.write_additional_data_value(self.additional_data)
    

