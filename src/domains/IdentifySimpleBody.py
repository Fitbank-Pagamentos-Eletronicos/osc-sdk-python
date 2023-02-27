from src.domains.__Domain import Domain
from src.enums.IdentityType import IdentityType


class IdentifySimpleBody(Domain):

    @classmethod
    def create(cls, type: IdentityType = None,
               number: str = None):
        obj = cls()
        obj.type = type
        obj.number = number
        return obj
