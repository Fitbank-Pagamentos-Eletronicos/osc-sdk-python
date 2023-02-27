from src.domains.__Domain import Domain
from src.domains.LogData import LogData


class Contract(Domain):

    @classmethod
    def create(cls, aceptedCheckSum: str = None,
               logData: LogData = None):
        obj = cls()
        obj.aceptedCheckSum = aceptedCheckSum
        obj.logData = logData
        return obj
