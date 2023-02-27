from src.domains.__Domain import Domain
from src.enums.AccountType import AccountType


class Bank(Domain):

    @classmethod
    def create(cls, bank: str = None,
               type: AccountType = None,
               agency: str = None,
               account: str = None):
        obj = cls()
        obj.bank = bank
        obj.type = type
        obj.agency = agency
        obj.account = account
        return obj
