from src.domains.Address import Address
from src.domains.Bank import Bank
from src.domains.Business import Business
from src.domains.ConsumerUnit import ConsumerUnit
from src.domains.Identity import Identity
from src.domains.Reference import Reference
from src.domains.Vehicle import Vehicle
from src.domains.Products import Products
from src.domains.__Domain import Domain
from src.enums.Education import Education
from src.enums.Gender import Gender
from src.enums.Nationality import Nationality
from src.enums.State import State
from src.enums.RelationshipStatus import RelationshipStatus


class Proposal(Domain):

    @classmethod
    def create(cls, mother: str = None,
               gender: Gender = None,
               nationality: Nationality = None,
               hometownState: State = None,
               hometown: str = None,
               education: Education = None,
               relationshipStatus: RelationshipStatus = None,
               phonelandlineidentity: Identity = None,
               address: Address = None,
               vehicle: Vehicle = None,
               consumerUnit: ConsumerUnit = None,
               business: Business = None,
               bank: Bank = None,
               reference: Reference = None,
               products: list[Products] = None):
        obj = cls()
        obj.mother = mother
        obj.gender = gender
        obj.nationality = nationality
        obj.hometownState = hometownState
        obj.hometown = hometown
        obj.education = education
        obj.relationshipStatus = relationshipStatus
        obj.phonelandlineidentity = phonelandlineidentity
        obj.address = address
        obj.vehicle = vehicle
        obj.consumerUnit = consumerUnit
        obj.business = business
        obj.bank = bank
        obj.reference = reference
        obj.products = products
        return obj
