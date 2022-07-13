from src.Square import Square


def test_square_area():
    assert Square.area(3) == 9


def test_square_perimetr():
    assert Square.perimeter(3) == 12
