from src.domains.Products import Products
from src.enums.ProductType import ProductType
from src.enums.RealEstateType import RealEstateType


class ProductHome(Products):

    def __init__(self):
        self.type = ProductType.REFINANCING_HOME

    @classmethod
    def create(cls, value: float = None,
               installments: int = None,
               realEstateType: RealEstateType = None,
               realEstateValue: float = None,
               outstandingBalance: float = None):
        obj = cls()
        obj.value = value
        obj.installments = installments
        obj.realEstateType = realEstateType
        obj.realEstateValue = realEstateValue
        obj.outstandingBalance = outstandingBalance
        return obj
