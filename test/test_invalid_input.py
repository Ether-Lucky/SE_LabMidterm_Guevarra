import pytest
from src.model.calculator import CalculatorModel

def test_invalid_input():
    model = CalculatorModel()

    with pytest.raises(ValueError):
        model.evaluate("2+abc")