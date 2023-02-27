from src.domains.Products import Products
from src.enums.Network import Network
from src.enums.ProductType import ProductType


class ProductCard(Products):

    def __init__(self):
        self.type = ProductType.CARD

    @classmethod
    def create(cls, network: Network = None,
               payDay: str = None):
        obj = cls()
        obj.network = network
        obj.payDay = payDay
        return obj
