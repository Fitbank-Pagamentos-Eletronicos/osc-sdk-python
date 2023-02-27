from src.domains.__Domain import Domain


class PubSubConfig(Domain):

    def __init__(self):
        self.topic_id = None
        self.subscription_id = None
        self.project_id = None
        self.service_account = None

    @classmethod
    def create(cls, topic_id: str = None,
               subscription_id: str = None,
               project_id: str = None,
               service_account: int = None):
        obj = cls()
        obj.topic_id = topic_id
        obj.subscription_id = subscription_id
        obj.project_id = project_id
        obj.service_account = service_account
        return obj
