from src.domains.Products import Products
from src.enums.ProductType import ProductType


class ProductLoan(Products):

    def __init__(self):
        self.type = ProductType.LOAN

    @classmethod
    def create(cls, value: float = None,
               installments: int = None):
        obj = cls()
        obj.value = value
        obj.installments = installments
        return obj
