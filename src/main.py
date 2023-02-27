import unicodedata
from datetime import datetime

from src.domains import Contract
from src.domains.Document import Document
from src.domains.Pipeline import Pipeline
from src.domains.Proposal import Proposal
from src.domains.ProposalBankAccount import ProposalBankAccount
from src.domains.SignupMatch import SignupMatch
from src.domains.SimpleSignup import SimpleSignup
from src.requests.ODocument import ODocument
from src.requests.OProposal import OProposal
from src.requests.PubSub import PubSub
from src.requests.OAuth import OAuth
from src.requests.OContract import OContract
from src.domains.AuthSucess import AuthSucess
from typing import TypeVar, Callable

from src.requests.Signup import Signup

T = TypeVar('T', bound='Osc')


class Osc:
    intances = {}
    default_instance_name = "default"

    def __init__(self, name, client_id, client_secret) -> None:
        self.__name = self.get_instance(name)
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__token = None
        self.__expire_at = None

    @staticmethod
    def normalize(name: str) -> str:
        return unicodedata.normalize("NFD", name.lower()).encode("ascii", "ignore").decode("utf-8").replace(" ", "")

    @classmethod
    def create_instance(cls, client_id, client_secret, name=default_instance_name) -> T:

        instance = cls.get_instance(name)

        if instance is not None:
            if instance.client_id != client_id or instance.client_secret != client_secret:
                raise NameError(f'Instance named {name} already exist')

            return instance

        instance = cls(name, client_id, client_secret)
        normalized = cls.normalize(name)
        cls.intances[normalized] = instance
        return instance

    @classmethod
    def get_instance(cls, name=default_instance_name) -> T:
        normalized = cls.normalize(name)
        return cls.intances.get(normalized)

    def get_token(self) -> str:
        if self.__token is None or self.__expire_at < datetime.now():
            self.new_token()
        return self.__token

    def new_token(self) -> None:
        resp = self.auth()
        self.__token = resp.access_token
        self.__expire_at = resp.expire_at

    def auth(self) -> AuthSucess:
        return OAuth.request(self.__client_id, self.__client_secret)

    def set_response_listening(self, listening_function: Callable[[Pipeline], None]) -> bool:
        config = PubSub.get_config(self.get_token())
        return PubSub.subscribe(config.project_id, config.topic_id, config.subscription_id,
                                config.service_account, listening_function)

    def signupMatch(self, data: SignupMatch) -> Pipeline:
        return Signup.signupMatch(self.get_token(), data)

    def simpleSignup(self, data: SimpleSignup) -> Pipeline:
        return Signup.simpleSignup(self.get_token(), data)

    def getContracts(self, customerServiceNumber) -> Pipeline:
        return OContract.get(self.get_token(), customerServiceNumber)

    def signContracts(self, customerServiceNumber, post_contract: Contract) -> Pipeline:
        return OContract.sign(self.get_token(), customerServiceNumber, post_contract)

    def proposal(self, pipeline_id, proposal: Proposal) -> Pipeline:
        return OProposal.proposal(self.get_token(), pipeline_id, proposal)

    def simpleProposal(self, pipeline_id, proposal: ProposalBankAccount) -> Pipeline:
        return OProposal.simple_proposal(self.get_token(), pipeline_id, proposal)

    def document(self, pipeline_id, document: Document) -> Pipeline:
        return ODocument.document(self.get_token(), pipeline_id, document)
