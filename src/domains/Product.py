from src.domains.__Domain import Domain


class Product(Domain):

    @classmethod
    def create(cls, productId: int = None,
               name: str = None,
               logo: str = None):
        obj = cls()
        obj.productId = productId
        obj.name = name
        obj.logo = logo
        return obj
