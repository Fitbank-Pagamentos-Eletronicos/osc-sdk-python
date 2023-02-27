import unittest
from src.domains.Bank import Bank
from src.enums.AccountType import AccountType


class TestBank(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "bank": "001",
            "type": "CONTA_CORRENTE_INDIVIDUAL",
            "agency": "0001",
            "account": "56478-91"
        }'''
        obj = Bank.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = Bank.create(
            bank='001', type=AccountType.CONTA_CORRENTE_INDIVIDUAL, agency='0001', account='56478-91')
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = Bank.create(
            bank='001', type=AccountType.CONTA_CORRENTE_INDIVIDUAL, agency='0001', account='56478-91')
        json = orig.to_json()
        dest = Bank.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
