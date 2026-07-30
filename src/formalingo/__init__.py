"""Handwritten convenience helpers for the Formalingo Python SDK."""

from uuid import UUID

from kiota_abstractions.authentication import ApiKeyAuthenticationProvider
from kiota_abstractions.authentication.api_key_authentication_provider import KeyLocation
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.headers_collection import HeadersCollection
from kiota_http.httpx_request_adapter import HttpxRequestAdapter

from .formalingo_client import FormalingoClient
from .api.v1.forms.item.recipients.bulk.bulk_post_request_body import (
    BulkPostRequestBody,
)
from .models.create_submission_body import CreateSubmissionBody
from .models.create_submission_result import CreateSubmissionResult
from .models.recipient_bulk_create_result import RecipientBulkCreateResult

__version__ = "0.1.1"


def create_client(
    api_key: str,
    base_url: str = "https://app.formalingo.com",
) -> FormalingoClient:
    """Create an authenticated Formalingo API client."""
    auth = ApiKeyAuthenticationProvider(
        key_location=KeyLocation.Header,
        api_key=f"Bearer {api_key}",
        parameter_name="Authorization",
    )
    adapter = HttpxRequestAdapter(auth, base_url=base_url)
    # Current Kiota Python releases do not apply the constructor's base_url
    # argument to the adapter, and generated clients store it under base_url
    # while request templates expand baseurl.
    adapter.base_url = base_url
    client = FormalingoClient(adapter)
    client.path_parameters["baseurl"] = base_url
    return client


async def create_document_submission(
    client: FormalingoClient,
    document_id: UUID,
    body: CreateSubmissionBody,
    idempotency_key: str,
) -> CreateSubmissionResult:
    """Create a retry-safe signing submission and return the response data."""
    _assert_idempotency_key(idempotency_key)

    headers = HeadersCollection()
    headers.try_add("Idempotency-Key", idempotency_key)
    response = await client.api.v1.documents.by_id(document_id).submissions.post(
        body,
        RequestConfiguration(headers=headers),
    )

    if response is None or response.data is None:
        raise RuntimeError("Formalingo returned no document submission data")

    return response.data


async def create_bulk_recipients(
    client: FormalingoClient,
    form_id: UUID,
    body: BulkPostRequestBody,
    idempotency_key: str,
) -> list[RecipientBulkCreateResult]:
    """Create up to 100 recipients with caller-owned retry metadata."""
    _assert_idempotency_key(idempotency_key)

    headers = HeadersCollection()
    headers.try_add("Idempotency-Key", idempotency_key)
    response = await client.api.v1.forms.by_id(form_id).recipients.bulk.post(
        body,
        RequestConfiguration(headers=headers),
    )

    if response is None or response.data is None:
        raise RuntimeError("Formalingo returned no bulk recipient data")

    return response.data


def _assert_idempotency_key(idempotency_key: str) -> None:
    if (
        not isinstance(idempotency_key, str)
        or not 1 <= len(idempotency_key) <= 255
        or any(ord(char) < 0x21 or ord(char) > 0x7E for char in idempotency_key)
    ):
        raise ValueError(
            "idempotency_key must contain 1-255 printable ASCII characters without spaces"
        )


__all__ = [
    "FormalingoClient",
    "create_bulk_recipients",
    "create_client",
    "create_document_submission",
]
