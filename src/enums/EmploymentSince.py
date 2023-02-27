from enum import Flag, auto


class EmploymentSince(Flag):
    LESS_THAN_SIX_MONTHS = auto()
    BETWEEN_SIX_MONTHS_AND_ONE_YEAR = auto()
    BETWEEN_ONE_AND_TWO_YEARS = auto()
    BETWEEN_TWO_AND_THREE_YEARS = auto()
    BETWEEN_THREE_AND_FOUR_YEARS = auto()
    BETWEEN_FOUR_AND_FIVE_YEARS = auto()
    BETWEEN_FIVE_AND_TEN_YEARS = auto()
    MORE_THAN_TEN_YEARS = auto()
