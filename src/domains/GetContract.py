from src.domains.__Domain import Domain
from src.domains.ContractBody import ContractBody


class GetContract(Domain):

    @classmethod
    def create(cls, customerServiceNumber: str = None,
               contracts: list[ContractBody] = None):
        obj = cls()
        obj.customerServiceNumber = customerServiceNumber
        obj.contracts = contracts
        return obj
