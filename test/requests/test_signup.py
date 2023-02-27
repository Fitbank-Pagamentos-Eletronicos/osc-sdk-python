import os
import unittest
from datetime import datetime

from src.domains.ProductAuto import ProductAuto
from src.domains.ProductCard import ProductCard
from src.domains.ProductHome import ProductHome
from src.domains.ProductLoan import ProductLoan
from src.requests.Signup import Signup

from src.domains.SignupMatch import SignupMatch
from src.domains.SimpleSignup import SimpleSignup
from src.domains.LogData import LogData
from src.main import Osc
from src.enums.Education import Education
from src.enums.Network import Network
from src.enums.Occupation import Occupation
from src.enums.RealEstateType import RealEstateType


class TestSignup(unittest.TestCase):
    def setUp(self):
        osc = Osc.get_instance()
        if osc is not None:
            return
        client_id = os.getenv("client_id")
        client_secret = os.getenv("client_secret")
        Osc.create_instance(client_id, client_secret)

    def teste_simple_signup_acert(self):

        osc = Osc.get_instance()

        logData = LogData(latitude=-16, longitude=-49,
                          occurrenceDate=datetime.now(), userAgent='str', ip='0.0.0.0')
        origen = SimpleSignup(cpf='647.318.290-03', name='Eduardo Silva', birthday='2002-07-01',
                              email='xxx@gmail.com', phone='11997971235', zipCode='60320-600',
                              hasCreditCard=True, hasRestriction=True, hasOwnHouse=True, hasVehicle=True,
                              hasAndroid=True, logData=logData)
        try:
            pipeline = Signup.request(osc, origen)
            assert pipeline.id is not None
            assert pipeline.status is not None
            assert pipeline.cpf is not None
            assert pipeline.name is not None
            assert pipeline.date_created is not None
            assert pipeline.last_updated is not None
        except Exception as e:
            print(e)
            assert False

    def teste_simple_signup_erro(self):

        osc = Osc.get_instance()

        origen = SimpleSignup(cpf='000.000.001-91', name='Fulanin Tals', birthday='2022-01-01',
                              email='test@email.com', phone='(10)98765-4321', zipCode='000001-000',
                              hasCreditCard=False, hasRestriction=False, hasOwnHouse=False,
                              hasVehicle=False, hasAndroid=False, logData={})

        try:
            pipeline = Signup.request(osc, origen)
            assert pipeline.id is not None
            assert pipeline.status is not None
            assert pipeline.cpf is not None
            assert pipeline.name is not None
            assert pipeline.date_created is not None
            assert pipeline.last_updated is not None
        except Exception as e:
            assert '"code":"invalid_inputs"' in e.args[0]

    def teste_signup_match_acert(self):

        osc = Osc.get_instance()

        logData = LogData(latitude=-16, longitude=-49,
                          occurrenceDate=datetime.now(), userAgent='str', ip='0.0.0.0')
        products = [ProductLoan(value=1000, installments=6),
                    ProductCard(network=Network.VISA, payDay=5),
                    ProductAuto(value=20000, installments=24,
                                codeFipe='00984', vehicleFipeValue=30000),
                    ProductHome(value=150000, installments=72, realEstateType=RealEstateType.HOUSE,
                                realEstateValue=200000, outstandingBalance=50000)]

        origen = SignupMatch(cpf='123.456.789-19', name='Jose Silva', birthday='1988-12-01',
                             email='fitbank@fitbank.com', phone='85999999999', zipCode='60000-000', income=7000,
                             education=Education.POS_GRADUACAO, banks='Santander', occupation=Occupation.AUTOMONO,
                             hasCreditCard=True, hasRestriction=False, hasOwnHouse=True,
                             hasVehicle=True, hasAndroid=True,
                             products=products, logData=logData)

        try:
            pipeline = Signup.request(osc, origen)
            assert pipeline.id is not None
            assert pipeline.status is not None
            assert pipeline.cpf is not None
            assert pipeline.name is not None
            assert pipeline.date_created is not None
            assert pipeline.last_updated is not None
        except Exception as e:
            assert e.args[0] == '{"message":"User not found"}'

    def teste_signup_match_erro(self):

        osc = Osc.get_instance()

        logData = LogData(latitude=-16, longitude=-49,
                          occurrenceDate=datetime.now(), userAgent='str', ip='0.0.0.0')
        products = [ProductLoan(value=1000, installments=6),
                    ProductCard(network=Network.VISA, payDay=5),
                    ProductAuto(value=20000, installments=24,
                                codeFipe='00984', vehicleFipeValue=30000),
                    ProductHome(value=150000, installments=72, realEstateType=RealEstateType.HOUSE,
                                realEstateValue=200000, outstandingBalance=50000)]

        origen = SignupMatch(cpf='000.000.001-91', name='Fulanin Tals', birthday='2022-01-01',
                             email='test@email.com', phone='11987654321', zipCode='000001-000', income=7000,
                             education=Education.POS_GRADUACAO, banks='Santander', occupation=Occupation.AUTOMONO,
                             hasCreditCard=False, hasRestriction=False, hasOwnHouse=False,
                             hasVehicle=False, hasAndroid=False,
                             products=products, logData=logData)

        try:
            pipeline = Signup.request(osc, origen)
            assert pipeline.id is not None
            assert pipeline.status is not None
            assert pipeline.cpf is not None
            assert pipeline.name is not None
            assert pipeline.date_created is not None
            assert pipeline.last_updated is not None
        except Exception as e:
            assert e.args[0] == '{"message":"User not found"}'
