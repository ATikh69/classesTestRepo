from src.Circle import Circle


def test_square_area():
    assert Circle.area(1) == 3.14


def test_square_perimetr():
    assert Circle.perimeter(1) == 6.28
