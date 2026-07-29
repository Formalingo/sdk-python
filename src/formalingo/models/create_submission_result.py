from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .create_submission_signer_result import CreateSubmissionSignerResult

@dataclass
class CreateSubmissionResult(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Durable delivery dispatch correlated with this signing submission.
    dispatch_id: Optional[UUID] = None
    # True when the Idempotency-Key matched the same normalized request and the existing submission and dispatch were returned.
    dispatch_reused: Optional[bool] = None
    # Confirms that signing links were created. Delivery continues independently through the correlated dispatch.
    links_created: Optional[bool] = None
    # The signers property
    signers: Optional[list[CreateSubmissionSignerResult]] = None
    # The submissionId property
    submission_id: Optional[UUID] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateSubmissionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateSubmissionResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateSubmissionResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .create_submission_signer_result import CreateSubmissionSignerResult

        from .create_submission_signer_result import CreateSubmissionSignerResult

        fields: dict[str, Callable[[Any], None]] = {
            "dispatchId": lambda n : setattr(self, 'dispatch_id', n.get_uuid_value()),
            "dispatchReused": lambda n : setattr(self, 'dispatch_reused', n.get_bool_value()),
            "linksCreated": lambda n : setattr(self, 'links_created', n.get_bool_value()),
            "signers": lambda n : setattr(self, 'signers', n.get_collection_of_object_values(CreateSubmissionSignerResult)),
            "submissionId": lambda n : setattr(self, 'submission_id', n.get_uuid_value()),
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
        writer.write_uuid_value("dispatchId", self.dispatch_id)
        writer.write_bool_value("dispatchReused", self.dispatch_reused)
        writer.write_bool_value("linksCreated", self.links_created)
        writer.write_collection_of_object_values("signers", self.signers)
        writer.write_uuid_value("submissionId", self.submission_id)
        writer.write_additional_data_value(self.additional_data)
    

