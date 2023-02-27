import unittest
from src.enums.Education import Education
from src.enums.Occupation import Occupation
from src.domains.SignupMatch import SignupMatch

class TestSignupMatch(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "cpf": "01204507800",
            "name":"Eduardo Silva",
            "birthday": "1992-07-25",
            "email": "fitbank@fitbank.com",
            "phone": "8599991234",
            "zipCode": "60000600",
            "education": "ENSINO_SUPERIOR_COMPLETO",
            "banks": "CaixaEconomica",
            "occupation": "EMPRESARIO",
            "income": "10000",
            "hasCredit_card": "True",
            "hasRestriction": "True",
            "hasOwnHouse": "True",
            "hasVehicle": "True",
            "hasAndroid": "True",
            "products": "Products",
            "logData": "LogData"
        }'''
        obj = SignupMatch.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = SignupMatch.create(cpf="01204507800", name="Eduardo Silva", birthday="1992-07-25",
                                  email="fitbank@fitbank.com", phone="8599991234",
                                  zipCode="60000600", education=Education.ENSINO_SUPERIOR_COMPLETO,
                                  banks="CaixaEconomica", occupation=Occupation.EMPRESARIO, income=10000,
                                  hasCreditCard=True, hasRestriction=True,
                                  hasOwnHouse=True, hasVehicle=True, hasAndroid=True)
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = SignupMatch.create(cpf="01204507800", name="Eduardo Silva", birthday="1992-07-25",
                                  email="fitbank@fitbank.com", phone="8599991234",
                                  zipCode="60000600", education=Education.ENSINO_SUPERIOR_COMPLETO,
                                  banks="CaixaEconomica", occupation=Occupation.EMPRESARIO, income=10000,
                                  hasCreditCard=True, hasRestriction=True,
                                  hasOwnHouse=True, hasVehicle=True, hasAndroid=True)
        json = orig.to_json()
        dest = SignupMatch.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
