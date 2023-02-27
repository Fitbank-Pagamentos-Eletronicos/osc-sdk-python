from src.domains.__Domain import Domain
from datetime import datetime


class LogData(Domain):

    @classmethod
    def create(cls, latitude: float = None,
               longitude: float = None,
               occurrenceDate: datetime = None,
               userAgent: str = None,
               ip: str = None,
               mac: str = None):
        obj = cls()
        obj.latitude = latitude
        obj.longitude = longitude
        obj.occurrenceDate = occurrenceDate
        obj.userAgent = userAgent
        obj.ip = ip
        obj.mac = mac
        return obj
