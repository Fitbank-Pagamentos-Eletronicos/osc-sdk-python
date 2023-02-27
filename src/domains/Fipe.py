from src.domains.VehicleBody import VehicleBody
from src.domains.__Domain import Domain

vehicle = [VehicleBody]


class Fipe(Domain):

    @classmethod
    def create(cls, lastUpdate: str = None,
               vehicle: VehicleBody = None):
        obj = cls()
        obj.lastUpdate = lastUpdate
        obj.vehicle = vehicle
        return obj
