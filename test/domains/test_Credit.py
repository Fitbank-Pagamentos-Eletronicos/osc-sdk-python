import unittest
from src.domains.Credit import Credit
from src.enums.ProductType import ProductType
from src.enums.CreditStatus import CreditStatus
from src.enums.PendentDocuments import PendentDocuments


class TestCredit(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "customerServiceNumber": "20190805062216",
            "type": "loan",
            "product": "EMPRÉSTIMO PESSOAL",
            "productId": 6215423,
            "hasDocuments": false,
            "hasContracts": true,
            "logo": "url",
            "lastStatus": "PRE_PROCESSAMENTO",
            "dateCreated": "2019-08-05T21:22:19Z",
            "lastUpdated": "2019-08-05T21:22:22Z",
            "value": 50000,
            "installments": 36,
            "pendentDocuments": [
                "SELF",
                "IDENTITY_FRONT",
                "IDENTITY_BACK",
                "ADDRESS_PROOF",
                "INCOME_PROOF"
            ],
            "monthlyTax": 0.059,
            "installmentsValue": 3490.77,
            "iofValue": 1652.59988,
            "grossValue": 51652.6,
            "firstPaymentDate": "2019-09-04T21:22:16Z",
            "cet": 1.052660058382551,
            "releasedDate": "2019-08-05T21:22:16Z"
        }'''
        obj = Credit.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = Credit.create(customerServiceNumber='123', type=ProductType.LOAN, product='emprestimo', productId=3,
                             hasDocuments=True, hasContracts=True, logo='logo', lastStatus=CreditStatus.PRE_APROVADO,
                             pendentDocuments=[
                                 PendentDocuments.SELF], dateCreated='2019-08-05T21:22:19Z',
                             lastUpdated='2019-08-05T21:22:22Z')
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = Credit.create(customerServiceNumber='123', type=ProductType.LOAN, product='emprestimo', productId=3,
                             hasDocuments=True, hasContracts=True, logo='logo', lastStatus=CreditStatus.PRE_APROVADO,
                             pendentDocuments=[
                                 PendentDocuments.SELF], dateCreated='29/12/2022',
                             lastUpdated='29/12/2022')
        json = orig.to_json()
        dest = Credit.from_json(json)
        self.assertEqual(orig.customerServiceNumber,
                         dest.customerServiceNumber)
