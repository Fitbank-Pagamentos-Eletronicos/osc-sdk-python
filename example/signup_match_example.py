import os
from datetime import datetime
from src.domains.LogData import LogData
from src.domains.ProductAuto import ProductAuto
from src.domains.ProductCard import ProductCard
from src.domains.ProductHome import ProductHome
from src.domains.ProductLoan import ProductLoan
from src.domains.SignupMatch import SignupMatch
from src.main import Osc
from src.enums.Education import Education
from src.enums.Network import Network
from src.enums.Occupation import Occupation
from src.enums.RealEstateType import RealEstateType

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")

osc = Osc.create_instance(client_id, client_secret)

signup_data = SignupMatch.create(
    cpf="",
    name="",
    birthday="",
    email="",
    phone="",
    zip_code="",
    education="",
    occupation="",
    banks="",
    income="",
    has_credit_card="",
    has_restriction="",
    has_own_house="",
    has_vehicle="",
    has_android="",
    products=[
        ProductLoan.create(value="", installments=""),
        ProductCard.create(network="", pay_day=""),
        ProductAuto.create(value="", installments="",
                           code_fipe="", vehicle_fipe_value=""),
        ProductHome.create(value="", installments="", real_state_type="",
                           real_state_value="", outstanding_balance="")
    ],
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
