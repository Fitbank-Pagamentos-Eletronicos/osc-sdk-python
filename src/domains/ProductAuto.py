from src.domains.Products import Products
from src.enums.ProductType import ProductType


class ProductAuto(Products):

    def __init__(self):
        self.type = ProductType.REFINANCING_AUTO
        self.vehicleBrand = None
        self.vehicleModelYear = None
        self.vehicleModelYear = None

    @classmethod
    def create(cls, value: float = None,
               vehicleBrand: str = None,
               vehicleModel: str = None,
               installments: int = None,
               vehicleModelYear: str = None,
               codeFipe: str = None,
               vehicleFipeValue: float = None):
        obj = cls()
        obj.value = value
        obj.vehicleBrand = vehicleBrand
        obj.vehicleModel = vehicleModel
        obj.installments = installments
        obj.vehicleModelYear = vehicleModelYear
        obj.codeFipe = codeFipe
        obj.vehicleFipeValue = vehicleFipeValue
        return obj
