import pytest

from src.Circle import Circle
from src.Square import Square
from src.Rectangle import Rectangle
from src.Triangle import Triangle


@pytest.fixture
def test_circle():
    return Circle(1)


@pytest.fixture
def test_rectangle():
    return Rectangle(3, 4)


@pytest.fixture
def test_triangle():
    return Triangle(3, 4, 5)

@pytest.fixture
def test_square():
    return Square(3)
