import os
from src.domains import domains
from src.main import Osc


class SignupProposalExemplo():
    client_id = os.getenv("client_id")
    client_secret = os.getenv("client_secret")

    osc = Osc.create_instance(client_id, client_secret)
