import unittest
from src.domains.VehicleBody import VehicleBody


class TestVehicleBody(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "vehicleBrand": "FIat",
            "vehicleModel": "Argo",
            "codeFipe": "007",
            "vehicleFipeValeu": "50000",
            "vehicleType": "1",
            "vehicleYear": "2022"
        }'''
        obj = VehicleBody.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = VehicleBody.create(vehicleBrand="FIat", vehicleModel="Argo", codeFipe="007", vehicleFipeValeu="50000",
                                  vehicleType="1", vehicleYear="2022")
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = VehicleBody.create(vehicleBrand="FIat", vehicleModel="Argo", codeFipe="007", vehicleFipeValeu="50000",
                                  vehicleType="1", vehicleYear="2022")
        json = orig.to_json()
        dest = VehicleBody.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
