import unittest
from src.domains.Error import Error


class TestError(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "code": "500",
            "message": "ErroServidor"
        }'''
        obj = Error.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = Error.create(code="500", message="ErroServidor")
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = Error.create(code="500", message="ErroServidor")
        json = orig.to_json()
        dest = Error.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
