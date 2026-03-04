# Formalingo Python SDK

Official Python SDK for the [Formalingo API](https://formalingo.com/docs), generated with [Microsoft Kiota](https://learn.microsoft.com/en-us/openapi/kiota/).

## Installation

```bash
pip install git+https://github.com/Formalingo/sdk-python.git
```

Or with uv:

```bash
uv pip install git+https://github.com/Formalingo/sdk-python.git
```

## Quick Start

```python
import asyncio
from formalingo.formalingo_client import FormalingoClient
from kiota_abstractions.authentication import ApiKeyAuthenticationProvider
from kiota_abstractions.authentication.api_key_authentication_provider import KeyLocation
from kiota_http.httpx_request_adapter import HttpxRequestAdapter


def create_client(api_key: str, base_url: str = "https://formalingo.com") -> FormalingoClient:
    auth = ApiKeyAuthenticationProvider(
        key_location=KeyLocation.Header,
        api_key=f"Bearer {api_key}",
        parameter_name="Authorization",
    )
    adapter = HttpxRequestAdapter(auth, base_url=f"{base_url}/api/v1")
    return FormalingoClient(adapter)


async def main():
    client = create_client("af_live_YOUR_KEY")

    # List forms
    forms = await client.forms.get()
    print(forms)


asyncio.run(main())
```

## Examples

### Create a form

```python
form = await client.forms.post(body)
# body.title = "Customer Survey"
```

### Create a recipient with pre-fill

```python
recipient = await client.forms.by_form_id("FORM_ID").recipients.post(body)
# body.label = "John Doe"
# body.email = "john@acme.com"
# body.prefill = {"question-id": "pre-filled value"}
print(recipient.link)
```

### Create a document submission

```python
submission = await client.documents.by_document_id("DOC_ID").submissions.post(body)
print(submission.signers[0].link)
```

## Requirements

- Python 3.10+
- Dependencies: `microsoft-kiota-bundle >= 1.9.0`

## Documentation

- [Python SDK Guide](https://formalingo.com/docs/sdks/python)
- [API Reference](https://formalingo.com/docs/api-reference)
- [Full Documentation](https://formalingo.com/docs)

## Development

This SDK is generated from the Formalingo OpenAPI spec using Microsoft Kiota. It is maintained as a [submodule](https://github.com/Formalingo/sdk-python) of the main Formalingo monorepo.

To regenerate after API changes:

```bash
# From the monorepo root
yarn sdk:generate
```

## License

[MIT](LICENSE)
