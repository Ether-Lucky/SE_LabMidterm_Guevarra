from src.model.calculator import CalculatorModel

class CalculatorController:
    
    def __init__(self, view):
        self.view = view
        self.model = CalculatorModel()

        # Bind buttons
        self.view.add_button.configure(command=self.handle_add)
        self.view.subtract_button.configure(command=self.handle_subtract)
        self.view.multiply_button.configure(command=self.handle_multiply)
        self.view.divide_button.configure(command=self.handle_divide)

    def validate_input(self, val1, val2):
        try:
            num1 = float(val1)
            num2 = float(val2)
            return num1, num2
        except ValueError:
            raise ValueError("Invalid input. Please enter numbers only.")

    def process_operation(self, operation):
        try:
            val1, val2 = self.view.get_inputs()
            num1, num2 = self.validate_input(val1, val2)

            result = operation(num1, num2)
            self.view.display_result(result)

        except Exception as e:
            self.view.display_error(str(e))

    def handle_add(self):
        self.process_operation(self.model.add)

    def handle_subtract(self):
        self.process_operation(self.model.subtract)

    def handle_multiply(self):
        self.process_operation(self.model.multiply)

    def handle_divide(self):
        self.process_operation(self.model.divide)