from src.domains.__Domain import Domain
from src.enums.HomeSince import HomeSince
from src.enums.HomeType import HomeType
from src.enums.State import State


class Address(Domain):

    @classmethod
    def create(cls, zipCode: str = None,
               address: str = None,
               number: str = None,
               complement: str = None,
               district: str = None,
               state: State = None,
               city: str = None,
               homeType: HomeType = None,
               homeSince: HomeSince = None):
        obj = cls()
        obj.zipCode = zipCode
        obj.address = address
        obj.number = number
        obj.complement = complement
        obj.district = district
        obj.state = state
        obj.city = city
        obj.homeType = homeType
        obj.homeSince = homeSince
        return obj
