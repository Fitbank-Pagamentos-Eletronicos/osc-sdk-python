import unittest
from src.domains.ConsumerUnit import ConsumerUnit


class TestConsumerUnit(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "number": "123456"
        }'''
        obj = ConsumerUnit.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = ConsumerUnit.create(number="123456")
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = ConsumerUnit.create(number="123456")
        json = orig.to_json()
        dest = ConsumerUnit.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
