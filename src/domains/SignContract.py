from src.domains.__Domain import Domain


class SignContract(Domain):

    @classmethod
    def create(cls, aceptedCheckSum: str = None):
        obj = cls()
        obj.aceptedCheckSum = aceptedCheckSum
        return obj
