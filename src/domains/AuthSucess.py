from datetime import datetime

from src.domains.__Domain import Domain


class AuthSucess(Domain):

    def __init__(self):
        self.expire_at = None
        self.access_token = None

    @classmethod
    def create(cls, access_token: str = None,
               expire_at: datetime = None):
        obj = cls()
        obj.access_token = access_token
        obj.expire_at = expire_at
        return obj
