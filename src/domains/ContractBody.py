from src.domains.__Domain import Domain


class ContractBody(Domain):

    @classmethod
    def create(cls, checksum: str = None,
               contract: str = None):
        obj = cls()
        obj.checksum = checksum
        obj.contract = contract
        return obj
