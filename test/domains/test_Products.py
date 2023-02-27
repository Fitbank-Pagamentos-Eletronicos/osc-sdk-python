import unittest
from src.domains.Products import Products
from src.enums.ProductType import ProductType


class TestProducts(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "type": "BANK_ACCOUNT"
        }'''
        obj = Products.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = Products.create(type=ProductType.BANK_ACCOUNT)
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = Products.create(type=ProductType.BANK_ACCOUNT)
        json = orig.to_json()
        dest = Products.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
