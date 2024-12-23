import pytest
from src.rectangle import Rectangle


@pytest.mark.parametrize(
    ("side_a", "side_b"),
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

@pytest.mark.parametrize(
    "args",
    [
        ([1, 0]),
        ([1, "string"]),
        ([-1, -100]),
        ([0, 2]),
    ]
)
def test_validate_numeric_negative(args):
    with pytest.raises(ValueError):
        Rectangle.validate_numeric(*args)

@pytest.mark.parametrize(
    "args",
    [
        ([1, 2, 3]),
        ([1.5, 2.5]),
        ([100.5, 1000]),
    ],
)
def test_validate_numeric_positive(args):
    try:
        Rectangle.validate_numeric(*args)
    except ValueError:
        pytest.fail("validate_numeric raised ValueError for valid inputs")