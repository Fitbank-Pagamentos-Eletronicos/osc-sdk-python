import unittest
from src.domains.ErrorField import ErrorField


class TestErrorField(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "field": "CampoErro",
            "message": "MessagemErro"
        }'''
        obj = ErrorField.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = ErrorField.create(field="CampoErro", message="MessagemErro")
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = ErrorField.create(field="CampoErro", message="MessagemErro")
        json = orig.to_json()
        dest = ErrorField.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
