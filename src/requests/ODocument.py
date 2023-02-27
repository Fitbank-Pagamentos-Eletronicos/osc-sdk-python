import requests
import os
from dotenv import load_dotenv

from src.domains.Pipeline import Pipeline
from src.domains.Document import Document
from src.main import Osc

load_dotenv()


class ODocument:

    @staticmethod
    def document(token: str, pipeline_id: str, document: Document) -> Pipeline:
        server_url = os.getenv('server_url')

        payload = document.to_json()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }

        response = requests.put(
            f'{server_url}/v2/process/document/{pipeline_id}', headers=headers, data=payload)

        return Pipeline.from_json(response.text)
