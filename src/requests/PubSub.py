import json
import os
from concurrent.futures import ThreadPoolExecutor
from typing import Callable, Any

import requests
from dotenv import load_dotenv
from google.auth import jwt
from google.cloud import pubsub_v1

from src.domains.Pipeline import Pipeline
from src.domains.PubSubConfig import PubSubConfig

load_dotenv()


def get_config(token: str) -> PubSubConfig:
    server_url = os.getenv('server_url')

    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.get(
        f'{server_url}/v2.1/pubsub', headers=headers)

    return PubSubConfig.from_json(response.text)


def subscribe(project_id: str, topic_id: str, subscription_id: str, service_account: str,
              listening_function: Callable[[Pipeline], None]):
    topic_name = f'projects/{project_id}/topics/{topic_id}'
    subscription_name = f'projects/{project_id}/subscriptions/{subscription_id}'

    service_account_info = json.loads(service_account)
    # audience = "https://www.googleapis.com/auth/pubsub"
    audience = "https://pubsub.googleapis.com/google.pubsub.v1.Subscriber"
    credentials = jwt.Credentials.from_service_account_info(service_account_info, audience=audience)

    executor = ThreadPoolExecutor(max_workers=1)

    def callback(message):
        print(message.data)
        pipeline = Pipeline.from_json(message.data)
        executor.submit(listening_function, pipeline)
        message.ack()

    subscriber = pubsub_v1.SubscriberClient(credentials=credentials)
    subscriber.create_subscription(name=subscription_name, topic=topic_name)
    return subscriber.subscribe(subscription_name, callback)
