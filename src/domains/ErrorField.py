from src.domains.__Domain import Domain


class ErrorField(Domain):

    @classmethod
    def create(cls, field: str = None,
               message: str = None):
        obj = cls()
        obj.field = field
        obj.message = message
        return obj
