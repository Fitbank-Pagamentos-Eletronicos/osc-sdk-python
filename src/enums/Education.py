from enum import Flag, auto


class Education(Flag):
    NAO_ALFABETIZADO = auto()
    ENSINO_FUNDAMENTAL_INCOMPLETO = auto()
    ENSINO_FUNDAMENTAL_COMPLETO = auto()
    ENSINO_MEDIO_INCOMPLETO = auto()
    ENSINO_MEDIO_COMPLETO = auto()
    ENSINO_SUPERIOR_INCOMPLETO = auto()
    ENSINO_SUPERIOR_COMPLETO = auto()
    POS_GRADUACAO = auto()
