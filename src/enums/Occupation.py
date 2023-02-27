from enum import Flag, auto


class Occupation(Flag):
    APONSETADO = auto()
    PENSIONISTA = auto()
    AUTOMONO = auto()
    EMPRESARIO = auto()
    PROFISSIONAL_LIBERAL = auto()
    ASSALARIADO = auto()
    FUNCIONARIO_PUBLICO = auto()
    DESEMPREGADO = auto()
