import unittest
from src.enums.Education import Education
from src.enums.Gender import Gender
from src.enums.Nationality import Nationality
from src.enums.RelationshipStatus import RelationshipStatus
from src.enums.State import State
from src.domains.Proposal import Proposal


class TestProposal(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "mother": "Fulana Mãe",
            "gender": "MASCULINO",
            "nationality": "BRASILEIRO",
            "hometownState": "GO",
            "hometown": "Goiânia",
            "education": "POS_GRADUACAO",
            "relationshipStatus": "CASADO",
            "phoneLandline": "6232345678",
            "identity": {
                "type": "RG",
                "number": "123456",
                "issuer": "SSP",
                "state": "GO",
                "issuingDate": "2010-01-01"
            },
            "address": {
                "zipCode": "74000000",
                "address": "Cidade de Goiânia",
                "number": 0,
                "complement": "toda a cidade",
                "district": "geral",
                "state": "GO",
                "city": "Goiânia",
                "homeType": "ALUGADA",
                "homeSince": "MAIOR_2_ANOS"
            },
            "vehicle": {
                "licensePlate": "XXX0000"
            },
            "consumerUnit": {
                "number": "000000000"
            },
            "business": {
                "occupation": "ASSALARIADO",
                "profession": "ADMINISTRADOR",
                "companyName": "Abobrinha",
                "phone": "6239413142",
                "income": 1500,
                "payday": 1,
                "employmentSince": "BETWEEN_ONE_AND_TWO_YEARS",
                "benefitNumber": "",
                "zipCode": "74000000",
                "address": "Cidade de Goiânia",
                "number": 1,
                "complement": "toda a cidade",
                "district": "geral",
                "state": "GO",
                "city": "Goiânia"
            },
            "bank": {
                "bank": "001",
                "type": "CONTA_CORRENTE_INDIVIDUAL",
                "agency": "0001",
                "account": "564789-1"
            },
            "reference": [
                {
                  "name": "Joana Maria",
                  "phone": "11987654321"
                }
            ],
            "products": [
            {
              "type": "LOAN",
              "value": "7000",
              "installments": 12
            },
            {
              "type": "CARD",
              "network": "MASTERCARD",
              "payDay": 15
            },
            {
              "type": "WORKING_CAPITAL",
              "installments": 12,
              "value": 7000.65,
              "cnpj": "12.000.256/0001-88",
              "businessProfession": "ADMINISTRADOR_DIRETOR",
              "employeesCount": "MAIS_DE_10",
              "businessIncomeCnpj": 15000,
              "loanObjectives": "EXPANSAO_DE_NEGOCIOS",
              "bank": "001",
              "accountType": "CONTA_CORRENTE_INDIVIDUAL",
              "agency": "0001",
              "account": "1234657-8"
            },
            {
              "type": "REFINANCING_AUTO",
              "value": "30000",
              "vehicleBrand": "Fiat",
              "vehicleModel": "Mobi",
              "installments": 12,
              "vehicleModelYear": "2010",
              "codeFipe": "038003-2",
              "vehicleFipeValue": "28000"
            },
            {
              "type": "REFINANCING_HOME",
              "value": "150000",
              "installments": 12,
              "realEstateType": "house",
              "realEstateValue": "148000",
              "outstandingBalance": "50000"
            }
            ]
        }'''
        obj = Proposal.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = Proposal.create(mother="Maria Silva", gender=Gender.MASCULINO, nationality=Nationality.BRASILEIRO,
                               hometownState=State.CE, hometown="Fortaleza", education=Education.POS_GRADUACAO,
                               relationshipStatus=RelationshipStatus.CASADO)
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = Proposal.create(mother="Maria Silva", gender=Gender.MASCULINO, nationality=Nationality.BRASILEIRO,
                               hometownState=State.CE, hometown="Fortaleza", education=Education.POS_GRADUACAO,
                               relationshipStatus=RelationshipStatus.CASADO)
        json = orig.to_json()
        dest = Proposal.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
