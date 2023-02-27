import unittest
from src.domains.Address import Address
from src.enums.HomeSince import HomeSince
from src.enums.HomeType import HomeType
from src.enums.State import State


class TestAddress(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "zipCode": "74000000",
            "address": "Cidade de Goiânia",
            "number": 0,
            "complement": "toda a cidade",
            "district": "geral",
            "state": "GO",
            "city": "Goiânia",
            "homeType": "ALUGADA",
            "homeSince": "MAIOR_2_ANOS"
        }'''
        obj = Address.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = Address.create(zipCode='74000000', address='Cidade de Goiânia', number='0', complement='toda a cidade',
                              district='geral', state=State.GO, city='Goiânia', homeType=HomeType.ALUGADA,
                              homeSince=HomeSince.MAIOR_2_ANOS)
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = Address.create(zipCode='74000000', address='Cidade de Goiânia', number='0', complement='toda a cidade',
                              district='geral', state=State.GO, city='Goiânia', homeType=HomeType.ALUGADA,
                              homeSince=HomeSince.MAIOR_2_ANOS)
        json = orig.to_json()
        dest = Address.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
