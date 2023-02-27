from src.domains.__Domain import Domain
from src.enums.Network import Network


class Match(Domain):

    @classmethod
    def create(cls, productId: int = None,
               name: str = None,
               logo: str = None,
               minValue: float = None,
               maxValue: float = None,
               minInstallment: int = None,
               maxInstallment: int = None,
               monthlyTax: float = None,
               annuity: float = None,
               network: Network = None):
        obj = cls()
        obj.productId = productId
        obj.name = name
        obj.logo = logo
        # Loan --> Auto, Home
        obj.minValue = minValue
        obj.maxValue = maxValue
        obj.minInstallment = minInstallment
        obj.maxInstallment = maxInstallment
        obj.monthlyTax = monthlyTax
        # Card
        obj.annuity = annuity
        obj.network = network
        return obj
