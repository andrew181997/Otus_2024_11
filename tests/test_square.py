import pytest
from src.square import Square


@pytest.mark.parametrize(
    ("side_a"),
    [(3), (4.5)],
    ids=["int", "float"],
)
def test_square_area_positive(side_a):
    a = Square(side_a)

    expected_area = round(side_a * side_a, 2)
    assert a.get_area == pytest.approx(expected_area)


@pytest.mark.parametrize(
    ("side_a"),
    [(3), (4.5)],
    ids=["int", "float"],
)
def test_perimeter_square(side_a):
    a = Square(side_a)
    expected_perimeter = side_a * 4
    assert a.get_perimeter == pytest.approx(expected_perimeter)


@pytest.mark.parametrize(
    "args",
    [
        (["string"]),
        ([-1]),
        ([0]),
    ],
)
def test_validate_numeric_negative(args):
    with pytest.raises(ValueError):
        Square.validate_numeric(*args)

@pytest.mark.parametrize(
    "args",
    [
        ([3]),
        ([3.5]),
        ([1000]),
    ],
)
def test_validate_numeric_positive(args):
    try:
        Square.validate_numeric(*args)
    except ValueError:
        pytest.fail("validate_numeric raised ValueError for valid inputs")
