import pytest
from src.rectangle import Rectangle


@pytest.mark.parametrize(
    ("side_a","side_b"),
    [
        (3, 5),
        (4.5, 5.5),
    ],
    ids=["int", "float"],
)
def test_area_rectangle(side_a, side_b):
    a = Rectangle(side_a, side_b)
    expected_area = round(side_a * side_b, 2)
    assert a.get_area == pytest.approx(expected_area)


@pytest.mark.parametrize(
    ("side_a", "side_b"),
    [
        (3, 5),
        (4.5, 5.5),
    ],
    ids=["int", "float"],
)
def test_perimeter_rectangle(side_a, side_b):
    a = Rectangle(side_a, side_b)
    expected_perimeter = (side_a + side_b) * 2
    assert a.get_perimeter == expected_perimeter
