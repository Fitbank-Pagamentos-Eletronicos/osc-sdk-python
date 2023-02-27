from src.domains.LogData import LogData
from src.domains.__Domain import Domain


class SimpleSignup(Domain):

    @classmethod
    def create(cls, cpf: str = None,
               name: str = None,
               birthday: str = None,
               email: str = None,
               phone: str = None,
               zipCode: str = None,
               hasCreditCard: bool = None,
               hasRestriction: bool = None,
               hasOwnHouse: bool = None,
               hasVehicle: bool = None,
               hasAndroid: bool = None,
               logData: LogData = None):
        obj = cls()
        obj.cpf = cpf
        obj.name = name
        obj.birthday = birthday
        obj.email = email
        obj.phone = phone
        obj.zipCode = zipCode
        obj.hasCreditCard = hasCreditCard
        obj.hasRestriction = hasRestriction
        obj.hasOwnHouse = hasOwnHouse
        obj.hasVehicle = hasVehicle
        obj.hasAndroid = hasAndroid
        obj.logData = logData
        return obj
