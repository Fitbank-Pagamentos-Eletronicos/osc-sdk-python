import unittest
from src.domains.DetalhamentoDaCET import DetalhamentoDaCET


class TestDetalhamentoDaCET(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "porcentagemDeJuros": "0,5",
            "porcentagemDeImpostos": "0,5",
            "porcentagemDeTarifas": "0,5",
            "porcentagemDeServicos": "0,5"
        }'''
        obj = DetalhamentoDaCET.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = DetalhamentoDaCET.create(porcentagemDeJuros="0,5", porcentagemDeImpostos="0,5",
                                        porcentagemDeTarifas="0,5", porcentagemDeServicos="0,5")
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = DetalhamentoDaCET.create(porcentagemDeJuros="0,5", porcentagemDeImpostos="0,5",
                                        porcentagemDeTarifas="0,5", porcentagemDeServicos="0,5")
        json = orig.to_json()
        dest = DetalhamentoDaCET.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
