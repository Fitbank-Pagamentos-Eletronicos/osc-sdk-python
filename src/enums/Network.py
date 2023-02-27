from enum import Flag, auto


class Network(Flag):
    VISA = auto()
    MASTERCARD = auto()
    ELO = auto()
