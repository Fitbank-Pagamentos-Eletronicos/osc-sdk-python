from src.domains.__Domain import Domain


class VehicleBody(Domain):

    @classmethod
    def create(cls, vehicleBrand: str = None,
               vehicleModel: str = None,
               codeFipe: str = None,
               vehicleFipeValeu: str = None,
               vehicleType: str = None,
               vehicleYear: str = None):
        obj = cls()
        obj.vehicleBrand = vehicleBrand
        obj.vehicleModel = vehicleModel
        obj.codeFipe = codeFipe
        obj.vehicleFipeValeu = vehicleFipeValeu
        obj.vehicleType = vehicleType
        obj.vehicleYear = vehicleYear
        return obj
