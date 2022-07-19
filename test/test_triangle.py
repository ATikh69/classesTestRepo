import pytest

from src.Triangle import Triangle


def test_triangle_creating_negative():
    with pytest.raises(ValueError, match="Треугольник не может быть создан"):
        Triangle(3, 8, 3)


def test_triangle_perimetr(test_triangle):
    assert test_triangle.perimeter == 12


def test_triangle_area(test_triangle):
    assert test_triangle.area == 6
