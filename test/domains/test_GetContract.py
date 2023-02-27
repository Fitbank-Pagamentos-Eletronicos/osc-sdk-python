import unittest
from src.domains.GetContract import GetContract
from src.domains.ContractBody import ContractBody


class TestGetContract(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "customerServiceNumber": "123456",
            "contracts": [{
                "checksum": "Validador",
                "contract": "Contratos"
            }]
        }'''
        obj = GetContract.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        contract_body = ContractBody.create(checksum="Validador", contract="Contratos")
        orig = GetContract.create(customerServiceNumber="123456", contracts=contract_body)
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        contract_body = ContractBody.create(checksum="Validador", contract="Contratos")
        orig = GetContract.create(customerServiceNumber="123456", contracts=[contract_body])
        json = orig.to_json()
        dest = GetContract.from_json(json)
        self.assertEqual(orig.customerServiceNumber, dest.customerServiceNumber)
