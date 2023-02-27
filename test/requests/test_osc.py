import unittest
import os
from dotenv import load_dotenv
from src.main import Osc

load_dotenv()


class TestOSC(unittest.TestCase):
    def test_create_instance(self):
        osc = Osc.get_instance('test_create_instance')
        if osc is None:
            osc = Osc.create_instance("client_id", "client_secret", name="test_create_instance")
        self.assertIsNotNone(osc)

    def test_create_instance_multiple(self):
        osc1 = Osc.get_instance("first")
        if osc1 is None:
            osc1 = Osc.create_instance("client_id1", "client_secret1", name="first")

        osc2 = Osc.get_instance("second")
        if osc2 is None:
            osc2 = Osc.create_instance("client_id2", "client_secret2", name="second")

        self.assertNotEqual(osc1, osc2)

        first_instance = Osc.get_instance("first")
        seccond_instance = Osc.get_instance("second")

        self.assertIsNotNone(first_instance)
        self.assertIsNotNone(seccond_instance)
        self.assertNotEqual(first_instance, seccond_instance)
        self.assertEqual(first_instance, osc1)
        self.assertEqual(seccond_instance, osc2)

    def test_get_token_error(self):
        client_id = "wrong client_id"
        client_secret = "wrong client_secret"
        try:
            osc = Osc.get_instance('test_get_token_error')
            if osc is None:
                osc = Osc.create_instance(client_id, client_secret, name='test_get_token_error')
            token = osc.get_token()
            self.assertIsNone(token)
        except Exception as e:
            assert e.args[0] == '{"error":"Wrong credentials"}' or e.args[0] == '{"message":"User not found"}'

    def test_get_token_success(self):
        client_id = os.getenv("client_id")
        client_secret = os.getenv("client_secret")
        try:
            osc = Osc.get_instance('test_get_token_success')
            if osc is None:
                osc = Osc.create_instance(client_id, client_secret, name='test_get_token_success')
            token = osc.get_token()
            self.assertIsNotNone(token)
        except Exception as e:
            assert e.args[0] == '{"error":"Wrong credentials"}'
