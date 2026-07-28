import unittest

from formalingo.models.update_recipient_body import UpdateRecipientBody


class Writer:
    def __init__(self): self.values = {}
    def write_bool_value(self, key, value):
        if value is not None: self.values[key] = value
    def write_str_value(self, *_): pass
    def write_datetime_value(self, *_): pass
    def write_additional_data_value(self, *_): pass


class PhoneClearSerializationTests(unittest.TestCase):
    def test_omitted_and_true_clear_phone_are_distinct(self):
        omitted = Writer(); UpdateRecipientBody().serialize(omitted)
        explicit = Writer(); UpdateRecipientBody(clear_phone=True).serialize(explicit)
        self.assertNotIn('clearPhone', omitted.values)
        self.assertEqual(True, explicit.values['clearPhone'])
