from enum import Flag, auto


class HomeSince(Flag):
    MENOR_6_MESES = auto()
    MENOR_1_ANO = auto()
    MENOR_2_ANOS = auto()
    MAIOR_2_ANOS = auto()
