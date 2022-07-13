import pytest

from src.Triangle import Triangle


def test_triangle_creating_negative():
    with pytest.raises(ValueError, match="Треугольник не может быть создан"):
        Triangle(3, 8, 3)


def test_triangle_perimetr():
    assert Triangle.perimeter(3, 4, 5) == 12


def test_triangle_area():
    assert Triangle.area(3, 4, 5) == 6
