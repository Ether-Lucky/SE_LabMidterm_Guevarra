from src.view.view import CalculatorView
from src.controller.controller import CalculatorController

if __name__ == "__main__":
    app = CalculatorView()
    controller = CalculatorController(app)
    app.mainloop()