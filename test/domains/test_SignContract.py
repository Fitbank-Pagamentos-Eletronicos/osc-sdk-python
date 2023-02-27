import unittest
from src.domains.SignContract import SignContract


class TestSignContract(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "acepted_check_sum": "CARD"
        }'''
        obj = SignContract.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = SignContract.create(aceptedCheckSum="acepted_check_sum")
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = SignContract.create(aceptedCheckSum="acepted_check_sum")
        json = orig.to_json()
        dest = SignContract.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
