from src.domains.Error import Error
from src.domains.ErrorField import ErrorField


class ErrorFields(Error):

    @classmethod
    def create(cls, code: str = None,
               message: str = None,
               erros: list[ErrorField] = None):
        obj = cls()
        super().__init__(code, message)
        obj.erros = erros
        return obj
