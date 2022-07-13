import pytest

from src.Rectangle import Rectangle


# проверка расчета периметра прямоугольника
def test_triangle_perimetr():
    assert Rectangle.perimeter(3, 4) == 14

# проверка расчета площади прямоугольника
def test_triangle_area():
    assert Rectangle.area(3, 4) == 12


