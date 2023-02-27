from src.domains.__Domain import Domain
from src.domains.Credit import Credit
from src.domains.Matches import Match


class Pipeline(Domain):

    # noinspection PyPep8Naming
    def __init__(self):
        self.id = None
        self.status = None
        self.cpf = None
        self.name = None
        self.dateCreated = None
        self.lastUpdated = None
        self.match = None
        self.proposals = None

    @classmethod
    def create(cls, id: str = None,
               status: str = None,
               cpf: int = None,
               name: str = None,
               dateCreated: str = None,
               lastUpdated: str = None,
               matches: list[Match] = None,
               proposals: list[Credit] = None):
        obj = cls()
        obj.id = id
        obj.status = status
        obj.cpf = cpf
        obj.name = name
        obj.dateCreated = dateCreated
        obj.lastUpdated = lastUpdated
        obj.matches = matches
        obj.proposals = proposals
        return obj
