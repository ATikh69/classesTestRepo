from src.figure import Figure

a = None


class Square(Figure):
    NAME = "SQUARE"

    def __init__(self, a):
        self.__a = a

    def area(a):
        return a * a

    def perimeter(a):
        return a * 4


