import unittest
import json
from uuid import UUID

from formalingo.models.create_submission_result import CreateSubmissionResult
from formalingo.models.create_submission_signer_result import CreateSubmissionSignerResult
from formalingo.models.recipient_create_result import RecipientCreateResult
from formalingo.models.update_recipient_body import UpdateRecipientBody
from formalingo.models.update_signer_body import UpdateSignerBody
from kiota_serialization_json.json_serialization_writer import JsonSerializationWriter


def serialized(model):
    writer = JsonSerializationWriter()
    model.serialize(writer)
    return json.loads(writer.get_serialized_content())


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
