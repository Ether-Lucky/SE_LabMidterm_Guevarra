import pytest
from src.model.calculator import CalculatorModel

def test_divide_by_zero():
    model = CalculatorModel()

    with pytest.raises(ValueError):
        model.evaluate("10/0")