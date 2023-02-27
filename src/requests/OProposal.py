import requests
import os
from dotenv import load_dotenv
from domains.ProposalBankAccount import ProposalBankAccount

from src.domains.Pipeline import Pipeline
from src.domains.Proposal import Proposal
from src.main import Osc

load_dotenv()


class OProposal:

    @staticmethod
    def proposal(token: str, pipeline_id: str, proposal: Proposal) -> Pipeline:
        server_url = os.getenv('server_url')

        payload = proposal.to_json()
        headers = {
            'Content-Type': 'application/json',
            'Acccept': 'aplication/json',
            'Authorization': f'Bearer {token}'
        }

        response = requests.post(
            f'{server_url}/v2.1/process/proposal/{pipeline_id}', headers=headers, data=payload)

        return Pipeline.from_json(response.text)

    @staticmethod
    def simple_proposal(token: str, pipeline_id: str, proposal: ProposalBankAccount) -> Pipeline:
        server_url = os.getenv('server_url')

        payload = proposal.to_json()
        headers = {
            'Content-Type': 'application/json',
            'Acccept': 'aplication/json',
            'Authorization': f'Bearer {token}'
        }

        response = requests.post(
            f'{server_url}/v2.1/process/simple_proposal/{pipeline_id}', headers=headers, data=payload)

        return Pipeline.from_json(response.text)
