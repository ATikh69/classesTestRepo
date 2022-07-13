import math

from src.figure import Figure


class Circle(Figure):
    NAME = "CIRCLE"

    def __init__(self, r):
        self.__r = r

    def perimeter(r):
        return round((2 * math.pi * r), 2)

    def area(r):
        return round((math.pi * r * r), 2)


