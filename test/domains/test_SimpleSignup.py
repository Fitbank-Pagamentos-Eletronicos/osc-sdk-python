import unittest
from src.domains.SimpleSignup import SimpleSignup

# noinspection DuplicatedCode
class TestSimpleSignup(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "cpf": "00000000191",
            "name": "Fulano d'Tal",
            "birthday": "1992-07-25",
            "email": "fulano@email.com",
            "phone": "62987654321",
            "zipCode": "74180040",
            "hasCreditCard": true,
            "hasRestriction": true,
            "hasOwnHouse": true,
            "hasVehicle": true,
            "hasAndroid": true,
            "logData": {
                "latitude": -16.6982283,
                "longitude": -49.2581201,
                "occurrenceDate": "2019-08-21T14:31:17.459Z",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ...",
                "ip": "0.0.0.0",
                "mac": "00:00:00:00:00:00"
            }
        }'''
        obj = SimpleSignup.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = SimpleSignup.create(cpf="00000000191", name="Fulano d'Tal", birthday="1992-07-25",
                                   email="fulano@email.com", phone="62987654321",
                                   zipCode="74180040", hasCreditCard=True, hasRestriction=True,
                                   hasOwnHouse=True, hasVehicle=True, hasAndroid=True)
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = SimpleSignup.create(cpf="00000000191", name="Fulano d'Tal", birthday="1992-07-25",
                                   email="fulano@email.com", phone="62987654321",
                                   zipCode="74180040", hasCreditCard=True, hasRestriction=True,
                                   hasOwnHouse=True, hasVehicle=True, hasAndroid=True)
        json = orig.to_json()
        dest = SimpleSignup.from_json(json)
        self.assertEquals(orig.__dict__, dest.__dict__)
