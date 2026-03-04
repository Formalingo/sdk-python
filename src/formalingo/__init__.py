"""Formalingo Python SDK."""

__version__ = "0.1.0"

from formalingo.formalingo_client import FormalingoClient
from kiota_abstractions.authentication import ApiKeyAuthenticationProvider
from kiota_abstractions.authentication.api_key_authentication_provider import KeyLocation
from kiota_http.httpx_request_adapter import HttpxRequestAdapter


def create_client(
    api_key: str,
    base_url: str = "https://formalingo.com",
) -> FormalingoClient:
    """Create a configured Formalingo API client.

    Args:
        api_key: Your Formalingo API key (e.g. "af_live_...")
        base_url: API base URL (defaults to production)

    Returns:
        A FormalingoClient instance ready to use.

    Usage::

        from formalingo import create_client

        client = create_client("af_live_YOUR_KEY")
        forms = await client.api.v1.forms.get()
    """
    auth = ApiKeyAuthenticationProvider(
        key_location=KeyLocation.Header,
        api_key=f"Bearer {api_key}",
        parameter_name="Authorization",
    )
    adapter = HttpxRequestAdapter(auth, base_url=base_url)
    return FormalingoClient(adapter)
