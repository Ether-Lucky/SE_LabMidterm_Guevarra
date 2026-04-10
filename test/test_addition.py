from src.model.calculator import CalculatorModel

def test_addition():
    model = CalculatorModel()
    result = model.evaluate("2+3")
    assert result == 5