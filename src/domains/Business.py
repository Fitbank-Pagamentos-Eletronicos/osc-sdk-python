from src.domains.__Domain import Domain
from src.enums.EmploymentSince import EmploymentSince
from src.enums.Occupation import Occupation
from src.enums.Profession import Profession
from src.enums.State import State


class Business(Domain):

    @classmethod
    def create(cls, occupation: Occupation = None,
               profession: Profession = None,
               companyName: str = None,
               phone: str = None,
               income: float = None,
               employmentSince: EmploymentSince = None,
               payday: int = None,
               benefitNumber: str = None,
               zipCode: str = None,
               address: str = None,
               number: int = None,
               complement: str = None,
               district: str = None,
               state: State = None,
               city: str = None):
        obj = cls()
        obj.occupation = occupation
        obj.profession = profession
        obj.companyName = companyName
        obj.phone = phone
        obj.income = income
        obj.employmentSince = employmentSince
        obj.payday = payday
        obj.benefitNumber = benefitNumber
        obj.zipCode = zipCode
        obj.address = address
        obj.number = number
        obj.complement = complement
        obj.district = district
        obj.state = state
        obj.city = city
        return obj
