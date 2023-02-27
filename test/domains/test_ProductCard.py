import unittest
from src.enums.Network import Network
from src.domains.ProductCard import ProductCard


class TestProductCard(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "type": "CARD",
            "network": "MASTERCARD",
            "payDay": "2023-01-05"
        }'''
        obj = ProductCard.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = ProductCard.create(
            network=Network.MASTERCARD, payDay="2023-01-05")
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = ProductCard.create(
            network=Network.MASTERCARD, payDay="2023-01-05")
        json = orig.to_json()
        dest = ProductCard.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
