from src.domains.__Domain import Domain


class Reference(Domain):

    @classmethod
    def create(cls, name: str = None,
               phone: str = None):
        obj = cls()
        obj.name = name
        obj.phone = phone
        return obj
