from src.domains.__Domain import Domain
from src.enums.CreditStatus import CreditStatus


class BankAccount(Domain):

    @classmethod
    def create(cls, customerServiceNumber: str = None,
               product: int = None,
               productId: int = None,
               hasDocuments: bool = None,
               hasContracts: bool = None,
               lastStatus: CreditStatus = None,
               dateCreated: str = None,
               lastUpdated: str = None):
        obj = cls()
        obj.customerServiceNumber = customerServiceNumber
        obj.product = product
        obj.productId = productId
        obj.hasDocuments = hasDocuments
        obj.hasContracts = hasContracts
        obj.lastStatus = lastStatus
        obj.dateCreated = dateCreated
        obj.lastUpdated = lastUpdated
        return obj
