from src.domains.__Domain import Domain


class Error(Domain):

    @classmethod
    def create(cls, code: str = None,
               message: str = None):
        obj = cls()
        obj.code = code
        obj.message = message
        return obj
