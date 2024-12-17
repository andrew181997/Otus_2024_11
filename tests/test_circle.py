import pytest
from src.circle import Circle, NUM_P
from math import sqrt


@pytest.mark.parametrize(
    ("radius"),
    [(3), (4.5)],
    ids=["int", "float"],
)
def test_area_circle(radius):
    a = Circle(radius)
    expected_area = round(NUM_P * sqrt(radius), 2)
    assert a.get_area == pytest.approx(expected_area)


@pytest.mark.parametrize(
    ("radius"),
    [(3), (4.5)],
    ids=["int", "float"],
)
def test_perimeter_circle(radius):
    a = Circle(radius)
    expected_perimeter = round(2 * radius * NUM_P, 2)
    assert a.get_perimeter == pytest.approx(expected_perimeter)
