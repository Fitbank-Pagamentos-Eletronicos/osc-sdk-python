import unittest
from src.domains.Vehicle import Vehicle


class TestVehicle(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "license_plate": "HXC0918"
        }'''
        obj = Vehicle.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = Vehicle.create(licensePlate="HXC0918")
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = Vehicle.create(licensePlate="HXC0918")
        json = orig.to_json()
        dest = Vehicle.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
