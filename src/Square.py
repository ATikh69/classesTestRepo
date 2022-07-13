from src.Rectangle import Rectangle


class Square(Rectangle):
    NAME = "SQUARE"

    @property
    def area(self):
        return self.a * self.b

    @property
    def perimeter(self):
        return self.a * 2 + self.b * 2
