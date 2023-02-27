import unittest
from src.domains.BankAccount import BankAccount
from src.enums.CreditStatus import CreditStatus
#from src.enums.PendentDocuments import PendentDocuments


class TestBankAccount(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "customerServiceNumber": "123456",
            "product": "2",
            "productId": "2",
            "hasDocuments": "True",
            "hasContracts": "True",
            "lastStatus": "PRE_APROVADO",
            "dateCreated": "2022-12-29",
            "lastUpdated": "2022-12-29"
        }'''
        obj = BankAccount.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = BankAccount.create(customerServiceNumber='123456', product=2, productId=2,
                                  hasDocuments=True, hasContracts=True, lastStatus=CreditStatus.PRE_APROVADO,
                                  dateCreated='29/12/2022', lastUpdated='29/12/2022')
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = BankAccount.create(customerServiceNumber='123456', product=2, productId=2,
                                  hasDocuments=True, hasContracts=True, lastStatus=CreditStatus.PRE_APROVADO,
                                  dateCreated='29/12/2022', lastUpdated='29/12/2022')
        json = orig.to_json()
        dest = BankAccount.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
