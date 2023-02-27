import unittest
from src.enums.Occupation import Occupation
from src.domains.BusinessSimpleBody import BusinessSimpleBody


class TestBusinessSimpleBody(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "occupation": "AUTOMONO",
            "income": "5000"
        }'''
        obj = BusinessSimpleBody.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = BusinessSimpleBody.create(
            occupation=Occupation.AUTOMONO, income="5000")
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = BusinessSimpleBody.create(
            occupation=Occupation.AUTOMONO, income="5000")
        json = orig.to_json()
        dest = BusinessSimpleBody.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
