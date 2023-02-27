from enum import Flag, auto


class RelationshipStatus(Flag):
    CASADO = auto()
    DIVORCIADO = auto()
    VIUVO = auto()
    SEPARADO = auto()
    SOLTEIRO = auto()
    COMPANHEIRO = auto()
    UNIAO_ESTAVEL = auto()
    SEPARADO_JUDICIALMENTE = auto()
