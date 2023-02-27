from src.domains.__Domain import Domain
from src.enums.State import State


class AddressSimpleBody(Domain):

    @classmethod
    def create(cls, zipCode: str = None,
               address: str = None,
               number: str = None,
               complement: str = None,
               district: str = None,
               state: State = None,
               city: str = None):
        obj = cls()
        obj.zipCode = zipCode
        obj.address = address
        obj.number = number
        obj.complement = complement
        obj.district = district
        obj.state = state
        obj.city = city
        return obj
