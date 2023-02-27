from enum import Flag, auto


class ProductType(Flag):
    LOAN = auto()
    CARD = auto()
    REFINANCING_AUTO = auto()
    REFINANCING_HOME = auto()
    CAAS = auto()
    WORKING_CAPITAL = auto()
    BANK_ACCOUNT = auto()
