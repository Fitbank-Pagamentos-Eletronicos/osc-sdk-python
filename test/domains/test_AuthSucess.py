import unittest
from datetime import datetime
from src.domains.AuthSucess import AuthSucess


class TestAuthSucess(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "access_token": "...",
            "expire_at": "..."
        }'''
        obj = AuthSucess.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = AuthSucess.create(
            access_token='...', expire_at=datetime.now())
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = AuthSucess.create(
            access_token='...', expire_at=datetime.now())
        json = orig.to_json()
        dest = AuthSucess.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
