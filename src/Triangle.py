from src.figure import Figure
from math import sqrt


class Triangle(Figure):
    NAME = "TRIANGLE"

    def __init__(self, a, b, c):
        if (a + b) < c or (b + c) < a or (a + c) < b:
            raise ValueError("Треугольник не может быть создан!")
        self.a = a
        self.b = b
        self.c = c

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        return round(sqrt(((self.a + self.b + self.c) / 2) * ((self.a + self.b + self.c) / 2 - self.a) * (
                (self.a + self.b + self.c) / 2 - self.b) * ((self.a + self.b + self.c) / 2 - self.c)), 2)
