import unittest
from src.domains.AddressSimpleBody import AddressSimpleBody
from src.enums.State import State


class TestAddressSimpleBody(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "zipCode": "74000000",
            "address": "Cidade de Goiânia",
            "number": 0,
            "complement": "toda a cidade",
            "district": "geral",
            "state": "GO",
            "city": "Goiânia"
        }'''
        obj = AddressSimpleBody.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = AddressSimpleBody.create(zipCode='74000000', address='Cidade de Goiânia', number='0',
                                        complement='toda a cidade', district='geral', state=State.GO, city='Goiânia')
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = AddressSimpleBody.create(zipCode='74000000', address='Cidade de Goiânia', number='0',
                                        complement='toda a cidade', district='geral', state=State.GO, city='Goiânia')
        json = orig.to_json()
        dest = AddressSimpleBody.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
