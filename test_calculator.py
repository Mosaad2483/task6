
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
        (-4, "-", 3, -7),
        (-3, "*", -2, 6),
        (7, "/", -2, -3.5),

        
        (0.1, "+", 0.2, 0.3),
        (5.5, "-", 2.25, 3.25),
        (1.5, "*", 2.0, 3.0),
        (7.5, "/", 2.5, 3.0),

       
        (0, "+", 5, 5),
    ],
)
def test_calculate(a, operator, b, expected):
    assert calculate(a, operator, b) == pytest.approx(expected)


def test_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculate(10, "/", 0)


def test_unsupported_operator():
    with pytest.raises(ValueError, match="Unsupported operator"):
        calculate(2, "%", 3)
