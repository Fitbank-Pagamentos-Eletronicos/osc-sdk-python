from src.domains.AuthSucess import AuthSucess
import requests
import os
from dotenv import load_dotenv

load_dotenv()


class OAuth:

    @staticmethod
    def request(client_id: str, client_secret: str) -> AuthSucess:
        auth_server_url = os.getenv('auth_server_url')

        token_req_payload = {'grant_type': 'client_credentials', 'scope': 'api-external'}

        response = requests.post(auth_server_url, data=token_req_payload, auth=(client_id, client_secret))

        if response.status_code != 200:
            raise Exception(response.text)

        return AuthSucess.from_json(response.text)
