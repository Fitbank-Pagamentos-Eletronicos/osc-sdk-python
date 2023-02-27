import unittest
from src.enums.RealEstateType import RealEstateType
from src.domains.ProductHome import ProductHome


class TestProductHome(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "type": "REFINANCING_HOME",
            "value": "50000",
            "installments": "40",
            "realEstateType": "HOUSE",
            "realEstateValue": "150000",
            "outstandingBalance": "0"
        }'''
        obj = ProductHome.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = ProductHome.create(value=50000, installments=40,
                                  realEstateType=RealEstateType.HOUSE, realEstateValue=150000,
                                  outstandingBalance=0)
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = ProductHome.create(value=50000, installments=40,
                                  realEstateType=RealEstateType.HOUSE, realEstateValue=150000,
                                  outstandingBalance=0)
        json = orig.to_json()
        dest = ProductHome.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
