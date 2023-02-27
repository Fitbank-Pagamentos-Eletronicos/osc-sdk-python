from enum import Flag, auto


class IdentityType(Flag):
    RG = auto()
    CNH = auto()
    PASSAPORTE = auto()
    CARTEIRA_CRC = auto()
    CARTEIRA_CREA = auto()
    CARTEIRA_OAB = auto()
    CARTEIRA_CRE = auto()
