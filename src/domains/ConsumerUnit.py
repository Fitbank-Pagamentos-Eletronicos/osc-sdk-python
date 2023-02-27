from src.domains.__Domain import Domain


class ConsumerUnit(Domain):

    @classmethod
    def create(cls, number: str = None):
        obj = cls()
        obj.number = number
        return obj
