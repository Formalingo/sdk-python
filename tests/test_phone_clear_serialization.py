import unittest
import json
from uuid import UUID

from formalingo import (
    create_bulk_recipients,
    create_client,
    create_document_submission,
)
from formalingo.api.v1.forms.item.recipients.bulk.bulk_post_request_body import (
    BulkPostRequestBody,
)
from formalingo.api.v1.forms.item.recipients.bulk.bulk_post_request_body_recipients import (
    BulkPostRequestBody_recipients,
)
from formalingo.api.v1.forms.item.recipients.bulk.bulk_post_response import (
    BulkPostResponse,
)
from formalingo.formalingo_client import FormalingoClient
from formalingo.models.create_submission_body import CreateSubmissionBody
from formalingo.models.create_submission_response import CreateSubmissionResponse
from formalingo.models.create_submission_result import CreateSubmissionResult
from formalingo.models.create_submission_signer_result import CreateSubmissionSignerResult
from formalingo.models.recipient_create_result import RecipientCreateResult
from formalingo.models.recipient_bulk_create_result import RecipientBulkCreateResult
from formalingo.models.signer_input import SignerInput
from formalingo.models.update_recipient_body import UpdateRecipientBody
from formalingo.models.update_signer_body import UpdateSignerBody
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_serialization_json.json_serialization_writer import JsonSerializationWriter
from kiota_serialization_json.json_serialization_writer_factory import (
    JsonSerializationWriterFactory,
)


def serialized(model):
    writer = JsonSerializationWriter()
    model.serialize(writer)
    return json.loads(writer.get_serialized_content())


class CapturingRequestAdapter(RequestAdapter):
    def __init__(self, response):
        self.base_url = "https://example.test"
        self.response = response
        self.request_info = None
        self.writer_factory = JsonSerializationWriterFactory()

    def get_serialization_writer_factory(self):
        return self.writer_factory

    async def send_async(self, request_info, parsable_factory, error_map):
        self.request_info = request_info
        return self.response

    async def send_collection_async(self, request_info, parsable_factory, error_map):
        raise NotImplementedError

    async def send_collection_of_primitive_async(
        self, request_info, response_type, error_map
    ):
        raise NotImplementedError

    async def send_primitive_async(self, request_info, response_type, error_map):
        raise NotImplementedError

    async def send_no_response_content_async(self, request_info, error_map):
        raise NotImplementedError

    def enable_backing_store(self, backing_store_factory):
        pass

    async def convert_to_native_async(self, request_info):
        raise NotImplementedError


class PhoneClearSerializationTests(unittest.TestCase):
    def test_omitted_and_true_clear_phone_are_distinct(self):
        self.assertNotIn('clearPhone', serialized(UpdateRecipientBody()))
        self.assertTrue(serialized(UpdateRecipientBody(clear_phone=True))['clearPhone'])

    def test_signer_omitted_and_true_clear_phone_are_distinct(self):
        self.assertNotIn('clearPhone', serialized(UpdateSignerBody()))
        self.assertTrue(serialized(UpdateSignerBody(clear_phone=True))['clearPhone'])

    def test_recipient_create_result_preserves_dispatch_correlation(self):
        payload = serialized(RecipientCreateResult(
            dispatch_id=UUID('00000000-0000-0000-0000-000000000042'),
            token='one-time-token',
            link='https://www.formalingo.com/f/one-time-token',
            plain_password='one-time-password',
        ))

        self.assertEqual(payload['dispatchId'], '00000000-0000-0000-0000-000000000042')
        self.assertEqual(payload['token'], 'one-time-token')
        self.assertEqual(payload['link'], 'https://www.formalingo.com/f/one-time-token')
        self.assertEqual(payload['plain_password'], 'one-time-password')
        self.assertNotIn('passwordHash', payload)

    def test_document_submission_result_preserves_safe_dispatch_receipt(self):
        payload = serialized(CreateSubmissionResult(
            submission_id=UUID('00000000-0000-0000-0000-000000000041'),
            dispatch_id=UUID('00000000-0000-0000-0000-000000000042'),
            dispatch_reused=True,
            links_created=True,
        ))

        self.assertEqual(payload['submissionId'], '00000000-0000-0000-0000-000000000041')
        self.assertEqual(payload['dispatchId'], '00000000-0000-0000-0000-000000000042')
        self.assertTrue(payload['dispatchReused'])
        self.assertTrue(payload['linksCreated'])

        signer_payload = serialized(CreateSubmissionSignerResult(
            id=UUID('00000000-0000-0000-0000-000000000043'),
            label='Buyer',
            role='buyer',
            name='Alice',
            color='#13A373',
            order=0,
            link='https://www.formalingo.com/d/one-time-token',
        ))
        self.assertEqual(signer_payload['link'], 'https://www.formalingo.com/d/one-time-token')
        self.assertNotIn('token', signer_payload)
        self.assertNotIn('email', signer_payload)
        self.assertNotIn('phone', signer_payload)
        self.assertNotIn('passwordHash', signer_payload)


