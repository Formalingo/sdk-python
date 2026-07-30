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

### Bulk create recipients safely

```python
from uuid import UUID
from formalingo import create_bulk_recipients
from formalingo.api.v1.forms.item.recipients.bulk.bulk_post_request_body import BulkPostRequestBody
from formalingo.api.v1.forms.item.recipients.bulk.bulk_post_request_body_recipients import BulkPostRequestBody_recipients

body = BulkPostRequestBody(
    confirm_bulk=True,
    recipients=[
        BulkPostRequestBody_recipients(
            label="Alice",
            email="alice@example.com",
        ),
    ],
)
recipients = await create_bulk_recipients(
    client,
    UUID("00000000-0000-0000-0000-000000000001"),
    body,
    "recipient-bulk-create-7f3f",
)
```

The required caller-owned key makes ambiguous retries safe. Reuse it only with the exact same serialized request body.
On `idempotency_request_in_progress`, retry the exact body with the same key. A different body returns `idempotency_key_conflict`; recipient erasure returns `idempotency_replay_unavailable`.

### Create a document submission

```python
from uuid import UUID

from formalingo import create_document_submission
from formalingo.models.create_submission_body import CreateSubmissionBody
from formalingo.models.signer_input import SignerInput

body = CreateSubmissionBody(
    signers=[SignerInput(
        role="signer_1",
        name="Alice",
        email="alice@example.com",
    )],
)
submission = await create_document_submission(
    client,
    UUID("00000000-0000-0000-0000-000000000001"),
    body,
    "document-create-7f3f",
)
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
