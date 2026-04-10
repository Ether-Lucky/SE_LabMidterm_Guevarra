from src.model.calculator import CalculatorModel

class CalculatorController:

    def __init__(self, view):
        self.view = view
        self.model = CalculatorModel()

        # Bind number & operator buttons
        for key, button in self.view.buttons.items():
            if key == 'C':
                button.configure(command=self.clear)
            else:
                button.configure(command=lambda k=key: self.append(k))

        # Equals button
        self.view.equals_button.configure(command=self.calculate)

    def append(self, value):
        self.view.append_to_display(value)

    def clear(self):
        self.view.clear_display()

    def calculate(self):
        try:
            expression = self.view.get_display()
            result = self.model.evaluate(expression)
            self.view.set_display(result)

        except Exception as e:
            self.view.display_error(str(e))