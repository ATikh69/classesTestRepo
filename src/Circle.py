import math

from src.figure import Figure


class Circle(Figure):
    NAME = "CIRCLE"

    def __init__(self, r):
        self.r = r

    @property
    def perimeter(self):
        return round((2 * math.pi * self.r), 2)

    @property
    def area(self):
        return round((math.pi * self.r * self.r), 2)