class DocumentSubmissionConvenienceTests(unittest.IsolatedAsyncioTestCase):
    def test_client_factory_applies_the_requested_base_url(self):
        client = create_client('test-key', 'https://example.test')

        self.assertEqual(client.request_adapter.base_url, 'https://example.test')
        self.assertEqual(client.path_parameters['baseurl'], 'https://example.test')

    async def test_emits_idempotency_metadata_and_returns_data_signers(self):
        signer_result = CreateSubmissionSignerResult(
            id=UUID('00000000-0000-0000-0000-000000000043'),
            label='Buyer',
            role='buyer',
            name='Alice',
            color='#13A373',
            order=0,
            link='https://www.formalingo.com/d/one-time-token',
        )
        response = CreateSubmissionResponse(
            success=True,
            data=CreateSubmissionResult(
                submission_id=UUID('00000000-0000-0000-0000-000000000041'),
                dispatch_id=UUID('00000000-0000-0000-0000-000000000042'),
                dispatch_reused=False,
                links_created=True,
                signers=[signer_result],
            ),
        )
        adapter = CapturingRequestAdapter(response)
        client = FormalingoClient(adapter)
        client.path_parameters['baseurl'] = adapter.base_url
        body = CreateSubmissionBody(
            signers=[
                SignerInput(
                    role='buyer',
                    name='Alice',
                    email='alice@example.com',
                ),
            ],
        )

        submission = await create_document_submission(
            client,
            UUID('00000000-0000-0000-0000-000000000001'),
            body,
            'document-create-1',
        )

        request = adapter.request_info
        self.assertIsNotNone(request)
        self.assertEqual(request.http_method, Method.POST)
        self.assertEqual(
            str(request.url),
            'https://example.test/api/v1/documents/00000000-0000-0000-0000-000000000001/submissions',
        )
        self.assertEqual(
            request.headers.get('Idempotency-Key'),
            {'document-create-1'},
        )
        self.assertEqual(
            json.loads(request.content),
            {
                'deliveryFormat': 'document',
                'signers': [{
                    'email': 'alice@example.com',
                    'name': 'Alice',
                    'role': 'buyer',
                }],
            },
        )
        self.assertEqual(
            submission.signers[0].link,
            'https://www.formalingo.com/d/one-time-token',
        )

    async def test_rejects_invalid_idempotency_metadata_before_sending(self):
        with self.assertRaisesRegex(ValueError, '1-255 printable ASCII'):
            await create_document_submission(
                None,
                UUID('00000000-0000-0000-0000-000000000001'),
                CreateSubmissionBody(),
                'contains a space',
            )


class BulkRecipientConvenienceTests(unittest.IsolatedAsyncioTestCase):
    async def test_emits_required_idempotency_metadata_and_returns_data(self):
        recipient = RecipientBulkCreateResult(
            id=UUID('00000000-0000-0000-0000-000000000043'),
            label='Alice',
        )
        adapter = CapturingRequestAdapter(BulkPostResponse(
            success=True,
            data=[recipient],
        ))
        client = FormalingoClient(adapter)
        client.path_parameters['baseurl'] = adapter.base_url
        body = BulkPostRequestBody(
            confirm_bulk=True,
            recipients=[BulkPostRequestBody_recipients(label='Alice')],
            send_notifications=False,
        )

        recipients = await create_bulk_recipients(
            client,
            UUID('00000000-0000-0000-0000-000000000001'),
            body,
            'recipient-bulk-1',
        )

        request = adapter.request_info
        self.assertEqual(request.http_method, Method.POST)
        self.assertEqual(
            str(request.url),
            'https://example.test/api/v1/forms/00000000-0000-0000-0000-000000000001/recipients/bulk',
        )
        self.assertEqual(
            request.headers.get('Idempotency-Key'),
            {'recipient-bulk-1'},
        )
        self.assertEqual(
            json.loads(request.content),
            {
                'confirmBulk': True,
                'recipients': [{'label': 'Alice'}],
                'sendNotifications': False,
            },
        )
        self.assertEqual(recipients[0].label, 'Alice')

    async def test_rejects_invalid_idempotency_metadata_before_sending(self):
        for value in ['', 'contains a space', 'a' * 256]:
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, '1-255 printable ASCII'):
                    await create_bulk_recipients(
                        None,
                        UUID('00000000-0000-0000-0000-000000000001'),
                        BulkPostRequestBody(),
                        value,
                    )
