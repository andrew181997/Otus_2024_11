import pytest
from src.triangle import Triangle
from math import sqrt


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c"),
    [
        (3, 5, 5),
        (4.5, 5.5, 6.5),
    ],
    ids=["int", "float"],
)
def test_area_triangle(side_a, side_b, side_c):
    a = Triangle(side_a, side_b, side_c)
    p = (side_a + side_b + side_c) / 2
    expected_area = round(sqrt(p * (p - side_a) * (p - side_b) * (p - side_c)), 2)
    assert a.get_area == pytest.approx(expected_area)


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c"),
    [
        (3, 5, 5),
        (4.5, 5.5, 6.5),
    ],
    ids=["int", "float"],
)
def test_perimeter_triangle(side_a, side_b, side_c):
    a = Triangle(side_a, side_b, side_c)
    expected_perimeter = round(side_a + side_b + side_c, 2)
    assert a.get_perimeter == pytest.approx(expected_perimeter)


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c"),
    [(3, 4, 4),
     (4.5, 5.5, 6.5)
     ],
    ids=["int", "float"]
)
def test_can_create(side_a, side_b, side_c):
    assert side_a + side_b > side_c, "Triangle cannot be created"
    assert side_a + side_c > side_b, "Triangle cannot be created"
    assert side_b + side_c > side_a, "Triangle cannot be created"
