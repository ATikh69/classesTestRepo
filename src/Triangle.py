from src.figure import Figure
from math import sqrt


class Triangle(Figure):
    NAME = "TRIANGLE"

    def __init__(self, a, b, c):
        if (a + b) < c or (b + c) < a or (a + c) < b:
            raise ValueError("Треугольник не может быть создан!")
        self.__a = a
        self.__b = b
        self.__c = c

    def perimeter(a, b, c):
        return a + b + c

    def area(a, b, c):
        return round(sqrt(((a + b + c) / 2) * ((a + b + c) / 2 - a) * ((a + b + c) / 2 - b) * ((a + b + c) / 2 - c)),2)
