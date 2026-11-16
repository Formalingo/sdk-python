"""Configured entry point for the Formalingo Python SDK.

This handwritten module is preserved by the SDK generation script.
"""

from typing import Any
from urllib.parse import urlsplit

from kiota_abstractions.authentication.api_key_authentication_provider import (
    ApiKeyAuthenticationProvider,
    KeyLocation,
)
from kiota_abstractions.request_information import RequestInformation
from kiota_http.httpx_request_adapter import HttpxRequestAdapter

from .formalingo_client import FormalingoClient

__all__ = ["FormalingoClient", "create_client"]


def _http_origin(url: str) -> tuple[str, str, int]:
    try:
        if not isinstance(url, str):
            raise ValueError
        parsed = urlsplit(url)
        if (
            parsed.scheme not in ("http", "https")
            or not parsed.hostname
            or parsed.username is not None
            or parsed.password is not None
        ):
            raise ValueError
        port = parsed.port
        effective_port = port if port is not None else (443 if parsed.scheme == "https" else 80)
        return parsed.scheme, parsed.hostname, effective_port
    except (TypeError, ValueError):
        raise ValueError("URL must be an absolute HTTP(S) URL without credentials") from None


class _OriginBoundApiKeyAuthenticationProvider(ApiKeyAuthenticationProvider):
    def __init__(self, api_key: str, base_url: str) -> None:
        super().__init__(KeyLocation.Header, f"Bearer {api_key}", "Authorization")
        self._origin = _http_origin(base_url)

    async def authenticate_request(
        self,
        request: RequestInformation,
        additional_authentication_context: dict[str, Any] | None = None,
    ) -> None:
        if request is None or _http_origin(request.url) != self._origin:
            raise ValueError("Request URL must match the configured API origin")
        await super().authenticate_request(request, additional_authentication_context or {})


def create_client(
    api_key: str,
    base_url: str = "https://app.formalingo.com",
) -> FormalingoClient:
    """Return a client whose API key is limited to the configured API origin."""
    if not isinstance(api_key, str) or not api_key.strip():
        raise ValueError("api_key must be a non-empty string")

    auth = _OriginBoundApiKeyAuthenticationProvider(api_key, base_url)
    adapter = HttpxRequestAdapter(auth)
    adapter.base_url = base_url
    return FormalingoClient(adapter)
