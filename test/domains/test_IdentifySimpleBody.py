import unittest
from src.enums.IdentityType import IdentityType
from src.domains.IdentifySimpleBody import IdentifySimpleBody


class TestIdentifySimpleBody(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "type": "RG",
            "number": "132456789"
        }'''
        obj = IdentifySimpleBody.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = IdentifySimpleBody.create(
            type=IdentityType.RG, number="132456789")
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = IdentifySimpleBody.create(
            type=IdentityType.RG, number="132456789")
        json = orig.to_json()
        dest = IdentifySimpleBody.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
