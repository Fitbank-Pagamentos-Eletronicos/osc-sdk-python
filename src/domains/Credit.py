from src.domains.__Domain import Domain
from src.enums.ProductType import ProductType
from src.enums.CreditStatus import CreditStatus
from src.enums.PendentDocuments import PendentDocuments
from src.enums.Network import Network


class Credit(Domain):

    @classmethod
    def create(cls, customerServiceNumber: str = None,
               type: ProductType = None,
               product: str = None,
               productId: int = None,
               hasDocuments: bool = None,
               hasContracts: bool = None,
               logo: str = None,
               lastStatus: CreditStatus = None,
               pendentDocuments: list[PendentDocuments] = None,
               dateCreated: str = None,
               lastUpdated: str = None,
               value: float = None,
               installments: int = None,
               monthlyTax: float = None,
               installmentsValue: float = None,
               iofValue: float = None,
               grossValue: float = None,
               firstPaymentDate: str = None,
               cet: float = None,
               releasedDate: str = None,
               international: bool = None,
               annuity: float = None,
               network: Network = None,
               prepaid: bool = None,
               digitalAccount: bool = None):
        obj = cls()
        obj.customerServiceNumber = customerServiceNumber
        obj.type = type
        obj.product = product
        obj.productId = productId
        obj.hasDocuments = hasDocuments
        obj.hasContracts = hasContracts
        obj.logo = logo
        obj.lastStatus = lastStatus
        obj.pendentDocuments = pendentDocuments
        obj.dateCreated = dateCreated
        obj.lastUpdated = lastUpdated
        # Loan --> Auto, Home
        obj.value = value
        obj.installments = installments
        obj.monthlyTax = monthlyTax
        obj.installmentsValue = installmentsValue
        obj.iofValue = iofValue
        obj.grossValue = grossValue
        obj.firstPaymentDate = firstPaymentDate
        obj.cet = cet
        obj.releasedDate = releasedDate
        # Card
        obj.international = international
        obj.annuity = annuity
        obj.network = network
        obj.prepaid = prepaid
        obj.digitalAccount = digitalAccount
        return obj
