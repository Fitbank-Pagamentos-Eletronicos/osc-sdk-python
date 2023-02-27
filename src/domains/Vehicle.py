from src.domains.__Domain import Domain


class Vehicle(Domain):

    @classmethod
    def create(cls, licensePlate: str = None):
        obj = cls()
        obj.licensePlate = licensePlate
        return obj
