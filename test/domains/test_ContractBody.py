import unittest
from src.domains.ContractBody import ContractBody


class TestContractBody(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "checksum": "Validador",
            "contract": "Contratos"
        }'''
        obj = ContractBody.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = ContractBody.create(checksum="Validador", contract="Contratos")
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = ContractBody.create(checksum="Validador", contract="Contratos")
        json = orig.to_json()
        dest = ContractBody.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
