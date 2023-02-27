from enum import Flag, auto


class HomeType(Flag):
    ALUGADA = auto()
    PARENTES = auto()
    FUNCIONAL = auto()
    PROPRIA_QUITADA = auto()
    PROPRIA_FINANCIADA = auto()
    OUTROS = auto()
