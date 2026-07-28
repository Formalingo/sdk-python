import unittest
import json

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
