import unittest
from src.domains.Fipe import Fipe
from src.domains.VehicleBody import VehicleBody


class TestFipe(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "lastUpdate": "2022-10-04",
            "vehicles": [
                {
                    "vehicleBrand": "VW - VolksWagen",
                    "vehicleModel": "Nivus Comfortline 1.0 200 TSI Flex",
                    "codeFipe": "005525-5",
                    "vehicleFipeValue": "114521",
                    "vehicleType": 1,
                    "vehicleYear": "2022"
                },
                {
                    "vehicleBrand": "YAMAHA",
                    "vehicleModel": "MT-09 850cc/ABS",
                    "codeFipe": "827094-5",
                    "vehicleFipeValue": "57854",
                    "vehicleType": 2,
                    "vehicleYear": "1991"
                }
                ]
        }'''
        obj = Fipe.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        vehicle_body = VehicleBody.create(vehicleBrand="Fiat", vehicleModel="Argo", codeFipe="789456",
                                          vehicleFipeValeu="40000", vehicleType="Automóvel", vehicleYear="2022")
        orig = Fipe.create(lastUpdate="2022-01-11", vehicle=vehicle_body)
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        vehicle_body = VehicleBody.create(vehicleBrand="Fiat", vehicleModel="Argo", codeFipe="789456",
                                          vehicleFipeValeu="40000", vehicleType="Automóvel", vehicleYear="2022")
        orig = Fipe.create(lastUpdate="2022-01-11", vehicle=vehicle_body)
        json = orig.to_json()
        dest = Fipe.from_json(json)
        self.assertEqual(orig.lastUpdate, dest.lastUpdate)
