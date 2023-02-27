from src.domains.Products import Products
from src.enums.ProductType import ProductType


class ProductBankAccount(Products):

    def __init__(self):
        self.type = ProductType.BANK_ACCOUNT

    @classmethod
    def create(cls):
        obj = cls()
        return obj
