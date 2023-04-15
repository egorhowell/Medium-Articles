from calculations import Calculations
import pytest


@pytest.fixture
def calculations():
    return Calculations(5, 10)


class TestCalculations:

    @pytest.mark.parametrize("a, b, expected_output",
                             [(1, 3, 4), (10, 50, 60), (100, 0, 100)])
    def test_sum(self, a, b, expected_output):
        assert Calculations(a, b).sum() == expected_output

    def test_multiply(self, calculations):
        assert calculations.multiply() == 50

    def test_divide(self, calculations):
        assert calculations.divide() == 0.5
