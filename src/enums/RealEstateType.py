from enum import Flag, auto


class RealEstateType(Flag):
    HOUSE = auto()
    APARTMENT = auto()
    COMMERCIAL = auto()
    LAND = auto()
    OTHERS = auto()
