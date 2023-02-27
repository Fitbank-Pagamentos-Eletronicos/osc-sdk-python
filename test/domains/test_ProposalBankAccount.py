import unittest
from src.domains.IdentifySimpleBody import IdentifySimpleBody
from src.domains.AddressSimpleBody import AddressSimpleBody
from src.domains.BusinessSimpleBody import BusinessSimpleBody
from src.domains.ProductBankAccount import ProductBankAccount
from src.domains.ProposalBankAccount import ProposalBankAccount
from src.enums.Occupation import Occupation
from src.enums.IdentityType import IdentityType
from src.enums.Gender import Gender
from src.enums.Nationality import Nationality
from src.enums.RelationshipStatus import RelationshipStatus
from src.enums.State import State


class TestProposalBankAccount(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "mother": "Fulana Mãe",
            "gender": "MASCULINO",
            "nationality": "BRASILEIRO",
            "hometownState": "GO",
            "relationshipStatus": "CASADO",
            "identity": {
                "type": "RG",
                "number": "123456"
            },
            "address": {
                "zipCode": "74000000",
                "address": "Cidade de Goiânia",
                "number": 0,
                "complement": "toda a cidade",
                "district": "geral",
                "state": "GO",
                "city": "Goiânia"
            },
            "business": {
                "occupation": "ASSALARIADO",
                "income": 1500
            },
            "products": [
                {
                    "type": "BANK_ACCOUNT"
                }
            ]
        }'''
        obj = ProposalBankAccount.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        identify_simple_body = IdentifySimpleBody.create(type=IdentityType.RG, number="99999999999")
        address_simple_body = AddressSimpleBody.create(zipCode="60320560", address="Rua da Bala", number="171",
                                                       complement="apto 007", district="Pirambu", state=State.CE,
                                                       city="Fortaleza")
        business_simple_body = BusinessSimpleBody.create(occupation=Occupation.APONSETADO, income="9000")
        product_bank_account = ProductBankAccount.create()
        orig = ProposalBankAccount.create(mother="Maria Silva", gender=Gender.FEMININO,
                                          nationality=Nationality.BRASILEIRO, hometownState=State.CE,
                                          relationshipStatus=RelationshipStatus.CASADO, identity=identify_simple_body,
                                          address=address_simple_body, business=business_simple_body,
                                          products=product_bank_account)
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = ProposalBankAccount.create(mother="Maria Silva", gender=Gender.FEMININO,
                                          nationality=Nationality.BRASILEIRO, hometownState=State.CE,
                                          relationshipStatus=RelationshipStatus.CASADO)
        json = orig.to_json()
        dest = ProposalBankAccount.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
