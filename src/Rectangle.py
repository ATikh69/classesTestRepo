from src.figure import Figure
from src.Circle import Circle


class Rectangle(Figure):
    NAME = "RECTANGLE"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def perimeter(self):
        return self.a * 2 + self.b * 2

    @property
    def area(self):
        return self.a * self.b
