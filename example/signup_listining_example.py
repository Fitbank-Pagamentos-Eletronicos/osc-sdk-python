import os
from datetime import datetime
from src.domains.LogData import LogData
from src.domains.Pipeline import Pipeline
from src.domains.SimpleSignup import SimpleSignup
from src.main import Osc


def main():
    client_id = os.getenv("client_id")
    client_secret = os.getenv("client_secret")
    osc = Osc.create_instance(client_id, client_secret)
    osc.set_response_listening(listening)
    signup()


def listening(pipeline: Pipeline):
    print(f'async! {pipeline.id}')


# noinspection DuplicatedCode
def signup():
    signup_data = SimpleSignup.create(
        cpf="",
        name="",
        birthday="",
        email="",
        phone="",
        zip_code="",
        has_credit_card="",
        has_restriction="",
        has_own_house="",
        has_vehicle="",
        has_android="",
        log_data=LogData.create(
            latitude="",
            longitude="",
            occurrence_date=datetime.now(),
            user_agent="",
            ip="",
            mac="")
    )

    pipeline = Osc.get_instance().signup(signup_data)
    print(pipeline.id)


if __name__ == "__main__":
    main()
