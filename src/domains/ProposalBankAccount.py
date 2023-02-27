from src.domains.AddressSimpleBody import AddressSimpleBody
from src.domains.BusinessSimpleBody import BusinessSimpleBody
from src.domains.ProductBankAccount import ProductBankAccount
from src.domains.__Domain import Domain
from src.enums.Gender import Gender
from src.enums.Nationality import Nationality
from src.enums.RelationshipStatus import RelationshipStatus
from src.domains.IdentifySimpleBody import IdentifySimpleBody
from src.enums.State import State


class ProposalBankAccount(Domain):

    @classmethod
    def create(cls, mother: str = None,
               gender: Gender = None,
               nationality: Nationality = None,
               hometownState: State = None,
               relationshipStatus: RelationshipStatus = None,
               identity: IdentifySimpleBody = None,
               address: AddressSimpleBody = None,
               business: BusinessSimpleBody = None,
               products: list[ProductBankAccount] = None):
        obj = cls()
        obj.mother = mother
        obj.gender = gender
        obj.nationality = nationality
        obj.hometownState = hometownState
        obj.relationshipStatus = relationshipStatus
        obj.identity = identity
        obj.address = address
        obj.business = business
        obj.products = products
        return obj
