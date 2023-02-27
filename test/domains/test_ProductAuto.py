import unittest
from src.domains.ProductAuto import ProductAuto


class TestProductAuto(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "type": "REFINANCING_AUTO",
            "value": 30000,
            "vehicleBrand": "Fiat",
            "vehicleModel": "Mobi",
            "installments": 12,
            "vehicleModelYear": "2010",
            "codeFipe": "038003-2",
            "vehicleFipeValue": 28000
        }'''
        obj = ProductAuto.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = ProductAuto.create(value=40000, vehicleBrand="Fiat",
                                  vehicleModel="Argo",
                                  installments=30, vehicleModelYear="2021", codeFipe="552211",
                                  vehicleFipeValue=50000)
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = ProductAuto.create(value=40000, vehicleBrand="Fiat",
                                  vehicleModel="Argo",
                                  installments=30, vehicleModelYear="2021", codeFipe="552211",
                                  vehicleFipeValue=50000)
        json = orig.to_json()
        dest = ProductAuto.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
