from src.domains.__Domain import Domain
from src.enums.DocumentType import DocumentType
from src.enums.MimeType import MimeType


class DocumentResponse(Domain):

    @classmethod
    def create(cls, type: DocumentType = None,
               mime_type: MimeType = None,
               name: str = None,
               url: str = None):
        obj = cls()
        obj.type = type
        obj.mimeType = mime_type
        obj.name = name
        obj.url = url
        return obj
