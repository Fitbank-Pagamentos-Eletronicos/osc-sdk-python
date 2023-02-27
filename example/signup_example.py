import os
from datetime import datetime
from src.domains.LogData import LogData
from src.domains.SimpleSignup import SimpleSignup
from src.main import Osc

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")

osc = Osc.create_instance(client_id, client_secret)

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
        occurrence_date="",
        user_agent="",
        ip="",
        mac="")
)

pipeline = osc.signup(signup_data)
print(pipeline.id)
