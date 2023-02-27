from src.domains.__Domain import Domain
from src.enums.Occupation import Occupation


class BusinessSimpleBody(Domain):

    @classmethod
    def create(cls, occupation: Occupation = None,
               income: str = None):
        obj = cls()
        obj.occupation = occupation
        obj.income = income
        return obj
