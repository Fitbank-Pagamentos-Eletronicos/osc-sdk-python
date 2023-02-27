from src.domains.__Domain import Domain
from src.enums.DocumentType import DocumentType
from src.enums.MimeType import MimeType


class Document(Domain):

    @classmethod
    def create(cls, type: DocumentType = None,
               mimeType: MimeType = None,
               name: str = None,
               base64: str = None):
        obj = cls()
        obj.type = type
        obj.mimeType = mimeType
        obj.name = name
        obj.base64 = base64
        return obj
