import unittest
from src.domains.Reference import Reference


class TestReference(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "name": "CARD",
            "phone": "85999991234"
        }'''
        obj = Reference.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = Reference.create(name="Francisco", phone="85999991234")
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = Reference.create(name="Francisco", phone="85999991234")
        json = orig.to_json()
        dest = Reference.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
