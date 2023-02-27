import unittest
from src.domains.BorrowerInfo import BorrowerInfo


class TestBorrowerInfo(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "isRegistered": "True",
            "isBlocked": "False"
        }'''
        obj = BorrowerInfo.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = BorrowerInfo.create(isRegistered=True, isBlocked=False)
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = BorrowerInfo.create(isRegistered=True, isBlocked=False)
        json = orig.to_json()
        dest = BorrowerInfo.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
