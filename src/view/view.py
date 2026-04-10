import customtkinter as ctk

class CalculatorView(ctk.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("Calculator ni Lucky")
        self.geometry("320x450")
        self.resizable(False, False)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Display
        self.display = ctk.CTkEntry(self, height=50, font=("Arial", 24), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=15, sticky="nsew")

        # Buttons layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
        ]

        self.buttons = {}

        for (text, row, col) in buttons:
            btn = ctk.CTkButton(
                self,
                text=text,
                width=60,
                height=60,
                font=("Arial", 18),
                corner_radius=12
            )
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            self.buttons[text] = btn

        # Equals button (wide)
        self.equals_button = ctk.CTkButton(
            self,
            text="=",
            height=60,
            font=("Arial", 18, "bold"),
            corner_radius=12
        )
        self.equals_button.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Make grid responsive
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.grid_columnconfigure(j, weight=1)

    # ===== Helper Methods =====

    def get_display(self):
        return self.display.get()

    def set_display(self, value):
        self.display.delete(0, "end")
        self.display.insert(0, value)

    def append_to_display(self, value):
        if self.get_display() == "Error":
            self.clear_display()
        self.display.insert("end", value)

    def clear_display(self):
        self.display.delete(0, "end")

    def display_error(self, message):
        self.set_display("Error")