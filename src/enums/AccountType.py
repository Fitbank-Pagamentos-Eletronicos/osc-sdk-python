from enum import Flag, auto


class AccountType(Flag):
    CONTA_CORRENTE_INDIVIDUAL = auto()
    CONTA_CORRENTE_CONJUNTA = auto()
    CONTA_POUPANCA_CONJUNTA = auto()
    CONTA_POUPANCA_INDIVIDUAL = auto()
