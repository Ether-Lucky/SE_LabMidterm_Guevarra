from src.model.calculator import CalculatorModel

def test_large_numbers():
    model = CalculatorModel()

    result = model.evaluate("999999999*999999999")
    assert result == 999999998000000001