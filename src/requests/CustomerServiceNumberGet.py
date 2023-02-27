import requests
import os
from src.domains.Pipeline import Pipeline

from src.main import Osc


class CustomerServiceNumber:

    @staticmethod
    def request(osc: Osc) -> Pipeline:
        server_url_demo = os.getenv('server_url_demo')

        token = osc.get_token()
        headers = {
            'Content-Type': 'application/json',
            'Acccept': 'aplication/json',
            'Authorization': f'Bearer {token}'
        }

        response = requests.get(
            f'{server_url_demo}/v2.1/contract/20221109182327351003700', headers=headers)

        return Pipeline.from_json(response.text)
