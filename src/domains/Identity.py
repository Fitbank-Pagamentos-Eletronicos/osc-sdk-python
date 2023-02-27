from src.domains.__Domain import Domain
from src.enums.IdentityIssuer import IdentityIssuer
from src.enums.IdentityType import IdentityType
from src.enums.State import State


class Identity(Domain):

    @classmethod
    def create(cls, type: IdentityType = None,
               number: str = None,
               issuer: IdentityIssuer = None,
               state: State = None,
               issuingDate: str = None):
        obj = cls()
        obj.type = type
        obj.number = number
        obj.issuer = issuer
        obj.state = state
        obj.issuingDate = issuingDate
        return obj
