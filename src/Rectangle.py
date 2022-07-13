from src.figure import Figure
from math import sqrt


class Rectangle(Figure):
    NAME = "RECTANGLE"

    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def perimeter(a, b):
        return a * 2 + b * 2

    def area(a, b):
        return a * b
