import unittest
from src.domains.Pipeline import Pipeline

class TestPipeline(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "id": "20190805062216",
            "status": "PROPOSAL_CREATED",
            "cpf": 191,
            "name": "Fulano d'Tal",
            "dateCreated": "2020-10-28T13:50:21.024Z",
            "lastUpdated": "2020-10-28T13:50:21.024Z",
            "proposals": [
                {
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
                    "monthlyTax": 0.059,
                    "installmentsValue": 3490.77,
                    "iofValue": 1652.59988,
                    "grossValue": 51652.6,
                    "firstPaymentDate": "2019-09-04T21:22:16Z",
                    "cet": 1.052660058382551,
                    "releasedDate": "2019-08-05T21:22:16Z"
                },
                {
                    "customerServiceNumber": "20190805062221",
                    "type": "card",
                    "product": "Cartão de Crédito - Visa Platinum",
                    "productId": 3412351,
                    "hasDocuments": false,
                    "hasContracts": false,
                    "logo": "url",
                    "lastStatus": "PRE_PROCESSAMENTO",
                    "dateCreated": "2019-08-05T21:22:21Z",
                    "lastUpdated": "2019-08-05T21:22:22Z",
                    "international": false,
                    "annuity": 499.92,
                    "network": "VISA",
                    "prepaid": false,
                    "digitalAccount": false
                }
            ]
        }'''
        obj = Pipeline.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = Pipeline.create(id="1234", status="Aprovado", cpf=11234567809, name="Thiago Sales",
                               dateCreated="2022-12-30", lastUpdated="2022-12-30",
                               matches=[], proposals=[])
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = Pipeline.create(id="1234", status="Aprovado", cpf=11234567809, name="Thiago Sales",
                               dateCreated="2022-12-30", lastUpdated="2022-12-30",
                               matches=[], proposals=[])
        json = orig.to_json()
        dest = Pipeline.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
