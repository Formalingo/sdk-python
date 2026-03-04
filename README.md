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
from formalingo import create_client

async def main():
    client = create_client("af_live_YOUR_KEY")

    # List forms
    forms = await client.api.v1.forms.get()
    print(forms)

asyncio.run(main())
```

## Examples

### Create a form

```python
from formalingo.models.create_form_body import CreateFormBody

body = CreateFormBody()
body.title = "Customer Survey"

form = await client.api.v1.forms.post(body)
```

### Create a recipient with pre-fill

```python
from formalingo.models.create_recipient_body import CreateRecipientBody

body = CreateRecipientBody()
body.label = "John Doe"
body.email = "john@acme.com"
body.prefill = {"question-id": "pre-filled value"}

recipient = await client.api.v1.forms.by_form_id("FORM_ID").recipients.post(body)
print(recipient.link)
```

### Create a document submission

```python
from formalingo.models.create_submission_body import CreateSubmissionBody

submission = await client.api.v1.documents.by_document_id("DOC_ID").submissions.post(body)
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
