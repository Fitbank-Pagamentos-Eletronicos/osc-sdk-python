import unittest
from src.domains.ProductBankAccount import ProductBankAccount


class TestProductBankAccount(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "type": "BANK_ACCOUNT"
        }'''
        obj = ProductBankAccount.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = ProductBankAccount.create()
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = ProductBankAccount.create()
        json = orig.to_json()
        dest = ProductBankAccount.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
