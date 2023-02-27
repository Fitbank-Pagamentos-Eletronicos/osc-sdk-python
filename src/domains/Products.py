from src.domains.__Domain import Domain
from src.enums.ProductType import ProductType


class Products(Domain):

    @classmethod
    def create(cls, type: ProductType = None):
        obj = cls()
        obj.type = type
        return obj
