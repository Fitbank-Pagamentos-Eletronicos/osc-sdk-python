import requests
import os
from dotenv import load_dotenv

from src.domains.Pipeline import Pipeline
from src.domains.Contract import Contract
from src.main import Osc

load_dotenv()


class OContract:

    @staticmethod
    def get(token: str, customerServiceNumber: str) -> Pipeline:
        server_url = os.getenv('server_url')

        headers = {
            'Content-Type': 'application/json',
            'Acccept': 'aplication/json',
            'Authorization': f'Bearer {token}'
        }

        response = requests.get(
            f'{server_url}/v2.1/contract/{customerServiceNumber}', headers=headers)

        return Pipeline.from_json(response.text)

    @staticmethod
    def sign(token: str, customerServiceNumber: str, post_contract: Contract) -> Pipeline:
        server_url = os.getenv('server_url')

        payload = post_contract.to_json()
        headers = {
            'Content-Type': 'application/json',
            'Acccept': 'aplication/json',
            'Authorization': f'Bearer {token}'
        }

        response = requests.post(
            f'{server_url}/v2.1/contract/{customerServiceNumber}', headers=headers, data=payload)

        return Pipeline.from_json(response.text)
