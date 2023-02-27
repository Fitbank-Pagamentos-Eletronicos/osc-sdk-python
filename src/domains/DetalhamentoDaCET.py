from src.domains.__Domain import Domain


class DetalhamentoDaCET(Domain):

    @classmethod
    def create(cls, porcentagemDeJuros: str = None,
               porcentagemDeImpostos: str = None,
               porcentagemDeTarifas: str = None,
               porcentagemDeServicos: str = None):
        obj = cls()
        obj.porcentagemDeJuros = porcentagemDeJuros
        obj.porcentagemDeImpostos = porcentagemDeImpostos
        obj.porcentagemDeTarifas = porcentagemDeTarifas
        obj.porcentagemDeServicos = porcentagemDeServicos
        return obj
