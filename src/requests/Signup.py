import requests
import os
from dotenv import load_dotenv

from src.domains.Pipeline import Pipeline
from src.domains.SignupMatch import SignupMatch
from src.domains.SimpleSignup import SimpleSignup

load_dotenv()


# noinspection DuplicatedCode
class Signup:

    @staticmethod
    def signupMatch(token: str, signup: SignupMatch) -> Pipeline:
        server_url = os.getenv('server_url')

        payload = signup.to_json()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }

        response = requests.post(
            f'{server_url}/v2.1/process/signup', headers=headers, data=payload)

        if response.status_code != 201:
            raise Exception(response.text)

        return Pipeline.from_json(response.text)

    @staticmethod
    def simpleSignup(token: str, signup: SimpleSignup) -> Pipeline:
        server_url = os.getenv('server_url')

        payload = signup.to_json()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }

        response = requests.post(
            f'{server_url}/v2.1/process/simple_signup', headers=headers, data=payload)

        if response.status_code != 201:
            raise Exception(response.text)

        return Pipeline.from_json(response.text)
