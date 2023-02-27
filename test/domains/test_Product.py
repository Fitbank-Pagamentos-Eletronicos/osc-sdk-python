import unittest
from src.domains.Product import Product


class TestProduct(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "productId": "1234",
            "name": "nome",
            "logo": "logo"
        }'''
        obj = Product.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = Product.create(productId=2, name="nome", logo="logo")
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = Product.create(productId=2, name="nome", logo="logo")
        json = orig.to_json()
        dest = Product.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
