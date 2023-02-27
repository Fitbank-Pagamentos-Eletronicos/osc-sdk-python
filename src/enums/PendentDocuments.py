from enum import Flag, auto


class PendentDocuments(Flag):
    SELF = auto()
    IDENTITY_FRONT = auto()
    IDENTITY_BACK = auto()
    ADDRESS_PROOF = auto()
    INCOME_PROOF = auto()
