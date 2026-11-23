import pytest
from calculator import calculate


@pytest.mark.parametrize(
    "a, operator, b, expected",
    [
        (2, "+", 3, 5),
        (8, "-", 3, 5),
        (4, "*", 3, 12),
        (10, "/", 2, 5),
        (-2, "+", 3, 1),
    ],
)
def test_calculate(a, operator, b, expected):
    assert calculate(a, operator, b) == expected


def test_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculate(10, "/", 0)


def test_unsupported_operator():
    with pytest.raises(ValueError, match="Unsupported operator"):
        calculate(2, "%", 3)
