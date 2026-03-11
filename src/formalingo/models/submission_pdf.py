from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class SubmissionPdf(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The completedAt property
    completed_at: Optional[datetime.datetime] = None
    # Presigned download URL. Expires in 5 minutes.
    download_url: Optional[str] = None
    # URL expiry in seconds
    expires_in: Optional[float] = None
    # The submissionId property
    submission_id: Optional[UUID] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SubmissionPdf:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SubmissionPdf
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SubmissionPdf()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "completedAt": lambda n : setattr(self, 'completed_at', n.get_datetime_value()),
            "downloadUrl": lambda n : setattr(self, 'download_url', n.get_str_value()),
            "expiresIn": lambda n : setattr(self, 'expires_in', n.get_float_value()),
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
        writer.write_datetime_value("completedAt", self.completed_at)
        writer.write_str_value("downloadUrl", self.download_url)
        writer.write_float_value("expiresIn", self.expires_in)
        writer.write_uuid_value("submissionId", self.submission_id)
        writer.write_additional_data_value(self.additional_data)
    

