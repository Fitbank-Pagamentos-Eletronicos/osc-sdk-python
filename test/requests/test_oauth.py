import unittest
from src.requests.OAuth import OAuth
import os
from dotenv import load_dotenv

load_dotenv()


class TestAuth(unittest.TestCase):

    def test_request_error(self):
        try:
            client_id = 'id'
            client_secret = 'secret'
            response = OAuth.request(client_id, client_secret)

            assert response.access_token is not None
            assert response.expire_at is not None
        except Exception as e:
            assert e.args[0] == '{"message":"User not found"}'

    def test_request_success(self):
        client_id = os.getenv('client_id')
        client_secret = os.getenv('client_secret')
        response = OAuth.request(client_id, client_secret)

        assert response.access_token is not None
        assert response.expire_at is not None
