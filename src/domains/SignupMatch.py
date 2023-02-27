import re

from src.domains.LogData import LogData
from src.domains.Products import Products
from src.domains.__Domain import Domain
from src.enums.Occupation import Occupation
from src.enums.Education import Education


class SignupMatch(Domain):

    @classmethod
    def create(cls, cpf: str = None,
               name: str = None,
               birthday: str = None,
               email: str = None,
               phone: str = None,
               zipCode: str = None,
               education: Education = None,
               banks: str = None,
               occupation: Occupation = None,
               income: float = None,
               hasCreditCard: bool = None,
               hasRestriction: bool = None,
               hasOwnHouse: bool = None,
               hasVehicle: bool = None,
               hasAndroid: bool = None,
               products: list[Products] = None,
               logData: list[LogData] = None):
        obj = cls()
        obj.cpf = cpf
        obj.name = name
        obj.birthday = birthday
        obj.email = email
        obj.phone = phone
        obj.zipCode = zipCode
        obj.education = education
        obj.banks = banks
        obj.occupation = occupation
        obj.income = income
        obj.hasCreditCard = hasCreditCard
        obj.hasRestriction = hasRestriction
        obj.hasOwnHouse = hasOwnHouse
        obj.hasVehicle = hasVehicle
        obj.hasAndroid = hasAndroid
        obj.products = products
        obj.logData = logData
        return obj
