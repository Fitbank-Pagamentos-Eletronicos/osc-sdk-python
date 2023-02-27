import unittest
from src.domains.Business import Business
from src.enums.EmploymentSince import EmploymentSince
from src.enums.Occupation import Occupation
from src.enums.Profession import Profession
from src.enums.State import State


class TestBusiness(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "occupation": "ASSALARIADO",
            "profession": "ADMINISTRADOR",
            "companyName": "Abobrinha",
            "phone": "6239413142",
            "income": 1500,
            "employmentSince": "BETWEEN_ONE_AND_TWO_YEARS",
            "payday": 1,
            "benefitNumber": "",
            "zipCode": "74000000",
            "address": "Cidade de Goiânia",
            "number": 1,
            "complement": "toda a cidade",
            "district": "geral",
            "state": "GO",
            "city": "Goiânia"
        }'''
        obj = Business.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = Business.create(occupation=Occupation.ASSALARIADO, profession=Profession.ADMINISTRADOR,
                               companyName='Abobrinha', phone='6239413142', income=1500,
                               employmentSince=EmploymentSince.BETWEEN_FOUR_AND_FIVE_YEARS, payday=1,
                               benefitNumber='', zipCode='74000000', address='Cidade de Goiânia', number=1,
                               complement='toda a cidade', district='geral', state=State.GO, city='Goiânia')
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = Business.create(occupation=Occupation.ASSALARIADO, profession=Profession.ADMINISTRADOR,
                               companyName='Abobrinha', phone='6239413142', income=1500,
                               employmentSince=EmploymentSince.BETWEEN_FOUR_AND_FIVE_YEARS, payday=1,
                               benefitNumber='', zipCode='74000000', address='Cidade de Goiânia', number=1,
                               complement='toda a cidade', district='geral', state=State.GO, city='Goiânia')
        json = orig.to_json()
        dest = Business.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
