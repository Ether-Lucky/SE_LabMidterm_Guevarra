class CalculatorModel:

    def evaluate(self, expression):
        try:
            # Prevent unsafe input
            allowed_chars = "0123456789+-*/.() "
            for char in expression:
                if char not in allowed_chars:
                    raise ValueError("Invalid character")

            result = eval(expression)

            return result

        except ZeroDivisionError:
            raise ValueError("Cannot divide by zero")
        except Exception:
            raise ValueError("Invalid expression")