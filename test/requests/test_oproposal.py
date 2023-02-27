import os
import unittest
import json
from dotenv import load_dotenv
from src.requests.OProposal import OProposal

from src.domains.Proposal import Proposal
from src.main import Osc

load_dotenv()


class TestOProposal(unittest.TestCase):
    def setUp(self):
        osc = Osc.get_instance()
        if osc is not None:
            return
        client_id = os.getenv("client_id")
        client_secret = os.getenv("client_secret")
        Osc.create_instance(client_id, client_secret)

    def test_oproposal_acert(self):
        pipeline_id = os.getenv("pipeline_id")
        your_json = "{"
        "\n  \"mother\": \"Fulana Mae\","
        "\n  \"gender\": \"MASCULINO\","
        "\n  \"nationality\": \"BRASILEIRO\","
        "\n  \"hometownState\": \"GO\","
        "\n  \"hometown\": \"Goiania\","
        "\n  \"education\": \"POS_GRADUACAO\","
        "\n  \"relationshipStatus\": \"CASADO\","
        "\n  \"phoneLandline\": \"6232345678\","
        "\n  \"identity\": {"
        "\n    \"type\": \"RG\","
        "\n    \"number\": \"123456\","
        "\n    \"issuer\": \"SSP\","
        "\n    \"state\": \"GO\","
        "\n    \"issuingDate\": \"2010-01-01\""
        "\n  },"
        "\n  \"address\": {"
        "\n    \"zipCode\": \"74000-000\","
        "\n    \"address\": \"Cidade_de_Goiania\","
        "\n    \"number\": 0,"
        "\n    \"complement\": \"toda a cidade\","
        "\n    \"district\": \"geral\","
        "\n    \"state\": \"GO\","
        "\n    \"city\": \"Goiania\","
        "\n    \"homeType\": \"ALUGADA\","
        "\n    \"homeSince\": \"MAIOR_2_ANOS\""
        "\n  },"
        "\n  \"vehicle\": {"
        "\n    \"licensePlate\": \"XXX0000\""
        "\n  },"
        "\n  \"consumerUnit\": {"
        "\n    \"number\": \"000000000\""
        "\n  },"
        "\n  \"business\": {"
        "\n    \"occupation\": \"ASSALARIADO\","
        "\n    \"profession\": \"ADMINISTRADOR\","
        "\n    \"companyName\": \"Abobrinha\","
        "\n    \"phone\": \"6239413142\","
        "\n    \"income\": 1500,"
        "\n    \"payday\": 1,"
        "\n    \"benefitNumber\": \"\","
        "\n    \"zipCode\": \"74000000\","
        "\n    \"address\": \"Cidade de Goiania\","
        "\n    \"number\": 1,"
        "\n    \"complement\": \"toda a cidade\","
        "\n    \"district\": \"geral\","
        "\n    \"state\": \"GO\","
        "\n    \"city\": \"Goiania\""
        "\n  },"
        "\n  \"bank\": {"
        "\n    \"bank\": \"001\","
        "\n    \"type\": \"CONTA_CORRENTE_INDIVIDUAL\","
        "\n    \"agency\": \"0001\","
        "\n    \"account\": \"5647891\""
        "\n  },"
        "\n  \"reference\": ["
        "\n    {"
        "\n      \"name\": \"Joana Maria\","
        "\n      \"phone\": \"11987654321\""
        "\n    }"
        "\n  ],"
        "\n  \"products\": ["
        "\n    {"
        "\n      \"type\": \"LOAN\","
        "\n      \"value\": \"7000\","
        "\n      \"installments\": 12"
        "\n    },"
        "\n    {"
        "\n      \"type\": \"CARD\","
        "\n      \"network\": \"MASTERCARD\","
        "\n      \"payDay\": 15"
        "\n    },"
        "\n    {"
        "\n      \"type\": \"REFINANCING_AUTO\","
        "\n      \"value\": \"30000\","
        "\n      \"vehicleBrand\": \"Fiat\","
        "\n      \"vehicleModel\": \"Mobi\","
        "\n      \"installments\": 12,"
        "\n      \"vehicleModelYear\": \"2010\","
        "\n      \"codeFipe\": \"038003-2\","
        "\n      \"vehicleFipeValue\": \"28000\""
        "\n    },"
        "\n    {"
        "\n      \"type\": \"REFINANCING_HOME\","
        "\n      \"value\": \"150000\","
        "\n      \"installments\": 12,"
        "\n      \"realEstateType\": \"house\","
        "\n      \"realEstateValue\": \"148000\","
        "\n      \"outstandingBalance\": \"50000\""
        "\n    }"
        "\n  ]"
        "\n}"

        osc = Osc.get_instance()

        '''origen = Proposal(mother='Maria aline', gender='Masculino', nationality='Brasileiro', hometownState='CE', hometown='Fortaleza',
                          education='Ensino_Superior_Completo', relationshipStatus='Casado', phonelandlineidentity='Identity', address='Address',
                          vehicle='Vehicle', consumerUnit='ConsumerUnit', business='Business', bank='Bank', reference='Refence', products='Products')
        '''

        j = json.loads(your_json)
        u = Proposal(**j)
        pipeline = OProposal.request(osc, pipeline_id)
        assert pipeline.id is not None
        assert pipeline.status is not None
        assert pipeline.cpf is not None
        assert pipeline.name is not None
        assert pipeline.date_created is not None
        assert pipeline.last_updated is not None

    def test_oproposal_erro(self):
        pipeline_id = os.getenv("pipeline_id")

        osc = Osc.get_instance()

        origen = Proposal(mother='', gender='', nationality='', hometownState='', hometown='',
                          education='', relationshipStatus='', phonelandlineidentity='', address='',
                          vehicle='', consumerUnit='', business='', bank='', reference='', products='')

        try:
            OProposal.request(osc, pipeline_id, origen)
            assert False
        except Exception as e:
            # corrigir assert
            assert e.args[0] == '{"message":"User not found"}'
