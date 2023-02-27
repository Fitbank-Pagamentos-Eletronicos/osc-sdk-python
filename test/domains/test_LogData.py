import unittest
from datetime import datetime

from src.domains.LogData import LogData


class TestLogData(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "latitude": -16.6982283,
            "longitude": -49.2581201,
            "occurrenceDate": "2019-08-21T14:31:17.459Z",
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ...",
            "ip": "0.0.0.0",
            "mac": "00:00:00:00:00:00"
        }'''
        obj = LogData.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = LogData.create(latitude=-16, longitude=-48, occurrenceDate=datetime.now(), userAgent="www",
                              ip="001.122.000.111", mac="123456")
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = LogData.create(latitude=-16, longitude=-48, occurrenceDate=datetime.now(), userAgent="www",
                              ip="001.122.000.111", mac="123456")
        json = orig.to_json()
        dest = LogData.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
