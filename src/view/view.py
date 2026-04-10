import customtkinter as ctk

class CalculatorView(ctk.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("Simple Calculator")
        self.geometry("300x300")

        # Inputs
        self.entry1 = ctk.CTkEntry(self, placeholder_text="Enter first number")
        self.entry1.pack(pady=10)

        self.entry2 = ctk.CTkEntry(self, placeholder_text="Enter second number")
        self.entry2.pack(pady=10)

        # Buttons
        self.add_button = ctk.CTkButton(self, text="Add")
        self.add_button.pack(pady=5)

        self.subtract_button = ctk.CTkButton(self, text="Subtract")
        self.subtract_button.pack(pady=5)

        self.multiply_button = ctk.CTkButton(self, text="Multiply")
        self.multiply_button.pack(pady=5)

        self.divide_button = ctk.CTkButton(self, text="Divide")
        self.divide_button.pack(pady=5)

        # Result Label
        self.result_label = ctk.CTkLabel(self, text="Result: ")
        self.result_label.pack(pady=10)

    def get_inputs(self):
        return self.entry1.get(), self.entry2.get()

    def display_result(self, result):
        self.result_label.configure(text=f"Result: {result}")

    def display_error(self, message):
        self.result_label.configure(text=f"Error: {message}")