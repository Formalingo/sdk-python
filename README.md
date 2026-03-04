# Formalingo Python SDK

Official Python SDK for the [Formalingo API](https://formalingo.com/docs).

## Installation

```bash
pip install formalingo-sdk
```

## Quick Start

```python
from formalingo.formalingo_client import FormalingoClient
from kiota_abstractions.authentication import ApiKeyAuthenticationProvider
from kiota_abstractions.authentication.api_key_authentication_provider import KeyLocation
from kiota_http.httpx_request_adapter import HttpxRequestAdapter

auth = ApiKeyAuthenticationProvider(
    key_location=KeyLocation.Header,
    api_key="Bearer af_live_YOUR_KEY",
    parameter_name="Authorization",
)
adapter = HttpxRequestAdapter(auth, base_url="https://formalingo.com/api/v1")
client = FormalingoClient(adapter)

# List forms
forms = await client.forms.get()
```

## Documentation

Full documentation: [formalingo.com/docs/sdks/python](https://formalingo.com/docs/sdks/python)
