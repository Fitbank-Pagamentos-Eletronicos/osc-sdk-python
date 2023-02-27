from src.domains.__Domain import Domain


class BorrowerInfo(Domain):

    @classmethod
    def create(cls, isRegistered: bool = None,
               isBlocked: bool = None):
        obj = cls()
        obj.isRegistered = isRegistered
        obj.isBlocked = isBlocked
        return obj
