from enum import Flag, auto


class Products(Flag):
    productLoan = auto()
    productCard = auto()
    productAuto = auto()
    productHome = auto()
