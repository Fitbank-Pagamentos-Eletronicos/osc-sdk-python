import unittest
from src.domains.Identity import Identity
from src.enums.IdentityIssuer import IdentityIssuer
from src.enums.IdentityType import IdentityType
from src.enums.State import State


class TestIdentity(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "type": "RG",
            "number": "123456",
            "issuer": "SSP",
            "state": "GO",
            "issuingDate": "2010-01-01"
        }'''
        obj = Identity.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = Identity.create(type=IdentityType.CNH, number='123456', issuer=IdentityIssuer.DETRA, state=State.CE,
                               issuingDate='2010-01-01')
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = Identity.create(type=IdentityType.CNH, number='123456', issuer=IdentityIssuer.DETRA, state=State.CE,
                               issuingDate='2010-01-01')
        json = orig.to_json()
        dest = Identity.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
