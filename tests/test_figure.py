import pytest
from src.figure import Figure



@pytest.mark.parametrize(
    "args, expected",
    [
        ([1, 2, 3], True),
        ([1.5, 2.5, 3.5], True),
        ([-1, 2, 3], False),
        ([1, 0, 3], False),
        ([1, "string", 3], False),
        ([-1], False),
        ([0], False),
        ([100.5, 99, 1000], True),
    ],
)
def test_validate_numeric(args, expected):
    if expected:
        try:
            Figure.validate_numeric(*args)
        except ValueError:
            pytest.fail("validate_numeric raised ValueError for valid inputs")
    else:
        with pytest.raises(ValueError):
            Figure.validate_numeric(*args)
