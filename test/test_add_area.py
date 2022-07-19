import pytest


def test_add1(test_rectangle, test_triangle):
    assert test_rectangle.add_area == 21


def test_add_negative(test_rectangle, test_foo):
    with pytest.raises(ValueError):
        test_rectangle.add_area(test_foo)
