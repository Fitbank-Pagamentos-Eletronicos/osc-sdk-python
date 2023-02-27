import unittest
from datetime import datetime
from src.domains.LogData import LogData
from src.domains.Contract import Contract


class TestContract(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "aceptedCheckSum": "Contratos",
            "logData": {
                "latitude": -16.6982283,
                "longitude": -49.2581201,
                "occurrenceDate": "",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ...",
                "ip": "0.0.0.0",
                "mac": "00:00:00:00:00:00"
            }
        }'''
        obj = Contract.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        logData = LogData.create(latitude=-16.6982283, longitude=-49.2581201, occurrenceDate=datetime.now(),
                                 userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ...",
                                 ip="0.0.0.0", mac="00:00:00:00:00:00")
        orig = Contract.create(aceptedCheckSum="Contratos", logData=logData)
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        logData = LogData.create(latitude=-16.6982283, longitude=-49.2581201, occurrenceDate=datetime.now(),
                                 userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ...",
                                 ip="0.0.0.0", mac="00:00:00:00:00:00")
        orig = Contract.create(aceptedCheckSum="Contratos", logData=logData)
        json = orig.to_json()
        dest = Contract.from_json(json)
        self.assertEqual(orig.aceptedCheckSum, dest.aceptedCheckSum)
